"""Connecte les boîtes d'envoi à Instantly par l'API puis les rattache aux campagnes selon le fournisseur du prospect :
groupe A PremiumInboxes → campagnes lot G (prospects Google) ; groupe B Zapmail → campagnes lots M (Outlook) et O (autres).
Entrée : export CSV des fournisseurs (format « Instantly » : email, prénom, nom, mot de passe d'application), déposé dans le
scratchpad, JAMAIS dans le repo. Chauffe activée, limite quotidienne basse (montée progressive UltB), rien n'est lancé.
Usage : python 56_instantly_accounts.py A <csv PremiumInboxes>   puis   python 56_instantly_accounts.py B <csv Zapmail>
        python 56_instantly_accounts.py assign   (rattache les boîtes aux campagnes G / M / O)"""
import csv, json, os, sys, urllib.request

H = {"Authorization": "Bearer " + os.environ["INSTANTLY_API"], "User-Agent": "Mozilla/5.0 decupler-outbound", "Content-Type": "application/json"}
FIRST_LIMIT = 10  # emails / jour / boîte au départ (montée UltB ensuite)


def api(method, path, body=None):
    r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=120).read() or b"{}")
    except urllib.error.HTTPError as e:
        return {"error": e.code, "detail": e.read().decode()[:300]}


def col(row, *names):
    low = {k.strip().lower(): v for k, v in row.items()}
    return next((low[n] for n in names if low.get(n)), "")


def accounts():
    out, after = [], None
    while True:
        r = api("GET", "/api/v2/accounts?limit=100" + (f"&starting_after={after}" if after else ""))
        out += r.get("items", [])
        after = r.get("next_starting_after")
        if not after or not r.get("items"): return out


mode = sys.argv[1]
if mode in ("A", "B"):
    tag = "groupe-A-premiuminboxes" if mode == "A" else "groupe-B-zapmail"
    ok = 0
    for row in csv.DictReader(open(sys.argv[2])):
        email = col(row, "email", "email address", "username")
        pwd = col(row, "app password", "app_password", "password", "smtp password")
        if not email or not pwd: continue
        body = {"email": email, "first_name": col(row, "first name", "first_name") or "Nathan", "last_name": col(row, "last name", "last_name") or "Fenina",
                "provider_code": 2, "imap_username": email, "imap_password": pwd, "imap_host": "imap.gmail.com", "imap_port": 993,
                "smtp_username": email, "smtp_password": pwd, "smtp_host": "smtp.gmail.com", "smtp_port": 587, "daily_limit": FIRST_LIMIT}
        r = api("POST", "/api/v2/accounts", body)
        if "error" in r:  # certains comptes Google passent en IMAP/SMTP générique
            r = api("POST", "/api/v2/accounts", dict(body, provider_code=1))
        print(email, "OK" if "error" not in r else r)
        ok += "error" not in r
    print(ok, "boîtes ajoutées ·", tag)
    print(api("POST", "/api/v2/accounts/warmup/enable", {"emails": [a["email"] for a in accounts()]}))
elif mode == "assign":
    acc = accounts()
    # groupe A = domaines PremiumInboxes (prospects Google) ; groupe B = domaines Zapmail (Outlook + autres)
    zap = ("decuplerapp.com", "decuplerlabs.com", "getdecupler.com", "godecupler.com", "mydecupler.com", "decuplerly.com", "decupleroy.com")
    grp_b = [a["email"] for a in acc if a["email"].split("@")[-1] in zap]
    listed = ("decupleragency.com", "decupler-search.com")  # listés SURBL (29/10) : hors campagnes jusqu'au retrait de la liste
    grp_a = [a["email"] for a in acc if a["email"] not in grp_b and not a["email"].endswith("decupler.com") and a["email"].split("@")[-1] not in listed]
    after, camps = None, []
    while True:
        r = api("GET", "/api/v2/campaigns?limit=100" + (f"&starting_after={after}" if after else ""))
        camps += r.get("items", []); after = r.get("next_starting_after")
        if not after or not r.get("items"): break
    for c in camps:
        code = c["name"].split(" · ")[0]
        lot = code.split("-")[1] if code.count("-") >= 2 else ""
        boxes = grp_a if lot == "G" else grp_b if lot in ("M", "O") else None
        if not boxes: continue  # groupe pas encore connecté (ex. PremiumInboxes en attente)
        r = api("PATCH", f"/api/v2/campaigns/{c['id']}", {"email_list": boxes})
        print(code, lot, len(boxes), "boîtes", "OK" if "error" not in r else r)
