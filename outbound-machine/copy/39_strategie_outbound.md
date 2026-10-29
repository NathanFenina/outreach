# 39 · Stratégie outbound Décupler (état au 29/10/2026)

Document de référence : il remplace les morceaux éparpillés (REGISTRE, Sheet, copy/25, 28, 29, 34). Le détail chiffré vit dans le Sheet « UltB Academy_Kickoff_Nathan » (onglets 2, 2b, 5, 6b).

## 1. Objectif
Remplir l'agenda de Nathan en rendez-vous qualifiés SEO + GEO, sans payer chaque contact, avec la méthode d'Igor (UltB) : ICP très découpés, un message par palier d'intention, (VP + FU) × 3.
Critère de réussite d'une campagne : ≥ 3 % de réponses humaines et ≥ 20 % de réponses positives, sur ≥ 100 prospects.

## 2. Cibles (37 sous-ICP, France d'abord)
- ICP 1 B2B (1.1 à 1.13) · ICP 2 BTP et services locaux, partenariat à la performance (2.1 à 2.15) · ICP 3 tourisme médical (3.1 à 3.4) · ICP 4 hospitalité et bien-être (4.1 à 4.5).
- Priorités vague 1 : **104** SaaS / IA · **106** conseil, compta, M&A, CGP · **110** BTP + travaux publics · **114** hôtels, spas, campings.
- ≥ 5 salariés, 3 contacts max par entreprise : décideur, marketing / commercial, champion SEO / contenu.

## 3. Pyramide (un message par palier)
| Palier | Signal | Source | Coût |
|---|---|---|---|
| P1 | a levé < 6 mois ET recrute | à trouver (Lemlist : aucune donnée de levée en France) | — |
| P2 | recrute en marketing / SEO / growth (offre < 90 j) | base Lemlist (filtre offres d'emploi) | 0 € |
| P3a | trafic Google en baisse > 10 % | DataForSEO | ≈ 0,24 cent / domaine |
| P3b | un concurrent est n°1 sur le mot-clé business | gpt-4o-mini (mot-clé) + DataForSEO (volume + SERP) | ≈ 0,1 cent / entreprise |
| P3c | ChatGPT cite un concurrent, pas eux | OpenAI recherche web | ≈ 2 à 3 cents / entreprise |
| P4 | marché principal, sans signal | base Lemlist | 0 € |
Ordre d'envoi : P1 → P2 → P3 → P4. Une entreprise n'est que dans un seul palier.

## 4. Nommage
- Dataset : `DS-<campagne>-<sous-ICP>-<pays>-<palier>` (ex. DS-104-1.1-FR-P4).
- Campagne : `<n°>-<lot>-<palier>[-<sous-ICP>]` (ex. 104-M-P4-1.1, 121-G-P2). Vague 1 France = 1xx, vague 2 francophone = 2xx, vague 3 anglophone = 3xx.
- Lot = fournisseur email du prospect (MX) : **G** Google · **M** Microsoft / Outlook · **O** autres. Une campagne par lot pour lire les résultats par fournisseur.

## 5. Données et enrichissement (cascade)
1. **Recherche** : base People Lemlist (gratuite jusqu'au 10/11, quota ≈ 1 300 pages de 100) ; ensuite dataset Igor + Instantly SuperSearch ; Google Maps (Outscraper) pour les niches locales.
2. **Liste noire** Supabase (6 891 domaines déjà contactés, répondus, désinscrits, clients) : contrôle avant enrichissement et avant import.
3. **Qualification** du site par IA (≈ 0,02 cent) : retire hors cible, concurrents, fonds, médias, écoles, sites morts (≈ 20 %).
4. **Emails** : Moltsets d'abord (forfait, 66 % trouvés en A/B sur 104), puis FullEnrich sur les manques (+ 70 % des manques), on garde valide / probable, on écarte catch-all.
5. **Contrôles** : email du même domaine que l'entreprise, un email = une seule campagne.

## 6. Envoi
- **Instantly** (Hypergrowth, pris au dernier moment) : campagnes et séquences déjà créées en brouillon ; leads importés à l'abonnement (le plan gratuit bloque l'import).
- Boîtes : groupe A PremiumInboxes (9 domaines) → lot G ; groupe B Zapmail (7 domaines, 21 boîtes Google Workspace, chauffe jusqu'au ~6/11) → lots M et O. Test de placement Outlook sur 2 boîtes avant de monter.
- Jamais depuis decupler.com. Suivi d'ouverture et de clics coupé, texte seul, arrêt à la réponse.
- Lemlist : arrêt du renouvellement avant le 10/11, export complet fait (`scripts/52_export_lemlist.py`).

## 7. Copies
- Méthode Igor : R.E.P.L.Y. / AAA, ≤ 80 mots, objet < 5 mots, CTA d'intérêt orienté « non », aucun lien au mail 1, PS = une seule preuve client proche du prospect, PPS = sortie.
- Séquence : VP1 → FU1 J+3 → VP2 J+8 « 1 levier » → FU2 J+11 1-2-3 → VP3 J+21 « une page travaillée gratuitement » → FU3 J+24 rupture.
- Copies V2 dans l'onglet 6b (à valider par Nathan) ; bibliothèque L / B / F / I dans l'onglet 7.

## 8. Lead magnets (partie mail → partie appel)
1 question ChatGPT où un concurrent est cité → les 9 autres en appel · 1 levier GEO → les 6 autres · « pourquoi X est n°1 » → le plan pour passer devant · 1 page travaillée gratuitement (50 critères) + données structurées.

## 9. Calendrier
- Jusqu'au 6/11 : validation des copies, enrichissement 106 / 110 / 114, intent P3 sur 104, dataset Igor.
- 6-9/11 : Hypergrowth Instantly, connexion des boîtes, import des leads, test Outlook, lancement progressif (rampup UltB).
- Avant le 10/11 : annulation Lemlist.
