"""Brouillons Instantly de la vague 1 avec les séquences V5 (doc « Séquences V5 », 06/11) : 3 mails, 2 fils
(J0 · J+3 même fil · J+8 nouveau fil), envoi 7h30-14h en semaine, opt-out au 1er mail de chaque fil.
Leads : dataset UltB d'Igor (lot G) + nos leads FR (Moltsets A/B ou FullEnrich utilisable), liste noire par personne
(contact_history : < 90 jours, réponse, désinscrit, bounce), Microsoft exclu, un email = une seule campagne.
Rien n'est lancé : aucune boîte rattachée (Zapmail ou PremiumInboxes se rattachent au lancement).
Mail 3 B (« {{competitor}} sort, pas vous ») et S3b mail 1 viendront quand les concurrents seront vérifiés dans Google.
Usage : python 66_instantly_v5.py plan | create | leads"""
import csv, datetime, glob, json, os, re, sys, urllib.request
import outreach_db as db

H = {"Authorization": "Bearer " + os.environ.get("INSTANTLY_API", ""), "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 decupler-outbound"}
SCHED = {"schedules": [{"name": "Semaine 7h30-14h", "timing": {"from": "07:30", "to": "14:00"},
                        "days": {"1": True, "2": True, "3": True, "4": True, "5": True}, "timezone": "Europe/Belgrade"}]}
SIG_EN, SIG_FR = "Nathan Fenina\nDécupler", "Nathan Fenina\nDécupler"
PS_CA_EN = "PS: For Cloudtech, +17% revenue in 6 months from Google and AI search."
PS_LEADS_EN = "PS: For Cloudtech, +17% leads in 6 months from Google and AI search."
PS_CA_FR = "PS : Pour Cloudtech, +17 % de CA en 6 mois grâce à Google et aux IA."
PS_LEADS_FR = "PS : Pour Cloudtech, +17 % de leads en 6 mois grâce à Google et aux IA."

M3A_EN = ("{{companyName}}'s organic opportunities", [
    "Hi {{firstName}},",
    "I'll be direct, and this may sound a bit random: I can put together a table that maps the organic opportunities for {{companyName}}, the keywords, AI prompts and competitors with real buying intent in {{niche}}, so search turns into sales opportunities.",
    "Some of them you probably already work on. Many others you don't.",
    "Can I record a 3-minute video walking you through it?", SIG_EN, "{{ps3}}",
    "PPS: Not a priority? Reply \"no thanks\" and I'll close the file."])
M3A_FR = ("les opportunités organiques de {{companyName}}", [
    "Bonjour {{firstName}},",
    "Je vais être direct, et ça peut sembler un peu sorti de nulle part : je peux vous préparer un tableau qui cartographie les opportunités organiques de {{companyName}}, les mots-clés, les questions posées aux IA et les concurrents à intention d'achat sur {{niche}}, pour transformer la recherche en opportunités commerciales.",
    "Certaines, vous les travaillez sûrement déjà. Beaucoup d'autres, non.",
    "Je vous enregistre une vidéo de 3 minutes pour vous le présenter ?", SIG_FR, "{{ps3}}",
    "PPS : Pas prioritaire ? Répondez « non merci » et je clos le dossier."])

SEQ = {
 "S1EN": [("{{niche}} on chatgpt", ["Hi {{firstName}},",
     "I was wondering how {{companyName}} shows up when someone asks ChatGPT for the best {{niche}}. More and more buyers build their shortlist there, before they ever book a demo.",
     "I can show you 3 quick wins that could get {{companyName}} recommended more often, the same kind of fixes that brought Cloudtech +23% visibility in AI answers.",
     "Would you be against a quick video showing you how?", SIG_EN,
     "PS: Not looking for more demos right now? Reply \"no thanks\" and I won't follow up."]),
   ("", ["Hi {{firstName}}, just floating this back up in case it got buried under the demo requests :)", "Shall I record the video? It's 3 minutes.", "Nathan"]),
   M3A_EN],
 "S2EN": [("{{niche}} firms on chatgpt", ["Hi {{firstName}},",
     "When a CEO asks ChatGPT for a {{niche}} firm, it usually names the big consultancies first, and a specialist like {{companyName}} can easily go unnoticed.",
     "I can show you 3 quick wins to get {{companyName}} cited in those answers and closer to the top 3 on Google, the approach that brought Cloudtech +23% visibility in AI answers.",
     "Would you be against a quick video showing you how?", SIG_EN,
     "PS: Your network keeps you busy enough? Reply \"no thanks\" and I won't follow up."]),
   ("", ["Hi {{firstName}}, I guess partners' calendars fill up fast :)", "Shall I record the video anyway? You can watch it between two meetings.", "Nathan"]),
   M3A_EN],
 "S1FR": [("{{niche}} sur chatgpt", ["Bonjour {{firstName}},",
     "Je me demandais comment {{companyName}} ressort quand on demande à ChatGPT le meilleur {{niche}}. De plus en plus d'acheteurs font leur shortlist là, avant même de demander une démo.",
     "Je peux vous montrer 3 quick wins pour que {{companyName}} soit recommandé plus souvent, le même type d'actions qui a apporté à Cloudtech +23 % de visibilité dans les réponses des IA.",
     "Seriez-vous contre une courte vidéo pour vous montrer comment ?", SIG_FR,
     "PS : Pas le sujet du moment ? Répondez « non merci » et je ne vous relance pas."]),
   ("", ["Bonjour {{firstName}}, je remonte mon message au cas où il serait passé sous une pile de demandes de démo :)", "Je vous enregistre la vidéo ? Elle dure 3 minutes.", "Nathan"]),
   M3A_FR],
 "S2FR": [("cabinets {{niche}} sur chatgpt", ["Bonjour {{firstName}},",
     "Quand un dirigeant demande à ChatGPT un cabinet en {{niche}}, il cite souvent d'abord les grands noms, et un spécialiste comme {{companyName}} peut facilement passer inaperçu.",
     "Je peux vous montrer 3 quick wins pour que {{companyName}} soit cité dans ces réponses et se rapproche du top 3 sur Google, la méthode qui a apporté à Cloudtech +23 % de visibilité dans les réponses des IA.",
     "Seriez-vous contre une courte vidéo pour vous montrer comment ?", SIG_FR,
     "PS : Votre réseau vous suffit ? Répondez « non merci » et je ne vous relance pas."]),
   ("", ["Bonjour {{firstName}}, j'imagine que l'agenda des associés se remplit vite :)", "Je vous enregistre quand même la vidéo ? Elle se regarde entre deux rendez-vous.", "Nathan"]),
   M3A_FR],
 "S3aFR": [("et chatgpt ?", ["Bonjour {{firstName}},", "J'imagine que certains de vos clients commencent à vous demander « et ChatGPT ? ».",
     "On fait le GEO en marque blanche : vous gardez le client et la marge, on exécute. Je peux faire un audit de visibilité IA offert pour un de vos clients, sous votre nom, pour que vous jugiez sur pièce.",
     "Seriez-vous contre qu'on choisisse lequel ?", SIG_FR, "PS : Pas pour vous ? Répondez « non merci » et l'audit ira à une autre agence."]),
   ("", ["Bonjour {{firstName}}, j'imagine que les briefs clients ont pris toute la semaine :)", "Je fais quand même l'audit ? Vous n'avez qu'à choisir le client.", "Nathan"]),
   ("le geo pour vos clients", ["Bonjour {{firstName}},",
     "J'imagine que monter une offre GEO chez {{companyName}} est sur la liste, juste derrière tout le reste. Il faut du temps, des outils et quelqu'un qui suit ce qui change chaque mois.",
     "Je peux vous enregistrer une vidéo de 3 minutes sur la façon dont le GEO en marque blanche s'ajoute à votre offre, sans recruter.",
     "Ce serait une mauvaise idée que je vous l'envoie ?", SIG_FR, "PS : On a déjà travaillé la visibilité d'agences comme BeTomorrow.",
     "PPS : Pas pertinent ? Répondez « non merci » et la vidéo reste dans mon dossier."])],
 # S3b : mail 1 « concurrent à [ville] » quand le concurrent sera vérifié ; en attendant, le mail 3 (agences de [ville] sur ChatGPT) passe en mail 1
 "S3bFR": [("les agences de {{city}} sur chatgpt", ["Bonjour {{firstName}},",
     "Quand une entreprise de {{city}} demande une agence à ChatGPT, il recommande en général 2 ou 3 noms. Je me demandais si {{companyName}} en faisait partie.",
     "Je peux vous montrer 3 quick wins pour entrer dans ces réponses, la méthode qui a apporté à Cloudtech +23 % de visibilité dans les réponses des IA.",
     "Seriez-vous contre une courte vidéo pour vous montrer comment ?", SIG_FR,
     "PS : Débordé par vos clients ? Répondez « non merci » et je ne vous relance pas."]),
   ("", ["Bonjour {{firstName}}, j'imagine que les rendus clients ont pris toute la semaine :)", "Je vous enregistre quand même la vidéo ? Elle dure 3 minutes.", "Nathan"]),
   M3A_FR],
 "S4FR": [("votre recrutement marketing", ["Bonjour {{firstName}},",
     "J'ai vu que {{companyName}} recrute en marketing. Je me suis dit que la personne qui arrive aura besoin de résultats rapidement.",
     "Je peux lui préparer un plan des 90 premiers jours : les 3 actions SEO et IA qui peuvent faire remonter {{companyName}} dans le top 3 sur Google et dans les réponses de ChatGPT.",
     "Ça vous intéresse que je vous l'envoie ?", SIG_FR, PS_CA_FR, "PPS : Pas pertinent ? Répondez « non merci » et je ne vous relance pas."]),
   ("", ["Bonjour {{firstName}}, j'imagine que les entretiens de recrutement prennent toute la place en ce moment :)", "Je vous envoie le plan ? Il peut servir dès le premier jour.", "Nathan"]),
   M3A_FR],
}
SEO_RX = re.compile(r"\bseo\b|search engine|référencement|referencement|digital|numérique|web|growth|acquisition|performance|sea\b|ppc|ads\b", re.I)
NICHE_FALLBACK = {"S1EN": "b2b software", "S2EN": "consulting", "S1FR": "logiciel b2b", "S2FR": "conseil", "S3aFR": "", "S3bFR": "votre secteur", "S4FR": "votre marché"}  # S3bFR : le mail 3 utilise {{niche}}
PLAN = {  # code : (nom, séquence, ps3, sources)
 "201-G": ("SaaS-AI UK-DACH · S1 EN", "S1EN", PS_CA_EN, [("igor", "saas-ai", None)]),
 "202-G": ("Consulting UK-DACH · S2 EN", "S2EN", PS_LEADS_EN, [("igor", "consulting", None)]),
 "203-G": ("SaaS / IA France · S1 FR", "S1FR", PS_CA_FR, [("ours", "1.1", None), ("ours", "1.2", None), ("igor", "bonus-fr", "SaaS / AI (FR)")]),
 "205-G": ("Conseil France · S2 FR · PremiumInboxes", "S2FR", PS_LEADS_FR, [("ours", "1.5", None), ("igor", "bonus-fr", "Consulting (FR)")]),
 "206-G": ("Agences SEO / digitales France · S3a FR · PremiumInboxes", "S3aFR", "", [("ours", "1.9", "seo"), ("igor", "bonus-fr", "Marketing agency (FR)|seo")]),
 "207-G": ("Agences classiques et événementielles France · S3b FR · PremiumInboxes", "S3bFR", PS_CA_FR,
           [("ours", "1.9", "classic"), ("ours", "1.10", None), ("igor", "bonus-fr", "Marketing agency (FR)|classic"), ("igor", "bonus-fr", "Event agency (FR)")]),
}


def html(lines):
    return "".join(f"<div>{l}</div><div><br /></div>" if i < len(lines) - 1 else f"<div>{l}</div>" for i, l in enumerate(x for l in lines for x in [l.replace("\n", "</div><div>")]))


def sequence(code):
    s = SEQ[code]
    return [{"steps": [{"type": "email", "delay": d, "variants": [{"subject": subj, "body": html(body)}]} for (subj, body), d in zip(s, (3, 5, 0))]}]


def blocked():
    lim = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=90)).isoformat()
    b = {h["email"] for h in db.select("contact_history", "email,last_contacted_at,replied,unsubscribed,bounced")
         if h["replied"] or h["unsubscribed"] or h["bounced"] or (h["last_contacted_at"] or "") >= lim}
    dom = {r["domain"].lower() for r in db.select("do_not_contact", "domain,reason") if r["reason"] in ("client", "concurrent", "agressif") and r["domain"]}
    return b, dom


def leads():
    bl, bdom = blocked()
    NICHE = {}
    for f in ("../data/datasets/niche_fr.json", "../data/datasets/niche.json"):  # FR puis EN (dataset Igor)
        if os.path.exists(f): NICHE.update(json.load(open(f)))
    Q = json.load(open("../data/campaigns/qualif.json")); M = json.load(open("../data/datasets/enriched_moltsets.json"))
    F = json.load(open("../data/datasets/enriched_fullenrich.json"))
    seen, out = set(), {}
    for code, (name, seq, ps3, sources) in PLAN.items():
        ls = []
        for kind, key, filt in sources:
            rows = []
            if kind == "igor":
                for r in csv.DictReader(open(f"../data/datasets/igor/ready_{key}.csv")):
                    if r["esp"] != "Google" or r["role_type"] == "Mailbox": continue
                    sub, _, typ = (filt or "").partition("|")
                    if sub and r["sub_industry"] != sub: continue
                    if typ:
                        is_seo = bool(SEO_RX.search(r["company_description"] + " " + r["company_keywords"]))
                        if (typ == "seo") != is_seo: continue
                    rows.append(dict(email=r["email"], first=r["first_name"], last=r["last_name"], company=r["company_name"], domain=r["domain"], city=r["company_city"]))
            else:
                for fn in glob.glob(f"../data/datasets/DS-1*-{key}-FR-*.csv"):
                    for r in csv.DictReader(open(fn)):
                        if r["esp"] != "google" or Q.get(r["domain"], {}).get("fit") is not True: continue
                        if filt:
                            is_seo = bool(SEO_RX.search(r["company"]))
                            if (filt == "seo") != is_seo: continue
                        m = M.get(r["linkedin_url"]) or {}
                        e = m.get("email") if m.get("risk_score") in ("A", "B") else None
                        if not e and (F.get(r["linkedin_url"]) or {}).get("usable"): e = F[r["linkedin_url"]]["email"]
                        if not e: continue
                        ed, cd = e.lower().split("@")[-1], r["domain"].lower()
                        if not (ed == cd or ed.endswith("." + cd) or ed.split(".")[0] == cd.split(".")[0]): continue
                        rows.append(dict(email=e, first=r["first_name"], last=r["last_name"], company=r["company"], domain=r["domain"], city=r.get("city") or ""))
            for r in rows:
                e = (r["email"] or "").lower()
                if not e or e in seen or e in bl or r["domain"].lower() in bdom: continue
                seen.add(e)
                n = ((NICHE.get(r["domain"].lower()) or {}).get("niche") or "").strip().lower()
                cv = dict(niche=n or NICHE_FALLBACK[seq], city=r["city"] or ("votre ville" if seq.endswith("FR") else "your city"), ps3=ps3, campaign=code)
                ls.append(dict(email=r["email"], first_name=r["first"], last_name=r["last"],
                               company_name=re.split(r" \| | - ", r["company"] or "")[0].replace("™", "").strip(), website=r["domain"], custom_variables=cv))
        out[code] = ls
    return out


def api(method, path, body=None):
    r = urllib.request.Request("https://api.instantly.ai" + path, data=json.dumps(body).encode() if body is not None else None, headers=H, method=method)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=120).read() or b"{}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} {e.code} {e.read().decode()[:300]}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "plan"
    L = leads()
    IDS = "../data/campaigns/instantly_v5_ids.json"
    ids = json.load(open(IDS)) if os.path.exists(IDS) else {}
    for code, (name, seq, ps3, _) in PLAN.items():
        ls = L[code]
        fb = sum(1 for l in ls if l["custom_variables"]["niche"] == NICHE_FALLBACK[seq] and NICHE_FALLBACK[seq])
        print(code, name, "·", len(ls), "leads ·", len({l["website"] for l in ls}), "entreprises · niche par défaut", fb)
        if mode == "create" and code not in ids:
            r = api("POST", "/api/v2/campaigns", {"name": f"{code} · {name} · BROUILLON V5", "campaign_schedule": SCHED, "sequences": sequence(seq),
                                                   "stop_on_reply": True, "stop_on_auto_reply": False, "open_tracking": False, "link_tracking": False,
                                                   "text_only": True, "daily_limit": 100, "email_gap": 10, "random_wait_max": 10, "prioritize_new_leads": False})
            ids[code] = r["id"]; json.dump(ids, open(IDS, "w"), indent=1); print("  créée", r["id"])
        if mode == "update" and code in ids:
            api("PATCH", f"/api/v2/campaigns/{ids[code]}", {"sequences": sequence(seq)}); print("  séquence mise à jour")
        if mode == "leads" and code in ids:
            for i in range(0, len(ls), 500):
                api("POST", "/api/v2/leads/add", {"campaign_id": ids[code], "skip_if_in_workspace": False, "leads": ls[i:i + 500]})
            print("  leads importés", len(ls))
