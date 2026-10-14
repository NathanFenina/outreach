"""Registre « déjà contacté » : toutes les adresses et tous les domaines présents dans
TOUTES les campagnes Lemlist (actives, en pause, archivées) + la liste noire Lemlist.

Usage :
  python check_deja_contacte.py --refresh                 # reconstruit le registre
  python check_deja_contacte.py leads.csv [--col email]   # écrit leads_jamais_contactes.csv
  python check_deja_contacte.py --campaign cam_xxx        # audite une campagne

Règle : un lead n'entre dans une campagne que s'il n'est ni dans le registre (email),
ni sur un domaine déjà contacté (sauf adresses génériques d'un salon type Batimat).
Clé API : variable LEMLIST_API_KEY ou fichier .lemkey.
"""
import argparse, base64, csv, io, json, os, sys, time, urllib.request

REG = os.path.join(os.path.dirname(__file__), "..", "data", "registre_contactes.json")
FREEMAIL = {"gmail.com", "hotmail.com", "hotmail.fr", "yahoo.fr", "yahoo.com", "outlook.com",
            "outlook.fr", "orange.fr", "wanadoo.fr", "free.fr", "icloud.com", "live.fr", "sfr.fr", "laposte.net"}


def key():
    k = os.environ.get("LEMLIST_API_KEY")
    if not k and os.path.exists(".lemkey"):
        k = open(".lemkey").read().strip()
    if not k:
        sys.exit("LEMLIST_API_KEY manquante")
    return "Basic " + base64.b64encode((":" + k).encode()).decode()


def get(path, auth, tries=5):
    req = urllib.request.Request("https://api.lemlist.com/api" + path, headers={"Authorization": auth})
    for i in range(tries):
        try:
            return urllib.request.urlopen(req, timeout=120).read().decode()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def refresh(auth):
    camps, off = [], 0
    while True:
        batch = json.loads(get(f"/campaigns?limit=100&offset={off}", auth))
        batch = batch if isinstance(batch, list) else batch.get("campaigns", [])
        camps += batch
        if len(batch) < 100:
            break
        off += 100
    emails = {}
    for c in camps:
        for r in csv.DictReader(io.StringIO(get(f"/campaigns/{c['_id']}/export/leads?state=all", auth))):
            e = (r.get("email") or "").strip().lower()
            if e:
                emails.setdefault(e, []).append(c["_id"])
    try:
        unsub = json.loads(get("/unsubscribes?limit=10000", auth))
        for u in unsub if isinstance(unsub, list) else []:
            e = (u.get("value") or u.get("email") or "").lower()
            if "@" in e:
                emails.setdefault(e, []).append("unsubscribed")
    except Exception:
        pass
    os.makedirs(os.path.dirname(REG) or ".", exist_ok=True)
    json.dump({"campaigns": len(camps), "emails": emails}, open(REG, "w"))
    print(f"registre : {len(emails)} adresses sur {len(camps)} campagnes")


def load():
    reg = json.load(open(REG))["emails"]
    doms = {}
    for e, cs in reg.items():
        d = e.split("@")[1]
        if d not in FREEMAIL:
            doms.setdefault(d, set()).update(cs)
    return reg, doms


def status(email, reg, doms, own=None):
    e = email.strip().lower()
    other = [c for c in reg.get(e, []) if c != own]
    if other:
        return "email déjà contacté"
    d = e.split("@")[-1]
    if [c for c in doms.get(d, ()) if c != own]:
        return "domaine déjà contacté"
    return "jamais contacté"


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv", nargs="?")
    p.add_argument("--col", default="email")
    p.add_argument("--refresh", action="store_true")
    p.add_argument("--campaign")
    a = p.parse_args()
    auth = key()
    if a.refresh or not os.path.exists(REG):
        refresh(auth)
    reg, doms = load()
    if a.campaign:
        rows = list(csv.DictReader(io.StringIO(get(f"/campaigns/{a.campaign}/export/leads?state=all", auth))))
        from collections import Counter
        print(Counter(status(r["email"], reg, doms, a.campaign) for r in rows if r.get("email")))
    elif a.csv:
        rows = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
        ok = [r for r in rows if status(r[a.col], reg, doms) == "jamais contacté"]
        out = a.csv.rsplit(".", 1)[0] + "_jamais_contactes.csv"
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(ok)
        print(f"{len(ok)}/{len(rows)} jamais contactés -> {out}")
