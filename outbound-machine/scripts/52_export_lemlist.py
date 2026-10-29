"""Sauvegarde complète de Lemlist avant la fin de l'abonnement (10/11) : leads de chaque campagne (tous états),
séquences, liste de désinscrits. Sortie : ../data/campaigns/lemlist_export/ (non commité, données personnelles)."""
import base64, csv, json, os, time, urllib.request

H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode()}
OUT = "../data/campaigns/lemlist_export"
os.makedirs(OUT, exist_ok=True)


def get(path, raw=False):
    for i in range(5):
        try:
            r = urllib.request.urlopen(urllib.request.Request("https://api.lemlist.com/api" + path, headers=H), timeout=120).read()
            return r if raw else json.loads(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503): time.sleep(3 * (i + 1)); continue
            return None
        except OSError:
            time.sleep(3 * (i + 1))
    return None


camps = [r for r in csv.DictReader(open("../data/synthese_campagnes.csv"))]
ok = 0
for c in camps:
    leads = get(f"/campaigns/{c['id']}/export/leads?state=all", raw=True)
    if leads:
        open(f"{OUT}/{c['id']}_leads.csv", "wb").write(leads); ok += 1
    seq = get(f"/campaigns/{c['id']}/sequences")
    if seq: json.dump(seq, open(f"{OUT}/{c['id']}_sequences.json", "w"), ensure_ascii=False)
    time.sleep(0.3)
uns = get("/unsubscribes?limit=10000")
if uns: json.dump(uns, open(f"{OUT}/unsubscribes.json", "w"), ensure_ascii=False)
json.dump(camps, open(f"{OUT}/campaigns.json", "w"), ensure_ascii=False)
print(len(camps), "campagnes ·", ok, "exports de leads ·", len(uns or []), "désinscrits")
