"""Déplie copy_v2.py en lignes pour l'onglet « 6b. Copies V2 à valider » : un mail 1 par sous-ICP × palier,
puis la suite (FU1 → FU3) par sous-ICP. Sortie : ../data/copies_v2.json (liste de lignes) + ../copy/35_copies_v2.md"""
import json, re
from copy_v2 import *

PS_LOCAL = "PS : pour un de nos clients, on est allé chercher 20 nouveaux clients par mois. Je vous explique comment au téléphone."
PS_PERF = "PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas."
PS_HOSP = "PS : le diagnostic est gratuit et vous le gardez, même si on ne travaille jamais ensemble."
rows = []


def words(t):
    return len(re.findall(r"\w+", re.sub(r"\{\{\w+\}\}", "X", t.split("\nPS")[0])))


def add(code, label, etape, objet, corps, ps=None, sober=False, note=""):
    if ps is not None:  # mail d'ouverture : signature + PS + PPS
        corps = f"{corps}\n\n{SIGN}\n" + (f"{ps}\n" if ps else "") + (OUT_SOBER if sober else OUT)
    rows.append([f"V2-{len(rows) + 1:03d}", f"{code} {label}", etape, objet, corps, words(corps), note, "", ""])


for code, d in B2B.items():
    who, what = d["preuve"].split(" : ") if " : " in d["preuve"] else (None, d["preuve"])
    ps = f"PS : pour {who}, {what}." if who else f"PS : {what}."
    for et, obj, body in B2B_PALIERS:
        add(code, d["label"], et, fill(obj, d), fill(body, d), ps, d.get("sober"), "variables P1/P2 : signal levée/offre ; P3a : DataForSEO")
    add(code, d["label"], "P4 · marché principal", d["p4"][0], d["p4"][1], ps, d.get("sober"), "cœur du sous-ICP")
    add(code, d["label"], B2B_CHAMPION[0], B2B_CHAMPION[1], B2B_CHAMPION[2], ps, d.get("sober"), "si le contact est SEO / contenu")
    for et, obj, body in B2B_SUITE:
        if d.get("sober") and et.startswith("FU2"):
            body = "{{firstName}}, une dernière question : la visibilité de {{companyName}} sur Google et dans ChatGPT est-elle un sujet pour vous cette année ?\n\nUn « oui » ou un « non » me suffit.\n\nNathan"
            et = "FU2 · J+11 · relance sobre"
        add(code, d["label"], et, obj, fill(body, d))

for code, d in LOCAL.items():
    for et, obj, body in LOCAL_PALIERS:
        if "saison" in et and not d.get("saison"): continue
        if "interdiction" in et and not d.get("demarchage"): continue
        if d.get("b2b") and ("plateformes" in et or "ChatGPT" in et): continue
        ps = PS_PERF if "performance" in body else PS_LOCAL
        if d.get("sober"): ps = ""
        add(code, d["label"], et, fill(obj, d), fill(body, d), ps, d.get("sober"))
    if d.get("b2b"):  # TP / génie civil : acheteurs publics et privés, pas de particuliers
        add(code, d["label"], "P4 · marché principal D · maîtres d'ouvrage privés", "vos marchés privés",
            "{{firstName}}, les marchés publics passent par les plateformes d'appel d'offres. Les maîtres d'ouvrage privés, eux, cherchent sur Google « {{motcle}} {{zone}} », et c'est {{concurrent}} qu'ils trouvent.\n\nUn marché privé qui arrive en direct, c'est un dossier sans mise en concurrence à 10.\n\nSeriez-vous contre que je vous montre ce qui le place devant {{companyName}} ?",
            PS_LOCAL)
    for et, obj, body in LOCAL_SUITE:
        if d.get("sober") and et.startswith("FU2"): et, obj, body = LOCAL_SOBER_FU2
        if d.get("b2b") and et.startswith("FU2"):
            body = body.replace("vous êtes sur un chantier", "vous êtes sur un chantier ou un appel d'offres")
        add(code, d["label"], et, fill(obj, d), fill(body, d))

for code, d in MED.items():
    for et, obj, body in MED_PALIERS:
        add(code, d["label"], et, fill(obj, d), fill(body, d), PS_PERF, note="langue : FR (patients France/BE/CH)")
    for et, obj, body in HOSP_SUITE:
        add(code, d["label"], et, fill(obj, d), fill(body, dict(d, recherche="clinique " + d["soin"], unit="patients en direct")).replace("vous êtes complets jusqu'en 2028", "votre planning opératoire est plein jusqu'en 2028").replace("en plein service", "au bloc"))

for code, d in HOSP.items():
    ps = "PS : pour l'École Humaniste de Gestalt, position moyenne Google passée de 18 à 10." if code == "4.5" else PS_HOSP
    for et, obj, body in HOSP_PALIERS:
        add(code, d["label"], et, fill(obj, d), fill(body, d), "" if d.get("sober") else ps, d.get("sober"))
    add(code, d["label"], "P4 · marché principal", fill(d["p4"][0], d), d["p4"][1], "" if d.get("sober") else ps, d.get("sober"), "cœur du sous-ICP")
    for et, obj, body in HOSP_SUITE:
        if d.get("sober") and et.startswith("FU2"): et, obj, body = LOCAL_SOBER_FU2[0].replace("2.6 pompes funèbres", "4.3"), "", LOCAL_SOBER_FU2[2]
        if code == "4.5" and et.startswith("FU2"): body = body.replace("vous êtes complets jusqu'en 2028", "vos promotions sont complètes jusqu'en 2028").replace("en plein service", "en cours")
        add(code, d["label"], et, fill(obj, d), fill(body, d))

sheet, seen = [], set()
for r in rows:
    body = r[4].split(f"\n\n{SIGN}\n")
    ps = body[1] if len(body) > 1 else ""
    fam = r[1].split(".")[0]
    if not r[2].startswith(("P", "Champion")):  # suite : une seule fois par famille et par texte
        key = (fam, r[2], r[3].replace(r[1], ""), body[0] if fam != "2" else r[2])
        if (fam, r[2]) in seen: continue
        seen.add((fam, r[2]))
        r = r[:1] + [{"1": "1.x B2B (tous)", "2": "2.x BTP / local (tous)", "3": "3.x tourisme médical (tous)", "4": "4.x hospitalité / bien-être (tous)"}[fam]] + r[2:]
        for a, b in [("« rénovation ", "« {{metier}} "), ("hôtel {{ville}}", "{{recherche}}"), ("clinique greffe de cheveux", "{{recherche}}"),
                     ("plus de réservations directes", "plus de {{clients}}"), ("plus de patients en direct", "plus de {{clients}}")]:
            body[0] = body[0].replace(a, b); r[3] = r[3].replace(a, b)
    sheet.append([r[0], r[1], r[2], r[3], body[0], ps, r[5], r[6], "", ""])
json.dump([["N°", "Sous-ICP", "Étape / palier", "Objet", "Texte (avant signature)", "PS / PPS", "Mots", "Note", "Validation", "Commentaire Nathan"]] + sheet,
          open("../data/copies_v2_sheet.json", "w"), ensure_ascii=False)
print("sheet", len(sheet), sum(len(json.dumps(x, ensure_ascii=False)) for x in sheet))
head = ["N°", "Sous-ICP", "Étape / palier", "Objet", "Texte", "Mots (hors PS)", "Note", "Validation", "Commentaire Nathan"]
json.dump([head] + rows, open("../data/copies_v2.json", "w"), ensure_ascii=False)
md = ["# Copies V2 à valider (29/10)\n", "Générées par scripts/47_copies_v2.py depuis scripts/copy_v2.py. Validation dans le Sheet, onglet « 6b. Copies V2 à valider ».\n"]
cur = None
for r in rows:
    if r[1] != cur: cur = r[1]; md.append(f"\n## {cur}\n")
    md.append(f"### {r[0]} · {r[2]}\n**Objet :** {r[3] or '(même fil)'}\n\n{r[4]}\n")
open("../copy/35_copies_v2.md", "w").write("\n".join(md))
from collections import Counter
print(len(rows), "lignes ;", "max mots", max(r[5] for r in rows), [ (r[0], r[5]) for r in rows if r[5] > 85][:15])
left = [r[0] for r in rows if re.search(r"(?<!\{)\{[a-z0-9]+\}(?!\})", r[3] + r[4])]
print("placeholders non remplis :", left[:10])
