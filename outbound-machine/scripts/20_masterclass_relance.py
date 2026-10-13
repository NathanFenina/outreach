#!/usr/bin/env python3
"""Crée la campagne Lemlist « Decupler · Masterclass · relance inscrits » (brouillon, sans leads).
Copy : copy/17_relance_masterclass.md. Mails 2 et 4 sans objet = envoyés dans le fil du mail précédent.
Usage: LEMLIST_API=... python3 20_masterclass_relance.py
"""
import os, json, base64, time, urllib.request, urllib.error

KEY = os.environ.get("LEMLIST_API_KEY") or os.environ["LEMLIST_API"]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
H = {"Authorization": "Basic " + base64.b64encode(f":{KEY}".encode()).decode(), "Content-Type": "application/json", "User-Agent": UA}
NAME = "Decupler · Masterclass · relance inscrits"

def api(m, u, b=None):
    for a in range(5):
        try:
            rq = urllib.request.Request(u, data=json.dumps(b).encode() if b is not None else None, method=m, headers=H)
            r = urllib.request.urlopen(rq, timeout=40); return json.load(r) if r.length != 0 else {}
        except urllib.error.HTTPError as e:
            if e.code < 500: raise SystemExit(f"{e.code} {e.read().decode()[:300]}")
            time.sleep(2 ** a)
        except (urllib.error.URLError, ConnectionError):
            time.sleep(2 ** a)
    raise SystemExit("api fail")

def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)

STEPS = [
 ("masterclass", 0, [
  "salut {{firstName}},", "",
  "merci à ceux qui ont déjà levé la main après la masterclass claude code seo. vous êtes plusieurs à m'avoir demandé d'en parler de vive voix et d'avoir plus de temps pour réfléchir.", "",
  "alors exceptionnellement, je laisse l'accompagnement ouvert jusqu'à lundi 19 octobre, 20h. le temps de s'assurer ensemble que ça marchera pour toi et que c'est le bon fit.", "",
  "je t'accompagne main dans la main pour que ton seo tourne en pilote automatique, installé sur ton projet en 4 sessions. comme vu pendant le workshop, on est partis de 0 à 200 clics par jour en 12 mois grâce à cette méthode.", "",
  "serais-tu contre un appel de 15 min pour voir si c'est adapté à ton cas ?", "",
  "Nathan", "",
  "ps : si à la fin des 4 sessions ton moteur ne tourne pas sur ton projet, je continue avec toi en 1:1, gratuitement, jusqu'à ce qu'il tourne. et si tu t'inscris après notre appel, une session 1:1 en plus avec moi.",
  "pps : si ce n'est pas pour toi, réponds « stop » et je ne t'écris plus."]),
 ("", 1, ["{{firstName}}, une idée sur mon dernier message ?", "", "Nathan"]),
 ("accès", 1, [
  "{{firstName}}, les personnes que j'accompagne n'en croient pas leurs yeux. chez un client, on a corrigé toutes les données structurées du site : c'était estimé à 7 jours de travail, c'était fait en 30 minutes.", "",
  "le repo partagé pendant la masterclass est gratuit, tu peux tout faire seul. l'accompagnement sert à ce que ça tourne vraiment sur ton projet, avec moi à côté quand ça bloque. 990 € ht, ou 2 × 495 €. le groupe suivant sera à 1 490 €, puis 2 590 €.", "",
  "Nathan", "",
  "ps : pour s'assurer que c'est le bon fit et que ça te correspond, je t'offre un appel rapide, si tu veux."]),
 ("", 3, [
  "{{firstName}}, je t'ai écrit plusieurs fois sans réponse. d'habitude, ça veut dire une de ces 3 choses :", "",
  "1. ton site est déjà premier sur google et cité par chatgpt sur tous tes mots-clés ;",
  "2. ce n'est pas le moment, ou pas pour toi ;",
  "3. claude code a pris le contrôle de ton ordi et t'empêche de répondre.", "",
  "réponds juste 1, 2 ou 3 pour que je sache quoi faire. je ferme lundi 19 octobre à 20h.", "",
  "Nathan"]),
]

def update(cid):
    seqs = api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")
    seqid, seq = next(iter(seqs.items()))
    for st in seq["steps"]:
        subj, delay, lines = STEPS[st["index"] - 1]
        body = {"type": "email", "message": html(lines), "delay": delay}
        if subj: body["subject"] = subj
        api("PATCH", f"https://api.lemlist.com/api/sequences/{seqid}/steps/{st['_id']}", body); time.sleep(0.4)
    print("MAJ", cid)

if __name__ == "__main__":
    camps, off = [], 0
    while True:
        page = api("GET", f"https://api.lemlist.com/api/campaigns?limit=100&offset={off}") or []
        camps += page; off += 100
        if len(page) < 100: break
    found = [c for c in camps if c.get("name") == NAME and not c.get("archived")]
    if found: update(found[0]["_id"]); raise SystemExit(0)
    camp = api("POST", "https://api.lemlist.com/api/campaigns", {"name": NAME})
    cid = camp.get("_id") or camp.get("id"); time.sleep(1)
    seqid = next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
    for i, (subj, delay, lines) in enumerate(STEPS, 1):
        body = {"type": "email", "message": html(lines), "delay": delay, "index": i}
        if subj: body["subject"] = subj
        api("POST", f"https://api.lemlist.com/api/sequences/{seqid}/steps", body); time.sleep(0.4)
    print("OK", NAME, cid)
