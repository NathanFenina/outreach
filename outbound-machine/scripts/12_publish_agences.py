#!/usr/bin/env python3
"""Publie le batch AGENCES francophones (white-label GEO) sur Lemlist.
Lit les leads depuis le fichier de résultat Supabase MCP persisté (enveloppe JSON), crée la
campagne, écrit les 4 mails, importe. Variables: {{firstName}} + {{companyName}}.
Usage: LEMLIST_API_KEY=... python3 12_publish_agences.py <result_file.txt>"""
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
            if isinstance(e, urllib.error.HTTPError) and e.code < 500:
                raise
            last = e; time.sleep(2 ** attempt)
    raise last
def list_campaigns(): return api("GET", "https://api.lemlist.com/api/campaigns?limit=200")
def find_campaign(name):
    for c in list_campaigns() or []:
        if c.get("name") == name: return c.get("_id") or c.get("id")
    return None
def find_campaigns_all(name):
    return [c.get("_id") or c.get("id") for c in (list_campaigns() or []) if c.get("name") == name]
def delete_campaign(cid):
    try: api("DELETE", f"https://api.lemlist.com/api/campaigns/{cid}")
    except Exception as e: print("delete fail", cid, e)
def create_campaign(name): return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
def get_seq_id(cid): return next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def write_step(seq, subj, lines, delay, index):
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps",
               {"type": "email", "subject": subj, "message": html(lines), "delay": delay, "index": index})
def add_lead(cid, email, fields):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    for attempt in range(5):
        rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST", headers=H)
        try:
            urllib.request.urlopen(rq, timeout=20); return "sent"
        except urllib.error.HTTPError as e:
            m = e.read().decode()
            if "other campaign" in m: return "dup"
            if "already" in m.lower(): return "sent"
            if e.code >= 500: time.sleep(2 ** attempt); continue
            return "error:" + m[:80]
        except (urllib.error.URLError, ConnectionError):
            time.sleep(2 ** attempt)
    return "error:network"

SIG = ["Nathan Fenina", "Agence Decupler"]
STEPS = [
 ("partenaires ?",
  ["{{firstName}}, vos clients vous demandent s'ils ressortent dans ChatGPT et les IA (Perplexity, AI Overviews). la plupart des agences n'ont pas encore la réponse technique et utilisent des outils faillibles.","",
   "nous chez Decupler on ne fait que ça : on crée nos propres systèmes et agents IA. et on peut le produire en marque blanche, sous le nom de {{companyName}}.","",
   "vous ajoutez une ligne SEO/GEO à vos offres, vous gardez la marge, on livre dans l'ombre.","",
   "on en parle 15 min pour vous montrer nos livrables ?","",*SIG,"",
   "PS : même si on ne bosse pas ensemble, je vous envoie notre grille de ce qu'un audit GEO doit couvrir."], 0),
 ("re: partenaires ?",
  ["{{firstName}}, pour vous montrer concrètement plutôt que d'en parler dans le vide :","",
   "choisissez UN de vos clients (ou un prospect que vous voulez signer), et on vous produit son audit de visibilité IA — en marque blanche, à votre nom, offert.","",
   "vous le présentez comme le vôtre. s'il vous sert à upseller ou à signer, on continue ensemble ; sinon vous gardez l'audit, vous ne perdez rien.","",
   "on cale 15 min pour que vous me donniez le client et que je vous montre le format de nos livrables ?","",*SIG], 2),
 ("on exécute, vous livrez",
  ["{{firstName}}, au fond c'est simple : avec nos systèmes et agents IA, on crée le livrable que VOUS voulez — audit de visibilité IA, cartographie GEO, contenu optimisé, monitoring des IA, page prête à publier... vous nous dites ce dont vos clients ont besoin, on l'exécute en marque blanche.","",
   "on prend un moment pour en discuter ?","",*SIG,"",
   "PS : si vous n'avez rien à déléguer là tout de suite, dites-le-moi et je vous laisse tranquille.",
   "PS2 : on a bossé sur le SEO de grands comptes — SG, Le Point, Sodexo."], 1),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse je pars du principe que :","1. vous gérez déjà le SEO/GEO en interne (top, je vous laisse),",
   "2. ce n'est pas le moment (on en reparle plus tard ?),","3. ce n'est pas vous qui gérez les partenariats (vers qui me tourner ?).","",
   "un mot et j'arrête. la grille d'audit GEO pour {{companyName}} reste à vous si vous la voulez.","",*SIG,"",
   "PPS : un « stop » et je vous laisse tranquille."], 2),
]

def load_leads(path):
    raw = open(path, encoding="utf-8").read()
    try:
        outer = json.loads(raw)
        text = outer.get("result", raw)
    except Exception:
        text = raw
    m = re.search(r'\[\s*\{\s*"leads"\s*:\s*\[.*\]\s*\}\s*\]', text, re.DOTALL)
    if not m:
        raise SystemExit("tableau leads introuvable dans le fichier")
    data = json.loads(m.group(0))
    return data[0]["leads"]

if __name__ == "__main__":
    path = sys.argv[1]
    leads = load_leads(path)
    # dédup par email
    seen = set(); uniq = []
    for l in leads:
        e = (l.get("email") or "").strip().lower()
        if e and e not in seen: seen.add(e); uniq.append(l)
    print(f"leads FR à publier: {len(uniq)}")
    name = "Decupler · Agences · White-label GEO (FR)"
    for old in find_campaigns_all(name):
        print("suppression campagne partielle:", old); delete_campaign(old); time.sleep(0.5)
    camp = create_campaign(name); cid = camp.get("_id") or camp.get("id"); time.sleep(1)
    seq = get_seq_id(cid)
    for i, (subj, lines, d) in enumerate(STEPS, 1): write_step(seq, subj, lines, d, i); time.sleep(0.4)
    print("CAMPAIGN=" + cid)
    sent = dup = err = 0; ok_ids = []
    for l in uniq:
        f = {"companyName": l.get("companyName", "")}
        fn = (l.get("firstName") or "").strip()
        if fn: f["firstName"] = fn
        res = add_lead(cid, l["email"].strip(), f)
        if res == "sent": sent += 1; ok_ids.append(l["id"])
        elif res == "dup": dup += 1; ok_ids.append(l["id"])
        else: err += 1; print("ERR", l["email"], res)
        time.sleep(0.22)
    print(f"STATS sent={sent} dup={dup} err={err}")
    json.dump(ok_ids, open("/tmp/claude-0/-home-user-outreach/a72cc66c-6ba4-5f27-98fd-79167fbf69f8/scratchpad/agences_ok_ids.json","w"))
    print("OK_IDS_WRITTEN", len(ok_ids))
