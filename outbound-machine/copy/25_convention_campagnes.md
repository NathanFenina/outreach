# 25 · Convention de nommage des campagnes (devoir Igor n° 8, 22/10)

Format : `N°-LOT-H · ICP · segment · angle`
Exemple : `101-G-1 · ICP1 · levée+recrute · Opportunity Map`, avec son jumeau `101-O-1`.

- **N°** : 3 chiffres, à partir de **101**. Les anciennes campagnes gardent leur nom. Un nouveau numéro = une nouvelle liste ou une nouvelle séquence.
- **LOT** : `G` = prospects sur Google (infra actuelle) · `O` = autres messageries (nouvelle infra). Microsoft, Mimecast et Proofpoint sont exclus. Plus tard : suffixe `-EN` pour hors France.
- **H** : n° d'hypothèse, écrit dans la bibliothèque avant le lancement, avec son critère de succès.

## Bibliothèque d'hypothèses (à valider avec Nathan et Igor)

| H | Hypothèse |
|---|---|
| 1 | ICP 1 · R.E.P.L.Y. + extrait de l'Opportunity Map (3 requêtes où un concurrent est cité) |
| 2 | ICP 1 · AAA + top 10 mots-clés qui font perdre des leads |
| 3 | ICP 1 · objet « concurrent mieux placé » + vidéo 3 min |
| 4 | ICP 2 · « je cherche des boîtes BTP qui veulent plus de clients » (commission) |
| 5 | ICP 2 · site offert + 97 €/mois |

Critère de succès proposé (à fixer avec Igor) : ≥ 3 % de réponses humaines / prospects uniques et ≥ 20 % de positives / réponses, mesuré sur au moins 100 prospects.

## Nouveaux angles proposés par Nathan (24/10), à soumettre à Igor le 27/10
Rédigés en entier dans l'artifact CR Igor, onglet « Session 3 » : https://claude.ai/artifact/G6GFRkatP6ZjJhJ1TaWXi4

| Angle | Hypothèse |
|---|---|
| A · BTP | « ouvert à 15 chantiers de plus ? » + partenariat à la performance (H4) ; relance « avez-vous l'équipe pour ? » |
| B · B2B | un fait vrai (levée, recrutement, actualité) + le concurrent que ChatGPT cite à leur place (H1) |
| C · B2B | volume d'un mot-clé où ils sont absents + liste des 10 recherches (H2) |
| D · B2B | une page rendue « GEO ready » offerte ; variantes : roadmap de 10 contenus, balisage entités / données structurées, feuille de route mot-clé |
| E · BTP | résultat + délai + paiement au résultat + vidéo d'audit 3 piliers (site, fiche Google, avis), d'après la vidéo Netswick |

Sources, vidéos lues avec Gemini le 24/10 :
- **Netswick, « This SEO Agency Closed $30K+ Using Cold Email »** : artisans / services à domicile ; 13 946 contacts, 585 réponses, 78 positives en un mois (1 pour 178). Mail : « [raison pertinente]. We can get you [résultat] in [délai] or you get a full refund. Can I share a quick 2-min video explaining how it works? ». Résultat dit avec les mots du métier. Aux répondants : vidéo d'audit 3 piliers (site, fiche Google, avis) qui montre le problème sans la solution (outil Tella).
- **ItsKeaton, « The Cold Calling Script That Makes Prospects Pitch Themselves »** : « vous pouvez prendre 3 ou 5 chantiers de plus, ou vous êtes complets ? » → « vous êtes sûr ? si je vous en donne 7 demain, il faut embaucher ? » (le prospect se vend) → « pas des leads, des rendez-vous qualifiés » → closing assumé « demain matin ou demain soir ? ».
- Le post Reddit « How I sold 200 websites in 12 months » n'a pas pu être lu (Reddit bloque l'accès).

## Inspiration Northwood Growth Partners (a prospecté Nathan, 16-24/10)
- Mail 1 en 2 lignes : « If you've got room for a few more clients, we help AI SEO agencies book meetings with businesses that aren't showing up in ChatGPT yet. Happy to send over a few details if you're keen. » → question de capacité, aucune promesse, aucun lien.
- Relance J+7 : « Wanted to bump this up. » + l'idée reformulée + « Would it be useful if I sent over an example campaign? »
- Leur modèle client : « Just typed 'best {{type}} in {{city}}' into ChatGPT and {{company}} didn't come up. Want to … show up first in your area? Asking because we've helped {{client}} generate {{result}} last month… Can I send over how we'd approach this for {{company}}? »
- Adaptés en N6 et N7 dans la Base Copy (https://claude.ai/artifact/Tnfz61qnYrMkJdqLtHCF4g).

## Sourcing : ce que Lemlist sait faire (vérifié le 25/10)
- La base « People database » de Lemlist (API `POST /api/database/people`) filtre par site d'entreprise (`currentCompanyWebsiteUrl`), titre, séniorité, pays, et a aussi des filtres natifs « offres d'emploi des 6 derniers mois » (`jobPostingTitle`, `jobPostingDate`) et « date de dernière levée » (`currentCompanyLastFundingRoundAt`).
- La recherche est gratuite ; trouver un email vérifié coûte 5 crédits (≈ 0,05 $). Solde au 25/10 : 180 crédits (= 36 emails).
- Test sur la liste ICP 1 v1 (136 entreprises) : 125 ont au moins un décideur dans Lemlist (110 sur les 121 sans alerte, 487 décideurs au total).
