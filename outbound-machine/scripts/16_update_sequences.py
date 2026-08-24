#!/usr/bin/env python3
"""Met à jour les séquences Lemlist existantes :
- délais -> J0/J3/J7/J12 (index 1->0, 2->3, 3->4, 4->5) sur toutes les campagnes 'Decupler ·'
- réécrit les 6 verticaux en copy UltB (CTA 'réponses IA + plus de {benef}', vous gardez l'analyse)
Usage: LEMLIST_API_KEY=... python3 16_update_sequences.py
"""
import os, json, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None):
    last = None
    for a in range(5):
        try:
            rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=H)
            r = urllib.request.urlopen(rq, timeout=40)
            return json.load(r) if r.length != 0 else {}
        except urllib.error.HTTPError as e:
            if e.code < 500: raise
            last = e; time.sleep(2**a)
        except (urllib.error.URLError, ConnectionError) as e:
            last = e; time.sleep(2**a)
    raise last

def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
DELAYS = {1: 0, 2: 3, 3: 4, 4: 5}
SIG = ["Nathan Fenina", "Agence Decupler"]

VERTICAUX = {
 "Commerce-Local": ("les commerces", "clients en boutique"),
 "Santé-Médical": ("les praticiens et structures de santé", "patients"),
 "Hôtellerie": ("les hôtels et hébergements", "réservations directes"),
 "Sport-Loisirs": ("les salles et centres", "adhérents"),
 "Services-Pro-B2B": ("les entreprises de services", "demandes entrantes"),
 "Institutions-Autres": ("les organisations", "demandes"),
}

def vsteps(cible, benef):
    def r(s): return s.replace("{CIBLE}", cible).replace("{BENEF}", benef)
    return [
     ("j'ai pris les devants",
      [r("bonjour, j'aide {CIBLE} à ressortir sur Google et dans les IA (ChatGPT, Perplexity) quand un client cherche près de chez lui à {{ville}}."), "",
       r("j'ai regardé {{companyName}} et j'ai pris les devants : je vous ai préparé une analyse de votre visibilité, avec les endroits où vous perdez des {BENEF}."), "",
       r("seriez-vous contre que je vous montre comment vous placer dans les réponses des IA et capter plus de {BENEF} ? 15 min la semaine prochaine ?"), "", *SIG, "",
       "PS : vous gardez l'analyse, elle est à vous et ne vous engage à rien.",
       "PPS : si c'est pas pour vous, un « no biz » et je vous laisse tranquille."]),
     ("re: j'ai pris les devants",
      ["vous êtes sûrement occupé — juste pour savoir : c'est vous qui gérez la visibilité de {{companyName}}, ou pas ?", "",
       "si c'est vous, je vous envoie l'analyse et vous la regardez tranquillement quand vous voulez.", "",
       "un « oui je veux bien » et je vous l'envoie.", "", *SIG]),
     ("je vous fais une version 0 ?",
      [r("je veux vraiment vous aider. si l'analyse ne vous parle pas, dites-moi juste ce qui vous bloque le plus aujourd'hui pour attirer des {BENEF}."), "",
       "je peux vous préparer une version 0 — un exemple concret de comment on vous rendrait visible sur Google et les IA, offert, sans engagement.", "", *SIG]),
     ("je clôture, {{companyName}} ?",
      ["sans réponse je pars du principe que :", "1. ce n'est pas vous qui gérez la visibilité (vers qui me tourner ?),",
       "2. vous êtes déjà au max (top, je vous laisse),", "3. ce n'est pas le moment (on en reparle ?).", "",
       "un mot et j'arrête. l'analyse pour {{companyName}} reste à vous si vous la voulez.", "", *SIG, "",
       "PPS : un « no biz » et je vous laisse tranquille."]),
    ]

def patch_step(seq, sid, subject, message, delay, index):
    body = {"type": "email", "subject": subject, "message": message, "delay": delay, "index": index}
    return api("PATCH", f"https://api.lemlist.com/api/sequences/{seq}/steps/{sid}", body)
def post_step(seq, subject, message, delay, index):
    body = {"type": "email", "subject": subject, "message": message, "delay": delay, "index": index}
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps", body)

if __name__ == "__main__":
    camps = api("GET", "https://api.lemlist.com/api/campaigns?limit=200") or []
    mine = [c for c in camps if str(c.get("name", "")).startswith("Decupler ·")]
    print(f"campagnes à traiter: {len(mine)}")
    for c in mine:
        cid = c["_id"]; name = c["name"]
        seqs = api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")
        seqid = next(iter(seqs)); seq = seqs[seqid]
        steps = sorted(seq.get("steps", []), key=lambda s: s.get("index", 0))
        vert = next((v for k, v in VERTICAUX.items() if k in name), None)
        try:
            if vert:
                newsteps = vsteps(*vert)
                for i, (subj, lines) in enumerate(newsteps, 1):
                    msg = html(lines); delay = DELAYS[i]
                    if i <= len(steps):
                        patch_step(seqid, steps[i-1]["_id"], subj, msg, delay, i)
                    else:
                        post_step(seqid, subj, msg, delay, i)
                    time.sleep(0.4)
                print(f"UltB+delais OK: {name} ({len(newsteps)} mails)")
            else:
                for s in steps:
                    idx = s.get("index", 1); delay = DELAYS.get(idx, s.get("delay", 0))
                    patch_step(seqid, s["_id"], s.get("subject", ""), s.get("message", ""), delay, idx)
                    time.sleep(0.35)
                print(f"delais OK: {name} ({len(steps)} mails)")
        except Exception as e:
            print(f"ERR {name}: {e}")
        time.sleep(0.3)
    print("DONE")
