"""Repêchage des entreprises écartées « hors du sous-ICP visé » : la recherche Lemlist par mots-clés range parfois un
cabinet de conseil dans « éditeurs SaaS », etc. Au lieu de les jeter, on demande dans quel sous-ICP de la cible elles
tombent (ou aucun). Celles qui tombent dans un sous-ICP ciblé repassent fit=True avec ce nouveau sous-ICP (champ
sub_icp_final), puis passent dans Moltsets. gpt-4o-mini via DataForSEO (≈ 0,0009 $ / entreprise).
Usage : python 67_requalify.py [--limit N]"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor

src = open("39_qualify.py").read().split("todo = {}")[0]
g = {"__name__": "x"}; exec(compile(src, "39_qualify.py", "exec"), g)
page, llm = g["page"], g["llm"]
CACHE = "../data/campaigns/qualif.json"
ICPS = {"1.1": "éditeur de logiciel SaaS B2B", "1.2": "startup IA / data", "1.5": "cabinet de conseil (stratégie, management, IT, RH)",
        "1.6": "cabinet d'expertise comptable / DAF externalisé", "1.7": "conseil M&A / transmission", "1.8": "gestion de patrimoine (CGP)",
        "1.9": "agence marketing, web, SEO, communication", "1.10": "agence événementielle / conférenciers", "4.1": "hôtel indépendant",
        "4.2": "spa / institut / bien-être"}
SYS = ("Tu ranges des entreprises françaises dans une cible. JSON uniquement : {\"sub_icp\": code ou null, \"why\": 5 mots}. Codes : "
       + "; ".join(f"{k} {v}" for k, v in ICPS.items()) + ". null si aucun, si grand groupe (> 1000 salariés), fonds, média, école, association, administration.")

q = json.load(open(CACHE))
todo = [d for d, v in q.items() if v.get("fit") is False and re.search(r"hors du sous-icp", (v.get("exclude_reason") or ""), re.I)
        and "requalified" not in v]
if "--limit" in sys.argv: todo = todo[:int(sys.argv[sys.argv.index("--limit") + 1])]
print("à repêcher", len(todo), flush=True)


def run(d):
    try:
        res, _ = llm(SYS, f"Entreprise : {d}. Site : " + (page(d) or "(inaccessible)"))
        return d, res
    except Exception as e:
        return d, {"error": str(e)[:80]}


ok = 0
with ThreadPoolExecutor(6) as ex:
    for n, (d, res) in enumerate(ex.map(run, todo), 1):
        code = res.get("sub_icp") if isinstance(res, dict) else None
        q[d]["requalified"] = res
        if code in ICPS:
            q[d].update(fit=True, sub_icp_final=code); ok += 1
        if n % 100 == 0: json.dump(q, open(CACHE, "w"), ensure_ascii=False, indent=0); print(n, "repêchées", ok, flush=True)
json.dump(q, open(CACHE, "w"), ensure_ascii=False, indent=0)
print("FIN repêchées", ok, "/", len(todo))
