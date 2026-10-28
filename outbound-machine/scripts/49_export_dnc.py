"""Exporte la liste d'exclusion à envoyer à Igor : domaines déjà contactés, ayant répondu, désinscrits, clients.
Sortie : ../data/datasets/DNC-igor.csv (non commité)."""
import csv
import outreach_db as db

BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
FREEMAIL = {"gmail.com", "hotmail.com", "hotmail.fr", "yahoo.fr", "yahoo.com", "outlook.com", "outlook.fr", "orange.fr", "wanadoo.fr",
            "free.fr", "icloud.com", "live.fr", "sfr.fr", "laposte.net", "me.com", "aol.com", "gmx.fr", "msn.com"}
doms = sorted({r["domain"].lower() for r in db.select("do_not_contact", "domain,reason")
               if r["reason"] in BLOCK and r["domain"] and r["domain"].lower() not in FREEMAIL})
with open("../data/datasets/DNC-igor.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["domain"]); w.writerows([d] for d in doms)
print(len(doms), "domaines")
