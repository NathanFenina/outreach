"""Récupère les résultats FullEnrich (fichiers JSON sauvegardés des appels get_enrichment_results) et les
fusionne dans ../data/campaigns/enriched.csv (clé : URL LinkedIn). Usage : python 40_collect_enrich.py <fichier>..."""
import csv, json, os, sys
OUT = "../data/campaigns/enriched.csv"
rows = {r["linkedin_url"]: r for r in csv.DictReader(open(OUT))} if os.path.exists(OUT) else {}
for p in sys.argv[1:]:
    d = json.load(open(p))
    if isinstance(d, list): d = json.loads(d[0]["text"])
    for r in d.get("results", []):
        i, c = r["input"], r.get("contact_info") or {}
        e = c.get("most_probable_work_email") or {}
        rows[i.get("professional_network_url", "")] = dict(linkedin_url=i.get("professional_network_url", ""), first_name=i.get("first_name", ""),
                                                           last_name=i.get("last_name", ""), email=e.get("email", ""), email_status=e.get("status", ""))
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["linkedin_url", "first_name", "last_name", "email", "email_status"]); w.writeheader(); w.writerows(rows.values())
from collections import Counter
print(len(rows), "contacts ·", Counter(r["email_status"] or "non trouvé" for r in rows.values()))
