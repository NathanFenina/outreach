"""Copies V2 (29/10) : un mail 1 par sous-ICP et par palier de la pyramide, suites par famille.
Pyramide : P1 a levé + recrute · P2 recrute · P3 intent SEO (P3a baisse de trafic, P3b concurrent devant sur Google,
P3c concurrent cité par ChatGPT) · P4 marché principal. Local / hôtellerie : P1 concurrent devant (Maps), P2 saison,
P3 ChatGPT, P4 marché principal.
Règles : Igor (R.E.P.L.Y. / AAA, 80 mots, objet < 5 mots « camouflage interne », CTA d'intérêt orienté « non », aucun lien,
PS = preuve ou inversion du risque, PPS = sortie), commentaires de Nathan sur les copies V1 (onglet 6), copies d'Igor
et d'Elena (UltB). Chiffres : uniquement ceux sourcés dans copy/31 et copy/32, ou fournis par Nathan.
Variables : {{firstName}} {{companyName}} {{ville}} {{zone}} {{poste}} {{concurrent}} {{prompt}} {{motcle}} {{volume}}
{{baisse}} {{preuve20}} (client réel à +20 nouveaux clients / mois : nom à fournir par Nathan)."""

SIGN = "Nathan Fenina, Décupler"
OUT = "PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille."
OUT_SOBER = "PPS : si ce n'est pas le sujet, répondez simplement « non merci »."

# ---------------------------------------------------------------- B2B (1.x) : contenu propre à chaque sous-ICP
# pb = le problème dans les mots du métier (1-2 phrases, sourcé ou vérifiable) ; preuve = PS ; p4 = mail 1 marché principal
B2B = {
 "1.1": dict(label="éditeurs SaaS", preuve="Cloudtech : 320 000 clics Google en 12 semaines",
    pb="La moitié des acheteurs de logiciels commencent maintenant leur recherche dans un chatbot plutôt que sur Google (G2, 2026).",
    p4=("shortlist", "{{firstName}}, quand un acheteur demande à ChatGPT « {{prompt}} », c'est là que se joue la shortlist, avant même votre site.\n\nUn sur trois finit par acheter à un éditeur qu'il ne connaissait pas (G2, 2026). Autrement dit, la place est encore à prendre.\n\nSeriez-vous contre que je vous montre sur quelles questions de votre catégorie {{companyName}} est absent ?")),
 "1.2": dict(label="startups IA", preuve="Cloudtech : 320 000 clics Google en 12 semaines",
    pb="On compte plus de 1 100 startups IA en France (France Digitale 2026) : se faire citer devient plus dur que lever.",
    p4=("1 100 startups IA", "{{firstName}}, il y a aujourd'hui plus de 1 100 startups IA en France (France Digitale). Quand un client demande à ChatGPT un outil pour « {{prompt}} », il en cite trois. Rarement les plus jeunes.\n\nLa différence ne se joue pas sur le produit mais sur ce que les IA savent de vous : cas d'usage, preuves, entités.\n\nÇa vaut 15 minutes pour voir où en est {{companyName}} ?")),
 "1.3": dict(label="ESN et intégrateurs", preuve="Cloudtech : 320 000 clics Google en 12 semaines",
    pb="Les demandes viennent du réseau et des appels d'offres ; sur « intégrateur + éditeur + ville », ce sont les partenaires les mieux référencés qui reçoivent les contacts.",
    p4=("{{motcle}}", "{{firstName}}, « {{motcle}} » est cherché environ {{volume}} fois par mois, et c'est {{concurrent}} qui récupère ces demandes.\n\nPour une ESN, c'est souvent le seul contact entrant qui n'est ni un appel d'offres ni une recommandation.\n\nSeriez-vous contre que je vous montre ce qui le place devant {{companyName}} ?")),
 "1.4": dict(label="sociétés de cybersécurité", preuve="Cloudtech : 320 000 clics Google en 12 semaines",
    pb="Un RSSI vérifie toujours avant d'appeler : sur Google, et de plus en plus dans ChatGPT. Ce sont les plus gros acteurs qui y sont cités.",
    p4=("audit de sécurité", "{{firstName}}, avant de contacter un prestataire pour un audit ou un pentest, un RSSI se renseigne seul, sur Google et de plus en plus dans ChatGPT.\n\nSur « {{prompt}} », la réponse cite {{concurrent}}. Pas {{companyName}}.\n\nÇa vaut 15 minutes pour voir les questions où vous pourriez être la référence citée ?")),
 "1.5": dict(label="cabinets de conseil", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="Les IA citent McKinsey, BCG et Bain ; les petits cabinets ne remontent que sur les questions de niche (test Consultor, juin 2026).",
    p4=("Big Four", "{{firstName}}, quand un dirigeant demande à ChatGPT un cabinet pour « {{prompt}} », il cite d'abord les grands noms. Sur les questions de niche, en revanche, les petits cabinets passent devant (test Consultor, 2026).\n\nC'est là que se fait votre shortlist, souvent un an avant le premier appel.\n\nSeriez-vous contre que je vous montre les 10 questions de votre spécialité, et qui y est cité ?")),
 "1.6": dict(label="cabinets d'expertise comptable", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="Depuis le 1er septembre 2026, la réception des factures électroniques est obligatoire : les dirigeants cherchent un cabinet qui les accompagne.",
    p4=("facture électronique", "{{firstName}}, depuis le 1er septembre, les dirigeants cherchent un cabinet qui les accompagne sur la facture électronique.\n\nSur « expert-comptable {{ville}} », c'est {{concurrent}} ou un cabinet en ligne qui sort, pas {{companyName}}.\n\nSeriez-vous contre que je vous montre ce qui leur donne cette place ?"), sober=True),
 "1.7": dict(label="conseils en M&A et transmission", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="7 cédants sur 10 dont le projet est à plus d'un an se renseignent seuls (Bpifrance Le Lab) : ils tombent sur les simulateurs et les plateformes d'annonces.",
    p4=("vos futurs cédants", "{{firstName}}, 7 dirigeants sur 10 qui pensent à céder dans plus d'un an se renseignent encore seuls (Bpifrance Le Lab).\n\nIls posent leurs questions à Google et à ChatGPT, et tombent sur les simulateurs de valorisation et les plateformes d'annonces, rarement sur un conseil comme {{companyName}}.\n\nSeriez-vous contre que je vous montre ces questions, et qui y répond aujourd'hui ?")),
 "1.8": dict(label="cabinets de gestion de patrimoine", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="44 % des épargnants décident seuls, et près d'un jeune sur cinq consulte une IA avant de placer (AMF 2025) ; le démarchage sans consentement est interdit depuis le 11 août 2026.",
    p4=("vos futurs clients", "{{firstName}}, depuis le 11 août, plus d'appel sans consentement préalable. Et 44 % des épargnants décident déjà seuls (AMF).\n\nQuand on demande à ChatGPT « {{prompt}} », il cite {{concurrent}}, pas {{companyName}}.\n\nSeriez-vous contre que je vous montre pourquoi ?"), sober=True),
 "1.9": dict(label="agences", preuve="nos clients en marque blanche gardent la relation et la marge",
    pb="Leurs clients demandent « et ChatGPT ? » ; peu d'agences ont une réponse technique.",
    p4=("vos clients et ChatGPT", "{{firstName}}, question directe : quand un client vous demande s'il ressort dans ChatGPT, vous refusez, vous sous-traitez ou vous gérez en interne ?\n\nOn produit le GEO en marque blanche pour quelques agences : vous gardez le client et la marge, on exécute.\n\nSeriez-vous contre que je fasse l'audit GEO d'un de vos clients, sous votre marque, pour que vous jugiez sur pièce ?")),
 "1.10": dict(label="agences événementielles et de conférenciers", preuve="Académie Madelrieux : +46 % de clics Google en 3 mois",
    pb="Les entreprises cherchent un lieu ou un conférencier sur Google et ChatGPT, et ce sont les plateformes qui captent la demande.",
    p4=("séminaire {{ville}}", "{{firstName}}, quand une entreprise cherche « {{motcle}} », ce sont les plateformes et {{concurrent}} qui récupèrent la demande.\n\nUn devis événementiel qui arrive en direct, c'est une commission en moins et un client à vous.\n\nÇa vaut 15 minutes pour voir ce qui vous manque pour être choisi en direct ?")),
 "1.11": dict(label="cabinets de recrutement", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="Les mandats viennent du réseau et de LinkedIn ; les DRH qui cherchent un cabinet par métier tombent sur les jobboards et les gros réseaux.",
    p4=("cabinet {{motcle}}", "{{firstName}}, quand une DRH cherche « {{motcle}} », elle tombe sur les jobboards et sur {{concurrent}}, rarement sur un cabinet spécialisé comme {{companyName}}.\n\nC'est pourtant exactement la demande que vous voulez : un mandat qui arrive sans prospection.\n\nSeriez-vous contre que je vous montre comment la capter ?")),
 "1.12": dict(label="organismes de formation", preuve="Académie Madelrieux : +46 % de clics Google en 3 mois",
    pb="Les inscriptions dépendent des financeurs et des plateformes ; sur « formation + métier », les gros organismes prennent la place.",
    p4=("vos inscriptions", "{{firstName}}, sur « {{motcle}} », ce sont les gros organismes et les plateformes qui récupèrent les inscriptions.\n\nPour l'Académie Madelrieux, un organisme comme vous, on a obtenu +46 % de clics Google en 3 mois, sans publicité.\n\nSeriez-vous contre que je vous montre ce qu'on ferait pour {{companyName}} ?")),
 "1.13": dict(label="cabinets d'avocats d'affaires", preuve="[client à confirmer] : +17 % de pipeline organique",
    pb="Les dossiers viennent de la recommandation ; les annuaires et les legaltech captent les recherches.",
    p4=("avocat {{motcle}}", "{{firstName}}, quand un dirigeant cherche « avocat {{motcle}} {{ville}} », ce sont les annuaires et {{concurrent}} qui sortent.\n\nDans le respect de vos règles déontologiques, votre expertise peut y apparaître : contenu de fond, pages par domaine, présence dans les réponses IA.\n\nSeriez-vous contre que je vous montre où {{companyName}} en est ?"), sober=True),
}

# Palier B2B : P1 à P3c (gabarits nourris par le contenu du sous-ICP)
B2B_PALIERS = [
 ("P1 · a levé + recrute", "après la levée",
  "Félicitations pour la levée, {{firstName}}. Avec le recrutement d'un·e {{poste}} en cours, j'imagine que les demandes entrantes doivent suivre.\n\n{pb}\n\nSeriez-vous contre que je vous montre où {{companyName}} perd des demandes aujourd'hui ?"),
 ("P2 · recrute", "{{poste}}",
  "J'ai vu que {{companyName}} recrute un·e {{poste}}, {{firstName}} : j'imagine que plus de demandes entrantes fait partie des objectifs.\n\n{pb}\n\nUn recrutement ne règle pas ça seul. Seriez-vous contre que je vous montre sur quelles questions vos concurrents sont cités à votre place ?"),
 ("P3a · baisse de trafic (si baisse > 10 %)", "trafic {{companyName}}",
  "{{firstName}}, d'après nos estimations, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an. Ce n'est pas forcément de votre fait : depuis juillet, les réponses IA de Google prennent une partie des clics.\n\nLa vraie question, c'est où vos clients posent leurs questions maintenant, et qui y est cité.\n\nSeriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?"),
 ("P3b · concurrent devant sur Google (hack Igor)", "{{concurrent}} devant",
  "{{firstName}}, sur « {{motcle}} », {{concurrent}} sort avant {{companyName}}.\n\nJe peux vous dire pourquoi il est n°1 sur ce terme, et ce qui vous manque pour passer devant.\n\nÇa vaut 15 minutes ?"),
 ("P3c · concurrent cité par ChatGPT", "{{concurrent}} sur ChatGPT",
  "{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}. {{companyName}} n'apparaît pas.\n\n{pb}\n\nSeriez-vous contre que je vous montre pourquoi {{concurrent}} est cité, et les 9 autres questions où ça se joue ?"),
]
B2B_CHAMPION = ("Champion (SEO / contenu / marketing)", "« {{motcle}} »",
  "Vous gérez le contenu chez {{companyName}}, c'est bien ça, {{firstName}} ?\n\n« {{motcle}} » est cherché {{volume}} fois par mois et {{concurrent}} y est devant vous, sur Google comme dans ChatGPT.\n\nJ'ai préparé la première partie des données structurées et des entités qui manquent sur votre page : c'est ce que les IA lisent pour vous citer. Je vous l'envoie ?")

B2B_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, des nouvelles de mon dernier message ?\n\nLa question où {{concurrent}} passe devant vous est la moins grave des 10 que j'ai testées.\n\nÇa vaut 15 minutes ?\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "1 levier sur 7",
  "{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.\n\nEn haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.\n\nJ'en ai 6 autres pour {{companyName}}, dans l'ordre où ils rapportent. Ce serait une mauvaise idée d'en parler 15 minutes ?\n\nNathan\nPS : ce levier est à vous, même si on ne travaille jamais ensemble."),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. vous avez demandé à ChatGPT de me répondre, et il a recommandé {{concurrent}}.\n\nRépondez juste le numéro, que je sache quoi faire.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée de ma part.\n\nDonnez-moi une page de {{companyName}}, celle qui compte le plus : je la travaille gratuitement pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque.\n\nVous gardez le résultat. Je vous l'envoie sur quelle page ?\n\nNathan"),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.\n\nSi la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.\n\nBonne continuation,\nNathan"),
]

# ---------------------------------------------------------------- LOCAL / BTP (2.x)
LOCAL = {
 "2.1": dict(label="entreprises du BTP et de la rénovation", unit="chantiers", metier="rénovation", saison=None),
 "2.2": dict(label="installateurs de pompes à chaleur et de clim", unit="installations", metier="pompe à chaleur", saison="Les PAC air-air font -14 % au premier semestre et +31 % au second avec les canicules (Uniclima) : l'hiver se prépare maintenant.", demarchage=True),
 "2.3": dict(label="installateurs photovoltaïques", unit="installations", metier="panneaux solaires", saison=None, demarchage=True),
 "2.4": dict(label="entreprises de rideaux métalliques", unit="interventions", metier="dépannage rideau métallique", saison=None),
 "2.5": dict(label="installateurs de monte-escaliers", unit="installations", metier="monte-escalier", saison=None),
 "2.6": dict(label="entreprises de pompes funèbres", unit="familles accompagnées", metier="pompes funèbres", saison=None, sober=True),
 "2.7": dict(label="entreprises de sécurité incendie", unit="contrats", metier="maintenance extincteurs", saison=None),
 "2.8": dict(label="menuisiers et poseurs de fenêtres", unit="chantiers", metier="fenêtres", saison=None, demarchage=True),
 "2.9": dict(label="couvreurs et entreprises d'isolation", unit="chantiers", metier="couvreur", saison="Après chaque tempête, le premier couvreur visible sur Google Maps prend les appels, et les faux couvreurs font fuir la confiance.", demarchage=True),
 "2.10": dict(label="piscinistes", unit="chantiers", metier="pisciniste", saison="Les projets de piscine se décident entre janvier et avril : c'est maintenant qu'il faut être visible."),
 "2.11": dict(label="installateurs d'alarmes et de vidéosurveillance", unit="contrats", metier="alarme maison", saison=None),
 "2.12": dict(label="cuisinistes", unit="projets", metier="cuisiniste", saison=None),
 "2.13": dict(label="entreprises de déménagement", unit="déménagements", metier="déménageur", saison="Les devis de l'été se demandent au printemps."),
 "2.14": dict(label="paysagistes", unit="chantiers", metier="paysagiste", saison="Les chantiers du printemps se décident en hiver."),
 "2.15": dict(label="entreprises de travaux publics et de génie civil", unit="marchés", metier="travaux publics", saison=None, b2b=True),
}
LOCAL_PALIERS = [
 ("P1 · concurrent devant sur Google Maps", "{{concurrent}} devant",
  "{{firstName}}, sur « {{metier}} {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.\n\nJe peux vous dire pourquoi il est n°1 sur ce terme, et ce qui vous manque pour passer devant.\n\nÇa vaut 15 minutes ?"),
 ("P2 · saison (métiers saisonniers)", "avant la saison",
  "{{firstName}}, {saison}\n\nJe cherche quelques {label} {{zone}} prêts à prendre 20 {unit} de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.\n\nSeriez-vous contre que je vous explique comment ça marche ?"),
 ("P3 · absent de ChatGPT", "ChatGPT et {{ville}}",
  "{{firstName}}, j'ai demandé à ChatGPT « meilleur {{metier}} à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.\n\nDe plus en plus de clients posent la question comme ça avant d'appeler.\n\nSeriez-vous contre que je vous montre pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?"),
 ("P4 · marché principal A · plateformes de devis (commentaire Nathan)", "vos devis",
  "{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.\n\nNous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.\n\nSeriez-vous contre que je vous montre comment ?"),
 ("P4 · marché principal B · capacité + performance (validée par Nathan)", "20 {unit} de plus ?",
  "Question directe, {{firstName}} : si 20 {unit} de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?\n\nJe cherche quelques {label} {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.\n\nSeriez-vous contre que je vous explique comment ça marche ?"),
 ("P4 · marché principal C · interdiction de prospecter (rénovation énergétique uniquement)", "prospecter, c'est fini",
  "{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.\n\nIl ne reste que les clients qui vous cherchent : Google, Maps, et de plus en plus ChatGPT.\n\nJe cherche quelques {label} {{zone}} prêts à prendre 20 {unit} de plus par mois, en partenariat à la performance. Seriez-vous contre que je vous explique comment ça marche ?"),
]
LOCAL_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, je remonte mon message.\n\n« {{metier}} {{ville}} » est cherché environ {{volume}} fois par mois. La plupart de ces appels partent chez les 3 premiers de la carte.\n\nVous voulez savoir ce qui vous sépare d'eux ?\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "pourquoi {{concurrent}}",
  "{{firstName}}, pas de rendez-vous cette fois.\n\nJe regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo pourquoi {{concurrent}} est n°1 sur « {{metier}} {{ville}} », et ce qui vous manque.\n\nJe vous l'envoie ?\n\nNathan\nPS : la vidéo est à vous, même si on ne travaille jamais ensemble."),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. votre planning est plein jusqu'en 2028 ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. vous êtes sur un chantier et vous lirez ce mail ce soir.\n\nRépondez juste le numéro.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée.\n\nDonnez-moi la page de votre site qui compte le plus : je la travaille gratuitement pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque.\n\nVous gardez le résultat. Sur quelle page je travaille ?\n\nNathan"),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.\n\nSi un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.\n\nBonne continuation,\nNathan"),
]
LOCAL_SOBER_FU2 = ("FU2 · J+11 · relance sobre (2.6 pompes funèbres)", "",
  "{{firstName}}, je me permets une dernière question : est-ce que la visibilité de {{companyName}} sur Google auprès des familles de {{ville}} est un sujet pour vous cette année ?\n\nUn « oui » ou un « non » me suffit.\n\nNathan")

# ---------------------------------------------------------------- HOSPITALITÉ, BIEN-ÊTRE, FORMATION BIEN-ÊTRE (4.x)
HOSP = {
 "4.1": dict(label="hôtels indépendants", unit="réservations directes", recherche="hôtel {{ville}}",
    p4=("vos commissions", "{{firstName}}, on aide nos clients hôteliers à ne plus payer jusqu'à 20 % de commission aux plateformes sur des réservations qu'ils auraient pu recevoir en direct.\n\nUn hôtel sur deux voit déjà une OTA vendre ses chambres moins cher que son propre site (HOTREC 2026).\n\nVous voulez faire pareil ?")),
 "4.2": dict(label="spas et instituts", unit="nouvelles clientes", recherche="spa {{ville}}",
    p4=("vos nouvelles clientes", "{{firstName}}, vos fidèles restent, mais les nouvelles clientes qui cherchent « spa {{ville}} » tombent sur {{concurrent}} avant vous, ou passent par une plateforme qui prend sa commission.\n\nUne cliente qui vous trouve sur Google Maps ne vous coûte rien.\n\nSeriez-vous contre que je vous montre comment la récupérer ?")),
 "4.3": dict(label="résidences seniors", unit="familles", recherche="résidence seniors {{ville}}", sober=True,
    p4=("familles à {{ville}}", "{{firstName}}, quand une famille cherche une résidence pour un parent, elle compare en ligne, sur Google et les annuaires, avant d'appeler.\n\nSur « résidence seniors {{ville}} », c'est {{concurrent}} qui est vu en premier.\n\nSeriez-vous contre que je vous montre ce qui le place devant {{companyName}} ?")),
 "4.4": dict(label="campings et résidences de tourisme", unit="réservations directes", recherche="camping {{lieu}}",
    p4=("900 € de séjour", "{{firstName}}, sur un séjour de 900 €, entre 135 et 180 € partent chez la plateforme selon le contrat.\n\nLes recherches « camping {{lieu}} » arrivent surtout sur Booking et sur les grands groupes, pas sur votre site.\n\nSeriez-vous contre que je vous montre où ces réservations directes vous échappent ?")),
 "4.5": dict(label="écoles et formations bien-être", unit="inscrits", recherche="formation {{motcle}} {{ville}}",
    p4=("vos inscriptions", "{{firstName}}, quand quelqu'un cherche « formation {{motcle}} », il compare les écoles sur Google et de plus en plus dans ChatGPT, et c'est {{concurrent}} qui est cité.\n\nPour l'École Humaniste de Gestalt, on a fait passer la position moyenne Google de 18 à 10.\n\nSeriez-vous contre que je vous montre ce qu'on ferait pour {{companyName}} ?")),
}
HOSP_PALIERS = [
 ("P1 · concurrent devant sur Google", "{{concurrent}} devant",
  "{{firstName}}, sur « {recherche} », {{concurrent}} sort avant {{companyName}}.\n\nJe peux vous dire pourquoi il est n°1 sur ce terme, et ce qui vous manque pour passer devant.\n\nÇa vaut 15 minutes ?"),
 ("P3 · ChatGPT cite un concurrent", "{{concurrent}} sur ChatGPT",
  "{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.\n\nUn Français sur trois a déjà préparé un voyage ou une sortie avec une IA, et ces réponses s'appuient sur les avis et les fiches Google.\n\nSeriez-vous contre que je vous montre pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?"),
]
HOSP_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, je remonte mon message.\n\n« {recherche} » est cherché environ {{volume}} fois par mois. Vous voulez savoir combien de ces recherches vous reviennent ?\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "pourquoi {{concurrent}}",
  "{{firstName}}, pas de rendez-vous cette fois.\n\nJe regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo pourquoi {{concurrent}} passe devant vous, et ce qui vous manque.\n\nJe vous l'envoie ?\n\nNathan\nPS : la vidéo est à vous, même si on ne travaille jamais ensemble."),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. vous êtes complets jusqu'en 2028 ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. vous êtes en plein service et vous lirez ce mail ce soir.\n\nRépondez juste le numéro.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée.\n\nNotre outil transforme une page en page citable par les IA, pas seulement par Google, sur 50 critères. Donnez-moi la page de votre choix : je la travaille gratuitement, et je vous ajoute les données structurées qui vous manquent.\n\nVous gardez le résultat. Sur quelle page ?\n\nNathan"),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, c'est mon dernier message.\n\nSi un jour vous voulez plus de {unit} en direct, répondez simplement « oui » et je reviens vers vous.\n\nBonne continuation,\nNathan"),
]

# ---------------------------------------------------------------- TOURISME MÉDICAL (3.x)
MED = {
 "3.1": dict(label="cliniques de greffe capillaire", soin="greffe de cheveux"),
 "3.2": dict(label="cliniques dentaires", soin="implants dentaires"),
 "3.3": dict(label="cliniques esthétiques", soin="chirurgie esthétique"),
 "3.4": dict(label="cliniques de chirurgie bariatrique", soin="sleeve gastrique"),
}
MED_PALIERS = [
 ("P1 · ChatGPT cite une autre clinique", "{{concurrent}} sur ChatGPT",
  "{{firstName}}, j'ai demandé à ChatGPT, comme le ferait un patient français : « meilleure clinique {soin} à {{ville}} ». Il recommande {{concurrent}}, pas {{companyName}}.\n\nCes patients passent ensuite souvent par un intermédiaire qui prend sa commission.\n\nSeriez-vous contre que je vous montre pourquoi {{concurrent}} est cité, et comment recevoir ces patients en direct ?"),
 ("P4 · marché principal · intermédiaires", "vos patients français",
  "{{firstName}}, chaque patient qui arrive par un facilitateur vous coûte une commission.\n\nJe cherche quelques {label} {{zone}} prêtes à recevoir plus de patients en direct, depuis la France, la Belgique et la Suisse, via leur propre site et ChatGPT. Vous payez sur les résultats.\n\nSeriez-vous contre que je vous explique comment ça marche ?"),
]


def fill(t, d):
    for k, v in d.items():
        if isinstance(v, str): t = t.replace("{{" + k + "}}", v).replace("{" + k + "}", v)
    return t
