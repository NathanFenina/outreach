"""Crée les campagnes en BROUILLON dans Lemlist (rien n'est lancé) : séquence de 6 étapes de l'hypothèse,
jetons de segment transformés en variables de lead ({{seg}}, {{unit}}, {{proof}}, {{icebreaker}}, {{zone}}),
puis enregistre la campagne dans Supabase. Idempotent (ne recrée pas une campagne existante)."""
import base64, html, json, os, time, urllib.request
import outreach_db as db
import sequences as S

H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode(), "Content-Type": "application/json"}
SEQ = {6: S.H6, 7: S.H7, 8: S.H8, 9: S.H9}
CAMPAIGNS = [  # code, nom, hypothèse, langue, icp (1 = B2B, 2 = local), sous-ICP principal
    ("101-G-9", "ICP 2 · PAC, solaire, sécurité incendie · FR · partenariat performance", 9, "fr", 2, "2.2"),
    ("101-O-9", "ICP 2 · PAC, solaire, sécurité incendie · FR · partenariat performance", 9, "fr", 2, "2.2"),
    ("102-G-7", "ICP 1 · B2B FR · recrute en marketing + palier 3 · AAA vidéo", 7, "fr", 1, "1.5"),
    ("102-O-7", "ICP 1 · B2B FR · recrute en marketing + palier 3 · AAA vidéo", 7, "fr", 1, "1.5"),
    ("103-G-7", "ICP 1.7 · M&A et transmission · FR · AAA vidéo", 7, "fr", 1, "1.7"),
    ("103-O-7", "ICP 1.7 · M&A et transmission · FR · AAA vidéo", 7, "fr", 1, "1.7"),
]


def api(m, path, body=None):
    for i in range(5):
        try:
            r = urllib.request.urlopen(urllib.request.Request("https://api.lemlist.com/api" + path, method=m, headers=H,
                                                              data=json.dumps(body).encode() if body is not None else None), timeout=60)
            t = r.read(); return json.loads(t) if t else {}
        except urllib.error.HTTPError as e:
            if e.code < 500 and e.code != 429: raise RuntimeError(f"{e.code} {e.read().decode()[:300]}")
            time.sleep(2 ** i)


def render(text, icp, lang):
    humor = S.HUMOR3.get(icp, ("", ""))[0 if lang == "fr" else 1]
    origin = S.ORIGIN.get(icp, ("", ""))[0 if lang == "fr" else 1]
    return (text.replace("[SEG]", "{{seg}}").replace("[UNIT]", "{{unit}}").replace("[PROOF_LINE]", "{{proof}}.\n\n")
            .replace("[PROOF]", "{{proof}}").replace("[HUMOR3]", humor).replace("[ORIGIN]", origin))


def to_html(t):
    return "".join("<div><br></div>" if l == "" else f"<div>{html.escape(l, quote=False)}</div>" for l in t.split("\n"))


existing = {c["name"]: c["_id"] for c in api("GET", "/campaigns?limit=100") + api("GET", "/campaigns?limit=100&offset=100")}
for code, name, hyp, lang, icp, seg in CAMPAIGNS:
    full = f"{code} · {name}"
    cid = existing.get(full)
    if not cid:
        cid = api("POST", "/campaigns", {"name": full})["_id"]; time.sleep(1)
        seq = next(iter(api("GET", f"/campaigns/{cid}/sequences")))
        for i, (subj, body) in enumerate(SEQ[hyp][lang]):
            api("POST", f"/sequences/{seq}/steps", {"type": "email", "subject": render(subj, icp, lang) if subj else "",
                                                    "message": to_html(render(body, icp, lang)), "delay": S.DELAYS[i], "index": i + 1})
            time.sleep(0.4)
        print("créée", full, cid)
    else:
        print("existe", full, cid)
    db.upsert("campaigns", [dict(code=code, name=full, lemlist_id=cid, tool="lemlist", icp_code=seg, esp_lot=code.split("-")[1],
                                 hypothesis_code=hyp, language=lang, country="FR", status="draft",
                                 notes="lot G = boîtes PremiumInboxes (Google) ; lot O = boîtes Zapmail, envoi après la chauffe (~6/11)")], "code")
