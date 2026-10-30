"""Crée (ou met à jour) les campagnes brouillon Instantly à partir des copies V2 (copy_v2.py) et y importe les leads
enrichis. Rien n'est lancé : aucune boîte n'est rattachée, la campagne reste en brouillon (status 0).
Séquence Igor (VP + FU) × 3, délais 0/3/5/3/10/3 ; suivi d'ouverture et de clics coupé ; texte seul ; arrêt à la réponse.
Variables de lead (custom_variables) : pb (problème du sous-ICP), ps (preuve du sous-ICP), poste, concurrent, motcle, volume, ville, zone…
Usage : python 51_instantly_drafts.py plan          (affiche le plan sans rien créer)
        python 51_instantly_drafts.py create        (crée / met à jour les campagnes, sans leads)
        python 51_instantly_drafts.py export        (un CSV de leads par campagne : ../data/campaigns/instantly/)
        python 51_instantly_drafts.py leads         (importe les leads enrichis : nécessite un plan payant, le gratuit bloque à quelques leads)"""
import csv, glob, json, os, re, sys, urllib.request
from collections import defaultdict
import outreach_db as db
from copy_v2 import (B2B, B2B_PALIERS, B2B_SUITE, B2B_SOBER_FU2, LOCAL, LOCAL_PALIERS, LOCAL_SUITE, LOCAL_P4D, LOCAL_SOBER_FU2, HOSP,
                     HOSP_PALIERS, HOSP_SUITE, SIGN, OUT, OUT_SOBER, fill, cta_rdv)

H = {"Authorization": "Bearer " + os.environ["INSTANTLY_API"], "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 decupler-outbound"}
DELAYS = [3, 5, 3, 10, 3, 0]  # attente après chaque étape (jours)
SCHEDULE = {"schedules": [{"name": "Semaine (heure de Paris)", "timing": {"from": "08:30", "to": "17:30"},
                           "days": {"1": True, "2": True, "3": True, "4": True, "5": True}, "timezone": "Europe/Belgrade"}]}
PS_LOCAL = "PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois."
PS_PERF = "PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas."
PS_HOSP = "PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble."
QUALIF = json.load(open("../data/campaigns/qualif.json"))  # 39_qualify.py : on n'enrichit / n'importe que fit=True
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}


def api(method, path, body=None):
    r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=120).read() or b"{}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} {e.code} {e.read().decode()[:300]}")


def html(t):
    return "".join(f"<div>{l}</div>" if l else "<div><br /></div>" for l in t.split("\n"))


def ps_b2b(code):
    d = B2B[code]
    if d.get("ps"): return d["ps"]
    who, what = d["preuve"].split(" : ")
    return f"PS : pour {who}, {what}."


def step1(body, ps, sober=False):
    return body + "\n\n" + SIGN + "\n" + ("{{ps}}\n" if ps == "var" else (ps + "\n" if ps else "")) + (OUT_SOBER if sober else OUT)


# Campagnes : code Instantly -> (famille, palier, sous-ICP couverts, lot, datasets sources)
# Paliers P1 / P2 B2B : un seul mail 1 gabarit, le problème et la preuve passent en variables {{pb}} / {{ps}}.
PLAN = {}


def add(code, fam, tier, icps, lot, sources, label):
    PLAN[code] = dict(fam=fam, tier=tier, icps=icps, lot=lot, sources=sources, label=label)


for lot in "GMO":  # G = Google, M = Microsoft / Outlook, O = autres fournisseurs (règle de nommage Nathan)
    # P1 (levée + recrute) : pas de données de levée en France dans la base Lemlist (29/10) → source à trouver
    add(f"121-{lot}-P2", "B2B", "P2", ["1.1", "1.2", "1.5", "1.6", "1.7", "1.8"], lot, ["DS-10[46]-*-FR-P2"], "B2B FR · recrute en marketing")
    add(f"122-{lot}-P2b", "B2B", "P2b", ["1.1", "1.2", "1.5", "1.6", "1.7", "1.8"], lot, ["DS-10[46]-*-FR-P2b"], "B2B FR · recrute des commerciaux")
    for icp in ["1.1", "1.2", "1.5", "1.6", "1.7", "1.8"]:
        camp = "104" if icp in ("1.1", "1.2") else "106"
        add(f"{camp}-{lot}-P4-{icp}", "B2B", "P4", [icp], lot, [f"DS-{camp}-{icp}-FR-P4*"], f"{B2B[icp]['label']} · FR · marché principal")
    add(f"110-{lot}-P4B-2.1", "LOCAL", "P4B", ["2.1"], lot, ["DS-110-2.1-FR-P4*"], "BTP et rénovation · FR · 20 chantiers de plus (performance)")
    add(f"110-{lot}-P4D-2.15", "LOCAL", "P4D", ["2.15"], lot, ["DS-110-2.15-FR-P4*"], "Travaux publics · FR · maîtres d'ouvrage privés")
    for icp in ["4.1", "4.2", "4.4"]:
        add(f"114-{lot}-P4-{icp}", "HOSP", "P4", [icp], lot, [f"DS-114-{icp}-FR-P4*"], f"{HOSP[icp]['label']} · FR · marché principal")


def sequence(c):
    """Séquence V2.2 : mail 1 en 2 variantes (A livrable / B rendez-vous, test demandé par Nathan), puis FU1 → FU3."""
    fam, tier, icps = c["fam"], c["tier"], c["icps"]
    if fam == "B2B":
        icp = icps[0]; sober = len(icps) == 1 and B2B[icp].get("sober")
        if tier in ("P1", "P2", "P2b"):
            subj, body = next((s, b) for e, s, b in B2B_PALIERS if e.startswith(tier + " "))
            first = (subj, body.replace("{pb}", "{{pb}}"), "var", False)
        else:
            subj, body = B2B[icp]["p4"]
            first = (subj, body, ps_b2b(icp), sober)
        suite = [(o, b) for _, o, b in B2B_SUITE]
        if sober: suite[2] = B2B_SOBER_FU2[1:]
    elif fam == "LOCAL":
        d = dict(LOCAL[icps[0]], label="entreprises du BTP", unit="chantiers") if icps[0] == "2.1" else LOCAL[icps[0]]
        if tier == "P4D": first = (LOCAL_P4D[1], LOCAL_P4D[2], PS_LOCAL, False)
        else:
            _, s, b = next(p for p in LOCAL_PALIERS if p[0].startswith("P4 · marché principal B"))
            first = (fill(s, d), fill(b, d), PS_PERF, False)
        suite = [(fill(o, d), fill(b, d)) for _, o, b in LOCAL_SUITE]
    else:
        d = HOSP[icps[0]]; sober = d.get("sober")
        first = (fill(d["p4"][0], d), d["p4"][1], "" if sober else (d.get("ps") or PS_HOSP), sober)
        suite = [(fill(o, d), fill(b, d)) for _, o, b in HOSP_SUITE]
        if sober: suite[2] = ("", LOCAL_SOBER_FU2[2])
    subj, body, ps, sober = first
    v1 = [{"subject": subj, "body": html(step1(body, ps, sober))}, {"subject": subj, "body": html(step1(cta_rdv(body), "" if "offert" in (ps or "") else ps, sober))}]  # PS « offert » sans objet en variante rendez-vous
    steps = [{"type": "email", "delay": DELAYS[0], "variants": v1}]
    steps += [{"type": "email", "delay": DELAYS[i + 1], "variants": [{"subject": o, "body": html(b)}]} for i, (o, b) in enumerate(suite)]
    return [{"steps": steps}]


def existing():
    out, after = {}, None
    while True:
        r = api("GET", "/api/v2/campaigns?limit=100" + (f"&starting_after={after}" if after else ""))
        for c in r.get("items", []): out[c["name"].split(" · ")[0]] = c["id"]
        after = r.get("next_starting_after")
        if not after: return out


_DNC = None


def dnc():
    global _DNC
    if _DNC is None:
        _DNC = (set(), set())
        for r in db.select("do_not_contact", "email,domain,reason"):
            if r["reason"] in BLOCK:
                if r["domain"]: _DNC[0].add(r["domain"].lower())
                if r["email"]: _DNC[1].add(r["email"].lower())
    return _DNC


LOT = {"google": "G", "microsoft": "M"}
SEEN = set()  # un email = une seule campagne


def leads_for(c):
    dnc_dom, dnc_mail = dnc()
    cache = json.load(open("../data/datasets/enriched_moltsets.json")) if os.path.exists("../data/datasets/enriched_moltsets.json") else {}
    fe = {r["linkedin_url"]: r for r in csv.DictReader(open("../data/campaigns/enriched.csv"))} if os.path.exists("../data/campaigns/enriched.csv") else {}
    out = []
    for pat in c["sources"]:
        for fn in sorted(glob.glob(f"../data/datasets/{pat}.csv")):
            for r in csv.DictReader(open(fn)):
                if LOT.get(r["esp"], "O") != c["lot"] or r["icp_code"] not in c["icps"] or r["domain"].lower() in dnc_dom: continue
                if QUALIF.get(r["domain"], {}).get("fit") is not True: continue
                m = cache.get(r["linkedin_url"]) or {}
                email = m.get("email") if m.get("risk_score") in ("A", "B") else None
                if not email and fe.get(r["linkedin_url"], {}).get("email_status") in ("DELIVERABLE", "HIGH_PROBABILITY", "Valid & safe to send email", "Probably Valid Email"):
                    email = fe[r["linkedin_url"]]["email"]
                if not email or email.lower() in dnc_mail or email.lower() in SEEN: continue
                edom, cdom = email.lower().split("@")[-1], r["domain"].lower()
                if not (edom == cdom or edom.endswith("." + cdom) or cdom.endswith("." + edom)): continue  # email d'une autre société
                SEEN.add(email.lower())
                cv ={"pb": B2B[r["icp_code"]]["pb"], "ps": ps_b2b(r["icp_code"])} if c["fam"] == "B2B" else {}
                cv.update(ville=r.get("city") or "", zone=f"à {r['city']}" if r.get("city") else "en France", tier=r["tier"], dataset=r["dataset"], icp=r["icp_code"])
                out.append(dict(email=email, first_name=r["first_name"], last_name=r["last_name"], company_name=r["company"],
                                website=r["domain"], personalization="", custom_variables=cv))
    return out


mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
STD = {"firstName", "lastName", "companyName", "pb", "ps", "ville", "zone", "poste"}
if mode == "plan":
    for k, c in PLAN.items():
        txt = json.dumps(sequence(c), ensure_ascii=False)
        manque = sorted(set(re.findall(r"\{\{(\w+)\}\}", txt)) - STD)
        print(k, "·", c["label"], "· leads prêts :", len(leads_for(c)), "· variables à remplir :", ", ".join(manque) or "aucune")
elif mode == "reset":  # supprime les brouillons créés par ce script (aucun n'a de boîte ni de lead)
    for k, cid in existing().items():
        if re.match(r"^1\d\d-[GOM]-P", k): api("DELETE", f"/api/v2/campaigns/{cid}"); print("supprimée", k)
elif mode == "create":
    ids = existing()
    for k, c in PLAN.items():
        body = {"name": f"{k} · {c['label']} · BROUILLON copies V2 à valider", "campaign_schedule": SCHEDULE, "sequences": sequence(c),
                "stop_on_reply": True, "stop_on_auto_reply": False, "open_tracking": False, "link_tracking": False, "text_only": True,
                "daily_limit": 30, "email_gap": 10, "random_wait_max": 10, "prioritize_new_leads": False}
        if k in ids: api("PATCH", f"/api/v2/campaigns/{ids[k]}", body); print("mis à jour", k)
        else: r = api("POST", "/api/v2/campaigns", body); ids[k] = r["id"]; print("créée", k, r["id"])
        db.upsert("campaigns", [dict(code=k, name=body["name"], tool="instantly", icp_code=c["icps"][0], esp_lot=c["lot"], language="fr",
                                     country="FR", status="draft", notes=f"Instantly {ids[k]} · {c['tier']} · sous-ICP {', '.join(c['icps'])}")], "code")
elif mode == "export":  # plan gratuit Instantly : import bloqué (« Lead limit reached ») → un CSV par campagne, prêt à charger
    os.makedirs("../data/campaigns/instantly", exist_ok=True)
    for k, c in PLAN.items():
        ls = leads_for(c)
        if not ls: continue
        keys = sorted({x for l in ls for x in l["custom_variables"]})
        with open(f"../data/campaigns/instantly/{k}.csv", "w", newline="") as fh:
            w = csv.writer(fh); w.writerow(["email", "first_name", "last_name", "company_name", "website"] + keys)
            for l in ls: w.writerow([l["email"], l["first_name"], l["last_name"], l["company_name"], l["website"]] + [l["custom_variables"].get(x, "") for x in keys])
        print(k, len(ls))
elif mode == "leads":
    ids = existing()
    for k, c in PLAN.items():
        if k not in ids: continue
        ls = leads_for(c)
        if not ls: continue
        for i in range(0, len(ls), 500):
            api("POST", "/api/v2/leads/add", {"campaign_id": ids[k], "skip_if_in_workspace": True, "leads": ls[i:i + 500]})
        db.call({"action": "update", "table": "campaigns", "values": {"prospects": len(ls)}, "eq": {"code": k}})
        print(k, len(ls), "leads importés")
