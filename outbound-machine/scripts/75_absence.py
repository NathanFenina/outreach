"""« X ne sort pas sur ChatGPT » : preuve solide (Nathan, 10/11). Le vrai ChatGPT (avec recherche web) ne donne pas toujours la
même liste (SyncSpider : absent au 1er passage, cité au 2e). On pose donc la question au vrai ChatGPT au moins 2 fois, sur la
niche FINALE (après 74_niche_audit.py), et on n'écrit « ne sort pas » que si AUCUN passage ne cite l'entreprise. Dès qu'un
passage la cite, on s'arrête (phrase neutre). Le 1er passage de 73_verify_real.py est réutilisé si la niche n'a pas changé.
Agences S3b : 2 passages des 2 questions par ville. ≈ 0,004 $ / passage.
Sortie : ../data/datasets/absence.json. Usage : python 75_absence.py [--limit N]"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

src = open("73_verify_real.py").read().split("\nif __name__")[0]
g = {"__name__": "x"}; exec(compile(src, "73_verify_real.py", "exec"), g)
chatgpt, cited = g["chatgpt"], g["cited"]
P = "../data/datasets/absence.json"
FR = {"203-G", "204-G", "205-G", "206-G", "207-G"}


def prompt(n, fr):
    return f"Quels sont les meilleurs {n} ? Donne 10 noms d'entreprises." if fr else f"What are the best {n}? Give 10 company names."


def run(item):
    d, company, n, country, fr, prev, s3b_prompts, prev_s3b = item
    name = re.sub(r"[^a-z0-9]", "", (company or d.split(".")[0]).lower())[:12] or d.split(".")[0]
    out = {"niche": n, "runs": list(prev), "same_as_first": bool(prev)}
    tries = 0
    while n and len(out["runs"]) < 2 and not any(out["runs"]):
        txt = chatgpt(prompt(n, fr), country)
        if not txt:
            tries += 1
            if tries >= 3: break
            continue
        out["runs"].append(cited(txt, name, d))
    if s3b_prompts:
        out["s3b_runs"] = list(prev_s3b)
        while len(out["s3b_runs"]) < 2 and not any(out["s3b_runs"]):
            txts = [chatgpt(p, "FR") for p in s3b_prompts]
            if not any(txts): break
            out["s3b_runs"].append(any(cited(x, name, d) for x in txts))
    return d, out


if __name__ == "__main__":
    import csv, glob
    src66 = open("66_instantly_v5.py").read().split('if __name__ == "__main__":')[0]
    g66 = {"__name__": "x"}; exec(compile(src66, "66_instantly_v5.py", "exec"), g66)
    C, A, R = g66["CHECKS"], g66["AGENCY"], g66["REAL"]
    CTRY = {r["domain"].lower(): (r.get("company_country") or "GB").upper() for f in glob.glob("../data/datasets/igor/ready_*.csv") for r in csv.DictReader(open(f))}
    cache = json.load(open(P)) if os.path.exists(P) else {}
    todo = {}
    for code, ls in g66["leads"]().items():
        if code in ("204-G", "206-G"): continue  # S4 et S3a n'ont pas la phrase « ne sort pas »
        for l in ls:
            d, cv = l["website"].lower(), l["custom_variables"]
            n = (cv.get("niche") or "").lower()
            old = cache.get(d) or {}
            done = (len(old.get("runs") or []) >= 2 or any(old.get("runs") or [])) if code != "207-G" else \
                   (len(old.get("s3b_runs") or []) >= 2 or any(old.get("s3b_runs") or []))
            if d in todo or (old and old.get("niche") == n and done): continue
            c, r, a = C.get(d) or {}, R.get(d) or {}, A.get(d) or {}
            same = (c.get("niche") or "").lower() == n
            if code == "207-G":
                if not (a.get("tested") and not a.get("cited")): continue
                prev_s3b = old.get("s3b_runs") or ([r["real_cited_s3b"]] if "real_cited_s3b" in r else [])
                todo[d] = (d, l["company_name"], "", "FR", True, [], a.get("prompts") or [], prev_s3b)
                continue
            if same and c.get("ai_cited"): continue  # déjà cité par gpt-4o-mini : phrase neutre, rien à tester
            prev = (old.get("runs") or []) if old.get("niche") == n and old.get("runs") else ([r["real_cited"]] if same and "real_cited" in r else [])
            todo[d] = (d, l["company_name"], n, "FR" if code in FR else CTRY.get(d, "GB"), code in FR, prev, [], [])
    items = list(todo.values())
    if "--limit" in sys.argv: items = items[:int(sys.argv[sys.argv.index("--limit") + 1])]
    print("à tester", len(items), "· passages déjà faits", sum(len(i[5]) for i in items), flush=True)
    import urllib.request
    def balance():  # solde réel DataForSEO (10/11 : on mesure, on n'estime plus)
        t = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.dataforseo.com/v3/appendix/user_data", headers=g["g"]["DFS"]), timeout=60).read())
        return t["tasks"][0]["result"][0]["money"]["balance"]
    cap = float(sys.argv[sys.argv.index("--budget") + 1]) if "--budget" in sys.argv else 10.0
    b0 = balance(); print("solde de départ", round(b0, 2), "$ · plafond", cap, "$", flush=True)
    with ThreadPoolExecutor(8) as ex:
        for i in range(0, len(items), 100):  # par lots de 100, contrôle du solde entre chaque lot
            for d, res in ex.map(run, items[i:i + 100]): cache[d] = res
            json.dump(cache, open(P, "w"), ensure_ascii=False)
            spent = b0 - balance(); print(i + 100, "· dépensé", round(spent, 2), "$", flush=True)
            if spent >= cap: print("PLAFOND ATTEINT, arrêt"); break
    json.dump(cache, open(P, "w"), ensure_ascii=False)
    v = [cache[i[0]] for i in items]
    print("absents sur 2 passages", sum(1 for x in v if len(x.get("runs") or []) >= 2 and not any(x["runs"])),
          "· cités au moins une fois", sum(1 for x in v if any(x.get("runs") or [])),
          "· agences absentes 2 fois", sum(1 for x in v if len(x.get("s3b_runs") or []) >= 2 and not any(x["s3b_runs"])), "/", sum(1 for x in v if "s3b_runs" in x))
