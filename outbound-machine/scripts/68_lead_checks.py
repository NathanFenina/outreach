"""Vérifications par entreprise pour que les phrases de la V6 soient VRAIES (Igor : la personnalisation ne marche que si
elle est réelle ; règle Nathan : aucune donnée inventée). Pour chaque domaine :
1. Test IA : on demande à ChatGPT (gpt-4o-mini via DataForSEO, ≈ 0,0009 $) « les meilleurs {niche} » → l'entreprise est-elle citée ?
2. Mini-audit de la page d'accueil (gratuit) : données structurées, FAQ, llms.txt, meta description, H1, titre → liste de
   corrections concrètes (« quick wins »). On n'écrit « j'ai trouvé 3 quick wins » que s'il y en a au moins 3.
3. Google (DataForSEO SERP, ≈ 0,002 $) sur {niche} dans le pays de l'entreprise → l'entreprise est-elle dans le top 10 ?
   1er vrai résultat (hors annuaires, médias, places de marché) = concurrent pour le mail 3 B.
Sortie : ../data/datasets/lead_checks.json (cache par domaine). Usage : python 68_lead_checks.py <csv...> [--limit N]"""
import base64, csv, html as H, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json", "User-Agent": "decupler-outbound"}
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
CACHE = "../data/datasets/lead_checks.json"
NICHE = {}
for f in ("../data/datasets/niche_fr.json", "../data/datasets/niche.json"):
    if os.path.exists(f): NICHE.update(json.load(open(f)))
LOC = {"GB": (2826, "en"), "UK": (2826, "en"), "DE": (2276, "de"), "AT": (2040, "de"), "CH": (2756, "de"), "FR": (2250, "fr"), "BE": (2056, "fr")}
NOT_COMPETITOR = re.compile(r"(wikipedia|linkedin|facebook|youtube|reddit|quora|medium|g2\.com|capterra|getapp|trustpilot|clutch|sortlist|"
                            r"glassdoor|indeed|crunchbase|gartner|forbes|techradar|zapier\.com/blog|hubspot\.com/blog|amazon|google\.|apple\.com|"
                            r"pagesjaunes|societe\.com|lesechos|journaldunet|01net|bfm|lemonde|lefigaro|gouv|europa\.eu|\.edu|appvizer|"
                            r"softwareadvice|comparatif|selectra|codeur|malt)", re.I)


def post(path, body):
    try:
        t = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.dataforseo.com" + path, data=json.dumps(body).encode(),
                                                                     method="POST", headers=DFS), timeout=120).read())["tasks"][0]
        return t
    except Exception:
        return {}


def audit(d):
    wins = []
    try:
        t = urllib.request.urlopen(urllib.request.Request(f"https://{d}", headers=UA), timeout=12).read(500000).decode("utf-8", "ignore")
    except Exception:
        return None
    ld = re.findall(r'<script[^>]+application/ld\+json[^>]*>([\s\S]*?)</script>', t, re.I)
    types = set(re.findall(r'"@type"\s*:\s*"([^"]+)"', " ".join(ld)))
    if not ld: wins.append("aucune donnée structurée (schema.org)")
    elif not types & {"Organization", "Corporation", "LocalBusiness", "ProfessionalService", "SoftwareApplication", "Product", "Service"}:
        wins.append("pas de balisage Organization / Service lisible par les IA")
    if "FAQPage" not in types and not re.search(r"faq|questions fréquentes|frequently asked", t, re.I): wins.append("pas de FAQ qui répond aux questions des acheteurs")
    if not re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'][^"\']{50,}', t, re.I): wins.append("meta description absente ou trop courte")
    h1 = re.findall(r"<h1[^>]*>([\s\S]*?)</h1>", t, re.I)
    if len(h1) != 1: wins.append("titre H1 absent ou multiple")
    try:
        r = urllib.request.urlopen(urllib.request.Request(f"https://{d}/llms.txt", headers=UA), timeout=8)
        if r.status != 200 or b"<html" in r.read(2000).lower(): wins.append("pas de fichier llms.txt pour les IA")
    except Exception:
        wins.append("pas de fichier llms.txt pour les IA")
    return wins


def check(item):
    d, country, company = item
    n = ((NICHE.get(d) or {}).get("niche") or "").strip()
    out = {"niche": n, "audit": audit(d)}
    name = re.sub(r"[^a-z0-9]", "", (company or d.split(".")[0]).lower())[:12] or d.split(".")[0]
    if n:
        lang = LOC.get(country, (2826, "en"))[1]
        prompt = {"fr": f"Quels sont les meilleurs {n} ? Donne 10 noms d'entreprises.", "de": f"What are the best {n}? Give 10 company names.",
                  "en": f"What are the best {n}? Give 10 company names."}[lang]
        t = post("/v3/ai_optimization/chat_gpt/llm_responses/live", [{"user_prompt": prompt, "model_name": "gpt-4o-mini", "web_search": False}])
        txt = "".join(s.get("text", "") for it in ((t.get("result") or [{}])[0].get("items") or []) for s in it.get("sections", []))
        out["ai_tested"] = bool(txt)
        out["ai_cited"] = bool(txt) and (name in re.sub(r"[^a-z0-9]", "", txt.lower()) or d.split(".")[0] in txt.lower())
        out["ai_prompt"] = prompt
        loc, lg = LOC.get(country, (2826, "en"))
        t = post("/v3/serp/google/organic/live/regular", [{"keyword": n, "location_code": loc, "language_code": lg, "depth": 10}])
        items = [i for i in ((t.get("result") or [{}])[0].get("items") or []) if i.get("type") == "organic"]
        def host(i):  # Google masque l'URL (google.com/goto) : le vrai domaine est dans le fil d'Ariane
            m = re.match(r"https?://([^/ ›]+)", i.get("breadcrumb") or "")
            return (m.group(1) if m else (i.get("domain") or "")).lower().removeprefix("www.")
        doms = [(i.get("rank_group"), host(i)) for i in items]
        out["serp_ok"] = bool(items)
        out["serp_pos"] = next((p for p, x in doms if x.endswith(d)), None)
        comp = next(((p, x, i.get("website_name") or x) for (p, x), i in zip(doms, items) if not NOT_COMPETITOR.search(x) and not x.endswith(d)), None)
        if comp and (out["serp_pos"] is None or comp[0] < out["serp_pos"]):
            out["competitor_domain"] = comp[1]
            out["competitor"] = (comp[2] or comp[1]).strip()[:40]
    return d, out


if __name__ == "__main__":
    files = [a for a in sys.argv[1:] if a.endswith(".csv")]
    lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = {}
    for f in files:
        for r in csv.DictReader(open(f)):
            d = (r.get("domain") or r.get("website") or "").lower()
            if d and d not in cache and d not in todo:
                todo[d] = (d, (r.get("company_country") or r.get("country") or "FR").upper(), r.get("company_name") or r.get("company"))
    items = list(todo.values())[:lim] if lim else list(todo.values())
    print("à vérifier", len(items), flush=True)
    with ThreadPoolExecutor(6) as ex:
        for k, (d, res) in enumerate(ex.map(check, items), 1):
            cache[d] = res
            if k % 50 == 0: json.dump(cache, open(CACHE, "w"), ensure_ascii=False); print(k, flush=True)
    json.dump(cache, open(CACHE, "w"), ensure_ascii=False)
    sel = [cache[i[0]] for i in items]
    print("absents de l'IA", sum(1 for x in sel if x.get("ai_tested") and not x.get("ai_cited")), "/", sum(1 for x in sel if x.get("ai_tested")),
          "· ≥ 3 quick wins", sum(1 for x in sel if len(x.get("audit") or []) >= 3), "/", len(sel),
          "· hors top 10 Google", sum(1 for x in sel if x.get("serp_ok") and not x.get("serp_pos")),
          "· concurrent trouvé", sum(1 for x in sel if x.get("competitor")))
