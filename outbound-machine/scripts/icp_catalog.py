"""Catalogue ICP / intentions / lead magnets / séquences : source de vérité versionnée,
chargée dans Supabase (projet « Outreach Cold Mail ») par 31_seed_outreach.py.

Règles (Igor + Nathan) : un sous-ICP = une niche = un message ; effectifs >= 5 ; 3 contacts
max par entreprise ; FR en français, hors FR en anglais (Maghreb, Afrique francophone,
Suisse romande, Belgique : français) ; aucune preuve inventée (preuves = études de cas
publiées sur decupler.com ou banque de preuves validée).
"""

# ---------------------------------------------------------------- pays
# code, nom Lemlist, langue, vague, raison
COUNTRIES = [
    ("FR", "France", "fr", 1, "marché principal"),
    ("BE", "Belgium", "fr", 2, "francophone, proche"),
    ("CH", "Switzerland", "fr", 2, "pouvoir d'achat élevé (Igor : DACH)"),
    ("LU", "Luxembourg", "fr", 2, "pouvoir d'achat élevé"),
    ("MA", "Morocco", "fr", 2, "francophone, peu concurrentiel (Nathan)"),
    ("TN", "Tunisia", "fr", 2, "francophone, tourisme médical (Nathan)"),
    ("CI", "Côte d'Ivoire", "fr", 3, "Afrique francophone la plus solvable"),
    ("SN", "Senegal", "fr", 3, "Afrique francophone solvable"),
    ("UK", "United Kingdom", "en", 2, "pays riche (Igor)"),
    ("IE", "Ireland", "en", 3, "pays riche"),
    ("DE", "Germany", "en", 3, "DACH (Igor) ; idéalement en allemand plus tard"),
    ("AT", "Austria", "en", 3, "DACH (Igor)"),
    ("NL", "Netherlands", "en", 3, "Benelux (Igor)"),
    ("SE", "Sweden", "en", 3, "Nordiques (Igor)"),
    ("NO", "Norway", "en", 3, "Nordiques (Igor)"),
    ("DK", "Denmark", "en", 3, "Nordiques (Igor)"),
    ("FI", "Finland", "en", 3, "Nordiques (Igor)"),
    ("US", "United States", "en", 3, "plus gros marché (Igor, Nathan)"),
    ("AE", "United Arab Emirates", "en", 2, "argent, peu concurrentiel (Nathan)"),
    ("SA", "Saudi Arabia", "en", 2, "argent, déjà testé (Saudi AI)"),
    ("QA", "Qatar", "en", 3, "argent"),
    ("NG", "Nigeria", "en", 3, "Afrique anglophone, gros marché"),
    ("KE", "Kenya", "en", 3, "Afrique de l'Est, tech"),
    ("ZA", "South Africa", "en", 3, "Afrique la plus solvable"),
    ("GH", "Ghana", "en", 3, "Afrique anglophone stable"),
    ("TR", "Turkey", "en", 2, "tourisme médical (greffe, dentaire)"),
    ("HU", "Hungary", "en", 3, "tourisme dentaire"),
]

B2B_COUNTRIES = ["FR", "BE", "CH", "LU", "UK", "DE", "AT", "NL", "SE", "NO", "DK", "FI", "US", "AE", "SA", "MA", "TN"]
LOCAL_FR = ["FR", "BE", "CH", "LU", "MA", "TN"]
LOCAL_ALL = LOCAL_FR + ["UK", "US", "AE"]
MED_COUNTRIES = ["TR", "TN", "MA", "HU", "AE"]

# ---------------------------------------------------------------- preuves (réelles uniquement)
P_TECH = ("Cloudtech : 320 000 clics Google en 12 semaines",
          "Cloudtech: 320,000 Google clicks in 12 weeks")
P_PIPE = ("Le Point, Pluxee, Décathlon : +20 % de pipeline organique",
          "Le Point, Pluxee, Decathlon: +20% organic pipeline")
P_TRAIN = ("Académie Madelrieux : +46 % de clics Google en 3 mois",
           "Académie Madelrieux (training): +46% Google clicks in 3 months")
P_HVAC = ("Clim Confort, installateur de clim : 3,7 fois plus de clics Google en un an",
          "Clim Confort, an HVAC installer: 3.7x more Google clicks in one year")
P_LOCAL = ("L'Artisan d'à côté : +200 nouveaux clients par mois",
           "L'Artisan d'à côté: +200 new clients a month")
P_LEADS = ("BT Blue : +10 % de leads", "BT Blue: +10% leads")

# ---------------------------------------------------------------- sous-ICP
# family : B2B (séquence décideur/champion) ou PERF (partenariat à la performance)
def seg(code, name, kw_fr, kw_en, countries, priority, family, proof, unit=None, pains=None,
        industries=None, seg_fr=None, seg_en=None, notes=None):
    return dict(code=code, icp=int(code.split(".")[0]), name=name, kw_fr=kw_fr, kw_en=kw_en,
                countries=countries, priority=priority, family=family, proof=proof, unit=unit,
                pains=pains or [], industries=industries or [], seg_fr=seg_fr or name.lower(),
                seg_en=seg_en or name, notes=notes)

PAIN_B2B = ["Les acheteurs font leur shortlist sur ChatGPT, Perplexity et Google : des concurrents y sont cités à leur place",
            "Le pipeline dépend du réseau, du bouche-à-oreille ou des Ads de plus en plus chères",
            "Aucune visibilité sur ce que rapporte le SEO en demandes et en CA"]
PAIN_LOCAL = ["Les demandes viennent de plateformes partagées entre plusieurs entreprises, ou du bouche-à-oreille",
              "Un concurrent sort avant eux sur Google Maps et sur ChatGPT dans leur zone",
              "Ont déjà payé une agence sans résultat : refusent de payer d'avance"]
PAIN_MED = ["Dépendent d'intermédiaires (facilitateurs, plateformes) qui prennent une commission par patient",
            "Peu visibles sur Google et ChatGPT dans les pays d'origine des patients (France, UK…)",
            "Concurrence forte entre cliniques sur les mêmes mots-clés"]
PAIN_HOSP = ["Dépendance aux plateformes (Booking, annuaires) et à leurs commissions",
             "Peu de demandes directes depuis Google et les IA",
             "Un établissement concurrent sort en premier dans la zone"]

SEGMENTS = [
    # ---- ICP 1 : B2B services et tech
    seg("1.1", "Éditeurs SaaS B2B", ["logiciel SaaS", "éditeur de logiciel"], ["SaaS", "B2B software"], B2B_COUNTRIES, 1, "B2B", P_TECH,
        pains=PAIN_B2B, industries=["Technology, Information and Internet", "IT Services and IT Consulting"],
        seg_fr="éditeurs SaaS B2B", seg_en="B2B SaaS companies"),
    seg("1.2", "Startups IA et data", ["intelligence artificielle", "IA générative", "data"], ["artificial intelligence", "AI", "machine learning"], B2B_COUNTRIES, 2, "B2B", P_TECH,
        pains=PAIN_B2B, industries=["Technology, Information and Internet"], seg_fr="startups IA", seg_en="AI startups"),
    seg("1.3", "ESN et intégrateurs ERP / CRM", ["ESN", "intégrateur ERP", "intégrateur CRM", "Salesforce", "Odoo", "Sage"], ["IT services", "ERP integrator", "CRM integrator", "Microsoft Dynamics partner"], B2B_COUNTRIES, 1, "B2B", P_TECH,
        pains=PAIN_B2B, industries=["IT Services and IT Consulting"], seg_fr="ESN et intégrateurs", seg_en="IT services firms and ERP/CRM integrators",
        notes="Apogea (intégrateur ERP/CRM) est client : étude de cas publiée, sans chiffre en titre"),
    seg("1.4", "Cybersécurité", ["cybersécurité", "sécurité informatique", "pentest"], ["cybersecurity", "penetration testing", "SOC"], B2B_COUNTRIES, 1, "B2B", P_TECH,
        pains=PAIN_B2B, seg_fr="entreprises de cybersécurité", seg_en="cybersecurity companies"),
    seg("1.5", "Cabinets de conseil en stratégie et management", ["cabinet de conseil", "conseil en stratégie", "conseil en management"], ["management consulting", "strategy consulting"], B2B_COUNTRIES, 1, "B2B", P_PIPE,
        pains=PAIN_B2B, industries=["Business Consulting and Services"], seg_fr="cabinets de conseil", seg_en="consulting firms"),
    seg("1.6", "Conseil financier, DAF externalisé, expertise comptable", ["DAF externalisé", "conseil financier", "expertise comptable"], ["fractional CFO", "financial advisory", "accounting firm"], B2B_COUNTRIES, 2, "B2B", P_PIPE,
        pains=PAIN_B2B, industries=["Accounting", "Financial Services"], seg_fr="cabinets de conseil financier", seg_en="financial advisory firms"),
    seg("1.7", "M&A, fusions-acquisitions, transmission d'entreprise", ["fusions acquisitions", "M&A", "cession d'entreprise", "transmission d'entreprise"], ["M&A advisory", "mergers and acquisitions", "business brokerage"], ["FR", "BE", "CH", "LU"], 1, "B2B", P_PIPE,
        pains=["Les dirigeants qui veulent céder cherchent un conseil sur Google et ChatGPT : d'autres cabinets sont cités",
               "Le deal flow dépend du réseau et des apporteurs",
               "Peu de contenus qui prouvent l'expertise sectorielle"],
        industries=["Financial Services", "Capital Markets", "Business Consulting and Services"], seg_fr="cabinets de M&A", seg_en="M&A advisory firms",
        notes="Demande de Nathan (N23) : France d'abord"),
    seg("1.8", "Gestion de patrimoine (CGP)", ["gestion de patrimoine", "conseiller en gestion de patrimoine", "family office"], ["wealth management", "family office"], ["FR", "BE", "CH", "LU", "MA", "AE"], 2, "B2B", P_PIPE,
        pains=PAIN_B2B, industries=["Financial Services"], seg_fr="cabinets de gestion de patrimoine", seg_en="wealth management firms"),
    seg("1.9", "Agences marketing et web (marque blanche GEO)", ["agence web", "agence marketing digital", "agence SEO", "agence de communication"], ["digital marketing agency", "web agency", "SEO agency"], B2B_COUNTRIES, 2, "B2B", P_TRAIN,
        pains=["Leurs clients demandent « est-ce qu'on sort dans ChatGPT ? » sans réponse outillée",
               "Pas le temps ni l'outillage pour monter une offre GEO",
               "Peur de perdre des clients au profit d'agences « IA »"],
        industries=["Advertising Services", "Marketing Services"], seg_fr="agences marketing", seg_en="marketing agencies",
        notes="Offre marque blanche ; Igor : agences = sous-ICP à part"),
    seg("1.10", "Agences événementielles et de conférenciers", ["agence événementielle", "conférenciers", "séminaire"], ["event agency", "speaker bureau", "corporate events"], B2B_COUNTRIES, 2, "B2B", P_TRAIN,
        pains=PAIN_B2B, industries=["Events Services"], seg_fr="agences événementielles", seg_en="event agencies",
        notes="Orators (agence de conférenciers) : étude de cas GEO publiée"),
    seg("1.11", "Cabinets RH et recrutement", ["cabinet de recrutement", "chasseur de têtes", "conseil RH"], ["recruitment agency", "executive search", "HR consulting"], B2B_COUNTRIES, 3, "B2B", P_PIPE,
        pains=PAIN_B2B, industries=["Staffing and Recruiting"], seg_fr="cabinets de recrutement", seg_en="recruitment firms"),
    seg("1.12", "Organismes de formation professionnelle", ["organisme de formation", "formation professionnelle", "Qualiopi"], ["professional training", "corporate training"], ["FR", "BE", "CH", "LU", "MA", "TN"], 1, "B2B", P_TRAIN,
        pains=["Les inscriptions dépendent des plateformes et du CPF",
               "Des organismes concurrents sortent sur Google et ChatGPT sur leurs thèmes",
               "Peu de contenus qui convertissent les visiteurs en inscrits"],
        industries=["Professional Training and Coaching", "E-Learning Providers"], seg_fr="organismes de formation", seg_en="training companies",
        notes="Preuves : Académie Madelrieux, École Humaniste de Gestalt"),
    seg("1.13", "Cabinets d'avocats d'affaires", ["cabinet d'avocats", "avocat d'affaires"], ["law firm", "business lawyers"], ["FR", "BE", "CH", "LU", "MA", "AE"], 3, "B2B", P_PIPE,
        pains=PAIN_B2B, industries=["Legal Services"], seg_fr="cabinets d'avocats d'affaires", seg_en="business law firms",
        notes="Page « référencement avocat » sur decupler.com ; déontologie : pas de promesse de résultat"),

    # ---- ICP 2 : services locaux, partenariat à la performance
    seg("2.1", "Rénovation et entreprise générale", ["rénovation", "entreprise générale du bâtiment"], ["renovation contractor", "general contractor"], LOCAL_ALL, 2, "PERF", P_LOCAL, unit=("chantiers", "projects"),
        pains=PAIN_LOCAL, industries=["Construction", "Building Construction"], seg_fr="entreprises de rénovation", seg_en="renovation contractors"),
    seg("2.2", "Pompes à chaleur et climatisation", ["pompe à chaleur", "climatisation", "génie climatique"], ["heat pump", "air conditioning", "HVAC"], LOCAL_ALL, 1, "PERF", P_HVAC, unit=("chantiers", "installations"),
        pains=PAIN_LOCAL, industries=["Specialty Trade Contractors", "Construction"], seg_fr="installateurs de pompes à chaleur et de climatisation", seg_en="heat pump and HVAC installers",
        notes="Preuve sectorielle directe : Clim Confort (N28)"),
    seg("2.3", "Panneaux solaires et photovoltaïque", ["photovoltaïque", "panneaux solaires"], ["solar installer", "photovoltaic"], LOCAL_ALL, 1, "PERF", P_HVAC, unit=("chantiers", "installations"),
        pains=PAIN_LOCAL, industries=["Services for Renewable Energy", "Specialty Trade Contractors"], seg_fr="installateurs de panneaux solaires", seg_en="solar installers"),
    seg("2.4", "Rideaux métalliques et fermetures commerciales", ["rideau métallique", "fermeture commerciale"], ["roller shutter", "commercial shutters"], LOCAL_FR, 2, "PERF", P_LOCAL, unit=("clients", "clients"),
        pains=PAIN_LOCAL, seg_fr="entreprises de rideaux métalliques", seg_en="roller shutter companies"),
    seg("2.5", "Monte-escaliers et accessibilité", ["monte-escalier", "monte escalier", "accessibilité PMR"], ["stairlift", "home accessibility"], LOCAL_ALL, 1, "PERF", P_LOCAL, unit=("installations", "installations"),
        pains=PAIN_LOCAL, seg_fr="installateurs de monte-escaliers", seg_en="stairlift companies"),
    seg("2.6", "Pompes funèbres", ["pompes funèbres", "services funéraires"], ["funeral home", "funeral services"], LOCAL_FR, 2, "PERF", P_LOCAL, unit=("familles", "families"),
        pains=["Les familles choisissent en urgence, souvent le premier résultat Google ou ChatGPT",
               "Les contrats obsèques se vendent en ligne chez des acteurs nationaux",
               "Peu de visibilité sur la prévoyance obsèques"],
        seg_fr="entreprises de pompes funèbres", seg_en="funeral homes", notes="Ton sobre, jamais d'humour (tactique 1-2-3 désactivée)"),
    seg("2.7", "Sécurité incendie", ["sécurité incendie", "extincteurs", "désenfumage", "SSI"], ["fire safety", "fire protection"], LOCAL_ALL, 1, "PERF", P_LOCAL, unit=("contrats", "contracts"),
        pains=PAIN_LOCAL, industries=["Security and Investigations", "Facilities Services"], seg_fr="entreprises de sécurité incendie", seg_en="fire safety companies"),
    seg("2.8", "Menuiseries, fenêtres et vérandas", ["menuiserie", "fenêtres", "véranda"], ["windows and doors", "conservatory"], LOCAL_ALL, 2, "PERF", P_LOCAL, unit=("chantiers", "projects"),
        pains=PAIN_LOCAL, seg_fr="menuisiers et installateurs de fenêtres", seg_en="window and door installers"),
    seg("2.9", "Toiture, couverture et isolation", ["couverture", "toiture", "isolation"], ["roofing", "insulation"], LOCAL_ALL, 2, "PERF", P_LOCAL, unit=("chantiers", "projects"),
        pains=PAIN_LOCAL, seg_fr="couvreurs et entreprises d'isolation", seg_en="roofing and insulation companies"),
    seg("2.10", "Piscines et spas (installateurs)", ["piscine", "pisciniste"], ["swimming pool builder"], LOCAL_ALL, 2, "PERF", P_LOCAL, unit=("chantiers", "projects"),
        pains=PAIN_LOCAL, seg_fr="piscinistes", seg_en="pool builders"),
    seg("2.11", "Alarme et vidéosurveillance", ["alarme", "vidéosurveillance", "contrôle d'accès"], ["security systems", "CCTV"], LOCAL_ALL, 2, "PERF", P_LOCAL, unit=("contrats", "contracts"),
        pains=PAIN_LOCAL, industries=["Security and Investigations"], seg_fr="installateurs d'alarmes et de vidéosurveillance", seg_en="security system installers"),
    seg("2.12", "Cuisinistes", ["cuisiniste", "cuisines sur mesure"], ["kitchen design", "kitchen fitter"], LOCAL_ALL, 3, "PERF", P_LOCAL, unit=("projets", "projects"),
        pains=PAIN_LOCAL, seg_fr="cuisinistes", seg_en="kitchen companies"),
    seg("2.13", "Déménagement", ["déménagement", "déménageur"], ["removals", "moving company"], LOCAL_ALL, 3, "PERF", P_LOCAL, unit=("déménagements", "moves"),
        pains=PAIN_LOCAL, seg_fr="entreprises de déménagement", seg_en="moving companies"),
    seg("2.14", "Paysagistes", ["paysagiste", "aménagement extérieur"], ["landscaping"], LOCAL_FR, 3, "PERF", P_LOCAL, unit=("chantiers", "projects"),
        pains=PAIN_LOCAL, seg_fr="paysagistes", seg_en="landscapers"),

    # ---- ICP 3 : santé, tourisme médical
    seg("3.1", "Greffe de cheveux (patients internationaux)", ["greffe de cheveux", "implant capillaire"], ["hair transplant", "FUE"], MED_COUNTRIES, 1, "PERF", None, unit=("patients internationaux", "international patients"),
        pains=PAIN_MED, industries=["Medical Practices", "Hospitals and Health Care"], seg_fr="cliniques de greffe de cheveux", seg_en="hair transplant clinics",
        notes="Aucune étude de cas santé : preuve transversale ou aucune"),
    seg("3.2", "Implants dentaires et facettes (tourisme dentaire)", ["implants dentaires", "facettes dentaires", "clinique dentaire"], ["dental implants", "dental veneers", "dental clinic"], MED_COUNTRIES, 1, "PERF", None, unit=("patients internationaux", "international patients"),
        pains=PAIN_MED, industries=["Medical Practices", "Hospitals and Health Care"], seg_fr="cliniques dentaires", seg_en="dental clinics"),
    seg("3.3", "Chirurgie et médecine esthétique (tourisme médical)", ["chirurgie esthétique", "médecine esthétique"], ["cosmetic surgery", "aesthetic clinic"], MED_COUNTRIES, 2, "PERF", None, unit=("patients internationaux", "international patients"),
        pains=PAIN_MED, industries=["Medical Practices", "Hospitals and Health Care"], seg_fr="cliniques esthétiques", seg_en="cosmetic surgery clinics"),
    seg("3.4", "Chirurgie bariatrique", ["chirurgie bariatrique", "sleeve"], ["bariatric surgery", "gastric sleeve"], MED_COUNTRIES, 3, "PERF", None, unit=("patients internationaux", "international patients"),
        pains=PAIN_MED, seg_fr="cliniques de chirurgie bariatrique", seg_en="bariatric surgery clinics"),

    # ---- ICP 4 : hôtellerie, bien-être, seniors
    seg("4.1", "Hôtels indépendants", ["hôtel", "boutique hôtel"], ["boutique hotel", "independent hotel"], LOCAL_ALL, 2, "PERF", None, unit=("réservations directes", "direct bookings"),
        pains=PAIN_HOSP, industries=["Hospitality", "Accommodation Services"], seg_fr="hôtels indépendants", seg_en="independent hotels",
        notes="Observé : 2 « oui envoyez » sur 245 envois (Kerbot, Carnac Lodge)"),
    seg("4.2", "Spas et centres de bien-être", ["spa", "centre de bien-être", "institut de beauté"], ["day spa", "wellness centre"], LOCAL_ALL, 2, "PERF", None, unit=("clients", "clients"),
        pains=PAIN_HOSP, industries=["Personal and Laundry Services", "Wellness and Fitness Services"], seg_fr="spas et centres de bien-être", seg_en="spas and wellness centres"),
    seg("4.3", "Maisons de retraite et résidences seniors privées", ["maison de retraite", "résidence seniors", "EHPAD privé"], ["care home", "senior living", "retirement home"], LOCAL_ALL, 1, "PERF", None, unit=("résidents", "residents"),
        pains=["Les familles cherchent en urgence sur Google et ChatGPT, et appellent les premiers résultats",
               "Taux d'occupation sous pression, places vacantes coûteuses",
               "Dépendance aux plateformes d'orientation qui facturent chaque admission"],
        industries=["Nursing Homes and Residential Care Facilities"], seg_fr="résidences seniors", seg_en="care homes"),
    seg("4.4", "Campings et résidences de tourisme haut de gamme", ["camping", "résidence de tourisme", "glamping"], ["holiday park", "glamping"], LOCAL_FR, 3, "PERF", None, unit=("réservations directes", "direct bookings"),
        pains=PAIN_HOSP, industries=["Accommodation Services", "Recreational Facilities"], seg_fr="campings et résidences de tourisme", seg_en="holiday parks"),
]

# ---------------------------------------------------------------- personas (3 contacts max)
PERSONAS = {
    "B2B": [("decideur", 1, ["CEO", "Founder", "Co-founder", "Fondateur", "Président", "Directeur général", "Managing Partner", "Gérant"], "pipeline, croissance, coût d'acquisition"),
            ("decideur", 2, ["CMO", "Head of Marketing", "Directeur marketing", "Head of Growth", "Responsable growth", "Sales Director", "Directeur commercial"], "demandes entrantes, part de voix face aux concurrents"),
            ("champion", 3, ["SEO Manager", "Responsable SEO", "Content Manager", "Responsable communication", "Marketing Manager", "Responsable acquisition"], "feuille de route qui le fait briller auprès du décideur")],
    "PERF": [("decideur", 1, ["Gérant", "Owner", "Founder", "Fondateur", "CEO", "Directeur général", "Président"], "plus de clients sans payer d'avance"),
             ("decideur", 2, ["Directeur commercial", "Sales Director", "Responsable commercial"], "volume de demandes qualifiées"),
             ("champion", 3, ["Responsable marketing", "Marketing Manager", "Responsable communication", "Patient Coordinator Manager", "International Patient Manager"], "visibilité, demandes entrantes")],
}

# ---------------------------------------------------------------- intentions (pyramide)
# code, nom, description, comment détecter, outil, coût estimé $/entreprise (None = à mesurer), palier
INTENTS = [
    ("I1", "A levé des fonds (< 6 mois)", "Croissance financée, budgets marketing ouverts", "filtre Lemlist currentCompanyLastFundingRoundAt", "Lemlist DB (recherche gratuite)", 0, 1),
    ("I2", "Recrute en marketing / SEO / growth / contenu", "Objectifs de croissance ; Décupler = une fraction du coût d'un recrutement", "filtres Lemlist jobPostingTitle + jobPostingDate (90 j) ; Apify LinkedIn Jobs en complément", "Lemlist DB / Apify", 0, 1),
    ("I3", "Recrute des commerciaux", "Pipeline à remplir", "jobPostingTitle « commercial / sales / business developer »", "Lemlist DB", 0, 2),
    ("I4", "Nouveau CMO / head of growth (< 6 mois)", "Nouveau décideur qui veut des résultats rapides", "filtre Lemlist currentPositionTenure « Less than 6 months » + titre", "Lemlist DB", 0, 2),
    ("I5", "Équipe marketing en croissance (+10 % sur 6 mois)", "Investit dans l'acquisition", "filtre Lemlist workforceGrowthMarketing", "Lemlist DB", 0, 2),
    ("I6", "Concurrent classé au-dessus sur le mot-clé principal", "Hack Igor : le nom du concurrent en variable (objet + corps)", "API SERP sur le mot-clé « service + ville » ou « catégorie »", "API SERP (voir 26_comparatif_outils.md)", None, 2),
    ("I7", "Absent des réponses ChatGPT sur sa catégorie", "La shortlist IA cite des concurrents", "10 questions de la catégorie posées à un modèle OpenAI, on relève les marques citées", "API OpenAI (clé disponible)", None, 2),
    ("I8", "Baisse de trafic organique (> 10 % sur 12 mois)", "Douleur visible, budget à réallouer", "historique de trafic estimé par domaine ; on ne garde que les baisses > 10 %", "DataForSEO Labs ou équivalent", None, 2),
    ("I9", "Paie des Ads Google", "« les Ads coûtent cher » (VoC) → l'organique moins cher à long terme", "technologie Google Ads détectée (filtre Lemlist currentCompanyTechnologies)", "Lemlist DB", 0, 2),
    ("I10", "Site faible : lent, pas de données structurées, pas de réponse directe", "Problème réel et vérifiable (méthode Swokei)", "PageSpeed API (clé disponible) + lecture du balisage", "Google PageSpeed (gratuit)", 0, 3),
    ("I11", "Fiche Google faible (avis, catégories) : local", "Pack local perdu", "données Google Maps (note, nb d'avis)", "Outscraper", None, 2),
    ("I12", "Saison (clim avant l'été, PAC et isolation avant l'hiver)", "Remplir le planning avant la saison", "calendrier, gratuit", "aucun", 0, 3),
    ("I13", "Aucun signal (marché principal)", "Volume : pain du métier + observation vraie ; filtre par lead magnet et formulaire", "industrie + effectifs + pays", "Lemlist DB", 0, 3),
]

# ---------------------------------------------------------------- lead magnets (en deux temps : mail / appel)
LEAD_MAGNETS = [
    ("LM1", "Les 10 questions ChatGPT où un concurrent est cité à votre place", "eleve", "≈ 1 cent d'API par entreprise + 10 min de Claude pour la version complète", "contre_appel",
     "1 question + le concurrent cité, dans le mail", "les 9 autres + ce qui fait citer le concurrent, en 15 min", 1, "1.x"),
    ("LM2", "7 actions rapides GEO / SEO", "eleve", "≈ 1 h de Claude par prospect", "contre_appel",
     "1 action concrète, donnée gratuitement dans le mail 3", "les 6 autres, adaptées à leurs priorités, en appel (« j'ai besoin de vos priorités pour bien les faire »)", 3, "1.x, 2.x"),
    ("LM3", "Extrait de l'Opportunity Map (3 lignes)", "eleve", "≈ 30 min (Scalezia : montrer 3 lignes, vendre 200)", "contre_appel",
     "1 ligne : requête, concurrent cité, manque à gagner estimé", "les 2 autres lignes + la méthode, en appel", 1, "1.x"),
    ("LM4", "Top 10 mots-clés qui font perdre des demandes", "moyen", "≈ 5 cents d'API + 10 min", "contre_appel",
     "1 mot-clé + son volume + le concurrent devant", "la liste des 10 + la page à créer pour chacun", 1, "1.x champion"),
    ("LM5", "« {{concurrent}} est devant vous sur {{mot-clé}} »", "faible", "1 requête SERP par entreprise", "avant_appel",
     "le nom du concurrent + le mot-clé (objet + corps)", "comment le dépasser, en appel", 1, "tous"),
    ("LM6", "Vidéo de 3 min : site, fiche Google, avis", "moyen", "≈ 10 min par vidéo (Loom / Tella)", "avant_appel",
     "envoyée après le « oui » : les problèmes, sans la solution", "la solution et le plan, en appel", 2, "2.x, 3.x, 4.x"),
    ("LM7", "Une page rendue « GEO ready », offerte", "eleve", "≈ 1 h", "contre_appel",
     "le diagnostic de la page en 2 lignes", "la page réécrite, livrée après un appel de cadrage", 3, "1.x"),
    ("LM8", "Note du site sur 10 (Swokei)", "faible", "automatisable (PageSpeed + balisage)", "avant_appel",
     "la note + le point qui coûte le plus de clients", "le détail des 5 critères, en appel", 2, "tous"),
    ("LM9", "Outil gratuit d'audit GEO (app Décupler)", "faible", "0 (outil existant)", "avant_appel",
     "envoyé sur demande (« répondez outil »), jamais de lien au 1er mail", "lecture des résultats ensemble", 5, "tous"),
    ("LM10", "Plugin / setup Claude Code SEO", "moyen", "temps d'installation", "apres_appel",
     "rien", "proposé après l'appel aux petites structures à l'aise avec Claude (pas aux grands comptes)", None, "1.x petites structures"),
    ("LM11", "Estimation des demandes perdues à {{ville}}", "moyen", "≈ 5 cents d'API + 10 min", "contre_appel",
     "le volume de recherches mensuelles du service dans la zone", "l'estimation complète + le plan, en appel", 1, "2.x"),
    ("LM12", "Roadmap de kick-off client, version 5/10 (Igor)", "eleve", "≈ 5 min d'agent, effet « wow »", "contre_appel",
     "rien (uniquement pour ceux qui disent oui)", "présentée en appel", None, "tous"),
    ("LM13", "Étude de cas A+B avant / après", "faible", "0 (pages publiées sur decupler.com)", "avant_appel",
     "le chiffre clé dans le PS", "le détail sur demande", 5, "tous"),
]
