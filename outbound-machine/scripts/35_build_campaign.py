"""Construit la liste d'une campagne : base People Lemlist (recherche gratuite) → entreprises du sous-ICP →
liste noire (Supabase do_not_contact) → messagerie par MX (G / O ; Microsoft exclu) → 3 contacts max par entreprise
(rangs personas) → Supabase (companies, contacts) + CSV ../data/campaigns/<code>.csv (à enrichir).
Usage : python 35_build_campaign.py 101"""
import csv, json, os, re, sys
import outreach_db as db
from lemlist_db import search, f, CNAME
from mx import classify_many
from campaign_specs import SPECS

code = sys.argv[1]; S = SPECS[code]
if S.get("keywords") is None: S["keywords"] = [k for _, kws in S["assign"] for k in kws]
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
dnc_dom, dnc_mail = set(), set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK:
        if r["domain"]: dnc_dom.add(r["domain"].lower())
        if r["email"]: dnc_mail.add(r["email"].lower())

RANK = [(1, r"\b(ceo|founder|fondat|co-?fond|pr[ée]sident|directeur g[ée]n[ée]ral|dg\b|g[ée]rant|managing (partner|director)|owner|associ[ée] g[ée]rant|partner|associ[ée])"),
        (2, r"(cmo|marketing|growth|commercial|sales|business development|d[ée]veloppement)"),
        (3, r"(seo|content|contenu|communication|acquisition|digital)")]


def rank(title):
    t = (title or "").lower()
    for n, rx in RANK:
        if re.search(rx, t): return n
    return None


def current_exp(p):
    name = p.get("current_exp_company_name")
    for e in p.get("experiences") or []:
        if e.get("company_name") == name and not e.get("date_to"): return e
    return (p.get("experiences") or [{}])[0]


filters = [f("currentCompanyCountry", [CNAME[c] for c in S["countries"]]), f("keywordInCompany", S["keywords"]),
           f("currentCompanyHeadcount", S["headcount"]), f("seniority", S["seniority"])] + [f(k, v) for k, v in S.get("extra", [])]
companies, page, seen = {}, S.get("start_page", 1), 0
while len(companies) < S["max_companies"] and page <= S.get("start_page", 1) - 1 + S.get("max_pages", 15):
    res = search("people", filters, page=page, size=100)
    if not res["results"]: break
    for p in res["results"]:
        e = current_exp(p); dom = (e.get("company_domain") or "").lower().removeprefix("www.")
        if not dom or dom in dnc_dom: continue
        if (e.get("company_employee_count") or 0) < 5: continue
        rk = rank(e.get("title"))
        if rk is None: continue
        fn = (p.get("full_name") or "").split(" ", 1)
        desc = ((e.get("company_description") or "") + " " + (e.get("company_name") or "")).lower()
        icp = next((ic for ic, kws in S.get("assign", []) if any(k.lower() in desc for k in kws)), S["icp_code"])
        c = companies.setdefault(dom, dict(domain=dom, icp_code=icp, name=e.get("company_name"), employees=e.get("company_employee_count"),
                                           linkedin_url=e.get("company_linkedin_url"), city=e.get("company_headquarters_city"),
                                           country=e.get("company_headquarters_country"), people=[], signals=S.get("signals", {})))
        c["people"].append(dict(first_name=fn[0], last_name=fn[1] if len(fn) > 1 else "", title=e.get("title"), rank=rk,
                                linkedin_url=p.get("lead_linkedin_url")))
    page += 1; print("page", page - 1, "total", res["total"], "entreprises", len(companies), "quota", res.get("limitation"), flush=True)

esp = classify_many(list(companies))
rows, kept = [], {"google": 0, "other": 0, "microsoft": 0, "unknown": 0}
for dom, c in companies.items():
    e, mxh = esp[dom]; kept[e] += 1
    if e not in ("google", "other"): continue
    ppl = sorted({(p["linkedin_url"] or p["first_name"] + p["last_name"]): p for p in c["people"]}.values(), key=lambda p: p["rank"])
    chosen, ranks = [], set()
    for p in ppl:                      # 1 personne par rang d'abord, puis complète jusqu'au max
        if p["rank"] not in ranks: chosen.append(p); ranks.add(p["rank"])
    chosen += [p for p in ppl if p not in chosen]
    for p in chosen[:S["per_company"]]:
        rows.append(dict(campaign=code, lot="G" if e == "google" else "O", icp_code=c["icp_code"], domain=dom, company=c["name"],
                         city=c["city"] or "", country=c["country"] or "", employees=c["employees"], esp=e, mx=mxh, **{k: p[k] for k in ("first_name", "last_name", "title", "rank", "linkedin_url")}))
print("messagerie (entreprises) :", kept)

comp = db.upsert("companies", [dict(domain=d, name=c["name"], country=c["country"], city=c["city"], icp_code=c["icp_code"], employees=c["employees"],
                                    linkedin_url=c["linkedin_url"], esp=esp[d][0], mx=esp[d][1], signals=c["signals"], pyramid_tier=S["tier"], source="lemlist_db")
                               for d, c in companies.items()], "domain", return_rows=True)
cid = {c["domain"]: c["id"] for c in comp}
os.makedirs("../data/campaigns", exist_ok=True)
with open(f"../data/campaigns/{code}.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
from collections import Counter
print("contacts :", len(rows), Counter(r["lot"] for r in rows), "entreprises retenues :", len({r['domain'] for r in rows}))
