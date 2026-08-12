#!/usr/bin/env python3
"""
Pousse une liste de leads (JSON) vers Lemlist avec leurs variables personnalisées.

Usage: LEMLIST_API_KEY=... python3 07_push_with_vars.py leads.json
  leads.json = [{"id":123,"email":"...","first_name":"...","last_name":"...",
                 "company":"...","domain":"...","ab":"A|B",
                 "secteur":"...","categorie":"...","concurrent":"..."}, ...]

Campagnes : A = X-Ray (cam_4vqWGAztL9Lir4ac6), B = Carto (cam_edt7pdBJjn6e7uzoD).
Sortie (stdout) : JSON {"sent":[ids], "dup":[ids], "error":[[id,msg]]}
-> l'appelant met à jour lemlist_status en base (sent -> 'Envoyé Lemlist',
   dup -> 'Déjà en campagne Lemlist').
"""
import os, sys, json, base64, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
CID = {"A": "cam_4vqWGAztL9Lir4ac6", "B": "cam_edt7pdBJjn6e7uzoD"}

def add_lead(cid, email, fields):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST",
        headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA})
    try:
        urllib.request.urlopen(rq, timeout=30); return "sent", ""
    except urllib.error.HTTPError as e:
        msg = e.read().decode()
        if "other campaign" in msg: return "dup", msg
        if "already" in msg.lower(): return "sent", msg
        return "error", msg[:200]

def main(path):
    leads = json.load(open(path))
    out = {"sent": [], "dup": [], "error": []}
    for l in leads:
        email = (l.get("email") or "").strip()
        if not email:
            out["error"].append([l.get("id"), "no email"]); continue
        cid = CID.get(l.get("ab", "A"), CID["A"])
        fields = {
            "firstName": l.get("first_name") or "",
            "lastName": l.get("last_name") or "",
            "companyName": l.get("company") or "",
            "companyDomain": l.get("domain") or "",
            "secteur": l.get("secteur") or "",
            "categorie": l.get("categorie") or "",
            "concurrent": l.get("concurrent") or "",
        }
        st, msg = add_lead(cid, email, fields)
        if st == "sent": out["sent"].append(l["id"])
        elif st == "dup": out["dup"].append(l["id"])
        else: out["error"].append([l["id"], msg])
    print(json.dumps(out))

if __name__ == "__main__":
    main(sys.argv[1])
