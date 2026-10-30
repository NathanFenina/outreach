"""Qualifie chaque entreprise d'une liste finale avant d'acheter des emails : page d'accueil (titre, meta, début du texte)
puis classement par un petit modèle OpenAI (≈ 0,0001 $ / entreprise). Écarte : hors cible, concurrents (agences SEO/marketing
hors sous-ICP 1.9), fonds d'investissement, médias, grands groupes. Écrit ../data/campaigns/qualif.json (cache)."""
import csv, glob, json, os, re, sys, html, urllib.request
from concurrent.futures import ThreadPoolExecutor
from icp_catalog import SEGMENTS
SEG = {s["code"]: s["name"] for s in SEGMENTS}
CACHE = "../data/campaigns/qualif.json"
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}


def page(d):
    for u in (f"https://{d}", f"https://www.{d}", f"http://{d}"):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=12).read(300000).decode("utf-8", "ignore")
            title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
            meta = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', t, re.I)
            body = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t)))
            return html.unescape(" | ".join(x for x in [title.group(1).strip() if title else "", meta.group(1) if meta else "", body[:700]] if x))[:1200]
        except Exception:
            continue
    return ""


SYS = ("Tu qualifies des prospects B2B pour une agence SEO/GEO. Réponds UNIQUEMENT en JSON : {\"fit\": true|false, \"sub_icp\": code ou null, "
       "\"exclude_reason\": null ou raison courte}. fit=false si : hors du sous-ICP visé ; agence SEO/marketing/web (concurrent) sauf "
       "sous-ICP 1.9 ; fonds d'investissement ; média ; école ou université ; association ; grand groupe (> 1000 salariés) ; site "
       "inaccessible et nom qui ne prouve pas l'activité.")


def classify(d, company, icp, text):
    head = f"Entreprise : {company} ({d}). Sous-ICP visé : {icp} {SEG.get(icp, '')}. Site : "
    return llm(SYS, (head + (text or "(site inaccessible)"))[:495])


DFS = {"Authorization": "Basic " + __import__("base64").b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json"}


def llm(system, prompt):
    """gpt-4o-mini via DataForSEO (≈ 0,0009 $ / appel ; le compte OpenAI direct est à 0 crédit depuis le 29/10)."""
    # limites DataForSEO : 500 caractères pour system_message et pour user_prompt
    body = json.dumps([{"system_message": system[:495], "user_prompt": prompt[:495], "model_name": "gpt-4o-mini", "web_search": False}]).encode()
    for i in range(3):  # résultat vide ponctuel côté DataForSEO : on réessaie
        req = urllib.request.Request("https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_responses/live", data=body, method="POST", headers=DFS)
        t = json.loads(urllib.request.urlopen(req, timeout=120).read())["tasks"][0]
        if t.get("result"): break
    txt = "".join(sec.get("text", "") for it in t["result"][0]["items"] for sec in it.get("sections", []))
    return json.loads(re.search(r"\{[\s\S]*\}", txt).group(0)), round(t.get("cost", 0) * 1e6)


todo = {}
for f in (sys.argv[1:] or glob.glob("../data/campaigns/final_*.csv")):  # ou les fichiers passés en argument (datasets DS-*)
    for r in csv.DictReader(open(f)):
        if r["domain"] not in cache: todo[r["domain"]] = (r["company"], r["icp_code"])
print("à qualifier :", len(todo))


def run(item):
    d, (company, icp) = item
    try:
        res, tok = classify(d, company, icp, page(d)); res["tokens"] = tok; return d, res
    except Exception as e:
        return d, {"fit": None, "error": str(e)[:120]}


with ThreadPoolExecutor(6) as ex:
    for n, (d, res) in enumerate(ex.map(run, todo.items()), 1):
        cache[d] = res
        if n % 50 == 0:  # sauvegarde au fil de l'eau : un arrêt du conteneur ne fait plus tout perdre
            json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=0); print(n, "/", len(todo), flush=True)
json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=0)
tok = sum(v.get("tokens", 0) for v in cache.values())
from collections import Counter
print("fit :", Counter(str(v.get("fit")) for v in cache.values()), "· coût cumulé ≈", round(tok * 0.3 / 1e6, 3), "$ (OpenAI) / micro-dollars DataForSEO dans tokens")
print(Counter(v.get("exclude_reason") for v in cache.values() if v.get("fit") is False).most_common(12))
