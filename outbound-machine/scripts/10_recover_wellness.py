#!/usr/bin/env python3
"""Récupère les leads wellness/beauté mal classés dans medspa_clean.csv (règle 'médecin' qui
sur-filtrait 'médecine', + fiches sans catégorie identifiées par nom) et les ajoute aux 2
campagnes Wellness A/B existantes. Sépare hôtels et salles de sport (buckets à part, non mailés).
Usage: LEMLIST_API_KEY=... python3 10_recover_wellness.py medspa_clean.csv medspa_wellness.csv <cidA> <cidB>"""
import os, sys, csv, json, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

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

def has(s, l): s = (s or "").lower(); return any(k in s for k in l)

# offre wellness/beauté/santé douce (même copy que A/B)
WELL_CAT = ['médecine alternative','médecine chinoise','massoth','épilation','électrolyse','parfumerie',
            'chirurgien plasticien','chirurgien esthét','conseiller santé','sophro','hypnose','acupunc',
            'tatouage','manucure','onglerie','coiffure','barbier']
NAMEKEEP = ['spa','institut','beaut','esthé','estheti','massage','bien-être','bien-etre','wellness','thalasso',
            'balnéo','balneo','ayurvéda','ayurveda','zen','détente','detente','relax','soin','onglerie','ongles',
            'nail','coiffure','barber','barbier','hammam','sauna','réflexo','reflexo','naturo','sophro','yoga',
            'pilates','beauty','bulle','cocon','parenthèse','évasion','evasion','sérénité','serenite','harmonie',
            'drainage','head spa','peeling','épil','epil']
NAMENOISE = ['médical','medical','matériel','ambulance','universit','vision','optique','dentaire','ventilation',
             'castorama','super u','carrefour','leclerc','intermarché','formation','bilan de comp','rh ',
             'handicap','orthopédie','ophtalmo','pharmac','laboratoire']
HOTEL = ['hôtel','hotel','manor','manoir','château','chateau','domaine','maison d\'hôtes','maison d’hôtes',
         'gîte','gite','camping','restaurant','love room','love-room','villa','logis','auberge','résidence']
GYM = ['club de sport','complexe sportif','salle de sport','fitness','aquatique','piscine']

def secteur_of(cat, name):
    s = ((cat or "") + " " + (name or "")).lower()
    if "spa" in s: return "spa"
    if any(k in s for k in ["massage","massoth","drainage","shiatsu","kobido"]): return "cabinet de massage"
    if any(k in s for k in ["réflexo","reflexo","ostéo","naturo","sophro","énergét","holistique","ayurvéd","médecine alternative","médecine chinoise","acupunc","hypnose"]): return "cabinet"
    if any(k in s for k in ["coiffure","manucure","onglerie","barbier","nail"]): return "salon"
    if any(k in s for k in ["bien-être","bien-etre","sauna","hammam"]): return "centre de bien-être"
    if any(k in s for k in ["beaut","esthé","estheti","épil","epil","parfum","bronzage"]): return "institut"
    return "établissement"

if __name__ == "__main__":
    clean, wellness, cida, cidb = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    seen = set(r["email"].strip().lower() for r in csv.DictReader(open(wellness)) if r["email"].strip())
    # rebuild what the wellness publisher already imported (wellness + KEEP-adjacent) so we skip them
    KEEP0 = ['réflexo','ostéo','naturo','médecine alternative','psychothérap','sophro','énergét','shiatsu','drainage','yoga','pilates','esthétique','esthéticien','onglerie','manucure','coiffure','bronzage','hammam','sauna','thalasso','balnéo','cryo','tatouage','barbier','spa','massage','beaut','bien-être','bien-etre','soin']
    NOISE0 = ['hotel','hôtel','hôpital','hopital','clinique','pharmacie','laborat','matériel médical','grossiste','intérim','interim','maison de retraite','ambulanc','mutuelle','administration','office de tourisme','camping','gîte','chambre','immobil','piscine','aquatique','auditif','formation','médecin','cabinet médical','centre médical','centre de santé','maison de santé','rééducation','soins palliatifs','soins à domicile','association','attraction','banque','assurance','vétérinaire','dentaire','opticien','pédicure','podolog']
    rows = list(csv.DictReader(open(clean)))
    for r in rows:
        e = r["email"].strip().lower()
        if e and e not in seen and has(r.get("category"), KEEP0) and not has(r.get("category"), NOISE0):
            seen.add(e)
    # recovery = wellness mal classés, en excluant hôtels & gyms
    recov, names = [], set()
    for r in rows:
        e = r["email"].strip().lower(); nm = (r.get("name") or "").strip().lower()
        if not e or e in seen: continue
        cat = r.get("category") or ""
        is_well_cat = has(cat, WELL_CAT)
        is_well_name = (not cat.strip()) and has(nm, NAMEKEEP) and not has(nm, NAMENOISE)
        if not (is_well_cat or is_well_name): continue
        if has(nm, HOTEL) or has(cat, GYM) or has(nm, GYM): continue   # hôtels/gyms = buckets à part
        if nm in names: continue                                       # dédup par nom
        names.add(nm); seen.add(e); recov.append(r)
    print(f"récupérés à ajouter en A/B: {len(recov)}")
    stats = {"A": 0, "B": 0, "err": 0}
    for i, r in enumerate(recov):
        which, cid = ("A", cida) if i % 2 == 0 else ("B", cidb)
        f = {"companyName": r.get("name",""), "secteur": secteur_of(r.get("category"), r.get("name")), "ville": r.get("city","")}
        fn = (r.get("first_name") or "").strip()
        if fn: f["firstName"] = fn
        res = add_lead(cid, r["email"].strip(), f)
        if res.startswith("error"): stats["err"] += 1; print("ERR", r["email"], res)
        else: stats[which] += 1
        time.sleep(0.25)
    print("STATS=" + json.dumps(stats))
