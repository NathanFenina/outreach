"""Importe un lot qualifié et enrichi dans sa campagne Lemlist EN BROUILLON (rien n'est lancé) et dans Supabase.
Garde-fous : email trouvé (DELIVERABLE / HIGH_PROBABILITY ; CATCH_ALL exclu), jamais contacté (email ET domaine,
table do_not_contact), dédoublonnage Lemlist (deduplicate=true), 300 leads max.
Usage : python 42_import_leads.py 101-G [--dry]"""
import base64, csv, json, os, sys, time, urllib.parse, urllib.request
import outreach_db as db

lot = sys.argv[1]; dry = "--dry" in sys.argv
D = "../data/campaigns/"
H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode(), "Content-Type": "application/json"}
camp = {c["code"].rsplit("-", 1)[0]: c for c in db.select("campaigns", "id,code,lemlist_id,esp_lot") if c["code"][:3].isdigit()}[lot]
emails = {r["linkedin_url"]: r for r in csv.DictReader(open(D + "enriched.csv"))}
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
dnc_e, dnc_d = set(), set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK:
        if r["email"]: dnc_e.add(r["email"].lower())
        if r["domain"]: dnc_d.add(r["domain"].lower())
rows, skipped = [], {"sans email": 0, "catch-all": 0, "déjà contacté": 0}
for r in csv.DictReader(open(f"{D}qualified_{lot}.csv")):
    e = emails.get(r["linkedin_url"], {})
    em = (e.get("email") or "").lower()
    if not em: skipped["sans email"] += 1; continue
    if e.get("email_status") not in ("DELIVERABLE", "HIGH_PROBABILITY"): skipped["catch-all"] += 1; continue
    if em in dnc_e or em.split("@")[1] in dnc_d or r["domain"] in dnc_d: skipped["déjà contacté"] += 1; continue
    r["email"], r["email_status"] = em, e["email_status"]; rows.append(r)
rows = rows[:300]
print(lot, camp["code"], "→", len(rows), "leads ; écartés :", skipped)
if dry or len(rows) < 100:
    print("ARRÊT : moins de 100 leads (règle Nathan)" if len(rows) < 100 else "simulation"); sys.exit(0 if dry else 1)
comp = {c["domain"]: c["id"] for c in db.select("companies", "id,domain")}
ok = 0
for r in rows:
    body = {"firstName": r["first_name"], "lastName": r["last_name"], "companyName": r["company"], "companyDomain": r["domain"],
            "linkedinUrl": r["linkedin_url"], "jobTitle": r["title"], "seg": r["seg"], "unit": r["unit"], "proof": r["proof"],
            "icebreaker": r["icebreaker"], "zone": r["zone"]}
    url = f"https://api.lemlist.com/api/campaigns/{camp['lemlist_id']}/leads/{urllib.parse.quote(r['email'])}?deduplicate=true"
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=json.dumps(body).encode(), headers=H, method="POST"), timeout=60); ok += 1
    except urllib.error.HTTPError as ex:
        print("lemlist", r["email"], ex.code, ex.read().decode()[:120]); continue
    time.sleep(0.25)
    c = db.upsert("contacts", [dict(company_id=comp.get(r["domain"]), first_name=r["first_name"], last_name=r["last_name"], title=r["title"],
                                    persona_grp="champion" if r["rank"] == "3" else "decideur", email=r["email"], email_status=r["email_status"],
                                    linkedin_url=r["linkedin_url"], language="fr", source="lemlist_db+fullenrich", status="en_campagne")], "email", return_rows=True)
    db.upsert("campaign_contacts", [dict(campaign_id=camp["id"], contact_id=c[0]["id"], state="brouillon")], "campaign_id,contact_id")
db.update("campaigns", {"prospects": ok}, {"code": camp["code"]})
print("importés dans Lemlist (brouillon) :", ok)
