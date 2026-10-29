"""Intent SEO / GEO par entreprise (paliers P3b et P3c), pour remplir {{motcle}} {{volume}} {{concurrent}} {{prompt}} :
1. page d'accueil → gpt-4o-mini : thématique, mot-clé business principal (ce qu'un client tape sur Google), question d'acheteur pour ChatGPT ;
2. DataForSEO : volume mensuel du mot-clé (Google Ads, France) + SERP Google France top 10 → premier concurrent devant l'entreprise ;
3. ChatGPT avec recherche web (gpt-4o-mini-search-preview) : la question posée telle quelle → marques citées, l'entreprise est-elle citée ?
Sortie : ../data/datasets/intent_seo.json (cache par domaine). Usage : python 53_intent_seo.py --max 20 DS-104-1.1-FR-P4 ..."""
import base64, csv, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
ARGS = sys.argv[1:]

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
CACHE = "../data/datasets/intent_seo.json"
DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json"}
OAI = {"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"], "Content-Type": "application/json"}
SKIP = re.compile(r"(wikipedia|youtube|linkedin|facebook|instagram|twitter|x\.com|reddit|quora|indeed|welcometothejungle|pagesjaunes|societe\.com|pappers|amazon|google)\.", re.I)
QUALIF = json.load(open("../data/campaigns/qualif.json"))


def fetch_page(d):
    import html
    for u in (f"https://{d}", f"https://www.{d}"):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=12).read(300000).decode("utf-8", "ignore")
            title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
            meta = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', t, re.I)
            body = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t)))
            return html.unescape(" | ".join(x for x in [title.group(1).strip() if title else "", meta.group(1) if meta else "", body[:1500]] if x))[:2000]
        except Exception:
            continue
    return ""


def post(url, body, headers, timeout=120):
    r = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    return json.loads(urllib.request.urlopen(r, timeout=timeout).read())


def understand(d, company, text):
    prompt = (f"Entreprise : {company} ({d}). Texte du site : {text}\n\nRéponds en JSON : {{\"thematique\": activité en 5 mots, "
              "\"icp_client\": qui achète chez eux, \"motcle\": LE mot-clé Google (2 à 5 mots, en français, sans marque) qu'un client "
              "tape pour trouver ce type de prestataire et qui génère du business, \"prompt\": la question qu'un acheteur poserait à ChatGPT "
              "pour choisir un prestataire de ce type en France (sans citer de marque)}}")
    r = post("https://api.openai.com/v1/chat/completions", {"model": "gpt-4o-mini", "response_format": {"type": "json_object"}, "temperature": 0,
                                                            "messages": [{"role": "user", "content": prompt}]}, OAI)
    return json.loads(r["choices"][0]["message"]["content"])


def serp(kw, own):
    r = post("https://api.dataforseo.com/v3/serp/google/organic/live/regular",
             [{"keyword": kw, "location_code": 2250, "language_code": "fr", "depth": 10}], DFS)
    items = [i for i in (r["tasks"][0]["result"] or [{}])[0].get("items", []) if i.get("type") == "organic"]
    pos = next((i["rank_group"] for i in items if own in (i.get("domain") or "")), None)
    top = next((i for i in items if own not in (i.get("domain") or "") and not SKIP.search(i.get("domain") or "")), None)
    return pos, (top or {}).get("domain", "").removeprefix("www."), (top or {}).get("rank_group"), r["tasks"][0].get("cost", 0)


def volumes(kws):
    r = post("https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
             [{"keywords": kws, "location_code": 2250, "language_code": "fr"}], DFS)
    return {x["keyword"]: x.get("search_volume") for x in (r["tasks"][0]["result"] or [])}, r["tasks"][0].get("cost", 0)


def chatgpt(q, company, d):
    r = post("https://api.openai.com/v1/chat/completions", {"model": "gpt-4o-mini-search-preview", "web_search_options": {"search_context_size": "low",
             "user_location": {"type": "approximate", "approximate": {"country": "FR"}}}, "messages": [{"role": "user", "content": q}]}, OAI, timeout=180)
    ans = r["choices"][0]["message"]["content"]
    cited = company.lower().split()[0] in ans.lower() or d.split(".")[0] in ans.lower()
    ex = post("https://api.openai.com/v1/chat/completions", {"model": "gpt-4o-mini", "response_format": {"type": "json_object"}, "temperature": 0,
              "messages": [{"role": "user", "content": f"Liste en JSON {{\"marques\": [...]}} les entreprises / marques recommandées dans ce texte, dans l'ordre :\n{ans[:4000]}"}]}, OAI)
    return cited, json.loads(ex["choices"][0]["message"]["content"]).get("marques", [])[:5]


mx = int(ARGS[ARGS.index("--max") + 1]) if "--max" in ARGS else 20
codes = [a for a in ARGS if a.startswith("DS-")]
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
todo = []
for c in codes:
    for r in csv.DictReader(open(f"../data/datasets/{c}.csv")):
        d = r["domain"]
        if QUALIF.get(d, {}).get("fit") is True and d not in cache and d not in [t[0] for t in todo]: todo.append((d, r["company"]))
todo = todo[:mx]
print("entreprises", len(todo))


def step1(item):
    d, company = item
    try: return d, company, understand(d, company, fetch_page(d))
    except Exception as e: return d, company, {"error": str(e)[:150]}


with ThreadPoolExecutor(8) as ex:
    base = list(ex.map(step1, todo))
vols, cost = volumes(sorted({b[2]["motcle"].lower() for b in base if b[2].get("motcle")}))
for d, company, u in base:
    if not u.get("motcle"): cache[d] = u; continue
    try:
        pos, conc, conc_rank, c2 = serp(u["motcle"], d); cost += c2
        cited, marques = chatgpt(u["prompt"], company, d)
    except Exception as e:
        cache[d] = dict(u, error=str(e)[:150]); continue
    cache[d] = dict(u, company=company, volume=vols.get(u["motcle"].lower()), position=pos, concurrent_google=conc, concurrent_rank=conc_rank,
                    chatgpt_cite_entreprise=cited, chatgpt_marques=marques)
    print(d, "|", u["motcle"], vols.get(u["motcle"].lower()), "| pos", pos, "| n°1 :", conc, "| ChatGPT :", "cité" if cited else "absent", marques[:3], flush=True)
json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=1)
print("coût DataForSEO", round(cost, 4), "$")
