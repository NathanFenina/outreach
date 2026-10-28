"""Synchronise l'historique Lemlist vers Supabase « Outreach Cold Mail » :
- campaigns (anciennes campagnes en lot « legacy », compteurs par état de lead)
- do_not_contact : tout email déjà contacté (+ répondu / désinscrit), tous les domaines contactés,
  les désinscrits Lemlist et les clients (CLIENTS ci-dessous)
Écrit aussi data/synthese_campagnes.csv (lu par 33_synthese.py)."""
import base64, csv, io, json, os, sys, time, urllib.request
from collections import Counter, defaultdict
import outreach_db as db

K = os.environ["LEMLIST_API"]; H = {"Authorization": "Basic " + base64.b64encode((":" + K).encode()).decode()}
FREEMAIL = {"gmail.com", "hotmail.com", "hotmail.fr", "yahoo.fr", "yahoo.com", "outlook.com", "outlook.fr", "orange.fr",
            "wanadoo.fr", "free.fr", "icloud.com", "live.fr", "sfr.fr", "laposte.net", "me.com", "aol.com", "gmx.fr", "msn.com"}
# clients et références (decupler.com + mémoire) : jamais prospectés
CLIENTS = {"apogea.fr": "Apogea", "betomorrow.com": "BeTomorrow", "reuxtravaux.fr": "Reux Travaux", "gestalt.fr": "École Humaniste de Gestalt",
           "pluxee.fr": "Pluxee", "clim-confort.fr": "Clim Confort", "academiemadelrieux.com": "Académie Madelrieux",
           "lepoint.fr": "Le Point", "decathlon.fr": "Décathlon", "decathlon.com": "Décathlon", "atoo-energie.fr": "Atoo Énergie"}
CLIENT_NAMES = ["Cloudtech", "BT Blue", "TechMedias", "Orators", "L'Artisan d'à côté", "Atoo Énergie"]


def get(p):
    for i in range(5):
        try:
            return urllib.request.urlopen(urllib.request.Request("https://api.lemlist.com/api" + p, headers=H), timeout=120).read().decode()
        except Exception:
            if i == 4: raise
            time.sleep(2 ** i)


camps, off = [], 0
while True:
    b = json.loads(get(f"/campaigns?limit=100&offset={off}")); camps += b
    if len(b) < 100: break
    off += 100

dnc, doms, synth, crow, unsent = {}, defaultdict(set), [], [], set()
NOT_SENT = {"aucun", "", "scanned", "reviewed", "skipped", "paused"}
REPLIED = {"emailsReplied", "emailsInterested", "emailsNotInterested", "linkedinReplied", "interested", "notInterested"}
for c in camps:
    rows = list(csv.DictReader(io.StringIO(get(f"/campaigns/{c['_id']}/export/leads?state=all"))))
    st = Counter(r.get("lastState") or "aucun" for r in rows)
    launched = sum(v for k, v in st.items() if k not in NOT_SENT)
    replied = sum(v for k, v in st.items() if k in REPLIED)
    synth.append(dict(id=c["_id"], name=c["name"], status=c["status"], leads=len(rows), launched=launched, replied=replied,
                      bounced=st.get("emailsBounced", 0), unsub=st.get("emailsUnsubscribed", 0), states=json.dumps(st, ensure_ascii=False)))
    crow.append(dict(code="L-" + c["_id"][-8:], name=c["name"], lemlist_id=c["_id"], esp_lot="legacy", status=c["status"],
                     prospects=launched, human_replies=replied, notes="campagne Lemlist antérieure au 28/10 (réponses = états Lemlist, auto-réponses comprises)"))
    for r in rows:
        e = (r.get("email") or "").strip().lower()
        if "@" not in e: continue
        s = r.get("lastState") or ""
        if s in NOT_SENT:
            unsent.add(e); continue
        reason = "desinscrit" if s == "emailsUnsubscribed" else "repondu" if s in REPLIED else "deja_contacte"
        if dnc.get(e) not in ("desinscrit", "repondu"):
            dnc[e] = reason
        d = e.split("@")[1]
        if d not in FREEMAIL: doms[d].add(c["_id"])
try:
    for u in json.loads(get("/unsubscribes?limit=10000")):
        v = (u.get("value") or u.get("email") or "").lower()
        if "@" in v: dnc[v] = "desinscrit"
        elif "." in v: doms[v].add("unsubscribed")
except Exception as ex:
    print("unsubscribes:", ex)

rows = [dict(email=e, domain=e.split("@")[1], reason=r, source="lemlist") for e, r in dnc.items()]
rows += [dict(email=None, domain=d, reason="deja_contacte", source="lemlist:domaine") for d in doms]
rows += [dict(email=None, domain=d, reason="client", source=n) for d, n in CLIENTS.items()]
# remplace la liste (pas de delete via la fonction : on charge dans une table vide ou on ignore les doublons d'email)
db.upsert("do_not_contact", [r for r in rows if r["email"]], on_conflict="email", ignore_duplicates=True) if False else None
existing = {(x["email"] or "", x["domain"] or "") for x in db.select("do_not_contact", "email,domain")}
new = [r for r in rows if ((r["email"] or ""), (r["domain"] or "")) not in existing]
db.upsert("do_not_contact", new)
# leads chargés mais jamais envoyés : pas bloquants
fix = sorted(unsent - set(dnc))
for i in range(0, len(fix), 300):
    db.call({"action": "update", "table": "do_not_contact", "values": {"reason": "autre", "source": "lemlist:jamais_envoye"}, "in": {"email": fix[i:i + 300]}})
fixd = sorted({e.split("@")[1] for e in fix} - set(doms))
for i in range(0, len(fixd), 300):
    db.call({"action": "update", "table": "do_not_contact", "values": {"reason": "autre", "source": "lemlist:jamais_envoye"}, "in": {"domain": fixd[i:i + 300]}, "eq": {"source": "lemlist:domaine"}})
print("jamais envoyés (non bloquants) :", len(fix), "emails,", len(fixd), "domaines")
db.upsert("campaigns", crow, "code")
os.makedirs("../data", exist_ok=True)
with open("../data/synthese_campagnes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=synth[0].keys()); w.writeheader(); w.writerows(synth)
print(f"{len(camps)} campagnes · {len(dnc)} emails · {len(doms)} domaines · {len(new)} lignes ajoutées à do_not_contact")
print("clients sans domaine connu (à compléter) :", ", ".join(CLIENT_NAMES))
