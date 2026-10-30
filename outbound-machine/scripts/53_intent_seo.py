"""Intent SEO / GEO par entreprise (paliers P3b, P3c, P3d), tout sur DataForSEO :
1. page d'accueil → gpt-4o-mini (DataForSEO LLM, ≈ 0,0006 $) : thématique, mot-clé business (ce qu'un client tape), question d'acheteur ;
2. volume mensuel du mot-clé (Google Ads France, un appel pour tous) ;
3. SERP Google France top 10 + réponse IA de Google (≈ 0,002 $) : position de l'entreprise, n°1 hors sites publics / Wikipédia /
   annuaires / médias / comparateurs, domaines cités par la réponse IA ;
4. part du trafic du n°1 sur le mot-clé (DataForSEO Labs serp_competitors, trafic estimé par domaine) → {{part}} :
   > 80 % « récupère quasiment tout le trafic », > 50 % « la majorité du trafic », sinon « capte la plus grosse part des clics » ;
5. ChatGPT avec recherche web (gpt-5-mini, ≈ 0,016 $) : la question d'acheteur → marques citées, l'entreprise est-elle citée ;
6. contrôle que le concurrent vend bien la même chose (gpt-4o-mini).
Sortie : ../data/datasets/intent_seo.json (cache par domaine). Usage : python 53_intent_seo.py --max 20 DS-104-1.1-FR-P4 ..."""
import base64, csv, html, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

ARGS = sys.argv[1:]
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
CACHE = "../data/datasets/intent_seo.json"
DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json"}
NOT_COMPETITOR = re.compile(r"(\.gouv\.fr|\.gov|wikipedia|youtube|linkedin|facebook|instagram|twitter|x\.com|reddit|quora|indeed|welcometothejungle|"
                            r"pagesjaunes|societe\.com|pappers|infogreffe|amazon|google|lesechos|journaldunet|capterra|appvizer|g2\.com|getapp|"
                            r"trustpilot|leboncoin|bpifrance|service-public|legifrance|economie\.gouv|cci\.fr|lefigaro|lemonde|bfmtv|maddyness|frenchweb)", re.I)
QUALIF = json.load(open("../data/campaigns/qualif.json"))
COST = [0.0]


def post(path, body, timeout=180):
    for i in range(3):  # erreurs ponctuelles côté DataForSEO (« Internal SE Server Error ») : on réessaie
        r = urllib.request.Request("https://api.dataforseo.com" + path, data=json.dumps(body).encode(), headers=DFS, method="POST")
        t = json.loads(urllib.request.urlopen(r, timeout=timeout).read())["tasks"][0]
        COST[0] += t.get("cost") or 0
        if t["status_code"] == 20000: return (t.get("result") or [{}])[0] or {}
    raise RuntimeError(f"{path} {t['status_message']}")


def llm(system, prompt, model="gpt-4o-mini", web=False):
    b = {"system_message": system[:495], "user_prompt": prompt[:495], "model_name": model, "web_search": web}
    if web: b["web_search_country_iso_code"] = "FR"
    r = post("/v3/ai_optimization/chat_gpt/llm_responses/live", [b])
    return "".join(s.get("text") or "" for it in (r.get("items") or []) for s in (it.get("sections") or []))


def as_json(txt):
    return json.loads(re.search(r"\{[\s\S]*\}", txt).group(0))


def fetch_page(d):
    for u in (f"https://{d}", f"https://www.{d}"):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=12).read(300000).decode("utf-8", "ignore")
            title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
            meta = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', t, re.I)
            body = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t)))
            return html.unescape(" | ".join(x for x in [title.group(1).strip() if title else "", meta.group(1) if meta else "", body[:600]] if x))
        except Exception:
            continue
    return ""


SYS_U = ("Tu aides une agence SEO. Réponds UNIQUEMENT en JSON : {\"thematique\": activité en 5 mots, \"motcle\": LE mot-clé Google "
         "(2 à 5 mots, français, sans marque, avec un vrai volume) qu'un client tape pour trouver ce type de prestataire, \"prompt\": la "
         "question qu'un acheteur pose à ChatGPT pour choisir un prestataire de ce type en France, sans marque}.")
SYS_C = ("Réponds UNIQUEMENT en JSON {\"concurrent\": true|false}. true seulement si le site est une entreprise qui vend la même chose "
         "(pas un site public, un annuaire, un comparateur, un média, une école, un blog).")


def run(item):
    d, company = item
    out = {"company": company}
    try:
        u = as_json(llm(SYS_U, f"Entreprise : {company} ({d}). Site : {fetch_page(d)}"))
        out.update(u)
        serp = post("/v3/serp/google/organic/live/advanced", [{"keyword": u["motcle"], "location_code": 2250, "language_code": "fr", "depth": 10,
                                                                "load_async_ai_overview": True}])
        items = serp.get("items") or []
        org = [i for i in items if i.get("type") == "organic"]
        out["position"] = next((i["rank_group"] for i in org if d in (i.get("domain") or "")), None)
        cands = [i for i in org if d not in (i.get("domain") or "") and not NOT_COMPETITOR.search(i.get("domain") or "")]
        for c in cands[:3]:  # premier vrai concurrent
            dom = c["domain"].removeprefix("www.")
            if as_json(llm(SYS_C, f"Activité de référence : {u['thematique']}. Site : {dom} · {c.get('title', '')} · {c.get('description', '')}")).get("concurrent"):
                out.update(concurrent_google=dom, concurrent_rank=c["rank_group"]); break
        ai = next((i for i in items if i.get("type") == "ai_overview"), None) or {}
        out["ai_overview_cite"] = sorted({(r.get("domain") or "").removeprefix("www.") for r in (ai.get("references") or []) if r.get("domain")} - {"google.com"})
        out["ai_overview_entreprise"] = any(d in x for x in out["ai_overview_cite"])
        if out.get("concurrent_google"):
            sc = post("/v3/dataforseo_labs/google/serp_competitors/live", [{"keywords": [u["motcle"]], "location_code": 2250, "language_code": "fr",
                                                                            "item_types": ["organic"], "limit": 20}])
            etv = {x["domain"].removeprefix("www."): x.get("etv") or 0 for x in sc.get("items") or []}
            tot = sum(etv.values())
            out["part_trafic"] = round(100 * etv.get(out["concurrent_google"], 0) / tot) if tot else None
            p = out["part_trafic"] or 0  # trois niveaux, la formule forte seulement quand c'est mesuré
            out["part"] = ("et récupère quasiment tout le trafic" if p > 80 else "et récupère la majorité du trafic" if p > 50
                           else "et capte la plus grosse part des clics")
        ans = llm("Réponds comme ChatGPT à un acheteur en France, avec des recommandations nommées.", u["prompt"], model="gpt-5-mini", web=True)
        out["chatgpt_cite_entreprise"] = company.lower().split()[0] in ans.lower() or d.split(".")[0] in ans.lower()
        out["chatgpt_marques"] = as_json(llm("Réponds UNIQUEMENT en JSON {\"marques\": [...]}.", "Entreprises recommandées, dans l'ordre : " + ans[:420])).get("marques", [])[:5]
    except Exception as e:
        out["error"] = str(e)[:160]
    return d, out


mx = int(ARGS[ARGS.index("--max") + 1]) if "--max" in ARGS else 20
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
todo = []
for c in [a for a in ARGS if a.startswith("DS-")]:
    for r in csv.DictReader(open(f"../data/datasets/{c}.csv")):
        d = r["domain"]
        if QUALIF.get(d, {}).get("fit") is True and d not in cache and d not in dict(todo): todo.append((d, r["company"]))
todo = todo[:mx]
with ThreadPoolExecutor(5) as ex:
    res = list(ex.map(run, todo))
kws = sorted({o["motcle"].lower() for _, o in res if o.get("motcle")})
if kws:
    try:  # volume Google Ads : le résultat est une liste (pas un seul objet), d'où l'appel direct
        r = urllib.request.Request("https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live", headers=DFS, method="POST",
                                   data=json.dumps([{"keywords": kws, "location_code": 2250, "language_code": "fr"}]).encode())
        t = json.loads(urllib.request.urlopen(r, timeout=180).read())["tasks"][0]
        vol = {x["keyword"]: x.get("search_volume") for x in t.get("result") or []}
    except Exception:
        vol = {}
    for _, o in res:
        if o.get("motcle"): o["volume"] = vol.get(o["motcle"].lower())
for d, o in res:
    cache[d] = o
    print(d, "|", o.get("motcle"), o.get("volume"), "| pos", o.get("position"), "| n°1", o.get("concurrent_google"), o.get("part_trafic"), "%",
          "| IA Google", "cite" if o.get("ai_overview_entreprise") else "absent", "| ChatGPT", "cite" if o.get("chatgpt_cite_entreprise") else "absent",
          (o.get("chatgpt_marques") or [])[:3], o.get("error", ""), flush=True)
json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=1)
print("coût DataForSEO", round(COST[0], 3), "$")
