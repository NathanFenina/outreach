"""Variables par entreprise avec Gemini Flash (DataForSEO, sans recherche web, ≈ 0,0014 $ / entreprise) :
vrai concurrent direct (pas seulement SEO), {{thematique}} (ce que leurs clients cherchent) et {{observation}}
(un client, un partenaire ou une techno cités sur leur site). Lit la page d'accueil (fonction de 39_qualify).
Règle Igor : une variable vide = le prospect ne part pas dans ce palier, il descend au suivant.
Sortie : ../data/datasets/gemini_vars.json (cache par domaine).
Usage : python 58_gemini_concurrent.py test            (les 20 entreprises du test 53)
        python 58_gemini_concurrent.py dom1.com dom2.fr ..."""
import base64, json, os, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

src = open("39_qualify.py").read().split("todo = {}")[0]  # on ne reprend que les fonctions (page), pas l'exécution
q = {}; exec(compile(src, "39_qualify.py", "exec"), q)
UA = q["UA"]


def page(d):
    """Titre + meta + l'extrait autour de « clients / références / ils nous font confiance » (pour {{observation}}) :
    DataForSEO limite le prompt à 500 caractères, on envoie donc les passages utiles plutôt que le début du texte."""
    for u in (f"https://{d}", f"https://www.{d}", f"http://{d}"):
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=12).read(400000).decode("utf-8", "ignore")
        except Exception:
            continue
        title = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
        meta = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', t, re.I)
        alts = re.findall(r'<img[^>]+alt=["\']([^"\']{3,40})["\']', t, re.I)
        body = q["html"].unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t))))
        m = re.search(r"(ils nous font confiance|nos clients|nos références|références|partenaires|trusted by|our clients|they trust us)", body, re.I)
        ref = body[m.start():m.start() + 160] if m else ""
        logos = ", ".join(dict.fromkeys(a for a in alts if re.search(r"logo|client|partenaire", a, re.I)))[:120]
        head = " | ".join(x for x in [title.group(1).strip() if title else "", meta.group(1) if meta else ""] if x)
        return q["html"].unescape(" || ".join(x for x in [head[:220], ref, logos and "logos : " + logos, body[:150]] if x))
    return ""

DFS = {"Authorization": "Basic " + base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode(),
       "Content-Type": "application/json", "User-Agent": "decupler-outbound"}
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")  # 03/11 : 3.5 trouve les vrais concurrents, 2.5 non
CACHE = "../data/datasets/gemini_vars.json"
SYS = ("Analyste marché France. JSON uniquement : {\"activite\":1 phrase,\"thematique\":ce que leurs clients cherchent, 2-4 mots,"
       "\"observation\":client/partenaire/techno cité sur le site ou null,\"concurrents\":[{\"nom\",\"site\"}]} : 3 max, même type "
       "d'entreprise, même offre, mêmes clients, actifs en France ; site = domaine web. Exclus : associations, médias, annuaires, "
       "marketplaces, administrations, Wikipédia, grands groupes généralistes. Pas sûr = liste vide.")


def gemini(prompt):
    body = json.dumps([{"system_message": SYS[:495], "user_prompt": prompt[:495], "model_name": MODEL, "web_search": False}]).encode()
    for _ in range(3):
        req = urllib.request.Request("https://api.dataforseo.com/v3/ai_optimization/gemini/llm_responses/live", data=body, method="POST", headers=DFS)
        t = json.loads(urllib.request.urlopen(req, timeout=120).read())["tasks"][0]
        if t.get("result"): break
    if not t.get("result"): return {"error": t.get("status_message")}, t.get("cost", 0)
    txt = "".join(sec.get("text", "") for it in t["result"][0]["items"] for sec in it.get("sections", []))
    m = re.search(r"\{[\s\S]*\}", txt)
    return (json.loads(m.group(0)) if m else {"error": "pas de JSON", "raw": txt[:200]}), t.get("cost", 0)


def run(d):
    try:
        text = page(d)
        res, cost = gemini(f"Entreprise : {d}. Page d'accueil : {text or '(inaccessible)'}")
        res["cost"] = cost
        # garde-fou : un concurrent ne peut pas être l'entreprise elle-même
        res["concurrents"] = [c for c in res.get("concurrents") or [] if d.split(".")[0] not in (c.get("site") or "").lower()]
        return d, res
    except Exception as e:
        return d, {"error": str(e)[:150], "cost": 0}


if __name__ == "__main__":
    args = sys.argv[1:]
    doms = list(json.load(open("../data/datasets/intent_seo.json"))) if args == ["test"] else args
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [d for d in doms if d not in cache or cache[d].get("error")]
    print("à analyser", len(todo))
    with ThreadPoolExecutor(6) as ex:
        for n, (d, res) in enumerate(ex.map(run, todo), 1):
            cache[d] = res
            if n % 25 == 0: json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=0); print(n, flush=True)
    json.dump(cache, open(CACHE, "w"), ensure_ascii=False, indent=0)
    print("coût de ce lot", round(sum(cache[d].get("cost", 0) for d in todo), 4), "$ · erreurs", sum(1 for d in todo if cache[d].get("error")))
