#!/usr/bin/env python3
"""Publie le batch E-COMMERCE (style UltB, ventes + GEO) sur Lemlist depuis le fichier de
résultat Supabase MCP persisté. Variables: {{firstName}} + {{companyName}}.
Usage: LEMLIST_API_KEY=... python3 13_publish_ecommerce.py <result_file.txt>"""
import os, sys, json, re, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None):
    last = None
    for attempt in range(5):
        try:
            rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=H)
            return json.load(urllib.request.urlopen(rq, timeout=40))
        except (urllib.error.URLError, urllib.error.HTTPError, ConnectionError) as e:
            if isinstance(e, urllib.error.HTTPError) and e.code < 500: raise
            last = e; time.sleep(2 ** attempt)
    raise last
def list_campaigns(): return api("GET", "https://api.lemlist.com/api/campaigns?limit=200")
def find_campaign(name):
    for c in list_campaigns() or []:
        if c.get("name") == name: return c.get("_id") or c.get("id")
    return None
def create_campaign(name): return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
def get_seq_id(cid): return next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def write_step(seq, subj, lines, delay, index):
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps",
               {"type": "email", "subject": subj, "message": html(lines), "delay": delay, "index": index})
def add_lead(cid, email, fields, dedup="true"):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate={dedup}"
    for attempt in range(5):
        rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST", headers=H)
        try:
            urllib.request.urlopen(rq, timeout=20); return "sent"
        except urllib.error.HTTPError as e:
            m = e.read().decode()
            if "other campaign" in m: return "dup"
            if "already" in m.lower(): return "sent"
            if "graveyard" in m.lower(): return "grave"
            if e.code >= 500: time.sleep(2 ** attempt); continue
            return "error:" + m[:80]
        except (urllib.error.URLError, ConnectionError):
            time.sleep(2 ** attempt)
    return "error:network"

SIG = ["Nathan Fenina", "Agence Decupler"]
STEPS = [
 ("j'ai pris les devants",
  ["hello {{firstName}}, je cherche des marques e-commerce qui veulent augmenter leurs ventes sur Google et les IA (ChatGPT, Perplexity).","",
   "j'ai vu ce que vous faites chez {{companyName}} et j'ai pris les devants : je vous ai préparé une analyse de votre visibilité, avec les endroits où vous perdez des ventes.","",
   "seriez-vous contre un échange de 15 min jeudi prochain ?","",*SIG,"",
   "PS : je vous offre l'analyse, elle vous appartient et ne vous engage à rien — juste pour vous montrer la qualité de notre travail et comment choper plus de ventes.",
   "PPS : si c'est pas pour vous, dites « no biz » et je ne vous embête plus."], 0),
 ("re: j'ai pris les devants",
  ["{{firstName}}, je pense que vous êtes occupé — juste pour savoir : c'est vous qui gérez l'acquisition chez {{companyName}}, ou pas ?","",
   "si c'est vous, je vous envoie la petite analyse et vous la regardez tranquillement quand vous voulez.","",
   "un « oui je veux bien » et je vous l'envoie.","",*SIG,"",
   "PS : on a bossé pour Décathlon également."], 2),
 ("je vous fais une version 0 ?",
  ["{{firstName}}, je veux vraiment vous aider. si l'analyse ne vous parle pas, dites-moi juste ce qui vous embête le plus en ce moment sur l'acquisition.","",
   "je suis prêt à vous créer un prototype — une version 0 de comment on vous aiderait, offerte, sans engagement. histoire de vous montrer concrètement comment on peut vous trouver plus de ventes (ou économiser) avec l'IA.","",*SIG], 1),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse je pars du principe que :","1. ce n'est pas vous qui gérez l'acquisition (vers qui me tourner ?),",
   "2. vous êtes déjà au max côté Google et IA (top, je vous laisse),","3. ce n'est pas le moment (on en reparle plus tard ?).","",
   "un mot et j'arrête. l'analyse pour {{companyName}} reste à vous si vous la voulez.","",*SIG,"",
   "PPS : un « no biz » et je vous laisse tranquille."], 2),
]

def load_leads(path):
    raw = open(path, encoding="utf-8").read()
    try: text = json.loads(raw)["result"]      # dé-échappe l'enveloppe MCP
    except Exception: text = raw
    m = re.search(r'\[\s*\{\s*"leads"\s*:\s*\[.*\]\s*\}\s*\]', text, re.DOTALL)
    if not m: raise SystemExit("tableau leads introuvable")
    return json.loads(m.group(0))[0]["leads"]

if __name__ == "__main__":
    leads = load_leads(sys.argv[1])
    seen = set(); uniq = []
    for l in leads:
        e = (l.get("email") or "").strip().lower()
        if e and e not in seen: seen.add(e); uniq.append(l)
    print(f"leads e-commerce à publier: {len(uniq)}")
    name = "Decupler · E-commerce · Ventes+GEO (FR)"
    cid = find_campaign(name)
    if cid:
        print("campagne existante réutilisée (dedup=false):", cid); dedup = "false"
    else:
        camp = create_campaign(name); cid = camp.get("_id") or camp.get("id"); time.sleep(1)
        seq = get_seq_id(cid)
        for i, (subj, lines, d) in enumerate(STEPS, 1): write_step(seq, subj, lines, d, i); time.sleep(0.4)
        print("steps écrits"); dedup = "true"
    print("CAMPAIGN=" + cid)
    s = g = e = 0; ok = []
    for l in uniq:
        f = {"companyName": l.get("companyName", "")}
        fn = (l.get("firstName") or "").strip()
        if fn: f["firstName"] = fn
        r = add_lead(cid, l["email"].strip(), f, dedup)
        if r in ("sent", "dup"): s += 1; ok.append(l["id"])
        elif r == "grave": g += 1
        else: e += 1; print("ERR", l["email"], r)
        time.sleep(0.2)
    json.dump(ok, open("/tmp/claude-0/-home-user-outreach/a72cc66c-6ba4-5f27-98fd-79167fbf69f8/scratchpad/ecom_ok_ids.json", "w"))
    print(f"STATS ok={s} graveyard={g} err={e}")
