#!/usr/bin/env python3
"""'Rien jeter' : regroupe les leads restants de medspa_clean.csv en 6 verticaux et crée une
campagne Lemlist par groupe (angle Site-offert ou SEO encodé dans le titre). Exclut les leads
déjà importés en Wellness A/B (mêmes règles que scripts 09+10) pour zéro doublon.
Usage: LEMLIST_API_KEY=... python3 11_create_vertical_campaigns.py medspa_clean.csv medspa_wellness.csv"""
import os, sys, csv, json, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None):
    rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=H)
    return json.load(urllib.request.urlopen(rq, timeout=40))
def create_campaign(name): return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
def get_seq_id(cid): return next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def write_step(seq, subj, lines, delay, index):
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps",
               {"type": "email", "subject": subj, "message": html(lines), "delay": delay, "index": index})
def add_lead(cid, email, fields):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST", headers=H)
    try:
        urllib.request.urlopen(rq, timeout=20); return "sent"
    except urllib.error.HTTPError as e:
        m = e.read().decode()
        return "dup" if "other campaign" in m else ("sent" if "already" in m.lower() else "error:" + m[:80])
def has(s, l): s = (s or "").lower(); return any(k in s for k in l)

SIG = ["Nathan Fenina", "Agence Decupler"]
def bk(word_reason, keep):  # breakup mail commun
    return ("je clôture, {{companyName}} ?",
            [f"sans réponse je pars du principe que {word_reason}. un mot et j'arrête.", "",
             f"{keep} pour {{{{companyName}}}} reste dispo si vous la voulez.", "", *SIG, "",
             "PPS : un « stop » et je vous laisse tranquille."], 2)

GROUPS = {
 "hotellerie": ("Decupler · Hôtellerie · Site-offert", [
   ("le site de {{companyName}}",
    ["bonjour, je suis tombé sur {{companyName}} à {{ville}} et j'ai regardé votre site.", "",
     "il est bien, mais on peut le rendre plus moderne et surtout pousser les visiteurs à réserver en direct, sans passer par Booking (et sans la commission).", "",
     "je vous ai préparé une maquette. si elle vous plaît, vous la gardez — c'est offert, sans engagement.", "",
     "on regarde ensemble 15 min la semaine prochaine ?", "", *SIG, "",
     "PS : la maquette est à vous, même si on ne travaille pas ensemble."], 0),
   ("re: le site de {{companyName}}",
    ["au-delà du site, je vous montre comment {{companyName}} remonte sur Google et Maps à {{ville}} quand un voyageur cherche où dormir — c'est là que se jouent les réservations directes.", "",
     "15 min quand ça vous arrange ?", "", *SIG], 2),
   bk("ce n'est pas le moment, ou que votre site vous convient", "la maquette"),
 ]),
 "sante": ("Decupler · Santé-Médical · SEO", [
   ("vos patients vous trouvent-ils ?",
    ["bonjour, j'aide les structures de santé à être trouvées quand un patient cherche un praticien ou un soin « à {{ville}} » sur Google, Maps et les IA (ChatGPT).", "",
     "j'ai préparé pour {{companyName}} un point rapide : où vous apparaissez, où un confrère passe devant, et ce qui améliore votre visibilité et la prise de RDV en ligne.", "",
     "je vous le partage en 10 min ?", "", *SIG, "",
     "PS : le point est à vous, que vous travailliez avec nous ou pas."], 0),
   ("re: vos patients vous trouvent-ils ?",
    ["concrètement je vous montre les recherches où {{companyName}} n'apparaît pas encore, et les réglages simples (fiche Google, site) qui vous rendent visible à {{ville}}.", "",
     "15 min quand vous voulez.", "", *SIG], 2),
   bk("ce n'est pas le sujet du moment", "le point"),
 ]),
 "commerce": ("Decupler · Commerce-Local · SEO-Maps", [
   ("{{companyName}} sur Google Maps",
    ["bonjour, j'aide les commerces à ressortir sur Google et Maps quand un client cherche un produit près de chez lui à {{ville}}.", "",
     "j'ai préparé pour {{companyName}} un aperçu : ce qui vous fait remonter (ou pas) et comment capter plus de visites en boutique.", "",
     "je vous le partage en 10 min ?", "", *SIG, "",
     "PS : l'aperçu est à vous, que vous bossiez avec nous ou pas."], 0),
   ("re: {{companyName}} sur Google Maps",
    ["concrètement, une fiche Google optimisée + un site propre = plus de gens qui vous trouvent et poussent la porte. je vous montre les 3 réglages prioritaires pour {{companyName}}.", "",
     "15 min quand ça vous arrange ?", "", *SIG], 2),
   bk("ce n'est pas le moment", "l'aperçu"),
 ]),
 "sport": ("Decupler · Sport-Loisirs · SEO", [
   ("plus d'adhérents pour {{companyName}} ?",
    ["bonjour, j'aide les salles et centres à être trouvés quand quelqu'un cherche « sport, piscine ou remise en forme à {{ville}} ».", "",
     "j'ai préparé pour {{companyName}} un point sur votre visibilité et comment transformer ces recherches en inscriptions.", "",
     "10 min pour que je vous le partage ?", "", *SIG, "",
     "PS : le point est à vous, que vous travailliez avec nous ou pas."], 0),
   ("re: plus d'adhérents pour {{companyName}} ?",
    ["concrètement, la fiche Google + un site clair = plus de personnes qui vous trouvent et s'inscrivent. je vous montre les priorités pour {{companyName}} à {{ville}}.", "",
     "15 min quand vous voulez.", "", *SIG], 2),
   bk("ce n'est pas le moment", "le point"),
 ]),
 "services": ("Decupler · Services-Pro-B2B · SEO-Leads", [
   ("{{companyName}} — plus de demandes entrantes ?",
    ["bonjour, j'aide les entreprises de services à générer des demandes entrantes via le référencement (Google + IA), sans dépendre uniquement du bouche-à-oreille.", "",
     "j'ai préparé pour {{companyName}} un aperçu : les recherches de vos clients où vous êtes absent, et le volume de leads potentiels.", "",
     "je vous le partage en 10 min ?", "", *SIG, "",
     "PS : l'aperçu est à vous, que vous travailliez avec nous ou pas."], 0),
   ("re: {{companyName}} — plus de demandes entrantes ?",
    ["concrètement je vous montre, sur des recherches précises, quel concurrent capte les demandes à votre place et comment {{companyName}} récupère ces leads.", "",
     "15 min quand ça vous arrange ?", "", *SIG], 2),
   bk("ce n'est pas prioritaire là", "l'aperçu"),
 ]),
 "institutions": ("Decupler · Institutions-Autres · SEO", [
   ("la visibilité de {{companyName}}",
    ["bonjour, j'aide les organisations à être trouvées et à bien ressortir sur Google et les IA quand on cherche leurs services à {{ville}}.", "",
     "j'ai préparé un point rapide pour {{companyName}} : votre visibilité actuelle et les premières actions simples.", "",
     "10 min pour en parler ?", "", *SIG, "",
     "PS : le point est à vous, sans engagement."], 0),
   ("re: la visibilité de {{companyName}}",
    ["concrètement je vous montre où {{companyName}} apparaît (ou pas) et les réglages simples qui améliorent votre présence en ligne à {{ville}}.", "",
     "15 min quand vous voulez.", "", *SIG], 2),
   bk("ce n'est pas le moment", "le point"),
 ]),
}

# ---- classification (priorité de haut en bas) ----
HOTEL = ['hôtel','hotel','manor','manoir','château','chateau','domaine','hôtes','gîte','gite','camping','logis','auberge','résidence','vacances','vacation','love room','love-room','villa']
SPORT = ['salle de sport','complexe sportif','club de sport','fitness','centre aquatique','aquatic','espace aquatique','musculation','crossfit']
SANTE = ['hôpital','hopital','clinique','médecin','medecin','cabinet médical','centre médical','maison de santé','centre de santé','kinésith','infirmier','radiolog','ophtalmo','imagerie','rééducation','convalescence','ambulanc','soins à domicile','laboratoire d\'analyse','soins palliatifs','podolog','ergothérap','pharmacie','conseiller santé','dentaire','dentiste','sage-femme','orthophon','psychiatr','handicap','soins ambulatoires','soins aux personnes']
COMMERCE = ['parfumerie','opticien','magasin','matériel médical','appareils auditifs','grossiste','hypermarché','discount','fabricant','laboratoire pharmaceutique','technologies médicales','équipements médicaux','fournisseur','boutique','piscine','spa and','construction de piscine']
SERVICES = ['intérim','interim','recrutement','immobil','assurance','banque','formation','séminaire','centre d\'appel','centre d appel','siège social','bilan de comp',' rh ','ressources humaines','comptab','avocat','notaire','courtier','consulting','agence de','marketing','communication']
INSTIT = ['mairie','hôtel de ville','administration','université','universit','enseignement','association','organisme','mutuelle','refuge','à but non lucratif','office de tourisme','attraction','chambre de commerce','département','municipal','communaut']

def classify(cat, name):
    s = ((cat or "") + " | " + (name or "")).lower()
    if any(k in s for k in ['hôtel de ville','mairie','office de tourisme','chambre de commerce','communauté de communes']): return "institutions"
    if has(s, HOTEL): return "hotellerie"
    if has(s, SPORT): return "sport"
    if has(s, SANTE): return "sante"
    if has(s, COMMERCE): return "commerce"
    if has(s, SERVICES): return "services"
    if has(s, INSTIT): return "institutions"
    return "institutions"  # catch-all -> rien jeté

# ---- wellness déjà importé (scripts 09+10) à exclure ----
KEEP0 = ['réflexo','ostéo','naturo','médecine alternative','psychothérap','sophro','énergét','shiatsu','drainage','yoga','pilates','esthétique','esthéticien','onglerie','manucure','coiffure','bronzage','hammam','sauna','thalasso','balnéo','cryo','tatouage','barbier','spa','massage','beaut','bien-être','bien-etre','soin']
NOISE0 = ['hotel','hôtel','hôpital','hopital','clinique','pharmacie','laborat','matériel médical','grossiste','intérim','interim','maison de retraite','ambulanc','mutuelle','administration','office de tourisme','camping','gîte','chambre','immobil','piscine','aquatique','auditif','formation','médecin','cabinet médical','centre médical','centre de santé','maison de santé','rééducation','soins palliatifs','soins à domicile','association','attraction','banque','assurance','vétérinaire','dentaire','opticien','pédicure','podolog']
WELL_CAT = ['médecine alternative','médecine chinoise','massoth','épilation','électrolyse','parfumerie','chirurgien plasticien','chirurgien esthét','conseiller santé','sophro','hypnose','acupunc','tatouage','manucure','onglerie','coiffure','barbier']
NAMEKEEP = ['spa','institut','beaut','esthé','estheti','massage','bien-être','bien-etre','wellness','thalasso','balnéo','balneo','ayurvéda','ayurveda','zen','détente','detente','relax','soin','onglerie','ongles','nail','coiffure','barber','barbier','hammam','sauna','réflexo','reflexo','naturo','sophro','yoga','pilates','beauty','bulle','cocon','parenthèse','évasion','evasion','sérénité','serenite','harmonie','drainage','head spa','peeling','épil','epil']
NAMENOISE = ['médical','medical','matériel','ambulance','universit','vision','optique','dentaire','ventilation','castorama','super u','carrefour','leclerc','intermarché','formation','bilan de comp','rh ','handicap','orthopédie','ophtalmo','pharmac','laboratoire']
HOTELX = ['hôtel','hotel','manor','manoir','château','chateau','domaine','hôtes','gîte','gite','camping','logis','auberge','résidence','vacances','vacation','restaurant']
GYMX = ['club de sport','complexe sportif','salle de sport','fitness','aquatique','piscine']

def is_wellness(r, wellset):
    e = r["email"].strip().lower(); cat = r.get("category") or ""; nm = (r.get("name") or "")
    if e in wellset: return True
    if has(cat, KEEP0) and not has(cat, NOISE0): return True
    is_wc = has(cat, WELL_CAT); is_wn = (not cat.strip()) and has(nm, NAMEKEEP) and not has(nm, NAMENOISE)
    if (is_wc or is_wn) and not has(nm, HOTELX) and not has(cat, GYMX) and not has(nm, GYMX): return True
    return False

if __name__ == "__main__":
    clean, wellness = sys.argv[1], sys.argv[2]
    wellset = set(r["email"].strip().lower() for r in csv.DictReader(open(wellness)) if r["email"].strip())
    rows = list(csv.DictReader(open(clean)))
    buckets = {g: [] for g in GROUPS}; seen = set()
    for r in rows:
        e = r["email"].strip().lower(); nm = (r.get("name") or "").strip().lower()
        if not e or e in seen: continue
        if is_wellness(r, wellset): continue
        seen.add(e)
        buckets[classify(r.get("category"), r.get("name"))].append(r)
    print("répartition:", {g: len(v) for g, v in buckets.items()}, "total:", sum(len(v) for v in buckets.values()))
    result = {}
    for g, (title, steps) in GROUPS.items():
        leads = buckets[g]
        if not leads: continue
        camp = create_campaign(title); cid = camp.get("_id") or camp.get("id"); time.sleep(1)
        seq = get_seq_id(cid)
        for i, (subj, lines, d) in enumerate(steps, 1): write_step(seq, subj, lines, d, i); time.sleep(0.4)
        sent = 0; err = 0
        for r in leads:
            f = {"companyName": r.get("name", ""), "ville": r.get("city", "")}
            fn = (r.get("first_name") or "").strip()
            if fn: f["firstName"] = fn
            res = add_lead(cid, r["email"].strip(), f)
            if res.startswith("error"): err += 1
            else: sent += 1
            time.sleep(0.22)
        result[g] = {"cid": cid, "title": title, "leads": len(leads), "sent": sent, "err": err}
        print(f"OK {g}: {title} -> {cid} ({sent} sent, {err} err)")
    print("RESULT=" + json.dumps(result, ensure_ascii=False))
