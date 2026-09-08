#!/usr/bin/env python3
"""
Export CSV des leads "joignables par SMS" d'une audience (par défaut : Plombier · Nantes · local).

Cible les statuts d'appel encore ouverts (Répondeur / À appeler / Rappeler) et sépare
les numéros mobiles des numéros fixes (colonne type_tel = "mobile" ou "tel fixe"),
un SMS ne partant que sur un mobile.

Prérequis (variables d'environnement) :
  SUPABASE_URL   ex: https://<ref>.supabase.co
  SUPABASE_KEY   service_role (RLS activée sur outbound_leads)

Usage :
  python3 scripts/20_export_sms_plombier.py [--audience-id 45] [--out data/exports/xxx.csv]

Sortie : data/exports/ (gitignoré — les données restent hors du repo, cf. .gitignore).
"""
import argparse, csv, json, os, re, sys, urllib.parse, urllib.request

STATUTS = ["Répondeur", "À appeler", "Rappeler"]
COLS = "id,full_name,company,phone,call_status,notes,demo_url"


def fetch(audience_id):
    base = os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/outbound_leads"
    key = os.environ["SUPABASE_KEY"]
    q = urllib.parse.urlencode({
        "select": COLS,
        "audience_id": f"eq.{audience_id}",
        "call_status": "in.(" + ",".join(f'"{s}"' for s in STATUTS) + ")",
        "limit": "5000",
    })
    rq = urllib.request.Request(base + "?" + q, headers={
        "apikey": key, "Authorization": "Bearer " + key, "Accept": "application/json",
    })
    with urllib.request.urlopen(rq, timeout=60) as r:
        return json.load(r)


def normalise(raw):
    """+33/0033/06... -> E.164 (+33XXXXXXXXX). Renvoie None si inexploitable."""
    tel = re.sub(r"[^0-9+]", "", raw or "")
    if tel.startswith("0033"):
        tel = "+33" + tel[4:]
    elif tel.startswith("0") and len(tel) == 10:
        tel = "+33" + tel[1:]
    return tel if re.fullmatch(r"\+33[1-9]\d{8}", tel) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audience-id", type=int, default=45)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    root = os.path.join(os.path.dirname(__file__), "..")
    out = a.out or os.path.join(root, "data", "exports", f"audience_{a.audience_id}_sms.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)

    rows, skipped = [], []
    for lead in fetch(a.audience_id):
        tel = normalise(lead.get("phone"))
        if not tel:
            skipped.append(lead.get("company") or lead.get("full_name"))
            continue
        mobile = tel[3] in "67"
        rows.append({
            "entreprise": (lead.get("company") or lead.get("full_name") or "").strip(),
            "telephone": tel,
            "telephone_local": "0" + tel[3:],
            "type_tel": "mobile" if mobile else "tel fixe",
            "statut": lead.get("call_status") or "",
            "notes": lead.get("notes") or "",
        })
    rows.sort(key=lambda r: (r["type_tel"] != "mobile", r["entreprise"].lower()))

    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    nb_mob = sum(r["type_tel"] == "mobile" for r in rows)
    print(f"{out} — {len(rows)} lignes ({nb_mob} mobiles, {len(rows) - nb_mob} fixes)")
    if skipped:
        print(f"sans numéro exploitable : {len(skipped)} → {skipped[:5]}", file=sys.stderr)


if __name__ == "__main__":
    main()
