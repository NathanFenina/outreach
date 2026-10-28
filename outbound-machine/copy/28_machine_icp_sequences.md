# 28 · Machine cold mail : tableau ICP segmenté, intentions, lead magnets, séquences (28/10/2026)

Source de vérité : base Supabase **« Outreach Cold Mail »** (projet `teuvlvovgjjlbxdnxdtc`), tables `icp_segments`, `personas`, `intents`, `lead_magnets`, `hypotheses`, `messages`, vue `v_segment_messages` (chaque séquence rendue pour chaque sous-ICP). Catalogue versionné : `scripts/icp_catalog.py`, `scripts/sequences.py`. Tout est **proposé** tant que Nathan ne l'a pas validé.

## 1. Sous-ICP (35) et taille de marché
Taille = entreprises dans la base Lemlist (recherche gratuite du 28/10), par mots-clés du sous-ICP. « 11+ » et « 1-10 » = salariés (on garde ≥ 5 à l'extraction). Francophone = BE, CH, LU, MA, TN… ; anglophone = pays en anglais du sous-ICP.

| Code | Sous-ICP | Prio | Offre | FR 11+ | FR 1-10 | Franco. 11+ | Anglo. 11+ | Preuve |
|---|---|---:|---|---:|---:|---:|---:|---|
| 1.1 | Éditeurs SaaS B2B | 1 | OVI (SEO + IA) | 1186 | 2948 | 482 | 12911 | Cloudtech : 320 000 clics Google en 12 semaines |
| 1.2 | Startups IA et data | 2 | OVI (SEO + IA) | 6775 | 14471 | 6708 | 177856 | Cloudtech : 320 000 clics Google en 12 semaines |
| 1.3 | ESN et intégrateurs ERP / CRM | 1 | OVI (SEO + IA) | 2806 | 4069 | 3368 | 106892 | Cloudtech : 320 000 clics Google en 12 semaines |
| 1.4 | Cybersécurité | 1 | OVI (SEO + IA) | 1827 | 3458 | 887 | 15526 | Cloudtech : 320 000 clics Google en 12 semaines |
| 1.5 | Cabinets de conseil en stratégie et management | 1 | OVI (SEO + IA) | 4912 | 17837 | 2184 | 36851 | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 1.6 | Conseil financier, DAF externalisé, expertise comptable | 2 | OVI (SEO + IA) | 1207 | 2556 | 568 | 15613 | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 1.7 | M&A, fusions-acquisitions, transmission d'entreprise | 1 | OVI (SEO + IA) | 1585 | 2540 | 726 |  | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 1.8 | Gestion de patrimoine (CGP) | 2 | OVI (SEO + IA) | 1501 | 4107 | 906 | 941 | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 1.9 | Agences marketing et web (marque blanche GEO) | 2 | OVI (SEO + IA) | 2020 | 13161 | 1034 | 17291 | Académie Madelrieux : +46 % de clics Google en 3 mois |
| 1.10 | Agences événementielles et de conférenciers | 2 | OVI (SEO + IA) | 1010 | 3837 | 546 | 13706 | Académie Madelrieux : +46 % de clics Google en 3 mois |
| 1.11 | Cabinets RH et recrutement | 3 | OVI (SEO + IA) | 1207 | 4623 | 486 | 10587 | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 1.12 | Organismes de formation professionnelle | 1 | OVI (SEO + IA) | 4297 | 10629 | 1382 |  | Académie Madelrieux : +46 % de clics Google en 3 mois |
| 1.13 | Cabinets d'avocats d'affaires | 3 | OVI (SEO + IA) | 477 | 1431 | 459 | 595 | Le Point, Pluxee, Décathlon : +20 % de pipeline organique |
| 2.1 | Rénovation et entreprise générale | 2 | performance | 4250 | 9707 | 910 | 7646 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.2 | Pompes à chaleur et climatisation | 1 | performance | 1832 | 2554 | 759 | 14787 | Clim Confort, installateur de clim : 3,7 fois plus de clics Google en un an |
| 2.3 | Panneaux solaires et photovoltaïque | 1 | performance | 795 | 1316 | 310 | 920 | Clim Confort, installateur de clim : 3,7 fois plus de clics Google en un an |
| 2.4 | Rideaux métalliques et fermetures commerciales | 2 | performance | 24 | 28 | 14 |  | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.5 | Monte-escaliers et accessibilité | 1 | performance | 38 | 113 | 6 | 597 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.6 | Pompes funèbres | 2 | performance | 108 | 204 | 8 |  | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.7 | Sécurité incendie | 1 | performance | 868 | 1347 | 371 | 8158 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.8 | Menuiseries, fenêtres et vérandas | 2 | performance | 1864 | 2413 | 532 | 3652 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.9 | Toiture, couverture et isolation | 2 | performance | 2381 | 3449 | 688 | 15145 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.10 | Piscines et spas (installateurs) | 2 | performance | 961 | 1509 | 212 | 69 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.11 | Alarme et vidéosurveillance | 2 | performance | 928 | 1608 | 670 | 17067 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.12 | Cuisinistes | 3 | performance | 183 | 532 | 118 | 2822 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.13 | Déménagement | 3 | performance | 393 | 772 | 213 | 5431 | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 2.14 | Paysagistes | 3 | performance | 340 | 665 | 105 |  | L'Artisan d'à côté (BTP) : +20 nouveaux clients par mois |
| 3.1 | Greffe de cheveux (patients internationaux) | 1 | performance | 7 | 22 | 7 | 233 | aucune preuve sectorielle |
| 3.2 | Implants dentaires et facettes (tourisme dentaire) | 1 | performance | 64 | 74 | 24 | 591 | aucune preuve sectorielle |
| 3.3 | Chirurgie et médecine esthétique (tourisme médical) | 2 | performance | 96 | 197 | 33 | 389 | aucune preuve sectorielle |
| 3.4 | Chirurgie bariatrique | 3 | performance | 28 | 27 | 9 | 75 | aucune preuve sectorielle |
| 4.1 | Hôtels indépendants | 2 | performance | 2159 | 1976 | 464 | 2217 | aucune preuve sectorielle |
| 4.2 | Spas et centres de bien-être | 2 | performance | 1371 | 2064 | 674 | 7147 | aucune preuve sectorielle |
| 4.3 | Maisons de retraite et résidences seniors privées | 1 | performance | 291 | 404 | 207 | 31670 | aucune preuve sectorielle |
| 4.4 | Campings et résidences de tourisme haut de gamme | 3 | performance | 421 | 844 | 71 |  | aucune preuve sectorielle |

Limites : les mots-clés larges gonflent certains chiffres (1.2 « IA / data », 1.3 « IT services ») ; les niches très locales (2.4 rideaux métalliques : 52 en France) sont mal couvertes par LinkedIn → Google Maps (Outscraper) pour celles-là. Le tourisme médical est surtout en Turquie (3.2 dentaire : 591 cliniques de 11+ salariés hors France).

## 2. Personas (3 contacts max par entreprise)
- **B2B** : decideur #1 (CEO, Founder, Co-founder, Fondateur, Président…) : pipeline, croissance, coût d'acquisition · decideur #2 (CMO, Head of Marketing, Directeur marketing, Head of Growth, Responsable growth…) : demandes entrantes, part de voix face aux concurrents · champion #3 (SEO Manager, Responsable SEO, Content Manager, Responsable communication, Marketing Manager…) : feuille de route qui le fait briller auprès du décideur
- **PERF** : decideur #1 (Gérant, Owner, Founder, Fondateur, CEO…) : plus de clients sans payer d'avance · decideur #2 (Directeur commercial, Sales Director, Responsable commercial…) : volume de demandes qualifiées · champion #3 (Responsable marketing, Marketing Manager, Responsable communication, Patient Coordinator Manager, International Patient Manager…) : visibilité, demandes entrantes

## 3. Pays et langue
| Code | Pays | Langue | Vague | Raison |
|---|---|---|---:|---|
| FR | France | fr | 1 | marché principal |
| BE | Belgium | fr | 2 | francophone, proche |
| CH | Switzerland | fr | 2 | pouvoir d'achat élevé (Igor : DACH) |
| LU | Luxembourg | fr | 2 | pouvoir d'achat élevé |
| MA | Morocco | fr | 2 | francophone, peu concurrentiel (Nathan) |
| TN | Tunisia | fr | 2 | francophone, tourisme médical (Nathan) |
| CI | Côte d'Ivoire | fr | 3 | Afrique francophone la plus solvable |
| SN | Senegal | fr | 3 | Afrique francophone solvable |
| UK | United Kingdom | en | 2 | pays riche (Igor) |
| IE | Ireland | en | 3 | pays riche |
| DE | Germany | en | 3 | DACH (Igor) ; idéalement en allemand plus tard |
| AT | Austria | en | 3 | DACH (Igor) |
| NL | Netherlands | en | 3 | Benelux (Igor) |
| SE | Sweden | en | 3 | Nordiques (Igor) |
| NO | Norway | en | 3 | Nordiques (Igor) |
| DK | Denmark | en | 3 | Nordiques (Igor) |
| FI | Finland | en | 3 | Nordiques (Igor) |
| US | United States | en | 3 | plus gros marché (Igor, Nathan) |
| AE | United Arab Emirates | en | 2 | argent, peu concurrentiel (Nathan) |
| SA | Saudi Arabia | en | 2 | argent, déjà testé (Saudi AI) |
| QA | Qatar | en | 3 | argent |
| NG | Nigeria | en | 3 | Afrique anglophone, gros marché |
| KE | Kenya | en | 3 | Afrique de l'Est, tech |
| ZA | South Africa | en | 3 | Afrique la plus solvable |
| GH | Ghana | en | 3 | Afrique anglophone stable |
| TR | Turkey | en | 2 | tourisme médical (greffe, dentaire) |
| HU | Hungary | en | 3 | tourisme dentaire |

## 4. Intentions (pyramide d'Igor) et coût par entreprise
| Code | Intention | Détection | Outil | Coût / entreprise | Palier |
|---|---|---|---|---|---:|
| I1 | A levé des fonds (< 6 mois) | filtre Lemlist currentCompanyLastFundingRoundAt | Lemlist DB (recherche gratuite) | gratuit | 1 |
| I2 | Recrute en marketing / SEO / growth / contenu | filtres Lemlist jobPostingTitle + jobPostingDate (90 j) ; Apify LinkedIn Jobs en complément | Lemlist DB / Apify | gratuit | 1 |
| I3 | Recrute des commerciaux | jobPostingTitle « commercial / sales / business developer » | Lemlist DB | gratuit | 2 |
| I4 | Nouveau CMO / head of growth (< 6 mois) | filtre Lemlist currentPositionTenure « Less than 6 months » + titre | Lemlist DB | gratuit | 2 |
| I5 | Équipe marketing en croissance (+10 % sur 6 mois) | filtre Lemlist workforceGrowthMarketing | Lemlist DB | gratuit | 2 |
| I6 | Concurrent classé au-dessus sur le mot-clé principal | API SERP sur le mot-clé « service + ville » ou « catégorie » | API SERP (voir 26_comparatif_outils.md) | ≈ 0,0018 $ (3 SERP) | 2 |
| I7 | Absent des réponses ChatGPT sur sa catégorie | 10 questions de la catégorie posées à un modèle OpenAI, on relève les marques citées | API OpenAI (clé disponible) | ≈ 0,005 $ (estimation) | 2 |
| I8 | Baisse de trafic organique (> 10 % sur 12 mois) | historique de trafic estimé par domaine ; on ne garde que les baisses > 10 % | DataForSEO Labs ou équivalent | ≈ 0,0013 $ | 2 |
| I9 | Paie des Ads Google | technologie Google Ads détectée (filtre Lemlist currentCompanyTechnologies) | Lemlist DB | gratuit | 2 |
| I10 | Site faible : lent, pas de données structurées, pas de réponse directe | PageSpeed API (clé disponible) + lecture du balisage | Google PageSpeed (gratuit) | gratuit | 3 |
| I11 | Fiche Google faible (avis, catégories) : local | données Google Maps (note, nb d'avis) | Outscraper | à vérifier | 2 |
| I12 | Saison (clim avant l'été, PAC et isolation avant l'hiver) | calendrier, gratuit | aucun | gratuit | 3 |
| I13 | Aucun signal (marché principal) | industrie + effectifs + pays | Lemlist DB | gratuit | 3 |

Constat du 28/10 : le filtre « dernière levée < 6 mois » de Lemlist ne renvoie rien en France ; le signal recrutement en marketing (offres < 90 j) donne ~230 entreprises B2B en France. Conclusion conforme à Igor : le signal est le 1 %, le volume vient du palier 3 avec un message précis par niche.

## 5. Lead magnets en deux temps (consigne Igor : une partie par mail, le reste en appel)
| Code | Lead magnet | Effort | Étape funnel | Dans le mail | En appel | Étape séquence | Cibles |
|---|---|---|---|---|---|---:|---|
| LM1 | Les 10 questions ChatGPT où un concurrent est cité à votre place | eleve | contre_appel | 1 question + le concurrent cité, dans le mail | les 9 autres + ce qui fait citer le concurrent, en 15 min | 1 | 1.x |
| LM2 | 7 actions rapides GEO / SEO | eleve | contre_appel | 1 action concrète, donnée gratuitement dans le mail 3 | les 6 autres, adaptées à leurs priorités, en appel (« j'ai besoin de vos priorités pour bien les faire ») | 3 | 1.x, 2.x |
| LM3 | Extrait de l'Opportunity Map (3 lignes) | eleve | contre_appel | 1 ligne : requête, concurrent cité, manque à gagner estimé | les 2 autres lignes + la méthode, en appel | 1 | 1.x |
| LM4 | Top 10 mots-clés qui font perdre des demandes | moyen | contre_appel | 1 mot-clé + son volume + le concurrent devant | la liste des 10 + la page à créer pour chacun | 1 | 1.x champion |
| LM5 | « {{concurrent}} est devant vous sur {{mot-clé}} » | faible | avant_appel | le nom du concurrent + le mot-clé (objet + corps) | comment le dépasser, en appel | 1 | tous |
| LM6 | Vidéo de 3 min : site, fiche Google, avis | moyen | avant_appel | envoyée après le « oui » : les problèmes, sans la solution | la solution et le plan, en appel | 2 | 2.x, 3.x, 4.x |
| LM7 | Une page rendue « GEO ready », offerte | eleve | contre_appel | le diagnostic de la page en 2 lignes | la page réécrite, livrée après un appel de cadrage | 3 | 1.x |
| LM8 | Note du site sur 10 (Swokei) | faible | avant_appel | la note + le point qui coûte le plus de clients | le détail des 5 critères, en appel | 2 | tous |
| LM9 | Outil gratuit d'audit GEO (app Décupler) | faible | avant_appel | envoyé sur demande (« répondez outil »), jamais de lien au 1er mail | lecture des résultats ensemble | 5 | tous |
| LM10 | Plugin / setup Claude Code SEO | moyen | apres_appel | rien | proposé après l'appel aux petites structures à l'aise avec Claude (pas aux grands comptes) | — | 1.x petites structures |
| LM11 | Estimation des demandes perdues à {{ville}} | moyen | contre_appel | le volume de recherches mensuelles du service dans la zone | l'estimation complète + le plan, en appel | 1 | 2.x |
| LM12 | Roadmap de kick-off client, version 5/10 (Igor) | eleve | contre_appel | rien (uniquement pour ceux qui disent oui) | présentée en appel | — | tous |
| LM13 | Étude de cas A+B avant / après | faible | avant_appel | le chiffre clé dans le PS | le détail sur demande | 5 | tous |

Escalier (Igor) : étape 1 = offre forte qui demande un appel ; sans réponse, étape 3 = une ressource offerte gratuitement (1 action) + « le reste en 15 min » ; étape 5 = au revoir + outil gratuit sur demande (« répondez outil »).

## 6. Hypothèses et séquences
Critère de succès commun : ≥ 3 % de réponses humaines / prospects uniques et ≥ 20 % de positives / réponses, sur au moins 100 prospects.

- **H1** · ICP 1 · extrait de l'Opportunity Map (3 requêtes où un concurrent est cité) (cadre R.E.P.L.Y., intention I7, lead magnet LM3) · historique (25_convention_campagnes)
- **H2** · ICP 1 · top 10 mots-clés qui font perdre des leads (cadre AAA, intention I6, lead magnet LM4) · historique
- **H3** · ICP 1 · objet « concurrent mieux placé » + vidéo 3 min (cadre R.E.P.L.Y., intention I6, lead magnet LM6) · historique
- **H4** · ICP 2 · « je cherche des boîtes BTP qui veulent plus de clients » (commission) (cadre AAA, intention None, lead magnet LM6) · historique, remplacée par H9
- **H5** · ICP 2 · site offert + 97 €/mois (cadre AAA, intention None, lead magnet None) · historique
- **H6** · B2B décideur · question ChatGPT où un concurrent est cité, 1 dans le mail, 9 en appel ; VP2 = 1 action offerte (LM2) (cadre R.E.P.L.Y., intention I7, lead magnet LM1) · paliers 1-2 (signal)
- **H7** · B2B · AAA sans recherche + vidéo 2 min (marché principal) (cadre AAA, intention I13, lead magnet LM13) · palier 3
- **H8** · B2B champion · feuille de route chiffrée qui le fait briller (1 mot-clé dans le mail, 9 en appel) (cadre R.E.P.L.Y., intention I6, lead magnet LM4) · champions
- **H9** · ICP 2/3/4 · partenariat à la performance « 10 [unités] de plus par mois ? », VP2 = vidéo 3 min des problèmes (cadre AAA, intention I13, lead magnet LM6) · Nathan N22
- **H12** · Tous ICP · variante VP1 : « {{concurrent}} devant vous » (objet + corps), hack Igor (cadre R.E.P.L.Y., intention I6, lead magnet LM5) · à tester après H6/H9

Séquences complètes (6 étapes, FR et EN) : `scripts/sequences.py` et vue Supabase `v_segment_messages`. Exemple rendu, H9 · 2.2 (PAC) · FR, mail 1 :

```
objet : chantiers en plus, {{firstName}} ?

Bonjour {{firstName}},

Vous seriez prêt à prendre 10 chantiers de plus par mois ?

Je cherche quelques installateurs de pompes à chaleur et de climatisation {{zone}} pour un partenariat à la performance : on travaille votre visibilité sur Google et ChatGPT, directement sur votre site, et vous payez sur les résultats.

Clim Confort, installateur de clim : 3,7 fois plus de clics Google en un an.

Seriez-vous contre que je vous explique comment ça marche ?

Nathan Fenina, fondateur de Décupler
PS : pas intéressé ? Répondez « stop ».
```

