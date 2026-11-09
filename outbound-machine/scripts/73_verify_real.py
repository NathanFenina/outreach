"""Contre-vérification « comme un humain » avant lancement (Nathan, 09/11 : 5Mins est 1er sur Google et cité par l'IA,
alors que le mail disait l'inverse). Deux sources de vérité, refaites fraîches :
1. ChatGPT réel (DataForSEO chat_gpt/llm_scraper = l'interface ChatGPT avec recherche web, ≈ 0,004 $) sur la même question
   que le mail 1 → « real_cited ». La phrase « X ne sort pas » n'est écrite que si X est absent de gpt-4o-mini ET du vrai ChatGPT.
2. Google frais, 20 résultats, dans le pays du lead (≈ 0,003 $) → « g20_pos » (position de l'entreprise) et « g5 » (les 5 premiers
   domaines, avec un drapeau « article » si l'URL est un blog / un comparatif). Le mail 3 B (concurrent) n'est écrit que si
   l'entreprise est absente des 20 premiers ET le concurrent est dans les 5 premiers avec une page commerciale (pas un article).
   « Plusieurs opportunités organiques non adressées » seulement si l'entreprise est absente des 20 premiers.
Agences S3b : les 2 questions par ville, sur le vrai ChatGPT → « real_cited_s3b ».
Sortie : ../data/datasets/verify_real.json (cache par domaine). Usage : python 73_verify_real.py [--limit N]"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

src = open("68_lead_checks.py").read().split("if __name__")[0]
g = {"__name__": "x"}; exec(compile(src, "68_lead_checks.py", "exec"), g)
post, LOC, NOT_COMPETITOR = g["post"], g["LOC"], g["NOT_COMPETITOR"]
P = "../data/datasets/verify_real.json"
ARTICLE = re.compile(r"/(blog|blogs|article|articles|news|insights|resources|guide|guides|magazine|actualites?|ressources)/|"
                     r"best-|top-\d|meilleur|comparatif|vs-|alternatives?", re.I)


def chatgpt(q, country):
    loc, lg = LOC.get(country, (2826, "en"))
    t = post("/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced", [{"keyword": q[:500], "location_code": loc, "language_code": lg}])
    r = (t.get("result") or [None])[0] or {}
    return (r.get("markdown") or json.dumps(r.get("items") or "")) if r else ""


def cited(txt, name, d):
    return bool(txt) and (bool(name) and name in re.sub(r"[^a-z0-9]", "", txt.lower()) or d.split(".")[0] in txt.lower())


def host(i):
    m = re.match(r"https?://([^/ ›]+)", i.get("breadcrumb") or "")
    return (m.group(1) if m else (i.get("domain") or "")).lower().removeprefix("www.")


def run(item):
    d, country, company, prompt, niche, s3b_prompts = item
    name = re.sub(r"[^a-z0-9]", "", (company or d.split(".")[0]).lower())[:12] or d.split(".")[0]
    out = {}
    if prompt:
        txt = chatgpt(prompt, country)
        out.update(real_tested=bool(txt), real_cited=cited(txt, name, d))
    if s3b_prompts:
        txts = [chatgpt(p, "FR") for p in s3b_prompts]
        out.update(real_tested_s3b=sum(1 for x in txts if x), real_cited_s3b=any(cited(x, name, d) for x in txts))
    if niche:
        loc, lg = LOC.get(country, (2826, "en"))
        t = post("/v3/serp/google/organic/live/regular", [{"keyword": niche, "location_code": loc, "language_code": lg, "depth": 20}])
        items = [i for i in ((t.get("result") or [{}])[0].get("items") or []) if i.get("type") == "organic"]
        doms = [(i.get("rank_group"), host(i), (i.get("breadcrumb") or "") + " " + (i.get("url") or "") + " " + (i.get("title") or "")) for i in items]
        out.update(g_ok=bool(items), g20_pos=next((p for p, x, _ in doms if x.endswith(d)), None),
                   g5=[{"pos": p, "domain": x, "article": bool(ARTICLE.search(u)), "directory": bool(NOT_COMPETITOR.search(x))} for p, x, u in doms if p and p <= 5])
    return d, out


if __name__ == "__main__":
    src66 = open("66_instantly_v5.py").read().split('if __name__ == "__main__":')[0]
    g66 = {"__name__": "x"}; exec(compile(src66, "66_instantly_v5.py", "exec"), g66)
    C, A = g66["CHECKS"], g66["AGENCY"]
    cache = json.load(open(P)) if os.path.exists(P) else {}
    import csv, glob
    CTRY = {r["domain"].lower(): (r.get("company_country") or "GB").upper() for f in glob.glob("../data/datasets/igor/ready_*.csv") for r in csv.DictReader(open(f))}
    todo = {}
    for code, ls in g66["leads"]().items():
        for l in ls:
            d, cv = l["website"].lower(), l["custom_variables"]
            if d in cache or d in todo: continue
            c = C.get(d) or {}
            country = "FR" if code in ("203-G", "204-G", "205-G", "206-G", "207-G") else CTRY.get(d, "GB")
            need_ai = c.get("ai_tested") and not c.get("ai_cited")
            need_g = False and cv.get("m3_variant") == "B"  # 09/11 : Google trop instable (4 relevés = 4 top 10 différents), plus aucune phrase Google or "ne sont pas encore adressées" in cv.get("m3a", "") or "isn't covering" in cv.get("m3a", "")
            a = A.get(d) or {}
            need_s3b = code == "207-G" and a.get("tested") and not a.get("cited")
            if need_ai or need_g or need_s3b:
                todo[d] = (d, country, l["company_name"], c.get("ai_prompt") if need_ai else None, c.get("niche") if need_g else None,
                           a.get("prompts") if need_s3b else None)
    items = list(todo.values())
    if "--limit" in sys.argv: items = items[:int(sys.argv[sys.argv.index("--limit") + 1])]
    print("à contre-vérifier", len(items), "· ChatGPT", sum(1 for i in items if i[3]), "· Google", sum(1 for i in items if i[4]),
          "· agences", sum(1 for i in items if i[5]), flush=True)
    with ThreadPoolExecutor(16) as ex:
        for k, (d, res) in enumerate(ex.map(run, items), 1):
            cache[d] = res
            if k % 100 == 0: json.dump(cache, open(P, "w"), ensure_ascii=False); print(k, flush=True)
    json.dump(cache, open(P, "w"), ensure_ascii=False)
    v = [cache[i[0]] for i in items]
    print("ChatGPT réel : cités alors que gpt-4o-mini disait absent", sum(1 for x in v if x.get("real_cited")), "/", sum(1 for x in v if x.get("real_tested")),
          "· Google : dans le top 20", sum(1 for x in v if x.get("g20_pos")), "/", sum(1 for x in v if x.get("g_ok")),
          "· agences citées", sum(1 for x in v if x.get("real_cited_s3b")), "/", sum(1 for x in v if x.get("real_tested_s3b")))
    if "5mins.ai" in cache: print("5mins.ai", cache["5mins.ai"])
