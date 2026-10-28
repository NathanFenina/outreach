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


def classify(d, company, icp, text):
    prompt = (f"Entreprise : {company} ({d}). Sous-ICP visé : {icp} {SEG.get(icp, '')}.\nTexte du site : {text or '(site inaccessible)'}\n\n"
              "Réponds en JSON {\"fit\": true/false, \"sub_icp\": code du sous-ICP le plus juste parmi " + ", ".join(SEG) +
              " ou null, \"exclude_reason\": null ou une raison courte}. fit=false si : hors du sous-ICP, agence SEO / marketing / web "
              "(concurrent) sauf si le sous-ICP est 1.9, fonds d'investissement, média, association, grand groupe (> 1000 salariés), "
              "site inaccessible ET nom qui ne prouve pas l'activité.")
    body = json.dumps({"model": "gpt-4o-mini", "response_format": {"type": "json_object"}, "temperature": 0,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=body, method="POST",
                                 headers={"Authorization": "Bearer " + (os.environ.get("OPENAI_API_KEY") or os.environ["OPEN_AI_KEY"]), "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=60).read())
    return json.loads(r["choices"][0]["message"]["content"]), r["usage"]["total_tokens"]


todo = {}
for f in glob.glob("../data/campaigns/final_*.csv"):
    for r in csv.DictReader(open(f)):
        if r["domain"] not in cache: todo[r["domain"]] = (r["company"], r["icp_code"])
print("à qualifier :", len(todo))


def run(item):
    d, (company, icp) = item
    try:
        res, tok = classify(d, company, icp, page(d)); res["tokens"] = tok; return d, res
    except Exception as e:
        return d, {"fit": None, "error": str(e)[:120]}


with ThreadPoolExecutor(12) as ex:
    for d, res in ex.map(run, todo.items()):
        cache[d] = res
json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=0)
tok = sum(v.get("tokens", 0) for v in cache.values())
from collections import Counter
print("fit :", Counter(str(v.get("fit")) for v in cache.values()), "· tokens", tok, "· coût ≈", round(tok * 0.3 / 1e6, 3), "$")
print(Counter(v.get("exclude_reason") for v in cache.values() if v.get("fit") is False).most_common(12))
