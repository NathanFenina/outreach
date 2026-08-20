#!/usr/bin/env python3
"""Crée les 3 campagnes Tech (USP1/2/3) sur Lemlist + écrit les 4 mails de chaque séquence.
Usage: LEMLIST_API_KEY=... python3 08_create_tech_campaigns.py
Affiche les campaignId créés (à réutiliser pour l'import des leads)."""
import os, json, base64, urllib.request, urllib.parse, urllib.error, time
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None):
    rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                                method=method, headers=H)
    return json.load(urllib.request.urlopen(rq, timeout=40))

def create_campaign(name):
    return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})

def get_seq_id(cid):
    seqs = api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")
    return next(iter(seqs))

def html(lines):
    return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)

def write_step(seq, subject, lines, delay, index):
    body = {"type": "email", "subject": subject, "message": html(lines), "delay": delay, "index": index}
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps", body)

SIG = ["Nathan Fenina", "Agence Decupler"]
# chaque étape = (subject, [lignes], delay_jours_apres_precedent)
SEQUENCES = {
"Decupler · Tech IT · USP1 Autorite": [
 ("j'arrive pas à vous trouver",
  ["hello {{firstName}}, je suis ingénieur en IT et j'aide les boîtes IT à être référencées sur Google et dans les IA (ChatGPT, Perplexity).","",
   "j'ai regardé ce que vous faites et j'ai préparé une analyse de votre visibilité organique, avec les endroits où vous perdez des leads.","",
   "on a déjà accompagné 40 boîtes IT à faire +20% de leads.","",
   "je vous la partage lors d'un échange de 10 min ?","",*SIG,"",
   "PS : l'analyse est à vous, que vous bossiez avec nous ou pas."], 0),
 ("re: j'arrive pas à vous trouver",
  ["{{firstName}}, on prend 20 min, je vous montre sur 10 prompts précis quel concurrent est cité et ce qu'il faut rédiger pour récupérer sa place.","",
   "et pendant ce RDV je vous montre la qualité de notre travail et comment on trouve des leads. si ça vous plaît, je vous offre en plus un contenu GEO-friendly prêt à publier sur un sujet.","",
   "ça vous dit ?","",*SIG], 2),
 ("re: j'arrive pas à vous trouver",
  ["{{firstName}}, si vous manquez de temps, pas besoin d'attendre notre échange : on a développé un outil interne qui vous sort votre score de visibilité IA.","",
   "vous mettez votre URL, il vous donne où vous en êtes + les premières actions. voici le lien : https://app.decupler.com/audit-geo-gratuit","",
   "toutefois, ça ne remplace pas une expertise humaine et un échange humain.","",*SIG], 1),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse je pars du principe que :","1. ce n'est pas vous qui gérez la visibilité (vers qui me tourner ?),",
   "2. vous le lancez déjà en interne (top, je vous laisse),","3. ce n'est pas le moment (on en reparle plus tard ?).","",
   "un mot et j'arrête. l'analyse pour {{companyName}} reste dispo si vous la voulez.","",*SIG,"",
   "PPS : pas le bon moment ? un « stop » et je vous laisse tranquille."], 2),
],
"Decupler · Tech IT · USP2 Cadeau": [
 ("petit cadeau {{companyName}}",
  ["hello {{firstName}}, je bosse avec des boîtes IT et tech qui veulent plus de demandes entrantes via le search.","",
   "je vous ai préparé une analyse avec les 10 grandes opportunités organiques prioritaires pour {{companyName}}, offert, pour vous montrer le niveau : les mots-clés qui rapportent, les prompts IA à viser, et une projection de leads/mois.","",
   "si l'approche vous parle, on vous montre comment on capte plus de leads. sinon vous gardez tout, sans engagement.","",
   "seriez-vous contre un échange de 10 min pour vous présenter la carto ?","",*SIG,"",
   "PS : on a travaillé sur la visibilité organique chez Le Point, Pluxee et Décathlon.",
   "PPS : pas le bon moment ? un « no biz » et je vous laisse tranquille."], 0),
 ("re: petit cadeau {{companyName}}",
  ["{{firstName}}, si vous manquez de temps pour qu'on en parle, je peux déjà vous partager la matière : un outil interne qui, depuis votre URL, sort les opportunités organiques + votre score de visibilité IA. voici le lien : https://app.decupler.com/cartographie-ia","",
   "toutefois, ça ne remplace pas un regard humain et un échange.","",*SIG], 2),
 ("comme cette boîte IT ?",
  ["{{firstName}}, vous me faites penser à une boîte IT qu'on accompagne : elle captait peu de demandes, ses concurrents raflaient les requêtes d'achat. on a priorisé 10 pages + le format GEO, résultat : plus de demandes qualifiées sans dépendre du paid.","",
   "on fait le même exercice pour {{companyName}} en 20 min ? je vous laisse la carto + 1 contenu rédigé, que vous gardez.","",*SIG], 1),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse, je pars du principe que : 1. ce n'est pas vous qui gérez le sujet ; 2. vous êtes déjà bien couvert en organique ; 3. ce n'est pas prioritaire là. un mot et j'arrête.","",
   "la cartographie pour {{companyName}} reste prête.","",*SIG,"",
   "PPS : un « no biz » et je vous laisse tranquille."], 2),
],
"Decupler · Tech IT · USP3 Leads trackes": [
 ("combien de leads rate {{companyName}} ?",
  ["hello {{firstName}}, je suis ingénieur en IT. la plupart des boîtes IT ne savent pas combien de leads elles perdent faute d'être visibles sur Google et les IA.","",
   "on a monté une infrastructure qui va chercher ces leads, et surtout qui vous montre le nombre exact que vous récupérez, mois par mois.","",
   "je vous fais une projection chiffrée pour {{companyName}} ?","",*SIG,"",
   "PS : la projection est à vous, que vous bossiez avec nous ou pas."], 0),
 ("re: combien de leads rate {{companyName}} ?",
  ["{{firstName}}, concrètement on branche un suivi qui compte les leads que la visibilité organique vous ramène, mois par mois, sans que vous ayez à toucher à quoi que ce soit.","",
   "je vous montre le dashboard sur un cas réel en 10 min ?","",*SIG], 2),
 ("re: combien de leads rate {{companyName}} ?",
  ["{{firstName}}, si vous voulez juste voir le potentiel : on vous fait une projection chiffrée du nombre de leads récupérables pour {{companyName}}.","",
   "et si on cale un RDV, je vous offre en plus un contenu GEO-friendly prêt à publier. ça vous dit ?","",*SIG], 1),
 ("je clôture, {{firstName}} ?",
  ["{{firstName}}, sans réponse je pars du principe que : 1. ce n'est pas vous qui gérez le sujet ; 2. vous suivez déjà vos leads organiques ; 3. ce n'est pas le moment. un mot et j'arrête.","",
   "la projection pour {{companyName}} reste dispo.","",*SIG,"",
   "PPS : un « stop » et je vous laisse tranquille."], 2),
],
}

if __name__ == "__main__":
    out = {}
    for name, steps in SEQUENCES.items():
        camp = create_campaign(name)
        cid = camp.get("_id") or camp.get("id")
        time.sleep(1)
        seq = get_seq_id(cid)
        for i, (subj, lines, delay) in enumerate(steps, start=1):
            write_step(seq, subj, lines, delay, i)
            time.sleep(0.5)
        out[name] = cid
        print(f"OK {name} -> {cid} ({len(steps)} steps)")
    print("CAMPAIGN_IDS=" + json.dumps(out))
