# REGISTRE · machine cold mail Décupler

> Document unique pour ne rien perdre. Créé le 28/10/2026 après les sessions Igor du 20/10 et du 27/10.
> À lire juste après le dernier `ETAT_*.md`. Chaque élément a un identifiant **stable** : on n'en réutilise jamais un, on ajoute à la suite.
> - **K** = connaissance acquise (fait, règle, chiffre sourcé)
> - **D** = décision ou consigne d'Igor (date de session entre crochets)
> - **V** = vérification faite (date)
> - **C** = chantier (statut : ⬜ à faire · 🟡 en cours · ⏸ attend Nathan · ✅ fait)
> - **Q** = question à Nathan (statut : ❓ ouverte · ✅ répondue, avec la réponse)
> - **N** = sujets 1 à 29 du message de Nathan du 28/10 (correspondance vers C et Q)

---

## 1. Connaissances (K)

### Infra
- **K1** Groupe A = 18 boîtes PremiumInboxes sur 9 domaines `decupler-*` : Google 100 % inbox (GlockApps 22/10), le reste en spam. Les 9 domaines sont listés SURBL, decuplerdigital.com aussi sur Spamhaus DBL.
- **K2** Groupe B = 21 boîtes Zapmail, 7 domaines × 3 (decuplerapp, decuplerlabs, getdecupler, godecupler, mydecupler, decuplerly, decupleroy). Chauffe démarrée le 26/10 ; prêtes vers le 6-9/11.
- **K3** Test GlockApps présenté le 27/10 : SpamAssassin 4,3 (devrait être 0) à cause d'une URL / domaine listé Spamhaus ; Google Workspace mitigé sur un des 2 tests (50/50), autres ESP mauvais (Amazon WorkMail…).
- **K4** Spamhaus / SURBL : on y entre quand des destinataires cliquent « signaler comme spam ». Il existe un processus de délistage. Google s'appuie surtout sur ses données internes (analyse vectorielle de chaque mail), les petits ESP s'appuient sur les listes publiques.
- **K5** Ce qui fait signaler en spam : mauvais message pour la mauvaise personne, trop de relances, pas d'option de désinscription, relancer après un non.
- **K6** Capacité actuelle ≈ 5 000 approches/mois ; Igor veut ≥ 10 000 (UltB : 50 000 prospects uniques/semaine en interne, ≥ 5 000/mois par client).
- **K7** Prospects Microsoft ≈ 42 % de nos anciennes listes (MX 14/10) ; Mimecast et Proofpoint = souvent Microsoft derrière. Exclus pour l'instant.

### Données et outils
- **K8** Tous les fournisseurs de données ont à peu près la même donnée (source principale LinkedIn + web) ; la différence = filtres, vitesse, coût.
- **K9** Apollo = le pire (prix en hausse, emails « vérifiés » non fiables). Instantly = un des plus gros pools d'envoi, sait si un email existe vraiment (rebonds/réponses observés).
- **K10** Instantly a une colonne « email service provider » dans les leads (≈ 90-99 % juste) et **SuperSearch** : on importe sa liste d'entreprises (ex. sortie Apify) puis on filtre les personnes.
- **K11** Apify : scrapers LinkedIn / Indeed ; un client d'Igor paie ~16 $ pour des milliers d'entreprises. Notre run du 24/10 : 2,60 $ → 1 300 offres → 702 entreprises → 216 dans la cible FR (trop peu pour l'ICP seul).
- **K12** Dataset UltB : recherche vectorielle d'entreprises, retrait des catch-all et des Outlook, 30+ sources pour les noms, organigramme décideurs / champions / référents, validation SMTP maison. **Pas de signal de recrutement** dans leur dataset.
- **K13** Lemlist People database : recherche gratuite, 5 crédits par email vérifié (≈ 0,05 $). Solde au 28/10 : **180 crédits offerts** (= 36 emails).
- **K14** FullEnrich : **1 045,75 crédits** au 28/10. Outscraper : crédits (solde non vérifié).
- **K15** DataForSEO : ≈ 5 cents par domaine pour une estimation de trafic organique → 10 000 entreprises = 500 €. Igor : trop cher si on ne sait pas quelle part a vraiment baissé ; viser 1-2 cents. Les estimations de trafic peuvent être fausses (un client dira « on a bien plus de trafic »).
- **K16** Hack Igor (client GEO) : chercher le concurrent classé au-dessus du prospect sur son mot-clé principal et le mettre en variable (corps **et objet**) : « {{concurrent}} est devant vous sur {{mot-clé}} ».

### Méthode
- **K17** Pyramide : 1 % = recrute ET a levé → 2 % = recrute → puis marché principal (sans signal, filtré par industrie, mots-clés, pain, observation réelle). La conversion baisse, le volume compense ; les lead magnets et un formulaire qualifient.
- **K18** Segmenter comme en SEO : une intention = un mail. Plus c'est granulaire, plus c'est pertinent, moins on est signalé en spam.
- **K19** Lead magnets : coût = temps + tokens + énergie + engagement. Effort faible (PDF, vidéo) → sans appel ; effort élevé (7 quick wins) → contre un appel de 15 min (« j'ai besoin de vos priorités pour bien le faire »). Échelonner dans la séquence : étape 1 = offre forte contre appel ; sans réponse, étape suivante = une ressource gratuite + « le reste en appel ». Exemple : donner 1 quick win par mail, les 6 autres en appel.
- **K20** Constat Nathan : les « oui » au pré-audit 10 prompts / 7 quick wins ne répondent plus après l'envoi → le lead magnet doit déclencher un appel, pas se livrer entièrement.
- **K21** Le recrutement n'est qu'un signal : le pain doit porter sur ce que Décupler résout (visibilité, leads). Ex. « vous recrutez un SEO → objectifs de croissance ; une fraction du coût d'un recrutement interne ».
- **K22** Résultats 20/10 : ~2 000 prospects, 55-60 réponses (≈ 2,7 %), ~10 positives (≈ 20 %), 1 RDV. Igor : « il faut 10× le volume ».
- **K24** decupler.fr est un domaine secondaire : autorisé pour le cold. Interdit : decupler.com (Nathan, 28/10).
- **K25** Taille de campagne : 100 leads minimum, 300 maximum (Nathan, 28/10).
- **K26** Prochaine session Igor : mardi 03/11/2026.
- **K27** Base Lemlist (28/10) : recherche gratuite mais quota de recherches (≈ 2 000, 1 600 restants) ; filtre « levée < 6 mois » vide pour la France ; « recrute en marketing < 90 j » ≈ 230 entreprises B2B FR.
- **K28** Messagerie des prospects locaux (PAC, solaire, incendie) : ≈ 10 % Google, 45 % autres (OVH…), 45 % Microsoft. → le lot O (Zapmail) porte l'essentiel du volume local.
- **K29** Qualification avant achat d'emails : ≈ 25 % des entreprises trouvées par mots-clés sont hors cible (concurrents, fonds, médias, sites morts) ; contrôle par IA ≈ 0,02 cent/entreprise.
- **K30** FullEnrich (28/10) : ≈ 85 % d'emails trouvés sur les dirigeants de TPE/PME FR, dont 60 % « DELIVERABLE ».
- **K23** Session 3 : 2 accords verbaux sur les ventes (1 confirmé, 1 en suspens pour raisons perso).

---

## 2. Décisions et consignes d'Igor (D)

### Infra
- **D1** [27/10] Infra actuelle (groupe A) = sûre pour Google uniquement. Nouvelle infra Zapmail (groupe B) = autres ESP (ni Google, ni Microsoft).
- **D2** [27/10] Refaire GlockApps **1 boîte par domaine** pour une image complète (données, pas ressenti).
- **D3** [27/10] Tenter le délistage Spamhaus / SURBL des domaines listés.
- **D4** [20/10] Outlook / Microsoft : infra dédiée plus tard (Azure, Hypertide, service « Entra »), plus chère, volumes plus bas, pas prioritaire.
- **D5** [20/10] Domaines « burner » : on remplace le lot tous les 3 à 9 mois ; ne pas mélanger les fournisseurs de boîtes sur un même domaine.

### Listes
- **D6** [27/10] À partir d'aujourd'hui, **chaque campagne est scindée Google / non-Google** (2 campagnes jumelles). Classer l'ESP par MX avec un outil gratuit ; sinon Igor le fait pour nous (jusqu'à ~1 000 entreprises).
- **D7** [27/10] Ouvrir hors de France dès maintenant : France d'abord, puis pays riches : **UK, Nordiques, Benelux, DACH (Allemagne, Autriche, Suisse), US**, éventuellement Italie. Espagne non pour l'instant. Séparer FR (en français) / hors FR (en anglais).
- **D8** [27/10] ICP 1 trop large : le découper en **sous-ICP 1.1, 1.2, 1.3…** (au moins : tech / SaaS / IA / logiciel ; conseil management, stratégie, finance + services B2B ; agences marketing / événementiel). Un message par sous-ICP.
- **D9** [27/10] Taille : filtrer sur **les effectifs, pas le CA** (filtres CA peu fiables). Seuil : **≥ 5 personnes** (UltB = 7-9 sur LinkedIn pour 1 M€).
- **D10** [27/10] Titres par sous-ICP en 2 groupes : **groupe 1 décideurs**, **groupe 2 champions** (différents selon l'industrie). Recherche à faire avec un LLM.
- **D11** [27/10] **Contacter tous les décideurs importants d'une même entreprise** (CEO, fondateur, CMO, CTO…), chacun avec un mail différent selon sa situation.
- **D12** [27/10] Signaux : priorité 1 = avec signal d'intention (≈ 1 %, ~500 mails), priorité 2 = sans signal. Recrutement via Apify uniquement.
- **D13** [27/10] Tester **Moltsets** (https://moltsets.com/our-data/, fournisseur « MCP first ») sur le plus petit plan ; résultats à la prochaine session.
- **D14** [27/10] Liste noire dans la base : tous les clients + toutes les entreprises qui ont déjà répondu ; l'importer dans la blocklist de l'outil d'envoi.
- **D15** [27/10] **Base centrale** (CRM) : qui a été approché, quand, réponse, blacklisté ou non. On y garde l'historique même quand on supprime les leads de l'outil d'envoi.
- **D16** [27/10] Dataset UltB : 2 voies. (a) Igor le fait « jusqu'à un certain niveau » ; (b) on teste Moltsets / autres. **Prérequis : finir le tableau ICP et fixer les priorités** (sinon des centaines de milliers d'entreprises).

### Nommage
- **D17** [20/10 + 27/10] Chaque campagne a un numéro, un lot ESP (G / O) et un n° d'hypothèse / framework, avec une bibliothèque des numéros (fait : `copy/25_convention_campagnes.md`).

### Intention SEO
- **D18** [27/10] Devoir : tester la baisse de trafic sur **100 à 1 000 entreprises** : part qui baisse, part qui baisse de **> 10 %**, coût. Chercher moins cher (1-2 cents). Philosophie : parfois moins cher d'approcher tout le monde que de filtrer.
- **D19** [27/10] Devoir : coût de collecte des **SERP** (concurrent au-dessus sur le mot-clé principal) via une API SERP bon marché + quelles autres infos collecter.

### Outil d'envoi
- **D20** [27/10] Si Nathan pense déjà à passer sur Instantly, le faire. Lien affilié + 20 % (https://instantly.ai/?via=ULTB, code ULTB20OFF1). PlusVibe : Igor ne l'a jamais testé, « ils sont tous pareils ».

### Lead magnets
- **D21** [27/10] Devoir : mapper chaque lead magnet aux avatars / industries (ex. le plugin : pas pour les grands comptes, oui pour les petites boîtes ou ceux qui savent utiliser Claude) ; noter son coût / effort ; le placer dans le funnel (avant appel / contre appel / après appel) ; le tester à différentes étapes de la séquence ; tableau avec métriques. Envoyer la liste à Igor pour retour à la prochaine session.

### Pain points et VP
- **D22** [20/10] Les 3 pains principaux doivent être liés au service ; 1 cas client par ICP (partir des cas publiés sur decupler.com) ; lead magnets : vidéo 3 min, top 10 mots-clés qui font perdre de l'argent, concurrents qui « volent » les clients.

### Ventes et admin
- **D23** [27/10] Rapports des appels de vente partagés par Igor sur Zoom ; suivre le guide en 8 étapes.
- **D24** [27/10] Envoyer un mail après la session avec les devoirs ; envoyer chaque devoir dès qu'il est prêt (Igor fait un retour asynchrone si possible).
- **D25** [27/10] Payer la 2e tranche le 28/10 et envoyer la preuve de paiement.
- **D26** [27/10] Prochaine session : semaine prochaine, lundi (ou dimanche), vers 17h-17h30.
- **D27** [27/10] Les sessions restantes se concentrent sur le cold outbound ; les appels de vente si le temps le permet.

---

## 3. Vérifications du 28/10 (V)

- **V1** DNS des 7 domaines Zapmail : MX Google, SPF, DKIM Google, DMARC `p=reject` → **OK pour les 7** (decuplerly et decupleroy compris).
- **V2** SURBL decuplerly / decupleroy : propres.
- **V3** Les 7 domaines Zapmail **ne répondent pas en HTTP** : la redirection vers decupler.com n'est pas en place.
- **V4** Lemlist (API) : aucune des 21 boîtes Zapmail n'est expéditrice d'une campagne (119 campagnes lues). ✅
- **V5** L'API Lemlist ne donne pas l'état de connexion ni lemwarm des boîtes → à vérifier dans l'interface.
- **V6** `nathan@decupler.fr` est expéditeur de la campagne **en cours** « BTP-Construction · SEO+IA (FR) » (+ 15 brouillons). Contraire à la règle « jamais de cold depuis le domaine principal ».
- **V7** decuplersystems.com (suspendu) est encore expéditeur dans 15 campagnes, aucune en cours.
- **V8** Lemlist : 11 campagnes en cours, 2 en pause, 61 brouillons, 36 archivées. Crédits : 180 (offerts).
- **V9** Supabase « LinkedIn App » : `outbound_leads` 10 532 lignes, 57 audiences, `outbound_funded_companies` 201, `outbound_campaigns` 2. Le CRM existe ; il ne trace pas encore statut de contact / réponses / liste noire de façon systématique.
- **V10** `leads/2026-10-25/liste_icp1_v2.csv` **n'est pas dans le repo** (les CSV sont exclus de git, conteneur précédent effacé).

---

## 4. Chantiers (C)

### Bloc A · Infra et délivrabilité
- **C1** ✅ Vérifier dans Lemlist : 21 boîtes Zapmail connectées + lemwarm actif (V5). → Q1
- **C2** ✅ Annulé : decupler.fr est un domaine secondaire, autorisé (Q2).
- **C3** 🟡 Redirection 301 des 7 domaines Zapmail vers decupler.com (V3). → Q3 → activée dans Zapmail + Postmaster validé (Nathan) ; en HTTPS, page « Security check » (hCaptcha) au lieu d'un 301 direct : demander au support Zapmail un 301 simple
- **C4** ⬜ GlockApps 1 boîte par domaine, 16 domaines (D2) ; Zapmail après la chauffe. → Q4
- **C5** ⬜ Délistage Spamhaus / SURBL des domaines du groupe A (D3) + question SURBL « domaines sosies ». → Q5
- **C6** ⬜ Nettoyer les expéditeurs decuplersystems.com des brouillons (V7).
- **C7** ⬜ Plan de capacité 10 000 approches/mois : boîtes, rampup, lots A/B (D1, K6).
- **C8** ⬜ Infra Microsoft (Azure / Hypertide) : étude seulement, plus tard (D4). (N9)

### Bloc B · Outils (envoi, données, enrichissement)
- **C9** ✅ Comparatif outil d'envoi : Lemlist vs Instantly vs PlusVibe (prix réels, base de leads incluse, détection ESP, SuperSearch, blocklist, API / MCP), date de renouvellement Lemlist, recommandation. (N13, N18, N19, N20) → Comparatif fait (`copy/26_comparatif_outils.md`) : reco Instantly Hypergrowth + crédits SuperSearch, ≈ 320 $/mois contre ≈ 535 $ Lemlist ; décision Nathan avant le 10/11
- **C10** ✅ Comparatif fournisseurs de données : Moltsets (D13), Monid, Treg, base Instantly, base Lemlist, dataset UltB ; plus le sort de FullEnrich (1 045 crédits) et Outscraper. (N13, N16, N17, N29) → Comparatif données (26) : Moltsets 97 $/mois (couverture non publiée), Monid/Treg = agrégateurs ; FullEnrich gardé en appoint
- **C11** ✅ Outil MX gratuit pour classer Google / Microsoft / autre (script DNS maison, gratuit) intégré au pipeline (D6). (N9) → `scripts/mx.py` (DNS-over-HTTPS gratuit), utilisé dans 35_build_campaign.py
- **C12** ✅ Coût intention SEO : test DataForSEO baisse de trafic sur 100 entreprises (D18) + API SERP la moins chère pour le « concurrent au-dessus » (D19) + OpenSEO. (N17, N25, N27) → Coûts : trafic DataForSEO ≈ 0,13 cent/domaine, SERP ≈ 0,06 cent/requête → ≈ 0,3 cent/entreprise ; test réel sur 100 entreprises à lancer (≈ 0,30 $)

### Bloc C · Base centrale (CRM)
- **C13** ✅ Faire du Supabase existant la base centrale : statut par contact (jamais contacté, en campagne, répondu, positif, RDV, client, ne pas contacter), date, campagne, ESP, pays, sous-ICP ; synchro depuis l'outil d'envoi (D15). (N7, N21) → Supabase « Outreach Cold Mail » (projet teuvlvovgjjlbxdnxdtc) : 17 tables + vues, accès script via fonction `ingest` (jeton hors repo)
- **C14** ✅ Liste noire : clients + tous ceux qui ont répondu + désinscrits + concurrents ; import dans la blocklist de l'outil d'envoi (D14). (N21) → do_not_contact : 8 495 emails et 6 891 domaines contactés (+ désinscrits, répondus) + 11 domaines clients ; à compléter : domaines de Cloudtech, BT Blue, TechMedias, Orators, L'Artisan d'à côté
- **C15** ✅ Brancher `check_deja_contacte.py` sur la base centrale (aujourd'hui il ne lit que Lemlist). → 42_import_leads.py contrôle email + domaine contre do_not_contact, et Lemlist dédoublonne

### Bloc D · Tableau ICP segmenté (fondation, prioritaire selon Igor)
- **C16** ✅ Grille de nommage ICP granulaire (D8, N11) : ICP 1.x B2B, 2.x services locaux / partenariat à la performance, 3.x santé / tourisme médical, 4.x bien-être / hôtellerie… (proposition en Q10). → 35 sous-ICP codés (1.1 → 4.4) dans `scripts/icp_catalog.py` et Supabase
- **C17** ✅ Pour chaque sous-ICP : mots-clés industrie, effectifs ≥ 5, pays, langue, ESP, titres décideurs / champions (D10), pains liés au service, VP, cas client, lead magnet, signaux, priorité pyramide, volume estimé. (N7, N10, N11) → Pour chaque sous-ICP : mots-clés FR/EN, pays, pains, preuve, unité, personas, taille de marché (base Lemlist)
- **C18** ✅ Nouveaux sous-ICP de Nathan : M&A France (N23), cybersécurité (N26), greffe de cheveux / implants dentaires à l'étranger (N22), rideaux métalliques, monte-escaliers, pompes funèbres, panneaux solaires, sécurité incendie (N22), pompes à chaleur / climatisation (N28). → M&A (1.7), cybersécurité (1.4), PAC/clim (2.2), rideaux métalliques (2.4), monte-escaliers (2.5), pompes funèbres (2.6), solaire (2.3), sécurité incendie (2.7), greffe (3.1), dentaire (3.2), maisons de retraite (4.3), spa (4.2)…
- **C19** ✅ Liste des pays par sous-ICP et par langue, pour Igor et pour Apify (D7, N8). → 27 pays, langue et vague (table countries)
- **C20** 🟡 Envoyer le tableau à Igor puis lui demander le dataset (D16, N14). → Mail rédigé (`copy/29_mail_igor_28-10.md`), à envoyer par Nathan

### Bloc E · Sourcing
- **C21** ✅ Pyramide par sous-ICP : palier 1 « a levé + recrute », palier 2 « recrute », palier 3 « marché principal » (D12, K17, N12). → Pyramide appliquée : palier 2 « recrute en marketing » (102) + palier 3 ; levées < 6 mois introuvables dans Lemlist pour la France
- **C22** ⬜ Apify multi-pays (offres d'emploi LinkedIn / Indeed) sur les pays retenus (N8).
- **C23** ⬜ Levées de fonds hors France (sources gratuites + Apify).
- **C24** ✅ Décideurs multiples par entreprise (D11, N15) + emails vérifiés (Lemlist / Instantly / FullEnrich selon C10). → 2-3 contacts par entreprise rangés par rôle ; emails FullEnrich (DELIVERABLE / HIGH_PROBABILITY, catch-all exclus)
- **C25** ✅ Split ESP de chaque liste (C11) puis contrôle « jamais contacté » (C15). → Split MX + liste noire à chaque campagne

### Bloc F · Copy et lead magnets
- **C26** ✅ Une séquence par sous-ICP × groupe (décideur / champion) × langue, dans le format Igor (6 étapes, R.E.P.L.Y./AAA, CTA permission) (D8, D11). → H6 (décideur, question ChatGPT), H7 (AAA + vidéo 2 min), H8 (champion), H9 (partenariat performance), H12 (concurrent devant) en FR et EN, 6 étapes
- **C27** ✅ Message « partenariat à la performance » pour les services locaux FR et étrangers : « je cherche des partenaires prêts à prendre 10 nouveaux clients / chantiers » (N22). → H9 « prêt à prendre 10 [unités] de plus par mois ? » + vidéo 3 min en VP2
- **C28** ✅ Variable « concurrent au-dessus de vous » en corps et en objet (K16, C12). → H12 rédigée (objet + corps) ; à brancher sur l'API SERP
- **C29** ✅ Tableau des lead magnets : avatar, effort / coût, étape du funnel, étape de séquence, métrique (D21, K19). À envoyer à Igor. → 13 lead magnets « mail / appel » (table lead_magnets + doc 28)
- **C30** ✅ Bibliothèque d'hypothèses mise à jour (H par sous-ICP) dans `copy/25`. → Hypothèses H6 à H12 (table hypotheses)

### Bloc G · Campagnes
- **C31** ✅ `101-G-1` (ancienne infra, prospects Google) sur la liste ICP 1 v2 : décideurs Lemlist, 36 emails avec les 180 crédits, séquence (étape 4c du 28/10). → Q18, Q19, Q20 → remplacée par 101 / 102 (liste ICP 1 v2 perdue) : 101-G-9 = 101 leads, 102-G-7 = 135 leads, en brouillon
- **C32** ⬜ `101-O-1` après la chauffe Zapmail (~6-9/11).
- **C33** ✅ Synthèse de toutes les campagnes : prospects uniques, réponses humaines, positives, RDV, et ce qu'on améliore (N24). Lecture Lemlist gratuite. → `copy/27_synthese_campagnes.md`

### Bloc H · Coaching Igor et suivi
- **C34** ✅ Reporter les décisions D1-D27 dans le CR Igor (artifact G6GFRkatP6ZjJhJ1TaWXi4) et dans le point d'étape (étape 4a du 28/10). → CR Igor : tableau des décisions D1-D27 en tête de l'onglet Session 3
- **C35** ✅ Mettre à jour la Base Copy (artifact Tnfz61qnYrMkJdqLtHCF4g) avec les sous-ICP et les hacks Igor (N5). → section « Machine 28/10 » (#machine2810) : campagnes 101/102, séquences H9 et H7 complètes, hypothèses H6-H12, 35 sous-ICP.
- **C36** ✅ Mail de devoirs à Igor (D24) : brouillon à préparer. → `copy/29_mail_igor_28-10.md`
- **C37** ⏸ 2e paiement + preuve (D25) : Nathan.
- **C38** ⬜ Rapports d'appels de vente d'Igor + guide 8 étapes : à archiver dans le repo (D23).

---

### Bloc I · Ajouts du 28/10 (2e retour de Nathan)
- **C39** ✅ Suivi de santé gratuit sans GlockApps : taux de réponse humaine par boîte et par domaine (API Lemlist), listes noires par DNS (SURBL, Spamhaus DBL, script), Google Postmaster Tools, score lemwarm. Rapport hebdo. → `scripts/37_health.py` (DNS, SURBL, Spamhaus, redirection) → tables sending_domains / health_checks ; Postmaster validé sur les 7 domaines
- **C40** ✅ Schéma Supabase « outreach » : entreprises, contacts, sous-ICP, pays, intentions, campagnes, hypothèses, lead magnets, boîtes et domaines, contrôles de santé, liste noire, événements de contact. Tables liées. → Schéma créé
- **C41** ✅ Lead magnets « en deux temps » : une partie offerte par mail, le reste « je vous le montre en appel » (K19). Chaque lead magnet a sa version mail et sa version appel. → Chaque lead magnet a sa partie mail et sa partie appel
- **C42** ✅ Pays riches et peu concurrentiels : Maroc, Tunisie, Arabie saoudite, Émirats, Afrique subsaharienne solvable, US, + pays d'Igor. → Pays ajoutés (MA, TN, SA, AE, CI, SN, NG, KE, ZA, GH, US)

### Bloc J · Ajouts du 28/10 (phase autonome)
- **C43** ⬜ Lots O (101-O, 102-O) : envoi après la chauffe Zapmail (~6/11) ; si bascule Instantly le 10/11, réimporter les mêmes leads (emails déjà trouvés).
- **C44** ⬜ Réglages Lemlist à faire à la main avant le go : expéditeurs (lot G = boîtes PremiumInboxes, lot O = boîtes Zapmail), tracking désactivé, texte brut, envoi lun-ven 7h30-14h, limites de rampup.
- **C45** ⬜ Enregistrer la vidéo de 2 min (H7) et la vidéo d'audit 3 min (H9, après le « oui ») : prérequis des séquences.
- **C46** ⬜ Brancher H6 (question ChatGPT par entreprise, API OpenAI ≈ 0,5 cent) et H12 (concurrent devant, API SERP) pour la 2e vague.
- **C47** ⬜ Niches locales mal couvertes par LinkedIn (rideaux métalliques, pompes funèbres, monte-escaliers) : Google Maps via Outscraper (clé à ajouter dans l'environnement d'une nouvelle session).
- **C48** ⬜ Campagnes hors France (EN) : sous-ICP 3.x tourisme médical (Turquie, Tunisie, Maroc) et 2.x / 4.x au Royaume-Uni, aux Émirats, aux États-Unis.
- **C49** ⬜ Brouillons 103-G-7 / 103-O-7 vides (M&A fusionné dans 102) : à réutiliser pour la prochaine campagne ou à archiver.

## 5. Correspondance avec le message de Nathan du 28/10 (N)

| N | Sujet | Va dans |
|---|---|---|
| N1 | Lecture des fichiers | fait |
| N2 | Règles permanentes | BRIEF.md (inchangé) |
| N3-N4 | Retour session 3 puis étapes 4a, 4b, 4c | C34 · C1-C3 + V1-V9 · C31 |
| N5 | Suivre les artifacts CR Igor et Base Copy | C34, C35 |
| N6-N7 | Fireflies 20/10 et 27/10 : toutes les actions | D1-D27, C1-C38 |
| N8 | Apify multi-pays (FR, UK, CH, TN, MA, SA, AE, Afrique subsaharienne) | C19, C22, Q12 |
| N9 | Split Azure / Google | D1, D6, C8, C11 |
| N10 | Split B2B : tech seule, conseil seul… | D8, C16, C17 |
| N11 | Nommage ICP 1.2… | C16, Q10 |
| N12 | Pyramide hiring / funding | C21 |
| N13 | Base Instantly ou mieux | C9, C10 |
| N14 | Demander le dataset à Igor | C20, Q16 |
| N15 | Plusieurs décideurs par boîte | D11, C24, Q14 |
| N16 | Moltsets | D13, C10 |
| N17 | Monid, Treg, OpenSEO | C10, C12 |
| N18 | PlusVibe | C9 |
| N19-N20 | Instantly 20 % / SECRET20 | C9, Q7 |
| N21 | Base : ne pas contacter + déjà contactés | C13, C14 |
| N22 | Sous-ICP services locaux + tourisme médical, partenariat performance | C18, C27, Q11, Q12 |
| N23 | M&A France | C18 |
| N24 | Synthèse par campagne | C33 |
| N25 | Intentions : hiring, funding, SEO, autres | C12, C21, Q13 |
| N26 | Cybersécurité | C18 |
| N27 | Baisse de trafic (baisse, concurrent) | C12, Q13 |
| N28 | Niche PAC / clim + « idées de mes reprises » | C18, Q15 |
| N29 | FullEnrich et Outscraper | C10, Q8 |

---

## 6. Questions à Nathan (Q)

Voir le message du 28/10 dans la conversation ; les réponses sont reportées ici au fil de l'eau.

| Q | Question | Statut |
|---|---|---|
| Q1 | Boîtes Zapmail connectées + lemwarm (capture) | ✅ connectées (Nathan, 28/10) |
| Q2 | Go pour retirer nathan@decupler.fr de « BTP-Construction » | ✅ decupler.fr = domaine secondaire, autorisé. Seul decupler.com est interdit. C2 annulé. |
| Q3 | Redirections des 7 domaines : qui / accès | ✅ redirection demandée par Nathan ; je fournis le prompt Claude in Chrome (C3) |
| Q4 | Budget GlockApps pour 16 tests | ✅ 3 tests faits (dans l'artifact). Suivi santé sans GlockApps à construire (C39) |
| Q5 | Délistage + noms des futurs domaines | ✅ go délistage |
| Q6 | Date de renouvellement Lemlist + budget outil | ✅ Lemlist se renouvelle le 10/11/2026 |
| Q7 | Outil de l'offre SECRET20 | ✅ SECRET20 = Instantly. PlusVibe à étudier (envoi + crédits d'enrichissement pour le même budget) |
| Q8 | FullEnrich / Outscraper : garder ? solde Outscraper | ✅ Outscraper : 15 $ de réduction chaque mois. Tous les outils sont à trancher dans le comparatif |
| Q9 | Budget global tests de données | ✅ « tu me dis » → enveloppe proposée en Q27 |
| Q10 | Validation de la grille ICP | ✅ beaucoup plus granulaire : 1 niche = 1 sous-ICP (ex. rideaux métalliques ≠ monte-escaliers), ajouter hospitalité, maisons de retraite, spa, etc. |
| Q11 | Mécanique du partenariat à la performance | ✅ pas de mécanique figée : « on cherche des boîtes X qui veulent Y, on a fait Z, seriez-vous contre… » ; Claude propose la meilleure copy |
| Q12 | Pays × langue × ICP | ✅ FR : France, Suisse romande, Tunisie, Maroc. EN : UK, Arabie saoudite, Dubaï, pays d'Igor, US. Tourisme médical = cliniques en Turquie, Tunisie… qui cherchent des patients étrangers. Afrique subsaharienne : pays solvables où le cold mail marche (au choix de Claude) |
| Q13 | Sens de « baisse de trafic interne » + autres intentions | ✅ Claude cherche les meilleures intentions, les croise avec les copy et estime le coût par outil (C12) |
| Q14 | Combien de décideurs par entreprise | ✅ 3 contacts max par entreprise parmi : CEO, fondateur, CMO, responsable growth, responsable SEO, responsable communication, directeur commercial |
| Q15 | « Idées de mes reprises » | ✅ abandonné |
| Q16 | Envoi du tableau et demande de dataset à Igor | ✅ mail à Igor rédigé dans la conversation du 28/10 |
| Q17 | Base centrale : Supabase existant ? | ✅ Supabase = base centrale ; créer des tables dédiées outreach / cold mail (C13) |
| Q18 | Liste ICP 1 v2 introuvable | ✅ nouvelles campagnes, 121 entreprises c'est trop peu |
| Q19 | 101-G-1 : 36 emails < 100 leads minimum | ✅ campagne = 100 min, **300 leads max**. Recharge décidée après le choix de l'outil |
| Q20 | Angle de 101-G-1 | ✅ pas besoin du transcript anglais ; Claude propose les hypothèses |
| Q21 | Cas clients citables par ICP | ✅ chercher les chiffres sur decupler.com, puis questions si besoin |
| Q22 | Lead magnets : lesquels et qui produit la vidéo | ✅ partir des idées de la Base Copy + consignes Igor, proposer ; Nathan valide |
| Q23 | Où vit le tableau segmenté (Google Sheet partagé ?) | ✅ tableau segmenté dans Supabase (tables liées), géré par Claude |
| Q24 | Liste des clients pour la liste noire | ✅ liste noire = tous les contacts Lemlist + clients (site decupler.com + mémoire) |
| Q25 | Date de la prochaine session + mail de devoirs | ✅ session mardi 03/11/2026. Mail envoyé aujourd'hui ; setup, ICP, scrape et copy terminés aujourd'hui |
| Q26 | Ce que je peux faire sans attendre | ✅ go |

### Dernier tour de questions (28/10, avant la phase autonome)
Sans réponse, Claude applique la valeur par défaut indiquée.

| Q | Question | Défaut | Statut |
|---|---|---|---|
| Q27 | Enveloppe de dépenses pour la journée | DataForSEO ≤ 10 $, Apify dans les 5 $ gratuits, FullEnrich ≤ 1 000 crédits déjà payés, Lemlist 180 crédits offerts ; 0 € de nouvel abonnement | ✅ DataForSEO ou autre outil moins cher ; estimer le coût d'abord |
| Q28 | Comptes d'essai à créer par Nathan (Instantly, PlusVibe, Moltsets, Monid) + clés API | comparatif sur infos publiques seulement | ✅ chercher sur le web (pas de comptes d'essai) |
| Q29 | Clé API Outscraper (et clé Apify régénérée ?) | pas de scraping Google Maps | ✅ OUTSCRAPER_API ajoutée ; garder la clé Apify |
| Q30 | Tables Supabase dans le projet « LinkedIn App », schéma séparé `outreach` | oui | ✅ nouveau projet Supabase dédié, au même niveau que LinkedIn App |
| Q31 | Campagnes créées en brouillon dans Lemlist (rien lancé) malgré le renouvellement du 10/11 | oui, lots G seulement | ✅ brouillons Lemlist, toujours scindés par ESP ; remplir le tableau ICP + messages + lead magnets |
| Q32 | Apify au-delà de 5 $ (plan payant) pour le scrape multi-pays | non | ✅ si ça ne suffit pas, Claude dit quel abonnement et Nathan recharge |
