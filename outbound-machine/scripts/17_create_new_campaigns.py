#!/usr/bin/env python3
"""Crée 3 nouvelles campagnes Lemlist (vides, prêtes pour import) :
- Immo Agents IA (FR)  - Plombier Genève (local visibilité)  - CMO Genève (copy SEO-pages de Nathan)
Cadence J0/J3/J7/J12 (délais 0/3/4/5). Usage: LEMLIST_API_KEY=... python3 17_create_new_campaigns.py
"""
import os, json, base64, time, urllib.request, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(m, u, b=None):
    for a in range(5):
        try:
            rq = urllib.request.Request(u, data=json.dumps(b).encode() if b is not None else None, method=m, headers=H)
            r = urllib.request.urlopen(rq, timeout=40); return json.load(r) if r.length != 0 else {}
        except urllib.error.HTTPError as e:
            if e.code < 500: raise
            time.sleep(2 ** a)
        except (urllib.error.URLError, ConnectionError):
            time.sleep(2 ** a)
    raise SystemExit("api fail")

def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def find(name):
    for c in api("GET", "https://api.lemlist.com/api/campaigns?limit=200"):
        if c.get("name") == name: return c.get("_id") or c.get("id")
    return None

SIG = ["Nathan Fenina", "Agence Decupler"]
SIG_TU = ["Nathan", "Decupler"]
DELAYS = [0, 3, 4, 5]

# Immo v2 (validée Nathan) : liste concrète + {{avisphrase}} (fiche Google) + agents IA "à votre taille"
IMMO = [
 ("des agents IA pour {{companyName}} ?",
  ["bonjour,","",
   "{{avisphrase}}","",  # = "je vous contacte depuis votre fiche Google, d'ailleurs bravo pour les {{avis}} avis positifs." (fallback si 0 avis)
   "on aide des agences immo de votre taille à automatiser ce qui bouffe du temps :",
   "— rédiger des annonces qui donnent envie de visiter,",
   "— répondre aux leads en quelques secondes, même la nuit,",
   "— qualifier les acheteurs avant de perdre du temps en visite,",
   "— récupérer plus d'avis sur Maps pour améliorer votre référencement.","",
   "seriez-vous contre un échange de 15 min pour vous montrer les agents IA qu'on peut créer pour vous ?","",*SIG,"",
   "PS : qu'est-ce qui vous prend le plus de temps aujourd'hui — les annonces, les relances, ou le tri des demandes ?"]),
 ("re: des agents IA pour {{companyName}} ?",
  ["une question simple : aujourd'hui, qui répond à vos leads le soir et le week-end ?","",
   "beaucoup d'agences perdent des acheteurs juste parce que la réponse arrive trop tard. nos agents répondent en quelques secondes, 24/7, et qualifient l'acheteur avant la visite.","",
   "je vous montre comment ça tournerait chez {{companyName}} en 15 min ?","",*SIG]),
 ("je vous fais une version 0 ?",
  ["dites-moi juste la tâche qui vous prend le plus de temps (annonces, relances, tri des demandes) et je vous construis une version 0 de l'agent qui la fait — offerte, sans engagement.","",
   "vous le voyez tourner sur VOTRE cas, et vous le gardez.","",*SIG]),
 ("je clôture, {{companyName}} ?",
  ["sans réponse je pars du principe que : 1. ce n'est pas le moment ; 2. vous gérez déjà ça en interne ; 3. ce n'est pas vous qui vous en occupez. un mot et j'arrête.","",
   "les agences immo qui surfent sur le digital vont plus vite et signent plus — c'est maintenant. la démo pour {{companyName}} reste à votre dispo.","",*SIG,"",
   "PPS : un « no biz » et je vous laisse tranquille."]),
]

PLOMBIER = [
 ("j'ai pris les devants",
  ["bonjour, j'aide les plombiers à ressortir sur Google et dans les IA (ChatGPT, Perplexity) quand quelqu'un cherche un plombier près de chez lui à Genève.","",
   "j'ai regardé {{companyName}} et j'ai pris les devants : je vous ai préparé une analyse de votre visibilité, avec les endroits où vous perdez des clients.","",
   "seriez-vous contre que je vous montre comment vous placer dans les réponses des IA et capter plus de clients ? 15 min la semaine prochaine ?","",*SIG,"",
   "PS : vous gardez l'analyse, elle est à vous et ne vous engage à rien.",
   "PPS : si c'est pas pour vous, un « no biz » et je vous laisse tranquille."]),
 ("re: j'ai pris les devants",
  ["vous êtes sûrement occupé — juste pour savoir : c'est vous qui gérez la visibilité de {{companyName}}, ou pas ?","",
   "si c'est vous, je vous envoie l'analyse et vous la regardez tranquillement quand vous voulez.","",
   "un « oui je veux bien » et je vous l'envoie.","",*SIG]),
 ("je vous fais une version 0 ?",
  ["si l'analyse ne vous parle pas, dites-moi juste ce qui vous bloque le plus aujourd'hui pour avoir plus de clients.","",
   "je peux vous préparer une version 0 — un exemple concret de comment on vous rendrait visible sur Google et les IA, offert, sans engagement.","",*SIG]),
 ("je clôture, {{companyName}} ?",
  ["sans réponse je pars du principe que : 1. ce n'est pas le moment ; 2. vous êtes déjà au max ; 3. ce n'est pas vous qui gérez ça. un mot et j'arrête.","",
   "l'analyse pour {{companyName}} reste à vous si vous la voulez.","",*SIG,"",
   "PPS : un « no biz » et je vous laisse tranquille."]),
]

CMO = [
 ("pas un outil SEO de plus",
  ["hello {{firstName}}, je vais pas te pitcher un outil SEO de plus 😅","",
   "j'ai créé un système qui sort des pages SEO rédigées, optimisées, designées et intégrées (sans toucher au code) en quelques jours au lieu de plusieurs semaines.","",
   "je l'ai testé sur 20+ sites — tu serais contre un échange de 10 min pour que je te montre ça ?","",*SIG_TU]),
 ("re: pas un outil SEO de plus",
  ["{{firstName}} :) je me permets de faire remonter au cas où c'est passé à la trappe.","",
   "tu serais partant pour 10 min cette semaine ?","",*SIG_TU]),
 ("un résumé vidéo de 3 min ?",
  ["{{firstName}}, si tu manques de temps, je te fais un résumé en vidéo de 3 min plutôt qu'un call — ça t'irait mieux ?","",
   "tu me dis et je te l'envoie.","",*SIG_TU]),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse je pars du principe que c'est pas le moment ou pas pour toi. un mot et j'arrête.","",
   "le système reste dispo si tu veux le voir tourner sur ton site.","",*SIG_TU,"",
   "PPS : un « no biz » et je te laisse tranquille."]),
]

CAMPAIGNS = [
 ("Decupler · Immo · Agents IA (FR)", IMMO),
 ("Decupler · Plombier · Genève (local)", PLOMBIER),
 ("Decupler · CMO Genève · SEO-pages", CMO),
]

if __name__ == "__main__":
    for name, steps in CAMPAIGNS:
        if find(name): print("existe déjà, skip:", name); continue
        camp = api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
        cid = camp.get("_id") or camp.get("id"); time.sleep(1)
        seqid = next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
        for i, (subj, lines) in enumerate(steps, 1):
            api("POST", f"https://api.lemlist.com/api/sequences/{seqid}/steps",
                {"type": "email", "subject": subj, "message": html(lines), "delay": DELAYS[i-1], "index": i})
            time.sleep(0.4)
        print(f"OK {name} -> {cid}")
    print("DONE")
