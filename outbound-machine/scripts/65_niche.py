"""Variable {{niche}} (hyper-personnalisation demandée par Igor) : sous-industrie précise en 2 à 5 mots, tirée de la
description de l'entreprise (dataset UltB) ou de sa page d'accueil (nos leads), par Gemini via DataForSEO (≈ 0,0014 $).
Ex. « CRM software for SMEs », « logiciel de paie pour TPE ». Vide si pas sûr → repli « your market » / « votre marché ».
Sortie : ../data/datasets/niche.json (cache par domaine). Usage : python 65_niche.py en <csv...> | fr <csv...>"""
import base64, csv, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json", "User-Agent": "decupler-outbound"}
CACHE = "../data/datasets/niche.json"
SYS = {"en": ("You classify B2B companies. Answer ONLY JSON {\"niche\": \"...\", \"sure\": true|false}. niche = what the company sells, "
              "2 to 5 words, lowercase, reads naturally after 'the best' (e.g. 'crm software for smes', 'cybersecurity consulting'). "
              "No company name, no marketing words."),
       "fr": ("Tu classes des entreprises B2B. Réponds UNIQUEMENT en JSON {\"niche\": \"...\", \"sure\": true|false}. niche = ce que "
              "l'entreprise vend, 2 à 5 mots, minuscules, qui se lit après « le meilleur » (ex. « logiciel crm pour pme », « conseil en "
              "cybersécurité »). Pas de nom d'entreprise, pas de mot marketing.")}


def gemini(lang, text, model="gemini-3.5-flash"):
    body = json.dumps([{"system_message": SYS[lang][:495], "user_prompt": text[:495], "model_name": model, "web_search": False}]).encode()
    for m in (model, "gemini-2.5-flash"):  # 3.5 souvent surchargé chez DataForSEO : repli 2.5
        body = json.dumps([{"system_message": SYS[lang][:495], "user_prompt": text[:495], "model_name": m, "web_search": False}]).encode()
        for _ in range(2):
            try:
                t = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.dataforseo.com/v3/ai_optimization/gemini/llm_responses/live",
                                                                             data=body, method="POST", headers=DFS), timeout=120).read())["tasks"][0]
            except Exception:
                continue
            if t.get("result"):
                txt = "".join(s.get("text", "") for it in t["result"][0]["items"] for s in it.get("sections", []))
                mm = re.search(r"\{[\s\S]*\}", txt)
                if mm: return dict(json.loads(mm.group(0)), cost=t.get("cost", 0), model=m)
    # dernier repli : gpt-4o-mini (endpoint ChatGPT de DataForSEO, plus stable que Gemini)
    body = json.dumps([{"system_message": SYS[lang][:495], "user_prompt": text[:495], "model_name": "gpt-4o-mini", "web_search": False}]).encode()
    for _ in range(2):
        try:
            t = json.loads(urllib.request.urlopen(urllib.request.Request("https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_responses/live",
                                                                         data=body, method="POST", headers=DFS), timeout=120).read())["tasks"][0]
        except Exception:
            continue
        if t.get("result"):
            txt = "".join(s.get("text", "") for it in t["result"][0]["items"] for s in it.get("sections", []))
            mm = re.search(r"\{[\s\S]*\}", txt)
            if mm: return dict(json.loads(mm.group(0)), cost=t.get("cost", 0), model="gpt-4o-mini")
    return {"error": "pas de réponse", "cost": 0}


if __name__ == "__main__":
    lang, files = sys.argv[1], sys.argv[2:]
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = {}
    for f in files:
        for r in csv.DictReader(open(f)):
            d = (r.get("domain") or "").lower()
            if d and (d not in cache or cache[d].get("error")) and d not in todo:
                todo[d] = f"{r.get('company_name') or r.get('company')}: {r.get('company_description') or ''} {r.get('company_keywords') or ''}".strip()
    print("à classer", len(todo), flush=True)
    with ThreadPoolExecutor(6) as ex:
        for n, (d, res) in enumerate(zip(todo, ex.map(lambda t: gemini(lang, t), todo.values())), 1):
            cache[d] = res
            if n % 100 == 0: json.dump(cache, open(CACHE, "w"), ensure_ascii=False); print(n, flush=True)
    json.dump(cache, open(CACHE, "w"), ensure_ascii=False)
    print("coût", round(sum(cache[d].get("cost", 0) for d in todo), 3), "$ · sûrs", sum(1 for d in todo if cache[d].get("sure")), "/", len(todo))
