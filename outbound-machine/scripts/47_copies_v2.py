"""Déplie copy_v2.py en lignes pour l'onglet « 6b. Copies V2 à valider » : un mail 1 par sous-ICP × palier,
puis la suite (FU1 → FU3) une fois par famille. Le tourisme médical est en pause (aucune ligne).
Sortie : ../data/copies_v2.json (toutes les lignes), ../data/copies_v2_sheet.json (onglet 6b) et ../copy/35_copies_v2.md"""
import json, re
from copy_v2 import *

PS_LOCAL = "PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois."
PS_PERF = "PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas."
PS_HOSP = "PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble."
rows = []


def words(t):
    return len(re.findall(r"\w+", re.sub(r"\{\{\w+\}\}", "X", t.split("\nPS")[0])))


def clean(t):
    return re.sub(r"\n{3,}", "\n\n", t).strip()  # paragraphe vide (ex. stat_ia absente) supprimé


def add(code, label, etape, objet, corps, ps=None, sober=False, note=""):
    corps = clean(corps)
    if ps is not None:  # mail d'ouverture : signature + PS + PPS
        corps = f"{corps}\n\n{SIGN}\n" + (f"{ps}\n" if ps else "") + (OUT_SOBER if sober else OUT)
    rows.append([f"V2-{len(rows) + 1:03d}", f"{code} {label}", etape, objet, corps, words(corps), note, "", ""])


def ps_b2b(d):
    if d.get("ps"): return d["ps"]
    who, what = d["preuve"].split(" : ")
    return f"PS : pour {who}, {what}."


for code, d in B2B.items():
    ps = ps_b2b(d)
    for et, obj, body in B2B_PALIERS:
        if et.startswith("P1") and code not in P1_ICPS: continue
        add(code, d["label"], et, fill(obj, d), fill(body, d), ps, d.get("sober"), "variante B : dernière phrase → « " + RDV + " »")
    add(code, d["label"], "P4 · marché principal", d["p4"][0], d["p4"][1], ps, d.get("sober"), "cœur du sous-ICP · variante B rendez-vous")
    add(code, d["label"], B2B_CHAMPION[0], B2B_CHAMPION[1], B2B_CHAMPION[2], ps, d.get("sober"), "si le contact est SEO / contenu")
    for et, obj, body in B2B_SUITE:
        if d.get("sober") and et.startswith("FU2"): et, obj, body = B2B_SOBER_FU2
        add(code, d["label"], et, obj, fill(body, d))

for code, d in LOCAL.items():
    for et, obj, body in LOCAL_PALIERS:
        if "saison" in et and not d.get("saison"): continue
        if "interdiction" in et and not d.get("demarchage"): continue
        if (d.get("sober") or d.get("b2b")) and ("marché principal A" in et or "marché principal B" in et): continue  # pompes funèbres, TP
        if d.get("b2b") and "Maps" in et: continue  # les maîtres d'ouvrage ne passent pas par Google Maps
        ps = "" if d.get("sober") else (PS_PERF if "performance" in body else PS_LOCAL)
        add(code, d["label"], et, fill(obj, d), fill(body, d), ps, d.get("sober"))
    if d.get("b2b"): add(code, d["label"], LOCAL_P4D[0], LOCAL_P4D[1], LOCAL_P4D[2], PS_LOCAL)
    if d.get("sober"): add(code, d["label"], LOCAL_P4_SOBER[0], LOCAL_P4_SOBER[1], LOCAL_P4_SOBER[2], "", True)
    for et, obj, body in LOCAL_SUITE:
        if d.get("sober") and et.startswith("FU2"): et, obj, body = LOCAL_SOBER_FU2
        add(code, d["label"], et, fill(obj, d), fill(body, d))

for code, d in HOSP.items():
    ps = d.get("ps") or PS_HOSP
    for et, obj, body in HOSP_PALIERS:
        add(code, d["label"], et, fill(obj, d), fill(body, d), "" if d.get("sober") else ps, d.get("sober"))
    add(code, d["label"], "P4 · marché principal", fill(d["p4"][0], d), d["p4"][1], "" if d.get("sober") else ps, d.get("sober"), "cœur du sous-ICP")
    for et, obj, body in HOSP_SUITE:
        if d.get("sober") and et.startswith("FU2"): et, obj, body = LOCAL_SOBER_FU2[0].replace("2.6 pompes funèbres", "4.3"), "", LOCAL_SOBER_FU2[2]
        if code == "4.5" and et.startswith("FU2"): body = body.replace("vous êtes complets jusqu'en 2028", "vos promotions sont complètes jusqu'en 2028")
        add(code, d["label"], et, fill(obj, d), fill(body, d))

for i, (fam, et, obj, body) in enumerate(INTENT_V21, 1):
    ps = {"B2B": "{{ps}} (preuve du sous-ICP)", "LOCAL": PS_LOCAL, "HOSP": PS_HOSP}[fam] if et.startswith("P") else None
    add({"B2B": "1.x", "LOCAL": "2.x", "HOSP": "4.x"}[fam], "intent SEO / GEO (tous)", et, obj, body, ps, False, "V2.1 · variables DataForSEO")

sheet, seen = [], set()
for r in rows:
    body = r[4].split(f"\n\n{SIGN}\n")
    ps = body[1] if len(body) > 1 else ""
    fam = r[1].split(".")[0]
    if not r[2].startswith(("P", "Champion")) and "intent" not in r[1]:  # suite : une seule fois par famille
        if (fam, r[2]) in seen: continue
        seen.add((fam, r[2]))
        r = r[:1] + [{"1": "1.x B2B (tous)", "2": "2.x BTP / local (tous)", "4": "4.x hospitalité / bien-être (tous)"}[fam]] + r[2:]
        for a, b in [("« rénovation ", "« {{metier}} "), ("hôtel {{ville}}", "{{recherche}}"), ("plus de réservations en direct", "plus de {{clients}}")]:
            body[0] = body[0].replace(a, b); r[3] = r[3].replace(a, b)
    sheet.append([r[0], r[1], r[2], r[3], body[0], ps, r[5], r[6], "", ""])
json.dump([["N°", "Sous-ICP", "Étape / palier", "Objet", "Texte (avant signature)", "PS / PPS", "Mots", "Note", "Validation", "Commentaire Nathan"]] + sheet,
          open("../data/copies_v2_sheet.json", "w"), ensure_ascii=False)
print("sheet", len(sheet), sum(len(json.dumps(x, ensure_ascii=False)) for x in sheet))
head = ["N°", "Sous-ICP", "Étape / palier", "Objet", "Texte", "Mots (hors PS)", "Note", "Validation", "Commentaire Nathan"]
json.dump([head] + rows, open("../data/copies_v2.json", "w"), ensure_ascii=False)
md = ["# Copies V2.2 à valider (30/10, après audit)\n",
      "Générées par scripts/47_copies_v2.py depuis scripts/copy_v2.py. Validation dans le Sheet, onglet « 6b. Copies V2 à valider ».",
      f"Chaque mail 1 existe en variante A (livrable, ci-dessous) et B (dernière phrase remplacée par « {RDV} »).\n",
      "## Hypothèses par palier (HADI)\n" + "\n".join(f"- **{k}** : {v}" for k, v in HYPOTHESES.items()) + "\n"]
cur = None
for r in rows:
    if r[1] != cur: cur = r[1]; md.append(f"\n## {cur}\n")
    md.append(f"### {r[0]} · {r[2]}\n**Objet :** {r[3] or '(même fil)'}\n\n{r[4]}\n")
open("../copy/35_copies_v2.md", "w").write("\n".join(md))
print(len(rows), "lignes ;", "max mots", max(r[5] for r in rows), [(r[0], r[5]) for r in rows if r[5] > 80][:15])
left = [r[0] for r in rows if re.search(r"(?<!\{)\{[a-z0-9_]+\}(?!\})", r[3] + r[4])]
print("placeholders non remplis :", left[:10])
bad = [(r[0], m) for r in rows for m in re.findall(r"(en direct en direct|plus de [aeiouéh]\w+|meilleur \{\{|ne descendent|gratuit|Big Four|un·e|vous montre|Ça vaut 15)", r[4])]
print("tournures à vérifier :", bad[:15])
