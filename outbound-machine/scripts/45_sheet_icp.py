"""Génère les lignes du tableau des sous-ICP (onglet « 2b. Sous-ICP » du Sheet kickoff d'Igor) en JSON.
Usage : python 45_sheet_icp.py > ../data/sheet_icp.json"""
import json
import sequences as S
from icp_catalog import SEGMENTS
from icp_sheet import SUB, TITLES, PALIER, INTENT, S_NAMES, USP_B2B, USP_PERF, USP_MED, USP_HOSP, CTA_B2B, CTA_PERF, COMP_B2B, COMP_LOCAL, REF_B2B, REF_LOCAL

SIZES = json.load(open("../data/market_size.json"))
WAVE = {"FR": 1, "BE": 2, "CH": 2, "LU": 2, "MA": 2, "TN": 2, "TR": 2, "HU": 2}
HEAD = ["Code", "Sous-ICP", "ICP parent (commun : onglet 2. ICP / VP)", "Industries (filtre base)", "Mots-clés FR / EN", "Pays (vague)",
        "Problème 1", "Problème 2", "Problème 3", "Solutions / VP (top 3)", "Cas client (decupler.com)", "Lead magnet (mail → appel)",
        "Séquence(s)", "Angle et source", "Hack / astuce", "Mail 1 (VP1) proposé", "Taille du marché (entreprises, base Lemlist)",
        "Source des leads", "Points à valider", "Validation Nathan", "Commentaires Nathan"]
PARENT = {"1": "ICP 1 · Services B2B", "2": "ICP 2 · Services locaux (partenariat à la performance)",
          "3": "ICP 3 · Tourisme médical (cliniques à l'étranger)", "4": "ICP 4 · Hospitalité et bien-être"}


def kind(code):
    return {"1": "B2B", "2": "PERF", "3": "MED", "4": "HOSP"}[code.split(".")[0]]


def vp1(sg):
    k = kind(sg["code"])
    if sg["code"] == "1.9":
        return "À écrire : séquence « marque blanche GEO pour agences » (les séquences S1-S5 vendent du SEO à l'agence, qui est concurrente)."
    proof = sg["proof"][0] if sg["proof"] else None
    if k == "B2B":
        subj, body = S.H7["fr"][0]
        body = body.replace("{{icebreaker}}", S.ICEBREAKER["fr"]["H7default"])
    else:
        subj, body = S.H9["fr"][0]
        unit = (sg.get("unit") or ("clients", ""))[0]
        icp = int(sg["code"][0])
        body = body.replace("[UNIT]", unit).replace("[SEG]", sg["seg_fr"]).replace("[ORIGIN]", S.ORIGIN.get(icp, ("", ""))[0])
        subj = subj.replace("[UNIT]", unit)
        body = body.replace("[PROOF_LINE]", (proof + ".\n\n") if proof else "")
    body = body.replace("[PROOF]", proof or "[preuve à fournir]").replace("[SEG]", sg["seg_fr"])
    return f"Objet : {subj}\n\n{body}"


def size(code):
    d = SIZES.get(code, {})
    parts = []
    for lab in ("FR", "francophone", "anglophone"):
        a, b = d.get(f"{lab} 11+"), d.get(f"{lab} 1-10")
        if a is not None: parts.append(f"{lab} : {a + b} ({a} à 11 sal. et +)")
    out = " · ".join(parts)
    if code.startswith("3."): out += " · ⚠ mesuré hors Turquie / Hongrie : à remesurer sur les pays des cliniques"
    return out


def source(code, d):
    tot_fr = sum(v for k, v in d.items() if k.startswith("FR"))
    k = kind(code)
    if k == "B2B": return "Base Lemlist (recherche gratuite) ou Instantly SuperSearch ; emails : FullEnrich / Moltsets (test en cours) ; signal recrute : Lemlist + Apify hors France"
    if k == "PERF":
        return ("Base Lemlist trop faible → Google Maps (Outscraper, ≈ 3 $ / 1 000 fiches) puis emails" if tot_fr < 500
                else "Base Lemlist (entreprises ≥ 5 sal.) + Google Maps (Outscraper) pour les plus petites ; emails FullEnrich / Moltsets")
    if k == "MED": return "Dataset Igor (demande à faire) + Google Maps Istanbul / Tunis / Budapest (Outscraper)"
    return "Google Maps (Outscraper) + base Lemlist ; dataset Igor pour l'international"


rows = [HEAD]
for sg in SEGMENTS:
    c = sg["code"]; k = kind(c); x = SUB[c]
    langs = sorted({(WAVE.get(p, 3), p) for p in sg["countries"]})
    pays = " · ".join(f"V{w} " + ", ".join(p for ww, p in langs if ww == w) for w in sorted({w for w, _ in langs}))
    rows.append([c, sg["name"], PARENT[c[0]], x["ind"], " · ".join(sg["kw_fr"]) + " / " + " · ".join(sg["kw_en"]), pays,
                 *x["pains"], "\n".join("• " + s for s in x["sol"]),
                 sg["proof"][0] if sg["proof"] else "à fournir (aucun cas publié dans ce secteur)",
                 x["lm"], x["seq"], x["angle"], x["hack"], vp1(sg), size(c), source(c, SIZES.get(c, {})), x.get("note", ""), "", ""])
print(json.dumps(rows, ensure_ascii=False))
