#!/usr/bin/env python3
"""
Consolide les 39 exports Clay + 1 export Apollo (data/00_raw/*.csv) en une base
maître unique, nettoyée et dédoublonnée -> data/01_clean/master_leads.csv

- Ramène 22 schémas hétérogènes à un schéma commun.
- Extrait l'email depuis (par ordre de priorité) : Custom Waterfall > Find work email > Email.
- Extrait les téléphones quand présents (export Apollo).
- Dédoublonne sur email, puis sur URL LinkedIn, puis sur (nom+entreprise).
- Journalise tout dans logs/nettoyage.log
"""
import glob, csv, re, os, sys, datetime

RAW = os.path.join(os.path.dirname(__file__), "..", "data", "00_raw")
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "01_clean")
LOG = os.path.join(os.path.dirname(__file__), "..", "logs", "nettoyage.log")
os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.dirname(LOG), exist_ok=True)

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
# emails génériques à écarter (on veut un contact nominatif)
GENERIC = re.compile(r"^(contact|info|hello|bonjour|team|sales|support|admin|"
                     r"commercial|rh|recrutement|compta|accueil|service|no-?reply)@", re.I)

def clean_email(*cands):
    for c in cands:
        if not c:
            continue
        m = EMAIL_RE.search(c)
        if m:
            return m.group(0).lower().strip()
    return ""

def norm_phone(*cands):
    for c in cands:
        if not c:
            continue
        digits = re.sub(r"[^\d+]", "", c)
        if len(re.sub(r"\D", "", digits)) >= 8:
            # format international FR simple
            d = re.sub(r"\D", "", digits)
            if digits.startswith("+"):
                return "+" + d
            if d.startswith("0") and len(d) == 10:
                return "+33" + d[1:]
            if d.startswith("33"):
                return "+" + d
            return "+" + d
    return ""

def g(row, *keys):
    for k in keys:
        if k in row and row[k] and row[k].strip():
            return row[k].strip()
    return ""

rows_out = []
per_file = []
files = sorted(glob.glob(os.path.join(RAW, "*.csv")))

for f in files:
    base = os.path.basename(f)
    n_in = n_kept = 0
    with open(f, encoding="utf-8", errors="replace") as fh:
        r = csv.DictReader(fh)
        for row in r:
            n_in += 1
            email = clean_email(g(row, "Custom Waterfall"),
                                g(row, "Find work email"),
                                g(row, "Email"),
                                g(row, "Secondary Email"))
            phone = norm_phone(g(row, "Mobile Phone"),
                               g(row, "Work Direct Phone"),
                               g(row, "Corporate Phone"),
                               g(row, "Other Phone"))
            first = g(row, "First Name")
            last = g(row, "Last Name")
            full = g(row, "Full Name") or (first + " " + last).strip()
            company = g(row, "Company Name", "Company Name for Emails")
            title = g(row, "Job Title", "Title")
            domain = g(row, "Company Domain", "Website", "Website clean")
            linkedin = g(row, "LinkedIn Profile", "Person Linkedin Url")
            location = g(row, "Location", "City", "Country")
            seniority = g(row, "Seniority")
            industry = g(row, "Industry")
            certainty = g(row, "Certainty - Emails", "Email Confidence", "Email Status")
            # on garde la ligne si on a au moins un identifiant exploitable
            if not (full or linkedin or company):
                continue
            rows_out.append(dict(
                first_name=first, last_name=last, full_name=full,
                email=email, phone=phone,
                job_title=title, seniority=seniority,
                company=company, domain=domain, industry=industry,
                location=location, linkedin=linkedin,
                email_certainty=certainty,
                is_generic_email=bool(email and GENERIC.match(email)),
                source_file=base,
            ))
            n_kept += 1
    per_file.append((base, n_in, n_kept))

# --- Dédoublonnage ---
def key_email(r): return r["email"]
def key_li(r): return r["linkedin"].rstrip("/").lower()
def key_nc(r): return (r["full_name"].lower(), r["company"].lower())

seen_e, seen_li, seen_nc = set(), set(), set()
deduped = []
dups = 0
for r in rows_out:
    e, li, nc = key_email(r), key_li(r), key_nc(r)
    if e and e in seen_e: dups += 1; continue
    if li and li in seen_li: dups += 1; continue
    if (not e and not li) and nc in seen_nc: dups += 1; continue
    if e: seen_e.add(e)
    if li: seen_li.add(li)
    seen_nc.add(nc)
    deduped.append(r)

cols = ["first_name","last_name","full_name","email","phone","job_title",
        "seniority","company","domain","industry","location","linkedin",
        "email_certainty","is_generic_email","source_file"]
out_path = os.path.join(OUT, "master_leads.csv")
with open(out_path, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    for r in deduped:
        w.writerow(r)

# --- Stats ---
tot = len(deduped)
with_email = sum(1 for r in deduped if r["email"])
with_phone = sum(1 for r in deduped if r["phone"])
nominal = sum(1 for r in deduped if r["email"] and not r["is_generic_email"])
generic = sum(1 for r in deduped if r["is_generic_email"])

ts = datetime.datetime.utcnow().isoformat()
with open(LOG, "a", encoding="utf-8") as lg:
    lg.write(f"\n===== Consolidation {ts}Z =====\n")
    for base, ni, nk in per_file:
        lg.write(f"  {base}: {ni} lues -> {nk} gardées\n")
    lg.write(f"  Total avant dédoublonnage: {len(rows_out)}\n")
    lg.write(f"  Doublons retirés: {dups}\n")
    lg.write(f"  TOTAL base maître: {tot}\n")
    lg.write(f"  Avec email: {with_email} | dont nominatifs: {nominal} | génériques: {generic}\n")
    lg.write(f"  Avec téléphone: {with_phone}\n")

print(f"Fichiers traités : {len(files)}")
print(f"Lignes lues (cumul) : {len(rows_out)}")
print(f"Doublons retirés : {dups}")
print(f"TOTAL base maître : {tot}")
print(f"  - avec email : {with_email} ({with_email/tot*100:.1f}%) dont {nominal} nominatifs, {generic} génériques")
print(f"  - avec téléphone : {with_phone} ({with_phone/tot*100:.1f}%)")
print(f"Sortie : {out_path}")
