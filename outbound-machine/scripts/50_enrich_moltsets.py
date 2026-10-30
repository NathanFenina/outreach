"""Étape 1 de la cascade d'emails : Moltsets (linkedin_to_business_email, lots de 100, 1 jeton par email trouvé).
Garde risk_score A ou B. Revérifie la liste noire (email + domaine) avant et après.
Entrée : ../data/datasets/DS-*.csv · Sortie : ../data/datasets/enriched_moltsets.json (cache par URL LinkedIn)
+ ../data/datasets/misses.csv (à passer à FullEnrich).
Usage : python 50_enrich_moltsets.py --max-tokens 600 DS-104-1.1-FR-P1 ..."""
import csv, json, os, sys, urllib.request
import outreach_db as db

H = {"Authorization": "Bearer " + os.environ["MOLTESETS_API"], "Content-Type": "application/json", "User-Agent": "decupler-outbound"}
CACHE = "../data/datasets/enriched_moltsets.json"
QUALIF = json.load(open("../data/campaigns/qualif.json"))  # 39_qualify.py : on n'enrichit / n'importe que fit=True
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
args = sys.argv[1:]
max_tokens = int(args[args.index("--max-tokens") + 1]) if "--max-tokens" in args else 0
codes = [a for a in args if a.startswith("DS-")]


def call(tool, body):
    req = urllib.request.Request(f"https://api.moltsets.com/api/v1/tools/{tool}", data=json.dumps(body).encode(), headers=H, method="POST")
    return json.loads(urllib.request.urlopen(req, timeout=240).read())


dnc_dom, dnc_mail = set(), set()
for r in db.select("do_not_contact", "email,domain,reason"):
    if r["reason"] in BLOCK:
        if r["domain"]: dnc_dom.add(r["domain"].lower())
        if r["email"]: dnc_mail.add(r["email"].lower())
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
todo = []
for c in codes:
    for r in csv.DictReader(open(f"../data/datasets/{c}.csv")):
        if r["domain"].lower() in dnc_dom or QUALIF.get(r["domain"], {}).get("fit") is not True: continue
        if r["linkedin_url"] and r["linkedin_url"] not in cache: todo.append(r["linkedin_url"])
todo = list(dict.fromkeys(todo))
acc = call("get_account", {})["results"]
# plan illimité (Solo) : la limite = emails trouvés restants sur la fenêtre de 5 h (fair use), pas des jetons
bal = acc["fair_use"]["enrich"]["records"]["5h"]["remaining"] if acc.get("unlimited") else acc["token_balance"]
print("à chercher", len(todo), "· jetons Moltsets", bal, "· plafond", max_tokens)
used = 0
for i in range(0, len(todo), 100):
    if used >= max_tokens or bal - used <= 0: print("plafond atteint"); break
    d = call("linkedin_to_business_email", {"linkedin_urls": todo[i:i + 100]})
    for x in d["results"]:
        cache[x["input"]] = x.get("data") or {}
    used += d.get("metadata", {}).get("tokens_used") or sum(1 for x in d["results"] if (x.get("data") or {}).get("email"))
    json.dump(cache, open(CACHE, "w"))
    print(i + 100, "jetons utilisés", used, flush=True)
ok = {u: v for u, v in cache.items() if v.get("email") and v.get("risk_score") in ("A", "B") and v["email"].lower() not in dnc_mail}
misses = [u for u in todo if u in cache and u not in ok]
with open("../data/datasets/misses.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["linkedin_url"]); w.writerows([u] for u in misses)
print("trouvés A/B", sum(1 for u in todo if u in ok), "/", sum(1 for u in todo if u in cache), "· manques pour FullEnrich", len(misses))
