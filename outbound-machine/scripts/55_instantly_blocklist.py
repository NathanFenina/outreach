"""Pousse la liste noire Supabase (domaines déjà contactés, répondus, désinscrits, clients) dans la blocklist Instantly,
pour que même un import manuel ne puisse pas recontacter ces entreprises. L'API n'a pas d'import groupé : un appel par domaine."""
import csv, json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

H = {"Authorization": "Bearer " + os.environ["INSTANTLY_API"], "User-Agent": "Mozilla/5.0 decupler-outbound", "Content-Type": "application/json"}


def req(method, path, body=None):
    for i in range(5):
        try:
            r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
            return json.loads(urllib.request.urlopen(r, timeout=60).read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500: time.sleep(2 * (i + 1)); continue
            return {"error": e.code}
        except OSError:
            time.sleep(2 * (i + 1))
    return {"error": "échec"}


have, after = set(), None
while True:
    r = req("GET", "/api/v2/block-lists-entries?limit=100" + (f"&starting_after={after}" if after else ""))
    for x in r.get("items", []):
        have.add(x["bl_value"].lower())
        if x["bl_value"] == "exemple-test-decupler.com": req("DELETE", f"/api/v2/block-lists-entries/{x['id']}")
    after = r.get("next_starting_after")
    if not after or not r.get("items"): break
doms = [r["domain"] for r in csv.DictReader(open("../data/datasets/DNC-igor.csv")) if r["domain"] not in have]
print("déjà en blocklist", len(have), "· à ajouter", len(doms), flush=True)
with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(lambda d: req("POST", "/api/v2/block-lists-entries", {"bl_value": d}), doms))
print("ajoutés", sum(1 for x in res if "id" in x), "· erreurs", sum(1 for x in res if "error" in x))
