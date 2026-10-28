"""Assemble les listes finales par campagne et par lot (G / O), sans doublon entre campagnes
(priorité 102 > 103 > 101), 300 leads max par lot, et écrit les variables de lead (seg, unit, proof,
icebreaker, zone) prêtes pour Lemlist. Sortie : ../data/campaigns/final_<code>-<lot>.csv"""
import csv, collections, glob
from icp_catalog import SEGMENTS, P_PIPE
import sequences as S
SEG = {s["code"]: s for s in SEGMENTS}
GROUPS = [("102", ["102", "102b", "103", "102c"], 7), ("101", ["101", "101b", "101c", "101d", "101e"], 9)]
seen, out = set(), {}
for code, parts, hyp in GROUPS:
    rows = []
    for p in parts:
        try: rows += list(csv.DictReader(open(f"../data/campaigns/{p}.csv")))
        except FileNotFoundError: print("manque", p)
    # signal d'abord (fichier sans suffixe = palier signal pour 102), puis rang de persona
    doms_here = []
    by_lot = collections.defaultdict(list)
    for r in sorted(rows, key=lambda r: (r["campaign"] != code, int(r["rank"]))):
        key = (r["first_name"].lower(), r["last_name"].lower(), r["domain"])
        if r["domain"] in seen or key in {(x["first_name"].lower(), x["last_name"].lower(), x["domain"]) for x in by_lot[r["lot"]]}: continue
        s = SEG[r["icp_code"]]; lang = "fr"
        sig = "I2" if (code == "102" and r["campaign"] == "102") else None
        ib = S.ICEBREAKER[lang]["H7I2" if sig else "H7default"] if hyp == 7 else S.ICEBREAKER[lang]["default"].replace("[SEG]", s["seg_fr"])
        ib = ib.replace("{{firstName}}", r["first_name"]).replace("{{companyName}}", r["company"])
        r.update(seg=s["seg_fr"], unit=(s["unit"] or ("clients", ""))[0], proof=(s["proof"] or P_PIPE)[0],
                 icebreaker=ib, zone=f"à {r['city']}" if r.get("city") else "en France", signal=sig or "")
        by_lot[r["lot"]].append(r)
    for lot, lst in by_lot.items():
        lst = lst[:300]
        for r in lst: doms_here.append(r["domain"])
        out[f"{code}-{lot}"] = lst
        with open(f"../data/campaigns/final_{code}-{lot}.csv", "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=lst[0].keys()); w.writeheader(); w.writerows(lst)
    seen.update(doms_here)
for k, v in sorted(out.items()):
    print(k, len(v), "contacts,", len({r["domain"] for r in v}), "entreprises,", dict(collections.Counter(r["icp_code"] for r in v)))
