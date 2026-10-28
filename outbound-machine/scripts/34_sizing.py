"""Taille de marché par sous-ICP (base Lemlist, entreprises) : FR, autres pays francophones, pays anglophones ; 1-10 et 11+ salariés."""
import json, outreach_db as db
from icp_catalog import SEGMENTS, COUNTRIES
from lemlist_db import search, seg_filters, BIG, SMALL
LANG = {c: l for c, _, l, *_ in COUNTRIES}
out, lim = {}, None
for s in SEGMENTS:
    groups = {"FR": ["FR"], "francophone": [c for c in s["countries"] if c != "FR" and LANG[c] == "fr"], "anglophone": [c for c in s["countries"] if LANG[c] == "en"]}
    m = {}
    for g, cs in groups.items():
        if not cs: continue
        for hc_name, hc in (("11+", BIG), ("1-10", SMALL)):
            r = search("companies", seg_filters(s, cs, hc), size=1)
            m[f"{g} {hc_name}"] = r["total"]; lim = r.get("limitation")
    out[s["code"]] = m
    db.update("icp_segments", {"market_size": m}, {"code": s["code"]})
    print(s["code"], s["name"][:40], m, flush=True)
json.dump(out, open("../data/market_size.json", "w"), ensure_ascii=False, indent=1)
print("quota restant", lim)
