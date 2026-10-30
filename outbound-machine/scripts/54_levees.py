"""Palier P1 (a levé < 6 mois) : liste des startups françaises financées, extraite des récaps hebdomadaires de levées
(Maddyness ; FrenchWeb à ajouter) avec Firecrawl (extraction JSON). Puis domaine, sous-ICP et signal « recrute » via Lemlist.
Sortie : ../data/datasets/levees.json (cache par URL d'article). Usage : python 54_levees.py <url> ..."""
import json, os, sys, urllib.request

KEYS = [os.environ.get("FIRECRAWL_API_KEY_1"), os.environ.get("FIRECRAWL_API_KEY_2")]
CACHE = "../data/datasets/levees.json"
SCHEMA = {"type": "object", "properties": {"startups": {"type": "array", "items": {"type": "object", "properties": {
    "nom": {"type": "string"}, "montant": {"type": "string"}, "secteur": {"type": "string"}, "activite": {"type": "string"},
    "site": {"type": "string"}, "ville": {"type": "string"}}, "required": ["nom"]}}}}


def scrape(url):
    body = {"url": url, "formats": ["json"], "onlyMainContent": True,
            "jsonOptions": {"schema": SCHEMA, "prompt": "Liste chaque startup ou entreprise qui a levé des fonds dans l'article : nom, montant, "
                                                       "secteur, activité en une phrase, site web si cité (ou lien de l'article vers elle), ville."}}
    for k in KEYS:  # 2 clés : si l'une est bloquée, on passe à l'autre
        if not k: continue
        try:
            r = urllib.request.Request("https://api.firecrawl.dev/v1/scrape", data=json.dumps(body).encode(), method="POST",
                                       headers={"Authorization": "Bearer " + k, "Content-Type": "application/json"})
            d = json.loads(urllib.request.urlopen(r, timeout=180).read())
            if d.get("success"): return d["data"].get("json", {}).get("startups", [])
        except urllib.error.HTTPError as e:
            print(url, "clé refusée", e.code, flush=True)
    return None


cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
for u in sys.argv[1:]:
    if u in cache: continue
    s = scrape(u)
    if s is not None:
        cache[u] = s; json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=1)
        print(u.split("/")[-1][:60], len(s), "startups", flush=True)
print("total", sum(len(v) for v in cache.values()), "startups sur", len(cache), "articles")
