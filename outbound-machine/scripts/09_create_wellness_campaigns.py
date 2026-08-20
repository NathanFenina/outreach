#!/usr/bin/env python3
"""Crée les 2 campagnes Wellness (A Analyse / B Site offert) sur Lemlist, écrit les 4 mails,
et importe les leads wellness+adjacents (split 50/50) depuis les CSV Outscraper nettoyés.
Usage: LEMLIST_API_KEY=... python3 09_create_wellness_campaigns.py <wellness.csv> <clean.csv>
Variables Lemlist utilisées : {{companyName}} {{secteur}} {{ville}} (pas de {{firstName}}, 6% l'ont)."""
import os, sys, csv, json, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None, timeout=30):
    rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                                method=method, headers=H)
    return json.load(urllib.request.urlopen(rq, timeout=timeout))

def create_campaign(name): return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
def get_seq_id(cid): return next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def write_step(seq, subject, lines, delay, index):
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps",
               {"type": "email", "subject": subject, "message": html(lines), "delay": delay, "index": index})

def add_lead(cid, email, fields):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST", headers=H)
    try:
        urllib.request.urlopen(rq, timeout=20); return "sent"
    except urllib.error.HTTPError as e:
        m = e.read().decode()
        if "other campaign" in m: return "dup"
        if "already" in m.lower(): return "sent"
        return "error:" + m[:80]

SIG = ["Nathan Fenina", "Agence Decupler"]
SEQ_A = [
 ("votre {{secteur}} sur Google",
  ["bonjour, je regarde comment les instituts et spas se font trouver quand un client tape « massage » ou « soin » près de chez lui — sur Google comme dans les IA (ChatGPT, Maps).","",
   "j'ai préparé une analyse pour {{companyName}} : j'ai repéré 10 recherches à {{ville}} où c'est un concurrent qui ressort à votre place, et les 3 choses simples qui vous font récupérer ces réservations.","",
   "je vous la partage lors d'un échange de 10 min ?","",*SIG,"",
   "PS : l'analyse est à vous, que vous travailliez avec nous ou pas."], 0),
 ("re: votre {{secteur}} sur Google",
  ["concrètement je vous montre les recherches où vos futurs clients tombent sur un concurrent plutôt que sur {{companyName}}, et quoi changer pour reprendre ces places.","",
   "on prend 15 min quand vous voulez — je vous montre aussi comment on travaille.","",*SIG], 2),
 ("re: votre {{secteur}} sur Google",
  ["si vous manquez de temps, pas besoin d'attendre : on a un outil qui, depuis le nom de votre {{secteur}}, sort votre visibilité et les premières actions à faire.","",
   "je le lance pour {{companyName}} et je vous renvoie le résultat — c'est offert.","",
   "un simple « ok » et je m'en occupe.","",*SIG], 1),
 ("je clôture, {{companyName}} ?",
  ["sans réponse je pars du principe que :","1. ce n'est pas le bon moment (on en reparle plus tard ?),",
   "2. vous êtes déjà complet côté réservations (top, je vous laisse),","3. ce n'est pas vous qui gérez ça (vers qui me tourner ?).","",
   "un mot et j'arrête. l'analyse pour {{companyName}} reste à vous si vous la voulez.","",*SIG,"",
   "PPS : pas le bon moment ? un « stop » et je vous laisse tranquille."], 2),
]
SEQ_B = [
 ("votre fiche {{companyName}}",
  ["bonjour, je suis tombé sur la fiche Google de {{companyName}} et j'ai vu vos avis clients — ils donnent vraiment envie de pousser la porte.","",
   "du coup je me suis permis de regarder votre site : il est bien, mais on peut le rendre plus moderne et surtout transformer plus de visiteurs en réservations. je vous ai préparé une maquette.","",
   "si elle vous plaît, vous la gardez — c'est offert, sans engagement.","",
   "on cale 15 min la semaine prochaine pour que je vous la partage à l'écran ?","",*SIG,"",
   "PS : que vous travailliez avec nous ou non, la maquette est à vous."], 0),
 ("re: votre fiche {{companyName}}",
  ["je vous montre la maquette en 10 min : l'accueil, la page soins et le bouton de réservation mis en avant. vous repartez avec, même si on n'avance pas ensemble.","",
   "quel créneau vous arrange la semaine prochaine ?","",*SIG], 2),
 ("re: votre fiche {{companyName}}",
  ["au-delà du design, un site propre c'est aussi ce qui fait remonter votre {{secteur}} sur Google et Maps à {{ville}} quand quelqu'un cherche autour de lui.","",
   "on regarde ensemble la maquette + les 2-3 réglages qui vous rendent plus visible ?","",*SIG], 1),
 ("je clôture, {{companyName}} ?",
  ["sans réponse je pars du principe que :","1. votre site actuel vous convient (parfait, je vous laisse),",
   "2. ce n'est pas le moment (on en reparle plus tard ?),","3. ce n'est pas vous qui gérez ça (vers qui me tourner ?).","",
   "un mot et j'arrête. la maquette pour {{companyName}} reste à vous.","",*SIG,"",
   "PPS : pas le bon moment ? un « stop » et je vous laisse tranquille."], 2),
]

def secteur_of(cat):
    c = (cat or "").lower()
    if "spa" in c: return "spa"
    if any(k in c for k in ["massage", "massoth", "drainage", "shiatsu"]): return "cabinet de massage"
    if any(k in c for k in ["réflexo", "ostéo", "naturo", "psychothérap", "médecine alternative", "sophro", "énergét"]): return "cabinet"
    if any(k in c for k in ["coiffure", "manucure", "onglerie", "barbier"]): return "salon"
    if any(k in c for k in ["bien-être", "bien-etre", "sauna"]): return "centre de bien-être"
    if any(k in c for k in ["beaut", "esthét", "esthéti", "épilation", "visage", "cosmét", "bronzage"]): return "institut"
    return "établissement"

KEEP = ['réflexo','ostéo','naturo','médecine alternative','psychothérap','sophro','énergét','shiatsu','drainage','yoga','pilates','esthétique','esthéticien','onglerie','manucure','coiffure','bronzage','hammam','sauna','thalasso','balnéo','cryo','tatouage','barbier','spa','massage','beaut','bien-être','bien-etre','soin']
NOISE = ['hotel','hôtel','hôpital','hopital','clinique','pharmacie','laborat','matériel médical','grossiste','intérim','interim','maison de retraite','ambulanc','mutuelle','administration','office de tourisme','camping','gîte','chambre','immobil','piscine','aquatique','auditif','formation','médecin','cabinet médical','centre médical','centre de santé','maison de santé','rééducation','soins palliatifs','soins à domicile','association','attraction','banque','assurance','vétérinaire','dentaire','opticien','pédicure','podolog']
def has(s, lst): s = (s or "").lower(); return any(k in s for k in lst)

def load_leads(wellness_csv, clean_csv):
    leads, seen = [], set()
    for r in csv.DictReader(open(wellness_csv)):
        e = (r.get("email") or "").strip().lower()
        if e and e not in seen:
            seen.add(e); leads.append(r)
    for r in csv.DictReader(open(clean_csv)):
        e = (r.get("email") or "").strip().lower()
        if e and e not in seen and has(r.get("category"), KEEP) and not has(r.get("category"), NOISE):
            seen.add(e); leads.append(r)
    return leads

if __name__ == "__main__":
    wellness_csv, clean_csv = sys.argv[1], sys.argv[2]
    leads = load_leads(wellness_csv, clean_csv)
    print(f"leads à importer: {len(leads)}")
    ca = create_campaign("Decupler · Wellness · A Analyse-10recherches"); cida = ca.get("_id") or ca.get("id")
    time.sleep(1); sa = get_seq_id(cida)
    for i, (subj, lines, d) in enumerate(SEQ_A, 1): write_step(sa, subj, lines, d, i); time.sleep(0.4)
    cb = create_campaign("Decupler · Wellness · B Site-offert"); cidb = cb.get("_id") or cb.get("id")
    time.sleep(1); sb = get_seq_id(cidb)
    for i, (subj, lines, d) in enumerate(SEQ_B, 1): write_step(sb, subj, lines, d, i); time.sleep(0.4)
    print(f"CAMPAIGN_A={cida}\nCAMPAIGN_B={cidb}")
    stats = {"A": {"sent": 0, "dup": 0, "error": 0}, "B": {"sent": 0, "dup": 0, "error": 0}}
    for idx, r in enumerate(leads):
        which, cid = ("A", cida) if idx % 2 == 0 else ("B", cidb)
        fields = {"companyName": r.get("name", ""), "secteur": secteur_of(r.get("category")),
                  "ville": r.get("city", "")}
        fn = (r.get("first_name") or "").strip()
        if fn: fields["firstName"] = fn
        res = add_lead(cid, r["email"].strip(), fields)
        k = "sent" if res == "sent" else ("dup" if res == "dup" else "error")
        stats[which][k] += 1
        if res.startswith("error"): print("ERR", r["email"], res)
        time.sleep(0.25)
    print("STATS=" + json.dumps(stats))
