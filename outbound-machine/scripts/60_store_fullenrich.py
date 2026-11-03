"""Range un export CSV FullEnrich dans ../data/datasets/enriched_fullenrich.json (cache par URL LinkedIn).
Utilisable = statut « Valid & safe to send email » ou « Probably Valid Email » (catch-all exclus), hors liste noire,
et email sur le domaine de l'entreprise visée (sinon le contact a changé de société).
Usage : python 60_store_fullenrich.py <export.csv> <lignes_source.json>   (lignes source : dataset d'origine, avec domain + linkedin_url)"""
import csv, json, os, sys
import outreach_db as db

BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
P = "../data/datasets/enriched_fullenrich.json"
src, rows = sys.argv[1], json.load(open(sys.argv[2]))
by_lk = {r["linkedin_url"].rstrip("/").lower(): r for r in rows}
by_name = {(r["first_name"].strip().lower(), r["last_name"].strip().lower(), r["domain"]): r for r in rows}
dnc = set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK: dnc.update(x.lower() for x in (r["email"], r["domain"]) if x)
cache = json.load(open(P)) if os.path.exists(P) else {}
stats = {"lignes": 0, "trouvés": 0, "utilisables": 0, "autre société": 0, "catch-all": 0}
for r in csv.DictReader(open(src, encoding="utf-8-sig")):
    stats["lignes"] += 1
    lk = (r.get("LinkedIn Profile Url") or r.get("Linkedin Url") or "").rstrip("/").lower()
    s = by_lk.get(lk) or next((v for (f, l, d), v in by_name.items() if f == (r.get("First Name") or "").strip().lower() and l == (r.get("Last Name") or "").strip().lower()), None)
    if not s: continue
    e, st = (r.get("Email (FullEnrich)") or "").lower(), r.get("Bounce Status (FullEnrich)") or ""
    stats["trouvés"] += bool(e); stats["catch-all"] += st == "Catch-All"
    d = s["domain"].lower(); ed = e.split("@")[-1]
    same = bool(e) and (ed == d or ed.endswith("." + d) or ed.split(".")[0] == d.split(".")[0])
    ok = bool(e) and st in ("Valid & safe to send email", "Probably Valid Email") and e not in dnc and ed not in dnc and same
    stats["autre société"] += bool(e) and not same
    stats["utilisables"] += ok
    cache[s["linkedin_url"]] = {"email": e, "status": st, "usable": ok, "domain_match": same}
json.dump(cache, open(P, "w"), ensure_ascii=False)
print(stats)
