"""Date du dernier contact par email, depuis l'historique Lemlist (avant la fin de l'abonnement le 10/11).
Règle d'Igor (04/11) : liste noire = seulement réponses négatives et désinscrits ; les autres peuvent être recontactés
après 90 jours, avec un nouvel angle. On garde donc pour chaque email : dernier envoi, nb d'envois, réponse, désinscription.
Sortie : ../data/campaigns/lemlist_last_contact.json (non commité, données personnelles)."""
import base64, json, os, time, urllib.request

H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode()}
OUT = "../data/campaigns/lemlist_last_contact.json"


def get(path):
    for i in range(5):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request("https://api.lemlist.com/api" + path, headers=H), timeout=120).read())
        except Exception as e:
            if i == 4: raise
            time.sleep(3 * (i + 1))


data = {}
for typ in ("emailsSent", "emailsReplied", "emailsUnsubscribed", "emailsBounced"):
    off, n = 0, 0
    while True:
        page = get(f"/activities?type={typ}&limit=100&offset={off}&version=v2")
        if not page: break
        for a in page:
            e = (a.get("leadEmail") or "").lower()
            if not e: continue
            d = data.setdefault(e, {"last_sent": None, "sent": 0, "replied": False, "unsubscribed": False, "bounced": False, "campaigns": []})
            t = a.get("createdAt")
            if typ == "emailsSent":
                d["sent"] += 1
                if t and (d["last_sent"] is None or t > d["last_sent"]): d["last_sent"] = t
                if a.get("name") and a["name"] not in d["campaigns"]: d["campaigns"].append(a["name"])
            elif typ == "emailsReplied": d["replied"] = True
            elif typ == "emailsUnsubscribed": d["unsubscribed"] = True
            else: d["bounced"] = True
        n += len(page); off += 100
        if n % 2000 == 0: print(typ, n, flush=True); json.dump(data, open(OUT, "w"))
        if len(page) < 100: break
    print(typ, "total", n, flush=True)
json.dump(data, open(OUT, "w"))
print("emails", len(data), "· dernier envoi le plus récent", max((v["last_sent"] or "") for v in data.values()))
