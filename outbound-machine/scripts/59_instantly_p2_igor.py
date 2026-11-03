"""Campagne P2 « recrute » (premier palier lancé, conseil d'Igor du 03/11) avec la séquence v3 d'Igor :
4 mails, 2 fils (J0 · J3 même fil · J8 nouveau fil · J11 même fil), envoi 7h30-14h en semaine, opt-out aux mails 1 et 3.
Une seule campagne pour tous les sous-ICP B2B : ce qui change par sous-ICP (preuve, mot d'arrêt, mails 2 à 4) passe dans
les variables du lead. Prospects Google + autres uniquement (pas de Microsoft depuis Zapmail, Igor 03/11).
Variable Gemini (58) : {{theme}} = « quand vos clients cherchent « X » » ; vide si Gemini n'a rien de sûr. {{observation}} retirée (faux positifs).
Test A/B demandé par Nathan sur le mail 1 : PS « +17 % de CA » (A) contre « +17 % de leads » (B).
Rien n'est lancé : brouillon, sans boîte rattachée.
Usage : python 59_instantly_p2_igor.py plan | domains | create | leads"""
import csv, glob, json, os, re, sys, urllib.request
import outreach_db as db

H = {"Authorization": "Bearer " + os.environ.get("INSTANTLY_API", ""), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 decupler-outbound"}
NAME = "123-GO-P2 · recrute · séquence Igor v3 · BROUILLON"
SCHEDULE = {"schedules": [{"name": "Semaine 7h30-14h (Paris)", "timing": {"from": "07:30", "to": "14:00"},
                           "days": {"1": True, "2": True, "3": True, "4": True, "5": True}, "timezone": "Europe/Belgrade"}]}
BLOCK = {"deja_contacte", "repondu", "desinscrit", "client", "concurrent", "agressif"}
SIG = "{{sendingAccountFirstName}}"

# Par sous-ICP (docs d'Igor du 02/11). 1.6, 1.7 et 1.8 (finance, M&A, CGP) prennent les lignes du conseil (1.5).
PS_CA = "PS : Pour Cloudtech, +17 % de CA en 6 mois grâce à Google et aux IA."
PS_LEADS = "PS : Pour Cloudtech, +17 % de leads en 6 mois grâce à Google et aux IA."
PS_IA = "PS : Pour Cloudtech, +23 % de visibilité sur les IA."  # chiffre donné par Nathan le 03/11 (mail 3)
ICP = {
    "1.1": dict(stop="pas de démo", s3o="coût par démo",
                s3=("J'imagine que chaque nouvelle démo chez {{companyName}} coûte un peu plus cher en Ads que la précédente, {{firstName}}.",
                    "Et le jour où le budget baisse, le pipeline baisse avec.",
                    "Je peux enregistrer une vidéo de 3 minutes sur les recherches que {{companyName}} pourrait recevoir sans payer le clic."),
                s4=("{{companyName}} est déjà cité partout sur Google et ChatGPT, et vous refusez des clients",
                    "Vous êtes curieux de voir comment on pourrait faire citer {{companyName}} par ChatGPT, mais les démos ont rempli votre semaine")),
    "1.2": dict(stop="pas de prompt", s3o="entre deux annonces",
                s3=("J'imagine que les demandes chez {{companyName}} arrivent surtout après un post LinkedIn ou une annonce de levée, {{firstName}}.",
                    "Entre deux annonces, c'est beaucoup plus calme.",
                    "Je peux enregistrer une vidéo de 3 minutes sur les recherches qui pourraient vous amener des demandes chaque semaine, sans attendre la prochaine annonce."),
                s4=("{{companyName}} est déjà la réponse de ChatGPT sur votre niche, et vous refusez des clients",
                    "Vous êtes curieux de voir comment on pourrait faire citer {{companyName}} par les IA, mais votre roadmap produit a pris toute la semaine")),
    "1.5": dict(stop="pas de mission", s3o="le réseau des associés",
                s3=("J'imagine que la plupart des missions de {{companyName}} arrivent par le réseau des associés, {{firstName}}.",
                    "Ça marche bien, jusqu'au trimestre où le réseau se tait.",
                    "Je peux enregistrer une vidéo de 3 minutes sur les recherches de dirigeants que vous pourriez capter, en plus du réseau."),
                s4=("Le réseau de {{companyName}} remplit déjà l'agenda pour toute l'année",
                    "Vous êtes curieux de voir comment on pourrait faire citer {{companyName}} par ChatGPT, mais vos missions ont pris toute la semaine")),
    "1.9": dict(stop="pas de brief", s3o="geo en interne", ps="PS : On a déjà travaillé la visibilité d'agences comme BeTomorrow.",
                s3=("J'imagine que monter une offre GEO chez {{companyName}} est sur la liste, juste derrière tout le reste, {{firstName}}.",
                    "Il faut du temps, des outils et quelqu'un qui suit ce qui change chaque mois.",
                    "Je peux enregistrer une vidéo de 3 minutes sur la façon dont le GEO en marque blanche s'ajoute à votre offre, sans recruter."),
                s4=("{{companyName}} vend déjà du GEO à tous ses clients",
                    "Vous êtes curieux de voir comment le GEO en marque blanche pourrait marcher chez {{companyName}}, mais les briefs clients ont pris toute la semaine")),
    "1.10": dict(stop="pas d'événement", s3o="saison des séminaires", ps="PS : On l'a fait pour Orators, une agence de conférenciers.",
                 s3=("J'imagine que chez {{companyName}}, l'agenda déborde en saison de séminaires puis se vide d'un coup, {{firstName}}.",
                     "Entre les deux, on attend les appels d'offres.",
                     "Je peux enregistrer une vidéo de 3 minutes sur les recherches d'entreprises que vous pourriez recevoir en direct, toute l'année."),
                 s4=("L'agenda de {{companyName}} est plein jusqu'en 2028",
                     "Vous êtes curieux de voir comment {{companyName}} pourrait recevoir plus de demandes en direct, mais vous étiez sur un événement toute la semaine")),
}
ALIAS = {"1.6": "1.5", "1.7": "1.5", "1.8": "1.5"}
# Relecture du 03/11 : hors cible malgré la qualification IA (fonds, banque, réseau immobilier, mutuelle, association, agences SEO concurrentes, hors France)
EXCLUDE = {"carac.fr", "coachingwaysme.com", "emotional-intelligence-mastery.com", "garageisep.com", "opalecapital.com", "orpi.com", "pictet.com",
           "simply-on.fr", "stride.vc", "tzcld.fr", "ucatchit.com"}


def html(t):
    return "".join(f"<div>{l}</div>" if l else "<div><br /></div>" for l in t.split("\n"))


def step1(ps):
    return html("\n\n".join([
        "Bonjour {{firstName}}, j'ai vu que {{companyName}} recrute.",
        "Une équipe qui grandit a besoin de demandes entrantes, et elles pourraient partir chez des concurrents mieux cités sur Google et ChatGPT.",
        "J'ai regardé votre site de près et relevé 7 leviers pour que ChatGPT et Google recommandent {{companyName}}{{theme}}.",
        "Seriez-vous contre que je vous les partage ? S'ils ne vous apprennent rien, dites-le moi et je ne vous relance plus.",
        SIG, ps, "PPS : Pas pertinent ? Répondez « {{stopword}} » et les 7 leviers iront à quelqu'un d'autre."]))


def sequence():
    s2 = html("\n\n".join(["Bonjour {{firstName}}, j'espère que ce message ne finit pas dans le trou noir des « je réponds plus tard, promis » :)",
                           "Ça vous embêterait que je vous envoie un levier concret pour que ChatGPT cite {{companyName}} ?", SIG,
                           "PS : Le levier tient en deux lignes : une réponse directe en haut de votre page clé, avec un chiffre. J'en ai 6 autres, classés par impact."]))
    s3 = html("\n\n".join(["{{s3a}}\n{{s3b}}", "{{s3c}}", "Ce serait une mauvaise idée que je vous l'envoie ?", SIG, "{{ps3}}",
                           "PPS : Pas pertinent ? Répondez « {{stopword}} » et la vidéo reste dans mon dossier."]))
    s4 = html("\n".join(["Je n'ai pas de nouvelles, {{firstName}}, alors j'imagine que c'est l'une de ces trois situations :",
                         "1) {{s4a}}", "2) {{s4b}}", "3) Claude a pris le contrôle de votre PC et ne vous laisse plus répondre", "",
                         "Répondez juste le numéro, que je sache où on en est.", "", SIG, "", "PS : Si c'est le 3, demandez-lui au moins de citer {{companyName}}."]))
    return [{"steps": [
        {"type": "email", "delay": 3, "variants": [{"subject": "votre recrutement", "body": step1("{{ps1a}}")},
                                                   {"subject": "votre recrutement", "body": step1("{{ps1b}}")}]},
        {"type": "email", "delay": 5, "variants": [{"subject": "", "body": s2}]},
        {"type": "email", "delay": 3, "variants": [{"subject": "{{s3o}}", "body": s3}]},
        {"type": "email", "delay": 0, "variants": [{"subject": "", "body": s4}]}]}]


def leads():
    dnc_dom, dnc_mail = set(), set()
    for r in db.select("do_not_contact", "email,domain,reason"):
        if r["reason"] in BLOCK:
            if r["domain"]: dnc_dom.add(r["domain"].lower())
            if r["email"]: dnc_mail.add(r["email"].lower())
    Q = json.load(open("../data/campaigns/qualif.json"))
    M = json.load(open("../data/datasets/enriched_moltsets.json"))
    F = json.load(open("../data/datasets/enriched_fullenrich.json")) if os.path.exists("../data/datasets/enriched_fullenrich.json") else {}
    G = json.load(open("../data/datasets/gemini_vars.json")) if os.path.exists("../data/datasets/gemini_vars.json") else {}
    out, seen = [], set()
    for fn in sorted(glob.glob("../data/datasets/DS-1*-FR-P2*.csv")):
        for r in csv.DictReader(open(fn)):
            icp = ALIAS.get(r["icp_code"], r["icp_code"])
            if icp not in ICP or r["domain"].lower() in EXCLUDE or r["esp"] == "microsoft" or r["domain"].lower() in dnc_dom: continue
            if Q.get(r["domain"], {}).get("fit") is not True: continue
            m = M.get(r["linkedin_url"]) or {}
            email = m.get("email") if m.get("risk_score") in ("A", "B") else None
            if not email and (F.get(r["linkedin_url"]) or {}).get("usable"): email = F[r["linkedin_url"]]["email"]
            if not email or email.lower() in dnc_mail or email.lower() in seen: continue
            edom, cdom = email.lower().split("@")[-1], r["domain"].lower()
            if not (edom == cdom or edom.endswith("." + cdom) or cdom.endswith("." + edom) or edom.split(".")[0] == cdom.split(".")[0]): continue
            seen.add(email.lower())
            g, d = G.get(r["domain"]) or {}, ICP[icp]
            # {{observation}} retirée (relecture 03/11 : trop de faux positifs) ; thématique = 1er terme proposé par Gemini
            th = (g.get("thematique") or "").split(",")[0].strip()
            if th and not th[:2].isupper(): th = th[0].lower() + th[1:]  # « CRM » garde ses majuscules, « Stratégie data » → « stratégie data »
            cv = dict(theme=f" quand vos clients cherchent « {th} »" if 2 < len(th) < 45 else "", stopword=d["stop"],
                      ps1a=d.get("ps", PS_CA), ps1b=d.get("ps", PS_LEADS), ps3=d.get("ps", PS_IA), s3o=d["s3o"],
                      s3a=d["s3"][0], s3b=d["s3"][1], s3c=d["s3"][2], s4a=d["s4"][0], s4b=d["s4"][1],
                      icp=r["icp_code"], tier=r["tier"], dataset=r["dataset"], lot="G" if r["esp"] == "google" else "O")
            out.append(dict(email=email, first_name=r["first_name"], last_name=r["last_name"], company_name=re.split(r" \| | - ", r["company"])[0].replace("™", "").strip(), website=r["domain"],
                            custom_variables=cv))
    return out


def api(method, path, body=None):
    r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=120).read() or b"{}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} {e.code} {e.read().decode()[:300]}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    ls = leads()
    if mode == "domains": print(" ".join(sorted({l["website"] for l in ls})))
    elif mode == "plan":
        from collections import Counter
        print(len(ls), "leads", Counter(l["custom_variables"]["icp"] for l in ls), Counter(l["custom_variables"]["lot"] for l in ls))
        print("avec thématique", sum(1 for l in ls if l["custom_variables"]["theme"]))
    elif mode == "create":
        r = api("POST", "/api/v2/campaigns", {"name": NAME, "campaign_schedule": SCHEDULE, "sequences": sequence(), "stop_on_reply": True,
                                               "stop_on_auto_reply": False, "open_tracking": False, "link_tracking": False, "text_only": True,
                                               "daily_limit": 60, "email_gap": 10, "random_wait_max": 10, "prioritize_new_leads": False})
        print("créée", r["id"]); open("../data/campaigns/instantly_123.id", "w").write(r["id"])
    elif mode == "leads":
        cid = open("../data/campaigns/instantly_123.id").read().strip()
        for i in range(0, len(ls), 500):
            api("POST", "/api/v2/leads/add", {"campaign_id": cid, "skip_if_in_workspace": False, "leads": ls[i:i + 500]})
        print(len(ls), "leads importés dans", cid)
