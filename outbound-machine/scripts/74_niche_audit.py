"""Audit de la niche de chaque entreprise contre sa page d'accueil (Nathan, 10/11 : « assure-toi que c'est la bonne niche, que tu
as bien compris le site »). gpt-4o-mini lit le titre / la description / le début de la page et répond :
- niche_ok : la niche décrit-elle bien l'offre principale ?
- niche : la bonne niche (2 à 6 mots, dans la langue de la campagne, formulée comme un acheteur la demanderait à ChatGPT) ;
- target_ok : l'entreprise est-elle bien du type visé par la campagne (ex. 205 = cabinet de conseil / compta / M&A / patrimoine) ?
≈ 0,0009 $ / entreprise. Sortie : ../data/datasets/niche_audit.json (cache par domaine).
Usage : python 74_niche_audit.py [--limit N]"""
import json, os, sys
from concurrent.futures import ThreadPoolExecutor

src = open("39_qualify.py").read().split("todo = {}")[0]
g = {"__name__": "x"}; exec(compile(src, "39_qualify.py", "exec"), g)
page, llm = g["page"], g["llm"]
P = "../data/datasets/niche_audit.json"
TARGET = {"201-G": ("en", "B2B software / SaaS / AI product or AI services company"), "202-G": ("en", "consulting or advisory firm"),
          "203-G": ("fr", "éditeur de logiciel SaaS, startup IA / data ou société tech B2B"), "204-G": ("fr", "entreprise B2B (tout secteur)"),
          "205-G": ("fr", "cabinet de conseil, d'expertise comptable, de M&A / transmission ou de gestion de patrimoine (CGP)"),
          "206-G": ("fr", "agence de communication, web, digital, design ou marketing"), "207-G": ("fr", "agence événementielle")}
SYS = ("You audit B2B prospect data. JSON only: {\"niche_ok\": true if the given niche accurately describes the company's MAIN offer, "
       "\"niche\": the correct niche, 2-6 words, lowercase, in the requested language, as a buyer would ask ChatGPT for it "
       "(e.g. 'logiciel de paie pour PME', 'guest engagement software for hospitality'), \"target_ok\": true if the company really is the "
       "target type}. Be strict.")


def run(item):
    d, code, niche = item
    lang, target = TARGET[code]
    site = page(d)[:300]
    if not site:
        return d, {"site": False}
    try:
        r, _ = llm(SYS, f"Language: {lang}. Target type: {target}. Niche: {niche}. Site {d}: {site}")
        return d, dict(r, site=True, code=code, old=niche)
    except Exception as e:
        return d, {"error": str(e)[:80]}


if __name__ == "__main__":
    src66 = open("66_instantly_v5.py").read().split('if __name__ == "__main__":')[0]
    g66 = {"__name__": "x"}; exec(compile(src66, "66_instantly_v5.py", "exec"), g66)
    cache = json.load(open(P)) if os.path.exists(P) else {}
    todo = {}
    for code, ls in g66["leads"]().items():
        for l in ls:
            d = l["website"].lower()
            if d not in cache and d not in todo: todo[d] = (d, code, l["custom_variables"].get("niche") or "")
    items = list(todo.values())
    if "--limit" in sys.argv: items = items[:int(sys.argv[sys.argv.index("--limit") + 1])]
    print("à auditer", len(items), flush=True)
    with ThreadPoolExecutor(16) as ex:
        for k, (d, res) in enumerate(ex.map(run, items), 1):
            cache[d] = res
            if k % 200 == 0: json.dump(cache, open(P, "w"), ensure_ascii=False); print(k, flush=True)
    json.dump(cache, open(P, "w"), ensure_ascii=False)
    v = [cache[i[0]] for i in items]
    print("site lu", sum(1 for x in v if x.get("site")), "/", len(v), "· niche corrigée", sum(1 for x in v if x.get("site") and x.get("niche_ok") is False),
          "· hors cible", sum(1 for x in v if x.get("site") and x.get("target_ok") is False))
