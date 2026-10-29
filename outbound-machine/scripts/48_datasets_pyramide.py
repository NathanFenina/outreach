"""Datasets des campagnes prioritaires, par palier de la pyramide V2 (base People Lemlist, recherche gratuite).
P1 = a levé (< 6 mois) ET recrute (offre < 90 j) · P2 = recrute en marketing / SEO / growth (offre < 90 j) · P4 = marché principal.
(P3 = intent SEO : calculé ensuite sur les domaines P4 avec DataForSEO, coût annoncé avant.)
Lots : G = MX Google (boîtes PremiumInboxes) ; O = tout le reste, Microsoft compris (boîtes Zapmail, décision Nathan 29/10).
Liste noire Supabase + entreprises déjà dans une campagne ou un dataset écartées ; 3 contacts max par entreprise, un par rang.
Nommage : DS-<campagne>-<sous-ICP>-<zone>-<palier>, ex. DS-104-1.1-FR-P2.
Usage : python 48_datasets_pyramide.py 104 [106 110 114]"""
import csv, glob, os, re, sys
from collections import Counter
import outreach_db as db
from lemlist_db import search, f, CNAME
from mx import classify_many
from icp_catalog import SEGMENTS
from campaign_specs import DECIDERS

SEG = {s["code"]: s for s in SEGMENTS}
CAMPAIGNS = {  # campagne : (sous-ICP, paliers, pages max par palier, contacts max par entreprise)
    "104": (["1.1", "1.2"], ["P1", "P2", "P4"], 20, 3),
    "106": (["1.5", "1.6", "1.7", "1.8"], ["P1", "P2", "P4"], 12, 3),
    "110": (["2.1", "2.15"], ["P4"], 20, 2),
    "114": (["4.1", "4.2", "4.4"], ["P4"], 15, 2),
}
FUNDED = ["Less than 1 month", "1 month to 3 months", "3 months to 6 months"]
SALES_JOBS = ["commercial", "business developer", "sales", "account executive", "chargé d'affaires", "responsable commercial"]
MKT_JOBS = ["marketing", "SEO", "growth", "contenu", "content", "acquisition", "communication", "demand generation"]
TIER_FILTERS = {
    "P1": [("currentCompanyLastFundingRoundAt", FUNDED), ("jobPostingDate", ["Last 90 days"])],
    "P2": [("jobPostingTitle", MKT_JOBS), ("jobPostingDate", ["Last 90 days"])],
    "P2b": [("jobPostingTitle", SALES_JOBS), ("jobPostingDate", ["Last 90 days"])],  # recrute en commercial
    "P4": [],
}
START = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--start=")), 1))  # reprise : pages suivantes
SUFFIX = next((a.split("=")[1] for a in sys.argv if a.startswith("--suffix=")), "")
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
RANK = [(1, r"\b(ceo|founder|fondat|co-?fond|pr[ée]sident|directeur g[ée]n[ée]ral|dg\b|g[ée]rant|managing (partner|director)|owner|associ[ée] g[ée]rant|partner|associ[ée]|propri[ée]taire|directeur|directrice|director)"),
        (2, r"(cmo|marketing|growth|commercial|sales|business development|d[ée]veloppement|revenue)"),
        (3, r"(seo|content|contenu|communication|acquisition|digital|web)")]


def rank(title):
    t = (title or "").lower()
    return next((n for n, rx in RANK if re.search(rx, t)), None)


def current_exp(p):
    for e in p.get("experiences") or []:
        if e.get("company_name") == p.get("current_exp_company_name") and not e.get("date_to"): return e
    return (p.get("experiences") or [{}])[0]


dnc, dnc_mail = set(), set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK:
        if r["domain"]: dnc.add(r["domain"].lower())
        if r["email"]: dnc_mail.add(r["email"].lower())
for fn in glob.glob("../data/campaigns/*.csv") + glob.glob("../data/datasets/DS-*.csv"):
    if "/DS-1" in fn and "-FR-P" not in fn and os.path.basename(fn).count("-") == 2:
        continue  # anciens datasets 44 (DS-1.1-FR…) : repris ici par palier, pas bloqués
    for r in csv.DictReader(open(fn)):
        if r.get("domain"): dnc.add(r["domain"].lower())

os.makedirs("../data/datasets", exist_ok=True)
TIERS_ARG = next((a.split("=")[1].split(",") for a in sys.argv if a.startswith("--tiers=")), None)
PAGES_ARG = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--pages=")), 0))
for camp in [a for a in sys.argv[1:] if not a.startswith("--")]:
    icps, tiers, pages, per_co = CAMPAIGNS[camp]
    tiers, pages = TIERS_ARG or tiers, PAGES_ARG or pages
    for icp in icps:
        s = SEG[icp]
        for tier in tiers:
            code = f"DS-{camp}-{icp}-FR-{tier}{SUFFIX}"
            if os.path.exists(f"../data/datasets/{code}.csv"): print("existe", code); continue
            filters = [f("currentCompanyCountry", [CNAME["FR"]]), f("keywordInCompany", s["kw_fr"] + s["kw_en"]),
                       f("currentCompanyHeadcount", ["1-10", "11-50", "51-200", "201-500"]), f("seniority", DECIDERS)]
            filters += [f(k, v) for k, v in TIER_FILTERS[tier]]
            companies, total, quota = {}, 0, None
            for page in range(START, START + (pages if tier == "P4" else 6)):
                try:
                    res = search("people", filters, page=page, size=100)
                except RuntimeError as e:
                    print(code, "erreur", e); break
                total, quota = res.get("total", 0), res.get("limitation")
                for p in res["results"]:
                    e = current_exp(p); dom = (e.get("company_domain") or "").lower().removeprefix("www.")
                    if not dom or dom in dnc or (e.get("company_employee_count") or 0) < 5: continue
                    rk = rank(e.get("title"))
                    if rk is None: continue
                    n = (p.get("full_name") or "").split(" ", 1)
                    c = companies.setdefault(dom, dict(name=e.get("company_name"), employees=e.get("company_employee_count"),
                                                       city=e.get("company_headquarters_city"), linkedin_url=e.get("company_linkedin_url"), people={}))
                    c["people"][p.get("lead_linkedin_url") or p.get("full_name")] = dict(
                        first_name=n[0], last_name=n[1] if len(n) > 1 else "", title=e.get("title"), rank=rk, linkedin_url=p.get("lead_linkedin_url"))
                if len(res["results"]) < 100: break
            esp = classify_many(list(companies)) if companies else {}
            rows = []
            for dom, c in companies.items():
                kind, mxh = esp[dom]
                if kind == "unknown": continue
                ppl = sorted(c["people"].values(), key=lambda p: p["rank"])
                chosen, seen = [], set()
                for p in ppl:
                    if p["rank"] not in seen: chosen.append(p); seen.add(p["rank"])
                chosen += [p for p in ppl if p not in chosen]
                for p in chosen[:per_co]:
                    rows.append(dict(dataset=code, campaign=camp, tier=tier, lot="G" if kind == "google" else "O", icp_code=icp, language="fr",
                                     domain=dom, company=c["name"], city=c["city"] or "", country="FR", employees=c["employees"], esp=kind, mx=mxh, **p))
            k = Counter(v[0] for v in esp.values()); lots = Counter(r["lot"] for r in rows)
            if rows:
                with open(f"../data/datasets/{code}.csv", "w", newline="") as fh:
                    w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
                dnc.update(r["domain"] for r in rows)
                db.upsert("companies", [dict(domain=d, name=c["name"], country="FR", city=c["city"], icp_code=icp, employees=c["employees"],
                                             linkedin_url=c["linkedin_url"], esp=esp[d][0], mx=esp[d][1], pyramid_tier=int(tier[1]),
                                             signals={"P1": ["levée < 6 mois", "recrute < 90 j"], "P2": ["recrute marketing < 90 j"], "P2b": ["recrute commercial < 90 j"]}.get(tier, []),
                                             source="lemlist_db") for d, c in companies.items()], "domain", ignore_duplicates=True)
            db.upsert("datasets", [dict(code=code, icp_code=icp, zone="FR", countries=["FR"], language="fr", source="lemlist_db",
                                        companies_found=len(companies), companies_g=k["google"], companies_o=k["other"] + k["microsoft"],
                                        companies_ms=k["microsoft"], contacts_g=lots["G"], contacts_o=lots["O"],
                                        enrich_credits_est=round(len(rows) * 0.87), status="a_enrichir" if rows else "vide", campaign_code=camp,
                                        notes=f"{tier} · total base Lemlist {total} · lot O = autres + Microsoft")], "code")
            print(code, "base", total, "entreprises", len(companies), dict(k), "contacts", dict(lots), "quota", quota, flush=True)
