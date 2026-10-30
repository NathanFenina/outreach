"""Copies V2.2 (30/10, après audit + validation Nathan) : un mail 1 par sous-ICP et par palier de la pyramide, suites par famille.
Pyramide : P1 a levé + recrute (1.1 à 1.4 seulement) · P2 recrute · P3 intent SEO / GEO (P3a baisse de trafic, P3b concurrent
devant sur Google, P3c concurrent cité par les IA, chiffré) · P4 marché principal. Local : P1 Maps · P2 saison · P3 IA · P4 A/B/C/D.
Règles : Igor (R.E.P.L.Y. / AAA, ≤ 80 mots, objet < 5 mots, PAS d'appel au mail 1 : on propose un livrable et on cherche un « oui »,
PS = UNE preuve client proche ou inversion du risque, PPS = sortie sur chaque mail qui ouvre un fil). Chiffres : uniquement ceux sourcés
dans copy/31 et copy/32 ou fournis par Nathan. A/B : chaque mail 1 a une variante B « rendez-vous » générée automatiquement (cta_rdv).
Variables : {{firstName}} {{companyName}} {{ville}} {{zone}} {{concurrent}} {{prompt}} {{motcle}} {{volume}} {{baisse}} {{part}}
{{n_reponses}} {{n_concurrent}} {{n_vous}} {{lieu}} {{pro}} {{pb}} {{ps}}. Une variable vide exclut le lead du palier (jamais de blanc)."""

SIGN = "Nathan Fenina, fondateur de Décupler (SEO + IA)"
OUT = "PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille."
OUT_SOBER = "PPS : si ce n'est pas le sujet, répondez simplement « non merci »."
RDV = "Ça vaut 15 minutes pour en parler cette semaine ?"  # variante B (test rendez-vous vs livrable, demande Nathan)
FU2_JOKE = "3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre."  # blague validée par Nathan pour tous


def cta_rdv(body):
    """Variante B : même mail, mais le dernier paragraphe (la demande de livrable) devient une demande de rendez-vous."""
    parts = body.rstrip().split("\n\n")
    return "\n\n".join(parts[:-1] + [RDV])


# ---------------------------------------------------------------- B2B (1.x)
# pb = le problème dans les mots du métier (sourcé) ; preuve = PS (un seul client, le plus proche) ; p4 = mail 1 marché principal
P_CLOUD = "Cloudtech : +17 % de leads issus du SEO et des IA en 6 mois"
P_MADEL = "l'Académie Madelrieux : +46 % de clics Google en 3 mois"
B2B = {
 "1.1": dict(label="éditeurs SaaS", preuve=P_CLOUD,
    pb="La moitié des acheteurs de logiciels commencent maintenant leur recherche dans un chatbot plutôt que sur Google (G2, 2026).",
    p4=("shortlist", "{{firstName}}, quand un acheteur demande à ChatGPT « {{prompt}} », c'est là que se joue la shortlist, avant même votre site.\n\nUn sur trois finit par acheter à un éditeur qu'il ne connaissait pas (G2, 2026) : la place est encore à prendre.\n\nSeriez-vous contre que je vous envoie les 10 questions de votre catégorie, et qui y est cité ?")),
 "1.2": dict(label="startups IA", preuve=P_CLOUD,
    pb="On compte plus de 1 100 startups IA en France (France Digitale 2026) : se faire citer devient plus dur que lever.",
    p4=("1 100 startups IA", "{{firstName}}, il y a plus de 1 100 startups IA en France (France Digitale). Quand un client demande à ChatGPT un outil pour « {{prompt}} », il en cite trois.\n\nLa différence se joue sur ce que les IA savent de vous : cas d'usage, preuves, entités.\n\nSeriez-vous contre que je vous envoie où en est {{companyName}} sur ces questions ?")),
 "1.3": dict(label="ESN et intégrateurs", preuve=P_CLOUD,
    pb="Sur « intégrateur + éditeur + ville », ce sont les partenaires les mieux référencés qui reçoivent les demandes entrantes.",
    p4=("{{motcle}}", "{{firstName}}, « {{motcle}} » est cherché environ {{volume}} fois par mois, et c'est {{concurrent}} qui récupère ces demandes.\n\nPour une ESN, c'est souvent le seul contact entrant qui n'est ni un appel d'offres ni une recommandation.\n\nSeriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?")),
 "1.4": dict(label="sociétés de cybersécurité", preuve=P_CLOUD,
    pb="Un RSSI vérifie toujours avant d'appeler : sur Google, et de plus en plus dans ChatGPT, où ce sont les gros acteurs qui sont cités.",
    p4=("audit de sécurité", "{{firstName}}, avant de contacter un prestataire pour un audit ou un pentest, un RSSI se renseigne seul, sur Google et de plus en plus dans ChatGPT.\n\nSur « {{prompt}} », la réponse cite {{concurrent}}. Pas {{companyName}}.\n\nSeriez-vous contre que je vous envoie les questions où vous pourriez être la référence citée ?")),
 "1.5": dict(label="cabinets de conseil", preuve=P_CLOUD,
    pb="Les IA citent d'abord McKinsey, BCG et Bain ; les petits cabinets ne remontent que sur les questions de niche (test Consultor, 2026).",
    p4=("grands cabinets", "{{firstName}}, quand un dirigeant demande à ChatGPT un cabinet pour « {{prompt}} », il cite d'abord les grands noms. Sur les questions de niche, en revanche, les petits cabinets passent devant (test Consultor, 2026).\n\nC'est là que se fait votre shortlist.\n\nSeriez-vous contre que je vous envoie les 10 questions de votre spécialité, et qui y est cité ?")),
 "1.6": dict(label="cabinets d'expertise comptable", preuve=P_CLOUD, sober=True,
    pb="Depuis le 1er septembre 2026, la réception des factures électroniques est obligatoire : les dirigeants cherchent un cabinet qui les accompagne.",
    p4=("facture électronique", "{{firstName}}, depuis le 1er septembre, les dirigeants cherchent un cabinet qui les accompagne sur la facture électronique.\n\nSur « expert-comptable {{ville}} », c'est {{concurrent}} qui sort, pas {{companyName}}.\n\nSeriez-vous contre que je vous envoie ce qui lui donne cette place ?")),
 "1.7": dict(label="conseils en M&A et transmission", preuve=P_CLOUD,
    pb="7 cédants sur 10 à plus d'un an de la vente se renseignent seuls (Bpifrance Le Lab), sur les simulateurs et les plateformes d'annonces.",
    p4=("vos futurs cédants", "{{firstName}}, 7 dirigeants sur 10 qui pensent à céder dans plus d'un an se renseignent encore seuls (Bpifrance Le Lab).\n\nIls posent leurs questions à Google et à ChatGPT, et tombent sur les simulateurs et les plateformes d'annonces, rarement sur un conseil comme {{companyName}}.\n\nSeriez-vous contre que je vous envoie ces questions, et qui y répond aujourd'hui ?")),
 "1.8": dict(label="cabinets de gestion de patrimoine", preuve=P_CLOUD, sober=True,
    pb="44 % des épargnants décident seuls, et près d'un jeune sur cinq consulte une IA avant de placer (AMF 2025).",
    p4=("vos futurs clients", "{{firstName}}, depuis le 11 août, plus d'appel sans consentement préalable. Et 44 % des épargnants décident déjà seuls (AMF).\n\nQuand on demande à ChatGPT « {{prompt}} », il cite {{concurrent}}, pas {{companyName}}.\n\nSeriez-vous contre que je vous envoie ce qui le fait citer ?")),
 "1.9": dict(label="agences", preuve=None, ps="PS : l'audit sous votre marque est offert, vous jugez sur pièce.",
    pb="Vos clients vous demandent « et ChatGPT ? », et peu d'agences ont une réponse technique à leur donner.",
    p4=("vos clients et ChatGPT", "{{firstName}}, question directe : quand un client vous demande s'il ressort dans ChatGPT, vous refusez, vous sous-traitez ou vous gérez en interne ?\n\nOn produit le GEO en marque blanche pour quelques agences : vous gardez le client et la marge, on exécute.\n\nSeriez-vous contre que je fasse l'audit GEO d'un de vos clients, sous votre marque ?")),
 "1.10": dict(label="agences événementielles et de conférenciers", preuve=P_MADEL,
    pb="Les entreprises cherchent un lieu ou un conférencier sur Google et ChatGPT, et ce sont les plateformes qui captent la demande.",
    p4=("séminaire {{ville}}", "{{firstName}}, quand une entreprise cherche « {{motcle}} », ce sont les plateformes et {{concurrent}} qui récupèrent la demande.\n\nUn devis qui arrive en direct, c'est une commission en moins et un client à vous.\n\nSeriez-vous contre que je vous envoie ce qui vous manque pour être choisi en direct ?")),
 "1.11": dict(label="cabinets de recrutement", preuve=P_CLOUD,
    pb="Les mandats viennent du réseau et de LinkedIn ; les DRH qui cherchent un cabinet par métier tombent sur les jobboards et les gros réseaux.",
    p4=("cabinet {{motcle}}", "{{firstName}}, quand une DRH cherche « {{motcle}} », elle tombe sur les jobboards et sur {{concurrent}}, rarement sur un cabinet spécialisé comme {{companyName}}.\n\nC'est pourtant le mandat que vous voulez : celui qui arrive sans prospection.\n\nSeriez-vous contre que je vous envoie comment le capter ?")),
 "1.12": dict(label="organismes de formation", preuve=None, ps="PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.",
    pb="Les inscriptions dépendent des financeurs et des plateformes ; sur « formation + métier », les gros organismes prennent la place.",
    p4=("vos inscriptions", "{{firstName}}, sur « {{motcle}} », ce sont les gros organismes et les plateformes qui récupèrent les inscriptions.\n\nPour l'Académie Madelrieux, un organisme comme vous, on a obtenu +46 % de clics Google en 3 mois, sans publicité.\n\nSeriez-vous contre que je vous envoie ce qu'on ferait pour {{companyName}} ?")),
 "1.13": dict(label="cabinets d'avocats d'affaires", preuve=P_CLOUD, sober=True,
    pb="Les dossiers viennent de la recommandation ; les annuaires et les legaltech captent les recherches.",
    p4=("avocat {{motcle}}", "{{firstName}}, quand un dirigeant cherche « avocat {{motcle}} {{ville}} », ce sont les annuaires et {{concurrent}} qui sortent.\n\nDans le respect de vos règles déontologiques, votre expertise peut y apparaître : contenu de fond, pages par domaine, présence dans les réponses IA.\n\nSeriez-vous contre que je vous envoie où {{companyName}} en est ?")),
}
P1_ICPS = ("1.1", "1.2", "1.3", "1.4")  # les autres métiers ne lèvent pas de fonds

B2B_PALIERS = [
 ("P1 · a levé + recrute", "après la levée",
  "Félicitations pour la levée, {{firstName}}. Recruter juste après, c'est le signe que le pipeline est la priorité des prochains mois.\n\n{pb}\n\nSeriez-vous contre que je vous envoie, en vidéo de 3 minutes, les 10 questions où vos acheteurs ne vous trouvent pas ?"),
 ("P2 · recrute en marketing", "votre recrutement",
  "J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.\n\n{pb}\n\nPour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?"),
 ("P2b · recrute des commerciaux", "votre recrutement",
  "J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.\n\n{pb}\n\nSeriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?"),
 ("P3a · baisse de trafic (si baisse > 10 %)", "trafic {{companyName}}",
  "{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).\n\nCe n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.\n\nSeriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?"),
 ("P3b · concurrent devant sur Google", "{{concurrent}} devant",
  "{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.\n\nJe peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.\n\nSeriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?"),
 ("P3c · concurrent cité par les IA (chiffré)", "{{concurrent}} cité, pas vous",
  "{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.\n\nSur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.\n\nC'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?"),
]
B2B_CHAMPION = ("Champion (SEO / contenu / marketing)", "« {{motcle}} »",
  "{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.\n\nIl vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.\n\nSeriez-vous contre que je vous en envoie la liste ?")

B2B_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.\n\nToujours partant pour que je vous l'envoie ? Un « oui » suffit.\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "1 levier sur 7",
  "{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.\n\nEn haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.\n\nJ'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?\n\nNathan\nPS : ce levier est à vous, même si on ne travaille jamais ensemble.\n" + OUT),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n" + FU2_JOKE + "\n\nRépondez juste le numéro, que je sache quoi faire.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée de ma part.\n\nDonnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.\n\nVous gardez le résultat. Je vous l'envoie sur quelle page ?\n\nNathan\n" + OUT),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.\n\nSi la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.\n\nBonne continuation,\nNathan"),
]
B2B_SOBER_FU2 = ("FU2 · J+11 · relance sobre", "",
  "{{firstName}}, une question simple : la visibilité de {{companyName}} sur Google et dans ChatGPT est-elle un sujet pour vous cette année ?\n\nUn « oui » ou un « non » me suffit.\n\nNathan")

# ---------------------------------------------------------------- LOCAL / BTP (2.x)
# metier = terme tapé sur Google ; pro = question posée à ChatGPT, correctement accordée
LOCAL = {
 "2.1": dict(label="entreprises du BTP et de la rénovation", unit="chantiers", metier="rénovation", pro="meilleure entreprise de rénovation", saison=None),
 "2.2": dict(label="installateurs de pompes à chaleur et de clim", unit="installations", metier="pompe à chaleur", pro="meilleur installateur de pompe à chaleur",
    saison="les PAC air-air font +31 % au second semestre avec les canicules (Uniclima). C'est cet hiver que se prépare la visibilité de l'été prochain.", demarchage=True),
 "2.3": dict(label="installateurs photovoltaïques", unit="installations", metier="panneaux solaires", pro="meilleur installateur de panneaux solaires", saison=None, demarchage=True),
 "2.4": dict(label="entreprises de rideaux métalliques", unit="interventions", metier="dépannage rideau métallique", pro="meilleure entreprise de rideaux métalliques", saison=None),
 "2.5": dict(label="installateurs de monte-escaliers", unit="installations", metier="monte-escalier", pro="meilleur installateur de monte-escalier", saison=None),
 "2.6": dict(label="entreprises de pompes funèbres", unit="familles accompagnées", metier="pompes funèbres", pro="quelles pompes funèbres choisir", saison=None, sober=True),
 "2.7": dict(label="entreprises de sécurité incendie", unit="contrats", metier="maintenance extincteurs", pro="meilleure entreprise de sécurité incendie", saison=None),
 "2.8": dict(label="menuisiers et poseurs de fenêtres", unit="chantiers", metier="fenêtres", pro="meilleur menuisier pour changer ses fenêtres", saison=None, demarchage=True),
 "2.9": dict(label="couvreurs et entreprises d'isolation", unit="chantiers", metier="couvreur", pro="meilleur couvreur",
    saison="après chaque tempête, le premier couvreur visible sur Google Maps prend les appels, et avec les arnaques, les clients vérifient les avis avant d'appeler.", demarchage=True),
 "2.10": dict(label="piscinistes", unit="chantiers", metier="pisciniste", pro="meilleur pisciniste", saison="les projets de piscine se décident entre janvier et avril : c'est maintenant qu'il faut être visible."),
 "2.11": dict(label="installateurs d'alarmes et de vidéosurveillance", unit="contrats", metier="alarme maison", pro="meilleur installateur d'alarme", saison=None),
 "2.12": dict(label="cuisinistes", unit="projets", metier="cuisiniste", pro="meilleur cuisiniste", saison=None),
 "2.13": dict(label="entreprises de déménagement", unit="déménagements", metier="déménageur", pro="meilleur déménageur", saison="les devis de l'été se demandent au printemps."),
 "2.14": dict(label="paysagistes", unit="chantiers", metier="paysagiste", pro="meilleur paysagiste", saison="les chantiers du printemps se décident en hiver."),
 "2.15": dict(label="entreprises de travaux publics et de génie civil", unit="marchés", metier="travaux publics", pro="meilleure entreprise de travaux publics", saison=None, b2b=True),
}
LOCAL_PALIERS = [
 ("P1 · concurrent devant sur Google Maps", "{{concurrent}} devant",
  "{{firstName}}, sur « {metier} {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.\n\nJe peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.\n\nSeriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?"),
 ("P2 · saison (métiers saisonniers)", "avant la saison",
  "{{firstName}}, {saison}\n\nJe cherche quelques {label} {{zone}} prêts à prendre 20 {unit} de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.\n\nSeriez-vous contre que je vous envoie comment ça marche ?"),
 ("P3 · absent de ChatGPT", "ChatGPT et {{ville}}",
  "{{firstName}}, j'ai demandé à ChatGPT « {pro} à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.\n\nDe plus en plus de clients posent la question comme ça avant d'appeler.\n\nSeriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?"),
 ("P4 · marché principal A · plateformes de devis (commentaire Nathan)", "vos devis",
  "{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.\n\nNous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.\n\nSeriez-vous contre que je vous envoie comment ?"),
 ("P4 · marché principal B · capacité + performance (validée par Nathan)", "20 {unit} de plus ?",
  "Question directe, {{firstName}} : si 20 {unit} de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?\n\nJe cherche quelques {label} {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.\n\nSeriez-vous contre que je vous envoie comment ça marche ?"),
 ("P4 · marché principal C · interdiction de prospecter (rénovation énergétique)", "prospecter, c'est fini",
  "{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.\n\nIl ne reste que les clients qui vous cherchent, sur Google et dans ChatGPT.\n\nSeriez-vous contre que je vous envoie comment en recevoir 20 de plus par mois, payé à la performance ?"),
]
LOCAL_P4D = ("P4 · marché principal D · maîtres d'ouvrage privés (2.15)", "vos marchés privés",
  "{{firstName}}, les marchés publics passent par les plateformes d'appel d'offres. Les maîtres d'ouvrage privés, eux, cherchent sur Google « travaux publics {{zone}} », et c'est {{concurrent}} qu'ils trouvent.\n\nUn marché privé qui arrive en direct, c'est un dossier sans mise en concurrence à 10.\n\nSeriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?")
LOCAL_P4_SOBER = ("P4 · marché principal · version sobre (2.6)", "familles à {{ville}}",
  "{{firstName}}, quand une famille doit organiser des obsèques à {{ville}}, elle cherche dans l'urgence, souvent sur son téléphone.\n\nSur « pompes funèbres {{ville}} », c'est {{concurrent}} qui apparaît en premier.\n\nSeriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?")
LOCAL_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, je remonte mon message.\n\n« {metier} {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.\n\nToujours partant pour que je vous envoie ce qui vous sépare d'eux ?\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "pourquoi {{concurrent}}",
  "{{firstName}}, pas de rendez-vous cette fois.\n\nJe regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « {metier} {{ville}} ».\n\nJe vous l'envoie ?\n\nNathan\nPS : la vidéo est à vous, même si on ne travaille jamais ensemble.\n" + OUT),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. votre planning est plein jusqu'en 2028 ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n" + FU2_JOKE + "\n\nRépondez juste le numéro.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée.\n\nDonnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.\n\nVous gardez le résultat. Sur quelle page je travaille ?\n\nNathan\n" + OUT),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.\n\nSi un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.\n\nBonne continuation,\nNathan"),
]
LOCAL_SOBER_FU2 = ("FU2 · J+11 · relance sobre (2.6 pompes funèbres)", "",
  "{{firstName}}, une question simple : est-ce que la visibilité de {{companyName}} sur Google auprès des familles de {{ville}} est un sujet pour vous cette année ?\n\nUn « oui » ou un « non » me suffit.\n\nNathan")

# ---------------------------------------------------------------- HOSPITALITÉ, BIEN-ÊTRE, FORMATION BIEN-ÊTRE (4.x)
# stat_ia : seulement pour les hébergements (sources Brandwatch / KAYAK-Ipsos) ; aucune référence client hôtelier (Nathan 30/10)
STAT_VOYAGE = "Un Français sur trois a déjà utilisé une IA pour préparer un voyage (KAYAK-Ipsos), et ces IA s'appuient surtout sur Booking, pas sur votre site."
HOSP = {
 "4.1": dict(label="hôtels indépendants", unit="réservations en direct", recherche="hôtel {{ville}}", stat_ia=STAT_VOYAGE,
    p4=("vos commissions", "{{firstName}}, chaque réservation Booking coûte de 15 à 25 % de commission (UMIH), et un hôtel sur deux voit une OTA vendre ses chambres moins cher que son propre site (HOTREC 2026).\n\nSeriez-vous contre que je vous envoie combien de recherches « hôtel {{ville}} » pourraient arriver en direct chez {{companyName}} ?")),
 "4.2": dict(label="spas et instituts", unit="nouvelles clientes", recherche="spa {{ville}}", stat_ia="",
    p4=("vos nouvelles clientes", "{{firstName}}, vos fidèles restent, mais les nouvelles clientes qui cherchent « spa {{ville}} » tombent sur {{concurrent}} avant vous, ou passent par une plateforme qui prend sa commission.\n\nUne cliente qui vous trouve sur Google Maps ne vous coûte rien.\n\nSeriez-vous contre que je vous envoie comment la récupérer ?")),
 "4.3": dict(label="résidences seniors", unit="familles", recherche="résidence seniors {{ville}}", sober=True, stat_ia="",
    p4=("familles à {{ville}}", "{{firstName}}, quand une famille cherche une résidence pour un parent, elle compare en ligne, sur Google et les annuaires, avant d'appeler.\n\nSur « résidence seniors {{ville}} », c'est {{concurrent}} qui est vu en premier.\n\nSeriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?")),
 "4.4": dict(label="campings et résidences de tourisme", unit="réservations en direct", recherche="camping {{lieu}}", stat_ia=STAT_VOYAGE,
    p4=("900 € de séjour", "{{firstName}}, sur un séjour de 900 €, entre 135 et 180 € partent chez la plateforme selon le contrat.\n\nLes recherches « camping {{lieu}} » arrivent surtout sur Booking et sur les grands groupes, pas sur votre site.\n\nSeriez-vous contre que je vous envoie où ces réservations directes vous échappent ?")),
 "4.5": dict(label="écoles et formations bien-être", unit="nouveaux inscrits", recherche="formation {{motcle}} {{ville}}", stat_ia="",
    ps="PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.",
    p4=("vos inscriptions", "{{firstName}}, quand quelqu'un cherche « formation {{motcle}} », il compare les écoles sur Google et de plus en plus dans ChatGPT, et c'est {{concurrent}} qui est cité.\n\nPour l'École Humaniste de Gestalt, on a fait passer la position moyenne Google de 18 à 10.\n\nSeriez-vous contre que je vous envoie ce qu'on ferait pour {{companyName}} ?")),
}
HOSP_PALIERS = [
 ("P1 · concurrent devant sur Google", "{{concurrent}} devant",
  "{{firstName}}, sur « {recherche} », {{concurrent}} sort avant {{companyName}}.\n\nJe peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.\n\nSeriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?"),
 ("P3 · ChatGPT cite un concurrent", "{{concurrent}} sur ChatGPT",
  "{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.\n\n{stat_ia}\n\nSeriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?"),
]
HOSP_SUITE = [
 ("FU1 · J+3 · même fil", "", "{{firstName}}, je remonte mon message.\n\n« {recherche} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?\n\nNathan"),
 ("VP2 · J+8 · nouvel objet", "pourquoi {{concurrent}}",
  "{{firstName}}, pas de rendez-vous cette fois.\n\nJe regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.\n\nJe vous l'envoie ?\n\nNathan\nPS : la vidéo est à vous, même si on ne travaille jamais ensemble.\n" + OUT),
 ("FU2 · J+11 · relance 1-2-3", "",
  "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. vous êtes complets jusqu'en 2028 ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n" + FU2_JOKE + "\n\nRépondez juste le numéro.\n\nNathan"),
 ("VP3 · J+21 · nouvel objet", "votre page",
  "{{firstName}}, dernière idée.\n\nDonnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.\n\nVous gardez le résultat. Sur quelle page ?\n\nNathan\n" + OUT),
 ("FU3 · J+24 · rupture", "",
  "{{firstName}}, c'est mon dernier message.\n\nSi un jour vous voulez plus de {unit}, répondez simplement « oui » et je reviens vers vous.\n\nBonne continuation,\nNathan"),
]

# ---------------------------------------------------------------- TOURISME MÉDICAL (3.x) · EN PAUSE (Nathan 30/10 : mails en anglais,
# offre à discuter : visibilité via le site de la clinique). Aucune campagne tant que l'offre n'est pas tranchée.
MED = {
 "3.1": dict(label="cliniques de greffe capillaire", soin="greffe de cheveux"),
 "3.2": dict(label="cliniques dentaires", soin="implants dentaires"),
 "3.3": dict(label="cliniques esthétiques", soin="chirurgie esthétique"),
 "3.4": dict(label="cliniques de chirurgie bariatrique", soin="sleeve gastrique"),
}
MED_PALIERS = []

# ---------------------------------------------------------------- V2.1 : mails 1 « intent SEO / GEO » + variantes VP2 / VP3
# {{part}} (53_intent_seo.py) : part estimée du trafic du n°1 > 80 % → « et récupère quasiment tout le trafic » ; > 50 % → « et récupère
# la majorité du trafic » ; sinon « et capte la plus grosse part des clics ». {{concurrent}} = vrai concurrent (jamais .gouv, Wikipédia,
# annuaire, média, comparateur), vérifié par IA.
INTENT_V21 = [
 ("B2B", "P3b · n°1 sur le mot-clé business + roadmap", "{{motcle}}",
  "{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), c'est {{concurrent}} qui est n°1 {{part}}.\n\nJe peux vous partager la roadmap pour le rattraper : ce qu'il a, ce qui vous manque, dans l'ordre où ça rapporte.\n\nSeriez-vous contre que je la monte pour vous ?"),
 ("B2B", "P3c · visibilité IA (ChatGPT + Perplexity + Google IA)", "{{concurrent}} cité, pas vous",
  "{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.\n\nSur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.\n\nC'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?"),
 ("B2B", "P3d · réponse IA de Google (AI Overview)", "la réponse de Google",
  "{{firstName}}, quand on cherche « {{motcle}} » sur Google, la réponse IA tout en haut cite {{concurrent}}. Pas {{companyName}}.\n\nCette réponse passe avant les liens, et beaucoup ne regardent plus ceux d'en dessous.\n\nSeriez-vous contre que je vous envoie comment y entrer ?"),
 ("B2B", "VP2 variante · roadmap de rattrapage", "votre roadmap",
  "{{firstName}}, on prépare des roadmaps SEO et IA pour des entreprises comme {{companyName}} : où vous perdez des demandes, qui les récupère, et les 3 actions qui rapportent le plus.\n\nSeriez-vous contre que je monte la vôtre ? Je vous l'envoie, vous gardez le résultat.\n\nNathan\n" + OUT),
 ("B2B", "VP3 variante · cas client et process", "comment on travaille",
  "{{firstName}}, dernière idée de ma part.\n\nJe peux vous envoyer un cas client proche de {{companyName}} et notre process, étape par étape : audit, pages, citations par les IA, suivi des demandes.\n\nJe vous l'envoie ?\n\nNathan\n" + OUT),
 ("LOCAL", "P3b · n°1 sur Google Maps + roadmap", "{{concurrent}} devant",
  "{{firstName}}, sur « {{metier}} {{ville}} » ({{volume}} recherches par mois), c'est {{concurrent}} qui est n°1 {{part}}.\n\nJe peux vous partager la roadmap pour passer devant lui : fiche Google, avis, pages du site, dans l'ordre.\n\nSeriez-vous contre que je la monte pour vous ?"),
 ("LOCAL", "P3c · ChatGPT + Google IA", "{{concurrent}} recommandé",
  "{{firstName}}, j'ai demandé à ChatGPT et à Google « {{pro}} à {{ville}} ». Les deux recommandent {{concurrent}}. {{companyName}} n'apparaît dans aucune réponse.\n\nDe plus en plus de clients choisissent comme ça avant d'appeler.\n\nSeriez-vous contre que je vous envoie ce qui le fait recommander ?"),
 ("HOSP", "P3c · ChatGPT + Google IA (hébergements)", "{{concurrent}} recommandé",
  "{{firstName}}, j'ai demandé à ChatGPT et à Google « {{prompt}} ». Les deux recommandent {{concurrent}}. {{companyName}} n'apparaît pas.\n\n" + STAT_VOYAGE + "\n\nSeriez-vous contre que je vous envoie ce qui le fait recommander, et la roadmap pour l'être aussi ?"),
]

# Hypothèses et critères de succès par palier (cycle HADI d'Igor), à valider avant l'envoi
HYPOTHESES = {
 "P1": "Une levée + un recrutement = budget et urgence : ≥ 5 % de réponses, ≥ 30 % positives (petit volume).",
 "P2": "Un recrutement marketing / commercial = objectif de pipeline : ≥ 4 % de réponses sur ≥ 150 prospects.",
 "P3": "Un constat chiffré sur leur propre visibilité (concurrent n°1, citations IA) : ≥ 4 % de réponses sur ≥ 300 prospects.",
 "P4": "Marché principal, problème du métier + livrable offert : ≥ 3 % de réponses, ≥ 20 % positives sur ≥ 300 prospects.",
 "A/B": "Livrable (A) contre rendez-vous (B) au mail 1 : on garde la variante avec le plus de « oui » sur ≥ 250 prospects par variante.",
}


def fill(t, d):
    for k, v in d.items():
        if isinstance(v, str): t = t.replace("{{" + k + "}}", v).replace("{" + k + "}", v)
    return t
