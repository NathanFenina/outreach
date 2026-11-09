"""Agences (campagnes 206 / 207) : 1) l'agence vend-elle déjà du SEO ? (si oui = concurrente, exclue) et quel type d'agence
(page d'accueil + gpt-4o-mini) ; 2) deux questions réelles à ChatGPT (« meilleure {type} à {ville} »), pour n'écrire
« vous ne remontez pas sur les 2 questions que j'ai lancées sur ChatGPT » que si c'est vrai. ≈ 0,003 $ / agence.
Sortie : ../data/datasets/agency_checks.json. Usage : python 70_agency_checks.py <csv domain,company,city>"""
import csv, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

src = open("39_qualify.py").read().split("todo = {}")[0]
g = {"__name__": "x"}; exec(compile(src, "39_qualify.py", "exec"), g)
page, llm = g["page"], g["llm"]
P = "../data/datasets/agency_checks.json"
SYS = ("Tu classes des agences françaises. JSON uniquement : {\"type\": type d'agence au singulier, 2 à 4 mots, minuscules (ex. "
       "\"agence de communication\", \"agence événementielle\", \"agence web\", \"studio de design\"), \"vend_seo\": true si l'agence vend du "
       "référencement / SEO / SEA / GEO à ses clients, sinon false, \"digitale\": true si elle fait surtout du web / digital / marketing en ligne}.")


def run(item):
    d, company, city = item
    try:
        info, _ = llm(SYS, f"Agence : {company} ({d}). Site : " + (page(d) or "(inaccessible)"))
    except Exception as e:
        return d, {"error": str(e)[:80]}
    t = (info.get("type") or "agence de communication").strip().lower()
    out = dict(info, type=t, city=city)
    if city:
        prompts = [f"Quelles sont les meilleures {t.replace('agence', 'agences', 1) if t.startswith('agence') else t} à {city} ?",
                   f"Quelle {t} me recommandes-tu à {city} ? Donne des noms."]
        answers = []
        for p in prompts:
            try:
                body = json.dumps([{"user_prompt": p, "model_name": "gpt-4o-mini", "web_search": False}]).encode()
                import urllib.request
                res = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_responses/live",
                                                                               data=body, method="POST", headers=g["DFS"]), timeout=120).read())["tasks"][0]
                answers.append("".join(s.get("text", "") for it in (res.get("result") or [{}])[0].get("items") or [] for s in it.get("sections", [])))
            except Exception:
                answers.append("")
        name = re.sub(r"[^a-z0-9]", "", (company or "").lower())[:12]
        tested = [a for a in answers if a]
        out.update(prompts=prompts, tested=len(tested), cited=any(name and name in re.sub(r"[^a-z0-9]", "", a.lower()) or d.split(".")[0] in a.lower() for a in tested))
    return d, out


if __name__ == "__main__":
    cache = json.load(open(P)) if os.path.exists(P) else {}
    todo = [(r["domain"], r["company"], r.get("city") or "") for r in csv.DictReader(open(sys.argv[1])) if r["domain"] not in cache]
    print("à vérifier", len(todo), flush=True)
    with ThreadPoolExecutor(6) as ex:
        for d, res in ex.map(run, todo): cache[d] = res
    json.dump(cache, open(P, "w"), ensure_ascii=False)
    v = [cache[t[0]] for t in todo]
    print("vendent du SEO", sum(1 for x in v if x.get("vend_seo")), "/", len(v), "· digitales", sum(1 for x in v if x.get("digitale")),
          "· testées", sum(1 for x in v if x.get("tested")), "· absentes de ChatGPT", sum(1 for x in v if x.get("tested") and not x.get("cited")))
