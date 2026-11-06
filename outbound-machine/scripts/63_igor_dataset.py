"""Import du dataset UltB d'Igor (04/11, Google Sheet « Decupler_Datasets_UltB_2026-11-04 », copié en CSV dans
../data/datasets/igor/, non commité). Pour chaque onglet : liste noire (refus, désinscrits, clients, concurrents),
contactés il y a moins de 90 jours (règle d'Igor), doublons avec nos propres leads, puis découpage Google / Others.
Sortie : ../data/datasets/igor/ready_<onglet>.csv + résumé imprimé (sert au suivi des audiences « à lancer / lancée »)."""
import csv, glob, json, os, datetime
import outreach_db as db

HARD = {"repondu", "desinscrit", "client", "concurrent", "agressif"}  # liste noire définitive (Igor : refus + désinscrits)
dnc_dom, dnc_mail, recent_dom, recent_mail = set(), set(), set(), set()
for r in db.select("do_not_contact", "email,domain,reason"):
    tgt = (dnc_dom, dnc_mail) if r["reason"] in HARD else (recent_dom, recent_mail) if r["reason"] == "deja_contacte" else None
    if not tgt: continue
    if r["domain"]: tgt[0].add(r["domain"].lower())
    if r["email"]: tgt[1].add(r["email"].lower())
# dates réelles du dernier envoi (62_lemlist_last_contact.py) : contacté < 90 jours = on attend
LC = "../data/campaigns/lemlist_last_contact.json"
if os.path.exists(LC):
    lim = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=90)).isoformat()
    lc = json.load(open(LC))
    recent_mail = {e for e, v in lc.items() if (v.get("last_sent") or "") >= lim} | recent_mail
    dnc_mail |= {e for e, v in lc.items() if v.get("unsubscribed")}
# nos propres leads (datasets Lemlist FR), pour ne pas écrire deux fois à la même personne
ours = set()
for f in glob.glob("../data/datasets/DS-*.csv"):
    for r in csv.DictReader(open(f)):
        if r.get("domain"): ours.add(r["domain"].lower())
out = {}
for f in sorted(glob.glob("../data/datasets/igor/*.csv")):
    tab = os.path.basename(f)[:-4]
    if tab.startswith("ready_"): continue
    rows, st = [], {"total": 0, "liste noire": 0, "contacté < 90 j": 0, "déjà chez nous": 0}
    for r in csv.DictReader(open(f)):
        st["total"] += 1
        d, e = (r.get("domain") or "").lower(), (r.get("email") or "").lower()
        if d in dnc_dom or e in dnc_mail: st["liste noire"] += 1; continue
        if e in recent_mail: st["contacté < 90 j"] += 1; continue  # règle Igor : la personne, pas toute l'entreprise
        if d in ours and tab == "bonus-fr": st["déjà chez nous"] += 1; continue
        rows.append(r)
    for k in ("Google", "Others"):
        st[k] = sum(1 for r in rows if r["esp"] == k)
    st["DM"] = sum(1 for r in rows if r["role_type"] == "DM"); st["Champion"] = sum(1 for r in rows if r["role_type"] == "Champion")
    st["Mailbox"] = sum(1 for r in rows if r["role_type"] == "Mailbox")
    if rows:
        with open(f"../data/datasets/igor/ready_{tab}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    out[tab] = st
    print(tab, st)
json.dump(out, open("../data/datasets/igor/summary.json", "w"), ensure_ascii=False, indent=1)
