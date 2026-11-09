"""Brouillons Instantly de la vague 1 avec les séquences V5 (doc « Séquences V5 », 06/11) : 3 mails, 2 fils
(J0 · J+3 même fil · J+8 nouveau fil), envoi 7h30-14h en semaine, opt-out au 1er mail de chaque fil.
Leads : dataset UltB d'Igor (lot G) + nos leads FR (Moltsets A/B ou FullEnrich utilisable), liste noire par personne
(contact_history : < 90 jours, réponse, désinscrit, bounce), Microsoft exclu, un email = une seule campagne.
Rien n'est lancé : aucune boîte rattachée (Zapmail se rattache au lancement ; AirMail pour les lots O quand il sera chauffé ; PremiumInboxes abandonné le 09/11).
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
 "204-G": ("Recrute en marketing ou commercial France · S4 FR", "S4FR", PS_LEADS_FR, [("tier", "P2", None)]),
 "203-G": ("SaaS / IA France · S1 FR", "S1FR", PS_CA_FR, [("ours", "1.1", None), ("ours", "1.2", None), ("igor", "bonus-fr", "SaaS / AI (FR)")]),
 "205-G": ("Conseil, compta, M&A, patrimoine France · S2 FR", "S2FR", PS_LEADS_FR, [("ours", "1.5", None), ("ours", "1.6", None), ("ours", "1.7", None), ("ours", "1.8", None), ("igor", "bonus-fr", "Consulting (FR)")]),
 "206-G": ("Agences SEO / digitales France · S3a FR", "S3aFR", "", [("ours", "1.9", "seo"), ("igor", "bonus-fr", "Marketing agency (FR)|seo")]),
 "207-G": ("Agences classiques et événementielles France · S3b FR", "S3bFR", PS_CA_FR,
           [("ours", "1.9", "classic"), ("ours", "1.10", None), ("igor", "bonus-fr", "Marketing agency (FR)|classic"), ("igor", "bonus-fr", "Event agency (FR)")]),
}

# ===== V6 (06/11, retours Nathan + vérifications par entreprise, 68_lead_checks.py) =====
# Les phrases « {{companyName}} ne sort pas sur les questions que j'ai testées », « j'ai trouvé 3 quick wins » et
# « plusieurs opportunités organiques ne sont pas adressées » ne partent que si la vérification le confirme pour CE lead ;
# sinon la version neutre. Le mail 3 B (concurrent) part aux leads dont le concurrent est trouvé dans Google, le A aux autres.
PAGE_EN = ["Hi {{firstName}}, simpler idea: send me one page of your site, and I'll send it back optimised to get cited by ChatGPT and Google.",
           "It's free, and you keep it either way. Which page would you pick?", "Nathan"]
PAGE_FR = ["Bonjour {{firstName}}, plus simple : envoyez-moi une page de votre site, je vous la renvoie travaillée pour être citée par ChatGPT et Google.",
           "C'est offert, et vous la gardez dans tous les cas. Laquelle choisiriez-vous ?", "Nathan"]
for k, lang in (("S1EN", "EN"), ("S2EN", "EN"), ("S1FR", "FR"), ("S2FR", "FR")):
    signature, ps1 = (SIG_EN, SEQ[k][0][1][-1]) if lang == "EN" else (SIG_FR, SEQ[k][0][1][-1])
    cta = "Would you be against a quick video showing you how to get more leads from AI search?" if lang == "EN" else \
          "Seriez-vous contre une courte vidéo pour vous montrer comment être recommandé par les IA ?"
    hi = "Hi {{firstName}}," if lang == "EN" else "Bonjour {{firstName}},"
    SEQ[k] = [(SEQ[k][0][0], [hi, "{{l1}}", "{{l2}}", cta, signature, ps1]),
              ("", PAGE_EN if lang == "EN" else PAGE_FR),
              ("{{m3s}}", [hi, "{{m3a}}", "{{m3b}}", "{{m3c}}", signature, "{{ps3}}",
                           "PPS: Not a priority? Reply \"no thanks\" and I'll close the file." if lang == "EN" else "PPS : Pas prioritaire ? Répondez « non merci » et je clos le dossier."])]
SEQ["S3bFR"][1] = ("", PAGE_FR)
SEQ["S3bFR"][2] = SEQ["S1FR"][2]
SEQ["S4FR"][2] = SEQ["S1FR"][2]
SEQ["S2FR"][0] = ("{{niche}} sur chatgpt", SEQ["S2FR"][0][1])
CHECKS = json.load(open("../data/datasets/lead_checks.json")) if os.path.exists("../data/datasets/lead_checks.json") else {}


ACRO = {"ai": "AI", "ia": "IA", "seo": "SEO", "geo": "GEO", "crm": "CRM", "erp": "ERP", "b2b": "B2B", "b2c": "B2C", "saas": "SaaS", "it": "IT",
        "hr": "HR", "rh": "RH", "grc": "GRC", "voip": "VoIP", "d2c": "D2C", "pr": "PR", "ux": "UX", "ui": "UI", "api": "API", "smes": "SMEs",
        "pme": "PME", "tpe": "TPE", "esg": "ESG", "rse": "RSE", "m&a": "M&A", "cfo": "CFO", "daf": "DAF", "ppc": "PPC", "sea": "SEA", "iot": "IoT"}


def nice(n):
    return " ".join(ACRO.get(w, w) for w in (n or "").split())


def que(x):  # « que IOWNIT » → « qu'IOWNIT »
    return "qu'" if (x or "a")[0].lower() in "aeiouyhéèêàâîôûœ" else "que "


def de(x):  # « cabinets de conseil », « cabinets d'expertise comptable »
    return "d'" if (x or "a")[0].lower() in "aeiouyhéèêàâîôûœ" else "de "


def personal(seq, company, niche, d):
    niche = nice(niche)
    c = CHECKS.get(d) or {}
    absent = c.get("ai_tested") and not c.get("ai_cited")
    wins = len(c.get("audit") or []) >= 3
    out_g = c.get("serp_ok") and not c.get("serp_pos")
    comp = c.get("competitor")
    if seq in ("S1EN", "S2EN"):
        what = f"the best {niche}" if seq == "S1EN" else f"the best {niche} firms"
        l1 = (f"I was looking at what ChatGPT recommends for {what}, and {company} didn't come up in the answers I tested." if absent
              else f"I was looking at what ChatGPT recommends for {what}.")
        l2 = (f"I found 3 quick wins that would help {company} get recommended more often in AI answers, the same kind of fixes that brought Cloudtech +23% visibility."
              if wins else f"I can show you 3 quick wins that would help {company} get recommended more often in AI answers, the same kind of fixes that brought Cloudtech +23% visibility.")
        if comp:
            m3 = (f"{comp} instead of {company}", f"I searched for \u201c{niche}\u201d on Google, and {comp} came up first, not {company}.",
                  f"I thought you might want to change that. I can put together a quick checklist on how to get {company} ahead, on Google and in ChatGPT.",
                  "Would you be against a 3-minute video walking you through it?")
        else:
            m3 = (f"{company}'s organic opportunities",
                  (f"I was looking at your site and noticed several organic opportunities {company} isn't covering yet." if out_g
                   else f"I was looking at your site and the organic opportunities around {niche}."),
                  "I can put them in a map: keywords with buying intent, AI prompts and the real competitors capturing them, so search turns into sales opportunities.",
                  "Can I record a 3-minute video showing how to get more of those opportunities?")
    else:
        what = f"le meilleur {niche}" if seq != "S2FR" else f"les meilleurs cabinets {de(niche)}{niche}"
        l1 = (f"Je regardais ce qui sort quand on demande à ChatGPT {what}, et j'ai remarqué {que(company)}{company} ne sort pas sur les questions que j'ai testées." if absent
              else f"Je regardais ce qui sort quand on demande à ChatGPT {what}.")
        l2 = (f"J'ai trouvé 3 quick wins pour {que(company)}{company} soit plus recommandé dans les réponses des IA, le même type d'actions qui a apporté à Cloudtech +23 % de visibilité."
              if wins else f"Je peux vous montrer 3 quick wins pour {que(company)}{company} soit plus recommandé dans les réponses des IA, le même type d'actions qui a apporté à Cloudtech +23 % de visibilité.")
        if comp:
            m3 = (f"{comp} plutôt {que(company)}{company}", f"J'ai tapé « {niche} » sur Google, et c'est {comp} qui est sorti en premier, pas {company}.",
                  f"Je me suis dit que vous voudriez peut-être changer ça. Je peux vous préparer une courte checklist pour faire passer {company} devant, sur Google et dans ChatGPT.",
                  "Seriez-vous contre une vidéo de 3 minutes pour vous la présenter ?")
        else:
            m3 = (f"les opportunités organiques de {company}",
                  (f"Je regardais votre site et j'ai vu que plusieurs opportunités organiques ne sont pas encore adressées par {company}." if out_g
                   else f"Je regardais votre site et les opportunités organiques autour de {niche}."),
                  "Je peux vous les sortir dans une cartographie : mots-clés à intention d'achat, questions posées aux IA, vrais concurrents qui les captent, pour transformer la recherche en opportunités commerciales.",
                  "Je vous enregistre une vidéo de 3 minutes pour vous montrer comment capter plus d'opportunités organiques ?")
    return dict(l1=l1, l2=l2, m3s=m3[0], m3a=m3[1], m3b=m3[2], m3c=m3[3], m3_variant="B" if comp else "A",
                checked=bool(c), ai_absent=bool(absent), quick_wins=len(c.get("audit") or []))



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
                for fn in glob.glob("../data/datasets/DS-1*-FR-*.csv"):
                    if kind == "tier" and not re.search(r"-FR-P2b?\.csv$", fn): continue
                    for r in csv.DictReader(open(fn)):
                        # sous-ICP effectif : celui du repêchage (67_requalify.py) s'il existe, sinon celui du dataset
                        if kind == "ours" and (Q.get(r["domain"], {}).get("sub_icp_final") or r["icp_code"]) != key: continue
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
                cv = dict(niche=nice(n) if n else NICHE_FALLBACK[seq], city=r["city"] or ("votre ville" if seq.endswith("FR") else "your city"), ps3=ps3, campaign=code)
                cname = re.split(r" \| | - ", r["company"] or "")[0].replace("™", "").strip()
                if seq in ("S1EN", "S2EN", "S1FR", "S2FR", "S3bFR", "S4FR"): cv.update(personal(seq, cname, cv["niche"], r["domain"].lower()))
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
            r = api("POST", "/api/v2/campaigns", {"name": f"{code} · {name} · BROUILLON V6", "campaign_schedule": SCHED, "sequences": sequence(seq),
                                                   "stop_on_reply": True, "stop_on_auto_reply": False, "open_tracking": False, "link_tracking": False,
                                                   "text_only": True, "daily_limit": 100, "email_gap": 10, "random_wait_max": 10, "prioritize_new_leads": False})
            ids[code] = r["id"]; json.dump(ids, open(IDS, "w"), indent=1); print("  créée", r["id"])
        if mode == "rebuild" and code in ids and (len(sys.argv) < 3 or code in sys.argv[2:]):
            c = api("GET", f"/api/v2/campaigns/{ids[code]}")
            if c.get("status") != 0: print("  pas un brouillon, on ne touche pas"); continue
            api("DELETE", f"/api/v2/campaigns/{ids[code]}", {})
            r = api("POST", "/api/v2/campaigns", {"name": f"{code} · {name} · BROUILLON V6", "campaign_schedule": SCHED, "sequences": sequence(seq),
                                                   "stop_on_reply": True, "stop_on_auto_reply": False, "open_tracking": False, "link_tracking": False,
                                                   "text_only": True, "daily_limit": 100, "email_gap": 10, "random_wait_max": 10, "prioritize_new_leads": False})
            ids[code] = r["id"]; json.dump(ids, open(IDS, "w"), indent=1)
            for i in range(0, len(ls), 500):
                api("POST", "/api/v2/leads/add", {"campaign_id": ids[code], "skip_if_in_workspace": False, "leads": ls[i:i + 500]})
            print("  reconstruite", len(ls), "leads")
        if mode == "update" and code in ids:
            api("PATCH", f"/api/v2/campaigns/{ids[code]}", {"sequences": sequence(seq)}); print("  séquence mise à jour")
        if mode == "leads" and code in ids:
            for i in range(0, len(ls), 500):
                api("POST", "/api/v2/leads/add", {"campaign_id": ids[code], "skip_if_in_workspace": False, "leads": ls[i:i + 500]})
            print("  leads importés", len(ls))
