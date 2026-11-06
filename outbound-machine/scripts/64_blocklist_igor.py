"""Liste noire Instantly selon la règle d'Igor (04/11) : on bloque des PERSONNES, pas des entreprises entières.
- Définitif : clients (domaine), réponses, désinscrits, bounces (email).
- Temporaire : contacté il y a moins de 90 jours (email) ; à relancer chaque semaine pour libérer ceux qui passent 90 jours.
- Les anciens blocages par domaine « déjà contacté » (6 904) sont retirés : les collègues deviennent joignables.
Source : table Supabase contact_history (62_lemlist_last_contact.py) + do_not_contact (clients).
Usage : python 64_blocklist_igor.py plan | apply"""
import datetime, json, os, sys, time, urllib.request
import outreach_db as db

H = {"Authorization": "Bearer " + os.environ["INSTANTLY_API"], "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 decupler-outbound"}


def api(method, path, body=None):
    for i in range(4):
        try:
            r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
            return json.loads(urllib.request.urlopen(r, timeout=60).read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code in (400, 404, 409): return {"error": e.code}
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
    return {"error": "réseau"}


lim = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=90)).isoformat()
hist = db.select("contact_history", "email,last_contacted_at,replied,unsubscribed,bounced")
keep_mail = {h["email"] for h in hist if h["replied"] or h["unsubscribed"] or h["bounced"] or (h["last_contacted_at"] or "") >= lim}
keep_dom = {r["domain"].lower() for r in db.select("do_not_contact", "domain,reason") if r["reason"] in ("client", "concurrent", "agressif") and r["domain"]}
want = keep_mail | keep_dom
entries, after = [], None
while True:
    r = api("GET", "/api/v2/block-lists-entries?limit=100" + (f"&starting_after={after}" if after else ""))
    entries += r.get("items", []); after = r.get("next_starting_after")
    if not after or not r.get("items"): break
have = {e["bl_value"].lower(): e["id"] for e in entries}
to_add = sorted(want - set(have)); to_del = [i for v, i in have.items() if v not in want]
print("dans Instantly", len(have), "· à garder", len(want), f"(emails {len(keep_mail)}, domaines clients {len(keep_dom)})", "· à ajouter", len(to_add), "· à retirer", len(to_del), flush=True)
if len(sys.argv) > 1 and sys.argv[1] == "apply":
    for n, v in enumerate(to_add, 1):  # on ajoute d'abord, on retire ensuite : jamais de trou dans la protection
        api("POST", "/api/v2/block-lists-entries", {"bl_value": v})
        if n % 500 == 0: print("ajoutés", n, flush=True)
    for n, i in enumerate(to_del, 1):
        api("DELETE", f"/api/v2/block-lists-entries/{i}")
        if n % 500 == 0: print("retirés", n, flush=True)
    print("FIN liste noire", flush=True)
