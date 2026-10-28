"""Applique la qualification (39_qualify.py) + filtres durs (concurrents, fonds, médias) aux listes finales
→ ../data/campaigns/qualified_<code>-<lot>.csv"""
import csv, json, collections, re
D = "../data/campaigns/"
q = json.load(open(D + "qualif.json"))
COMP = re.compile(r"(seo|référencement|referencement|agence|agency|webagency|marketing|digital|growth|media|média|communication|leadgen|^ads-|adfor|studio)", re.I)
BAD = re.compile(r"(\.vc$|\.org$|capital|invest|ventures|fund|cfnews|notaire|huissier|avocat|\.legal$|\.law$|\.cci\.|medef|indosuez|natixis|carrefourshec|lilyfacilite|recruitee|cfa-|initiative-|business-angels|\.pl$|piriou|realestate|arthur-loyd|winebankers|cybele-am|stories-design|clp-web|bdgs|capitem|cnaib|bersay|bonoconsiglio|icone-group|rightliens|patrickgautier|grandir\.fr|acamxconseil|groupe-bsf|wewysereply|acticam|mlacreative)", re.I)
MANUAL_OUT = {"artyseo.fr", "xpair.com", "cfnews.net", "conversion-boosters.com", "wearebold.co", "sorbonnejuniorconseil.com", "lexing.law"}
for lot in ("101-G", "101-O", "102-G", "102-O"):
    rows = list(csv.DictReader(open(f"{D}final_{lot}.csv")))
    keep = []
    for r in rows:
        v = q.get(r["domain"], {})
        if v.get("fit") is not True or r["domain"] in MANUAL_OUT or BAD.search(r["domain"]): continue
        if COMP.search(r["domain"] + " " + r["company"]) and r["icp_code"] != "1.9": continue
        if lot.startswith("101") and re.search(r"(formation|drone|events?)", r["domain"], re.I): continue
        si = v.get("sub_icp")
        if isinstance(si, str) and si.split(".")[0] == r["icp_code"].split(".")[0]: r["icp_code"] = si
        keep.append(r)
    with open(f"{D}qualified_{lot}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(keep)
    print(lot, len(rows), "→", len(keep), dict(collections.Counter(r["icp_code"] for r in keep)))
