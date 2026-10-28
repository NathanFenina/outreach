"""Construit un dataset par sous-ICP × zone (base People Lemlist, recherche gratuite) : liste noire, entreprises déjà
dans une campagne écartées, messagerie par MX (G / O ; Microsoft exclu), 3 contacts max par entreprise.
Sortie : ../data/datasets/DS-<icp>-<zone>.csv + Supabase (companies, datasets). Aucun crédit d'enrichissement dépensé.
Usage : python 44_datasets.py [icp_code ...]   (sans argument : tous les sous-ICP)"""
import csv, glob, json, os, re, sys
from collections import Counter
import outreach_db as db
from lemlist_db import search, f, CNAME
from mx import classify_many
from icp_catalog import SEGMENTS
from campaign_specs import DECIDERS

ZONES = {  # zone : pays, langue, pages max (100 profils par page)
    "FR": (["FR"], "fr", 8), "FRX": (["BE", "CH", "LU"], "fr", 4), "MAG": (["MA", "TN"], "fr", 4),
    "UK": (["UK", "IE"], "en", 5), "US": (["US"], "en", 5), "GULF": (["AE", "SA", "QA"], "en", 4),
    "EUN": (["DE", "AT", "NL", "SE", "NO", "DK", "FI"], "en", 4), "MED": (["TR", "TN", "MA", "HU", "AE"], "en", 5),
}
CREDITS_PER_CONTACT = 0.87  # mesuré le 28/10 : 544 crédits FullEnrich pour 629 contacts
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
RANK = [(1, r"\b(ceo|founder|fondat|co-?fond|pr[ée]sident|directeur g[ée]n[ée]ral|dg\b|g[ée]rant|managing (partner|director)|owner|associ[ée] g[ée]rant|partner|associ[ée]|propri[ée]taire|director|directeur|directrice)"),
        (2, r"(cmo|marketing|growth|commercial|sales|business development|d[ée]veloppement)"),
        (3, r"(seo|content|contenu|communication|acquisition|digital)")]


def rank(title):
    t = (title or "").lower()
    return next((n for n, rx in RANK if re.search(rx, t)), None)


def current_exp(p):
    for e in p.get("experiences") or []:
        if e.get("company_name") == p.get("current_exp_company_name") and not e.get("date_to"): return e
    return (p.get("experiences") or [{}])[0]


def zones_for(s):
    if s["code"].startswith("3."): return ["MED"]
    return [z for z, (cs, _, _) in ZONES.items() if z != "MED" and set(cs) & set(s["countries"])]


dnc = set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK and r["domain"]: dnc.add(r["domain"].lower())
for fn in glob.glob("../data/campaigns/*.csv"):  # entreprises déjà prises dans une campagne
    for r in csv.DictReader(open(fn)):
        if r.get("domain"): dnc.add(r["domain"].lower())
for fn in glob.glob("../data/datasets/DS-*.csv"):  # pas de doublon entre datasets
    for r in csv.DictReader(open(fn)):
        dnc.add(r["domain"].lower())

os.makedirs("../data/datasets", exist_ok=True)
todo = [s for s in SEGMENTS if len(sys.argv) < 2 or s["code"] in sys.argv[1:]]
for s in todo:
    for z in zones_for(s):
        code = f"DS-{s['code']}-{z}"
        if os.path.exists(f"../data/datasets/{code}.csv"): print("existe", code); continue
        cs, lang, pages = ZONES[z]
        cs = [c for c in cs if c in s["countries"]] if z != "MED" else cs
        filters = [f("currentCompanyCountry", [CNAME[c] for c in cs]), f("keywordInCompany", s["kw_fr"] + s["kw_en"]),
                   f("currentCompanyHeadcount", ["1-10", "11-50", "51-200", "201-500"]), f("seniority", DECIDERS)]
        companies, quota, total = {}, None, 0
        for page in range(1, pages + 1):
            try:
                res = search("people", filters, page=page, size=100)
            except RuntimeError as e:
                print(code, "erreur", e); break
            quota, total = res.get("limitation"), res.get("total", 0)
            for p in res["results"]:
                e = current_exp(p); dom = (e.get("company_domain") or "").lower().removeprefix("www.")
                if not dom or dom in dnc or (e.get("company_employee_count") or 0) < 5: continue
                rk = rank(e.get("title"))
                if rk is None: continue
                n = (p.get("full_name") or "").split(" ", 1)
                c = companies.setdefault(dom, dict(name=e.get("company_name"), employees=e.get("company_employee_count"), city=e.get("company_headquarters_city"),
                                                   country=e.get("company_headquarters_country"), linkedin_url=e.get("company_linkedin_url"), people={}))
                c["people"][p.get("lead_linkedin_url") or p.get("full_name")] = dict(first_name=n[0], last_name=n[1] if len(n) > 1 else "", title=e.get("title"),
                                                                                     rank=rk, linkedin_url=p.get("lead_linkedin_url"))
            if len(res["results"]) < 100: break
        if not companies:
            print(code, "0 entreprise (total base", total, ") quota", quota, flush=True)
            db.upsert("datasets", [dict(code=code, icp_code=s["code"], zone=z, countries=cs, language=lang, companies_found=0, contacts_g=0, contacts_o=0,
                                        enrich_credits_est=0, status="vide", notes=f"total base Lemlist {total}")], "code")
            continue
        esp = classify_many(list(companies))
        rows = []
        for dom, c in companies.items():
            kind, mxh = esp[dom]
            if kind not in ("google", "other"): continue
            ppl = sorted(c["people"].values(), key=lambda p: p["rank"])
            chosen, seen = [], set()
            for p in ppl:
                if p["rank"] not in seen: chosen.append(p); seen.add(p["rank"])
            chosen += [p for p in ppl if p not in chosen]
            for p in chosen[:3]:
                rows.append(dict(dataset=code, lot="G" if kind == "google" else "O", icp_code=s["code"], language=lang, domain=dom, company=c["name"],
                                 city=c["city"] or "", country=c["country"] or "", employees=c["employees"], esp=kind, mx=mxh, **p))
        k = Counter(v[0] for v in esp.values()); lots = Counter(r["lot"] for r in rows)
        if rows:
            with open(f"../data/datasets/{code}.csv", "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
            dnc.update(r["domain"] for r in rows)
        db.upsert("companies", [dict(domain=d, name=c["name"], country=c["country"], city=c["city"], icp_code=s["code"], employees=c["employees"],
                                     linkedin_url=c["linkedin_url"], esp=esp[d][0], mx=esp[d][1], pyramid_tier=3, source="lemlist_db")
                                for d, c in companies.items()], "domain", ignore_duplicates=True)
        db.upsert("datasets", [dict(code=code, icp_code=s["code"], zone=z, countries=cs, language=lang, companies_found=len(companies),
                                    companies_g=k["google"], companies_o=k["other"], companies_ms=k["microsoft"],
                                    contacts_g=lots["G"], contacts_o=lots["O"], enrich_credits_est=round(len(rows) * CREDITS_PER_CONTACT),
                                    status="a_enrichir" if rows else "vide", notes=f"total base Lemlist {total}")], "code")
        print(code, "entreprises", len(companies), dict(k), "contacts", dict(lots), "quota", quota, flush=True)
