#!/usr/bin/env python3
"""
Charge data/01_clean/master_leads.csv dans la table Supabase public.outbound_leads
via l'API PostgREST (bulk insert, par lots) — les données ne transitent pas par le LLM.

Prérequis (variables d'environnement) :
  SUPABASE_URL   ex: https://<ref>.supabase.co
  SUPABASE_KEY   clé anon/publishable (ou service_role pour bypass RLS)

Sécurité : la table a la RLS activée. Pour charger avec la clé anon, une policy
d'insertion temporaire doit exister le temps du run, puis être supprimée :
  create policy tmp_load_insert on public.outbound_leads for insert to anon with check (true);
  grant insert on public.outbound_leads to anon;
  -- ... run ...
  drop policy tmp_load_insert on public.outbound_leads;
  revoke insert on public.outbound_leads from anon;
Avec une clé service_role, rien de tout ça n'est nécessaire.
"""
import csv, json, os, sys, urllib.request, urllib.error

URL = os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/outbound_leads"
KEY = os.environ["SUPABASE_KEY"]
CSV = os.path.join(os.path.dirname(__file__), "..", "data", "01_clean", "master_leads.csv")
BATCH = 1000

def to_bool(x): return str(x).strip().lower() == "true"

def build_rows():
    rows = []
    with open(CSV, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            email = (r["email"] or "").strip() or None
            rows.append(dict(
                first_name=r["first_name"] or None, last_name=r["last_name"] or None,
                full_name=r["full_name"] or None, email=email, phone=(r["phone"] or None),
                job_title=r["job_title"] or None, seniority=r["seniority"] or None,
                company=r["company"] or None, domain=r["domain"] or None,
                industry=r["industry"] or None, location=r["location"] or None,
                linkedin=r["linkedin"] or None, email_certainty=r["email_certainty"] or None,
                is_generic_email=to_bool(r["is_generic_email"]),
                channel=("email" if email else "none"),
                source_file=r["source_file"] or None,
            ))
    return rows

def main():
    rows = build_rows()
    print("à charger:", len(rows))
    total = 0
    for i in range(0, len(rows), BATCH):
        batch = rows[i:i+BATCH]
        req = urllib.request.Request(
            URL, data=json.dumps(batch).encode(), method="POST",
            headers={"apikey": KEY, "Authorization": "Bearer " + KEY,
                     "Content-Type": "application/json", "Prefer": "return=minimal"})
        try:
            with urllib.request.urlopen(req) as resp:
                total += len(batch)
                print(f"  lot {i//BATCH+1}: {resp.status} total={total}")
        except urllib.error.HTTPError as e:
            print(f"  lot {i//BATCH+1} ERREUR {e.code}: {e.read().decode()[:300]}")
            sys.exit(1)
    print("OK chargé:", total)

if __name__ == "__main__":
    main()
