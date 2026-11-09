"""Mail 3 B (« [concurrent] plutôt que [entreprise] ») : validation STRICTE du concurrent trouvé par 68_lead_checks.py,
après les erreurs vues par Nathan le 09/11 (vertura.fr pour Joy, degiro.ch pour EQNX). On ne garde le concurrent que si :
1. la niche est précise (au moins 2 mots, pas un fonds / investissement) ;
2. gpt-4o-mini, avec la page d'accueil des DEUX sites sous les yeux, confirme que la niche décrit bien l'offre principale de
   l'entreprise, que le concurrent est une vraie entreprise (pas un média, annuaire, comparatif, outil) ET qu'il vend la même
   chose au même type de client.
≈ 0,0009 $ / entreprise. Sortie : ../data/datasets/competitor_strict.json (cache par domaine).
Usage : python 71_competitor_strict.py [--limit N]"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

src = open("39_qualify.py").read().split("todo = {}")[0]
g = {"__name__": "x"}; exec(compile(src, "39_qualify.py", "exec"), g)
page, llm = g["page"], g["llm"]
P = "../data/datasets/competitor_strict.json"
FUND = re.compile(r"invest|capital|fonds|fund|venture|private equity|banque|bank", re.I)
SYS = ("You check if B is a direct competitor of A. JSON only: {\"niche_ok\": true if the query describes A's main offer, "
       "\"b_company\": true if B is a company selling its own product/service (not media, blog, directory, comparison, marketplace, "
       "job board, school, public body), \"same\": true if B sells the same kind of product/service as A to the same kind of client}. "
       "Be strict: false if unsure.")


def run(item):
    d, v = item
    n = (v.get("niche") or "").strip()
    if len(n.split()) < 2 or FUND.search(n):
        return d, {"ok": False, "why": "niche vague ou finance"}
    a, b = page(d)[:190], page(v["competitor_domain"])[:190]
    if not a or not b:
        return d, {"ok": False, "why": "site inaccessible"}
    try:
        r, _ = llm(SYS, f"Query: {n}\nA ({d}): {a}\nB ({v['competitor_domain']}): {b}")
    except Exception as e:
        return d, {"ok": False, "why": "erreur " + str(e)[:60]}
    return d, dict(r, ok=bool(r.get("niche_ok") and r.get("b_company") and r.get("same")))


if __name__ == "__main__":
    C = json.load(open("../data/datasets/lead_checks.json"))
    cache = json.load(open(P)) if os.path.exists(P) else {}
    todo = [(d, v) for d, v in C.items() if v.get("competitor_domain") and d not in cache]
    if "--limit" in sys.argv: todo = todo[:int(sys.argv[sys.argv.index("--limit") + 1])]
    print("à valider", len(todo), flush=True)
    with ThreadPoolExecutor(6) as ex:
        for k, (d, res) in enumerate(ex.map(run, todo), 1):
            cache[d] = dict(res, competitor=C[d]["competitor_domain"], niche=C[d].get("niche"))
            if k % 100 == 0: json.dump(cache, open(P, "w"), ensure_ascii=False); print(k, flush=True)
    json.dump(cache, open(P, "w"), ensure_ascii=False)
    print("gardés", sum(1 for x in cache.values() if x.get("ok")), "/", len(cache))
    for d in ("joy.io", "eqnx.vc"):
        if d in cache: print(d, cache[d])
