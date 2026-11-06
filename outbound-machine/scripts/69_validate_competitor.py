"""Valide le concurrent trouvé dans Google (68_lead_checks.py) : est-ce bien une entreprise qui vend la même chose
(et pas un article, un comparatif, un outil ou un média) ? gpt-4o-mini via DataForSEO (≈ 0,0009 $). Sinon, le concurrent
est retiré et le lead reçoit le mail 3 A (sans concurrent). Usage : python 69_validate_competitor.py"""
import json, re
from concurrent.futures import ThreadPoolExecutor
src = open("39_qualify.py").read().split("todo = {}")[0]
g = {"__name__": "x"}; exec(compile(src, "39_qualify.py", "exec"), g)
llm = g["llm"]
P = "../data/datasets/lead_checks.json"
c = json.load(open(P))
SYS = ("You check competitors. Answer ONLY JSON {\"same_business\": true|false}. true only if the website is a company that itself "
       "sells the described service or product to clients (not a blog, listicle, comparison site, marketplace, directory, media, job board, "
       "software tool for a different job, or a huge generic group).")
todo = [d for d, v in c.items() if v.get("competitor_domain") and "competitor_valid" not in v]
print("à valider", len(todo), flush=True)


def run(d):
    v = c[d]
    try:
        res, _ = llm(SYS, f"Service: {v.get('niche')}. Website: {v['competitor_domain']} (name: {v.get('competitor')}).")
        return d, bool(res.get("same_business"))
    except Exception:
        return d, None


with ThreadPoolExecutor(6) as ex:
    for n, (d, ok) in enumerate(ex.map(run, todo), 1):
        c[d]["competitor_valid"] = ok
        if ok is False:
            c[d]["competitor_rejected"] = c[d].pop("competitor"); c[d].pop("competitor_domain", None)
        if n % 200 == 0: json.dump(c, open(P, "w"), ensure_ascii=False); print(n, flush=True)
json.dump(c, open(P, "w"), ensure_ascii=False)
print("gardés", sum(1 for d in todo if c[d].get("competitor_valid")), "/", len(todo))
