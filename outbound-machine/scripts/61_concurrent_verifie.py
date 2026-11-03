"""Concurrent VÉRIFIÉ (palier P3b) : Gemini propose le concurrent probable et la thématique (58_gemini_concurrent.py),
puis Google confirme. Recherche Google France sur la thématique (DataForSEO SERP, ≈ 0,002 $), volume de recherche groupé.
« Vérifié » = un concurrent proposé par Gemini est dans le top 10 ET devant l'entreprise (ou l'entreprise est absente).
On n'écrit jamais un concurrent dans un mail sans ce contrôle (règle : aucune donnée inventée).
Sortie : ../data/datasets/concurrent_verifie.json. Usage : python 61_concurrent_verifie.py --n 50"""
import base64, csv, glob, json, os, sys, urllib.request
import outreach_db as db

DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json", "User-Agent": "decupler-outbound"}
OUT = "../data/datasets/concurrent_verifie.json"
COST = [0.0]


def post(path, body):
    for _ in range(3):
        r = urllib.request.Request("https://api.dataforseo.com" + path, data=json.dumps(body).encode(), headers=DFS, method="POST")
        t = json.loads(urllib.request.urlopen(r, timeout=180).read())["tasks"][0]
        COST[0] += t.get("cost") or 0
        if t["status_code"] == 20000: return (t.get("result") or [{}])[0] or {}
    return {}


def base(d):
    return d.lower().removeprefix("www.").split("/")[0]


def candidates(n):
    """Entreprises 1.1 / 1.2 du marché principal, hors Microsoft, avec un email utilisable (Moltsets A/B ou FullEnrich)."""
    BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
    dnc = {r["domain"].lower() for r in db.select("do_not_contact", "domain,reason") if r["reason"] in BLOCK and r["domain"]}
    Q = json.load(open("../data/campaigns/qualif.json")); M = json.load(open("../data/datasets/enriched_moltsets.json"))
    F = json.load(open("../data/datasets/enriched_fullenrich.json"))
    test20 = set(json.load(open("../data/datasets/intent_seo.json")))
    doms = []
    for fn in sorted(glob.glob("../data/datasets/DS-104-1.[12]-FR-P4*.csv")):
        for r in csv.DictReader(open(fn)):
            d = r["domain"].lower()
            if d in doms or d in test20 or d in dnc or r["esp"] == "microsoft" or Q.get(r["domain"], {}).get("fit") is not True: continue
            m = M.get(r["linkedin_url"]) or {}
            if (m.get("email") and m.get("risk_score") in ("A", "B")) or (F.get(r["linkedin_url"]) or {}).get("usable"): doms.append(d)
    return doms[:n]


if __name__ == "__main__":
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 50
    doms = candidates(n)
    G = json.load(open("../data/datasets/gemini_vars.json"))
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    kws = {}
    for d in doms:
        g = G.get(d) or {}
        kw = (g.get("thematique") or "").split(",")[0].strip().lower()
        if not kw or g.get("error"): out[d] = {"statut": "pas de thématique"}; continue
        kws[d] = kw
        items = (post("/v3/serp/google/organic/live/regular", [{"keyword": kw, "location_code": 2250, "language_code": "fr", "depth": 10}]).get("items") or [])
        org = [(i.get("rank_group"), base(i.get("domain") or "")) for i in items if i.get("type") == "organic"]
        pos_me = next((p for p, x in org if x.endswith(base(d))), None)
        conc = [base(c.get("site") or "") for c in g.get("concurrents") or [] if c.get("site")]
        ahead = [(p, x) for p, x in org for c in conc if c and (x == c or x.endswith("." + c)) and (pos_me is None or p < pos_me)]
        out[d] = {"motcle": kw, "position_entreprise": pos_me, "concurrents_gemini": conc, "top3": [x for _, x in org[:3]],
                  "concurrent_verifie": ahead[0][1] if ahead else None, "position_concurrent": ahead[0][0] if ahead else None,
                  "statut": "vérifié" if ahead else "non confirmé"}
    if kws:  # volumes en un seul appel groupé
        r = urllib.request.Request("https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live", data=json.dumps(
            [{"keywords": sorted(set(kws.values())), "location_code": 2250, "language_code": "fr"}]).encode(), headers=DFS, method="POST")
        t = json.loads(urllib.request.urlopen(r, timeout=180).read())["tasks"][0]; COST[0] += t.get("cost") or 0
        v = {x["keyword"]: x.get("search_volume") for x in t.get("result") or []}
        for d, kw in kws.items(): out[d]["volume"] = v.get(kw)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    sel = {d: out[d] for d in doms}
    print("entreprises", len(doms), Counter(x["statut"] for x in sel.values()), "· coût", round(COST[0], 4), "$")
