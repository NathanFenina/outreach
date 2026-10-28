# 30 — Comparatif outils d'envoi + inboxes Microsoft (groupe C)

Lu le 2026-10-28. Prix en USD, HT, tels qu'affichés sur les pages lues ce jour. Tout ce qui n'a pas été trouvé dans une source est marqué **non trouvé**. Les hypothèses de calcul sont signalées **(hyp.)**.

Besoin Décupler : ~40 inboxes aujourd'hui, ~96 visées, ~10 000 prospects uniques/mois, ~50 000 emails/mois, ~7 500 emails à trouver et vérifier par mois. Indispensables : inboxes et warmup illimités, ESP matching (Google vers Google, bloquer ou router les destinataires Microsoft), blocklist, API/MCP, idéalement base de leads et crédits d'email finder.

---

## Partie 1 — Outils d'envoi

| | **Emelia** | **PlusVibe** | **Instantly** | **lemlist** |
|---|---|---|---|---|
| Plan adapté | Scale (Grow plafonné à 50 boîtes) [E1] | Business [P1] | Hypergrowth (Outreach) + crédits SuperSearch [I1][I2] | Email [L1] |
| Prix mensuel / annuel (par mois) | Scale 297 $ / 248 $ ; Grow 97 $ / 81 $ ; Start 37 $ / 31 $ [E1] | Business 77 $ / 64,20 $ (3K crédits) ; Personal 37 $ / 30,80 $ ; Agency dès 497 $ / 415 $ [P1] | Hypergrowth 97 $ / 77,6 $ ; Growth 47 $ / 37,6 $ ; Light Speed 358 $ / 286,3 $ [I1]. Note : un encart « bundle » de la même page affiche aussi un « Hypergrowth Plan » à 358 $/mois avec 5 000 crédits [I1] | Email 69 $ / 55 $ ; Multichannel 109 $ / 87 $ par utilisateur [L1] |
| Emails/mois | Illimités (tous plans) [E1] | 150 000 (Business) ; 25 000 (Personal) [P1] | 125 000 (Hypergrowth) [I1] | 50 000 (Email) [L1] |
| Contacts | Illimités [E1] | 100 000 leads actifs (Business) [P1] | 25 000 contacts uploadés (Hypergrowth) [I1] | Illimités [L1] |
| Limite d'inboxes | Start 3 / Grow 50 / Scale illimité [E1] | Non indiquée pour les plans payants (seul le plan Free est limité à 3) [P1] | Illimitées (« Unlimited Email Accounts ») [I1] | Senders illimités (plan Email) [L1] |
| Warmup inclus | Oui, illimité sur Grow et Scale [E1] | Oui : Basic (Personal), Advanced (Business) [P1] | Oui, illimité [I1] | Oui, lemwarm inclus [L1] |
| ESP matching / routage | **Non trouvé** (seulement une « multi-sender rotation » sur la page pricing) [E1] | Oui. Basic sur tous les plans, Advanced sur Business : on définit quels comptes envoient vers quels ESP destinataires, avec des tags. Sans compte correspondant, l'envoi part de n'importe quel compte [P1][P2] | Oui. Toggle « Provider Matching » par campagne ou par workspace, plus des règles de routage personnalisées, dont des règles « Do Not Send » qui bloquent une route (ex. Others vers Microsoft). Plan requis : non trouvé [I3] | Oui, « Email provider matchmaker » (Google/Microsoft via MX). Il exige au moins 1 boîte Google et 1 boîte Microsoft connectées. Sans correspondance, l'email part du pool par défaut : pas de blocage documenté. Plan requis : non trouvé [L2] |
| Blocklist | Oui, guide « blocklist / exclusions » [E3] | Non trouvé | Non trouvé sur les pages lues | Non trouvé sur les pages lues |
| Base de leads | Oui : « scraping », Email Finder / Verifier / Phone Finder [E1] | Crédits d'enrichissement ; extension Chrome « Lead Scraper » [P1] | Base de 450M+ leads (SuperSearch) [I1] | Base de 650M+ leads, incluse dans tous les plans [L1] |
| Crédits / prix par email trouvé | 1 crédit par email trouvé, ≈ 0,019 $. Vérification : 0,25 crédit (≈ 0,0048 $). Add-on dès 19 $/mois (1 000 crédits), puis paliers 5K/10K/50K/100K. Crédits valables 1 an. Scale inclut 5 000 crédits [E1][E2] | Paliers Business : 3K 77 $, 7K 92 $, 15K 119 $, 30K 165 $, 50K 220 $ (prix total du plan). **Crédits consommés par email : non trouvé** [P1] | Email vérifié : « 1,5 crédit en moyenne » ; vérification : 0,25 crédit. Paliers : Supersonic 2 (7 500 crédits) 147 $, Hyper (10 000) 197 $, Hyper 2 (20 000) 300 $. -10 % en annuel. Crédits mensuels expirés après 2 mois [I2] | 5 crédits par email trouvé et vérifié = 0,05 $ (1 crédit = 0,01 $). Plan Email : 0 crédit inclus. Add-on 2 000 crédits = 20 $/mois ou 16 $ en annuel [L1][L3] |
| API / MCP | « API access / Webhooks » listés, sans détail par plan. MCP officiel non trouvé (seul un MCP tiers viaSocket existe) [E1][E4] | API + webhooks sur Business. Le tableau mentionne un « custom MCP server », sans préciser le plan [P1] | « API, webhooks and integrations » [I1]. Serveur MCP sur mcp.instantly.ai, accès « any plan » selon Reply.io (source concurrente) [I4] | API, CLI et MCP inclus dans tous les plans [L1] |
| Essai gratuit | 7 jours, sans carte bancaire [E1] | 14 jours [P1] | « No credit card required » / « Start free » [I1]. 14 jours selon le blog Instantly [I4]. Allocation d'essai : 1 000 emails, 250 contacts, 100 crédits [I5] | 14 jours + 200 crédits (FAQ) ; une bannière annonce un essai étendu à 30 jours (offre limitée) [L1] |
| Promo | — | — | Codes **ULTB20OFF1 / SECRET20 : aucune référence publique trouvée**. Aucun code sur la page pricing [I1][S1] | — |

### Coût mensuel pour notre usage (50 000 emails, 7 500 emails trouvés/mois, ~96 inboxes)

**Emelia — Scale** (il faut Scale pour dépasser 50 boîtes) :
- Plan : 297 $ par mois.
- Crédits : 7 500 trouvés × 1 crédit = 7 500 crédits. Si les 5 000 crédits « free » de Scale sont mensuels **(hyp., non précisé)**, il reste 2 500 crédits à acheter, soit 2 500 × 0,019 $ ≈ 47,50 $.
- Total ≈ **344,50 $/mois** en mensuel, ou 248 $ + 47,50 $ ≈ **295,50 $/mois** en annuel.
- Si les crédits inclus ne sont pas mensuels : 297 $ + 7 500 × 0,019 $ (142,50 $) = **439,50 $/mois**.
- La vérification (0,25 crédit) n'est pas comptée, car on suppose que l'email trouvé est déjà vérifié **(hyp.)**.

**PlusVibe — Business** :
- Avec l'hypothèse 1 crédit = 1 email trouvé **(hyp., ratio non trouvé)**, il faut 7 500 crédits. Le palier 7K ne suffit pas, donc palier 15K.
- Total **119 $/mois** en mensuel, **99,20 $/mois** en annuel.
- Si l'on accepte 7 000 emails/mois : 92 $ / 76,70 $.

**Instantly — Hypergrowth + SuperSearch** :
- Outreach : 97 $ en mensuel (77,6 $ en annuel).
- Crédits, scénario officiel « 1,5 crédit en moyenne » : 7 500 × 1,5 = 11 250 crédits, donc Hyper 2 (20 000 crédits) à 300 $. Le palier Hyper (10 000) ne suffit pas.
  - Total **397 $/mois** en mensuel.
  - En annuel : 77,6 $ + 300 $ × 0,9 = **347,60 $/mois**.
- Crédits, scénario « 1 crédit par email trouvé en propre » : 7 500 crédits, donc Supersonic 2 à 147 $.
  - Total **244 $/mois** en mensuel.
  - En annuel : 77,6 $ + 132,30 $ = **209,90 $/mois**.
- Attention : la limite de 25 000 contacts uploadés passe si l'on purge les contacts terminés **(hyp.)**.

**lemlist — Email** :
- Plan : 69 $ par mois (55 $ en annuel). 50 000 emails/mois exactement : aucune marge.
- Crédits : 7 500 × 5 crédits × 0,01 $ = 375 $ en mensuel. En annuel, au tarif de l'add-on (16 $ / 2 000 crédits = 0,008 $/crédit) : 37 500 × 0,008 $ = 300 $.
- Total **444 $/mois** en mensuel, ou 55 $ + 300 $ = **355 $/mois** en annuel.

| Outil | Mensuel | Annuel (par mois) |
|---|---|---|
| PlusVibe Business 15K | **119 $** | **99,20 $** |
| Instantly Hypergrowth + crédits | 244 $ à 397 $ | 209,90 $ à 347,60 $ |
| Emelia Scale + crédits | 344,50 $ à 439,50 $ | 295,50 $ à 390,50 $ |
| lemlist Email + crédits | 444 $ | 355 $ |

### Recommandation Partie 1
1. **Instantly Hypergrowth** couvre le mieux le cahier des charges : inboxes et warmup illimités, 125k emails, règles de routage ESP avec « Do Not Send » pour bloquer Google vers Microsoft, MCP. Prévoir les crédits SuperSearch : budget ~245 à 400 $/mois.
2. **PlusVibe Business** est le moins cher (~119 $/mois) et propose un routage ESP avancé. Mais sans compte correspondant l'envoi part de n'importe quel compte, et le ratio crédits/email ainsi que la limite d'inboxes sont à confirmer pendant l'essai de 14 jours.
3. **lemlist (Email)** et **Emelia** sont écartés comme outil principal. lemlist plafonne à 50k emails et ne bloque pas les destinataires Microsoft. Emelia n'a ni ESP matching documenté, ni MCP officiel, et exige le plan Scale à 297 $ au-delà de 50 boîtes.

---

## Partie 2 — Inboxes Microsoft / Outlook (groupe C)

| Fournisseur | Prix | Minimum | Domaine | Inboxes/domaine | Envoi/inbox/jour | Type d'infra | Mise en route | Notes délivrabilité Outlook |
|---|---|---|---|---|---|---|---|---|
| **Zapmail** | Google et Microsoft au même prix. Starter 39 $/mois pour 10 boîtes (+3,50 $ par boîte en plus) ; Growth 99 $/30 (+3,25 $) ; Pro 299 $/100 (+3,00 $). « From 2,50 $ » en accroche [Z1] | Starter 39 $ (10 boîtes) [Z1] | Non inclus sur la page pricing. 15 $/an par domaine en plus (blog Zapmail) [Z2]. ZapShield : 3 $/domaine/mois [Z1] | 3 à 5 par domaine pour Outlook (help Smartlead) [Z3] | Rester sous 50/jour warmup inclus ; démarrer à 15/jour [Z3] | Microsoft 365 annoncé ; un workspace isolé par domaine [Z3]. Tenant réel : non précisé sur la page pricing | « Instant », 5 min en moyenne [Z1] | Pré-warmed dès 6 $/boîte [Z1] |
| **Hypertide Entra** | 25 $/domaine/mois, soit « 1 $/inbox » [H1] | Non indiqué [H1] | Inclus dans les 25 $/domaine **(hyp. : le produit est vendu « par domaine »)** | 25 [H1]. Les avis tiers parlent de 50 par domaine sur l'ancienne offre [H2] | Non trouvé par inbox. « 6 000+ » par domaine et par mois [H1] | Entra/Azure, « Native Outlook UI login », « tenant separation, unique domain & IP » [H1]. M365 réel : non précisé | Non trouvé pour Entra (Google : « live in hours ») [H1] | Un avis tiers évoque une bonne délivrabilité vers Outlook, sans test indépendant [H2] |
| **Primeforge** (Forge, l'offre Google/MS365 du groupe Infraforge/Mailforge) | 4,50 $/slot/mois, ou ≈ 3,76 $ en annuel (25 slots = 94 $/mois) [F3] | 10 slots [F3] | 14 $/an par .com [F3] | 2 à 3 [F3] | 30 recommandés, 100 max [F3] | « Google Workspace and MS365 mailboxes ». Tenant : non précisé [F3] | Non trouvé (DNS automatisé) [F3] | Non trouvé |
| **Infraforge** | 4 $/slot/mois (trimestriel) ; IP dédiée 99 $/mois [F1] | 10 slots [F1] | 14 $/an [F1] | 2 à 3 [F1] | 30 (100 max) [F1] | Serveurs SMTP privés, **pas Microsoft** [F1] | « Minutes » [F1] | Ne convient pas au groupe C (pas d'ESP Microsoft) |
| **Mailforge** | 3 $/slot/mois [F2] | 10 slots [F2] | 14 $/an [F2] | 2 à 3 [F2] | 30 (100 max) [F2] | Pool d'IP partagé, **pas Microsoft** [F2] | Non trouvé | Ne convient pas au groupe C |
| **PlusVibe DFY** | Microsoft 365 : 4,50 $/inbox/mois ; Microsoft Azure (agences) : 49 $/domaine/mois [P1] | Non trouvé (bundle de départ de 5 inboxes M365 cité) [P3] | Non trouvé | 3 maximum par domaine, 5 à 10 domaines par tenant [P3] | 30 à 50/jour [P3] ; montée de 10-15/jour à 50-80/jour en 4 semaines (blog) [P4] | M365 et Azure proposés séparément [P1] | Non trouvé | Non trouvé |
| **Instantly DFY** | Microsoft : **non trouvé**. DFY Google : 5 $/mois ; domaine 15 $/an [I5]. AirMail (infra propre) : 4 $/inbox [I6] | Non trouvé | 15 $/an [I5] | Non trouvé | Non trouvé | DFY = Google ; AirMail = infra Instantly, ni Google ni Microsoft [I6] | Non trouvé | Les comptes DFY sont mis en pause sans plan Outbound actif [I5] |
| **Maildoso** | SMTP : 30 boîtes = 75 $/mois (2,50 $), jusqu'à 0,49 $ par boîte en volume [M1] | 30 boîtes (plus petit plan) [M1] | 15 $/an (12 $/an selon une autre section) [M1] | 8 recommandés, 99 max [M1] | 15 cold/jour [M1] | SMTP propriétaire, **pas Microsoft** [M1] | Boîte : 5 min ; warmup ≥ 14 jours [M1] | Ne convient pas au groupe C |
| **ScaledMail** | Outlook : 50 $/domaine/mois, soit 2 $/boîte à 25 boîtes ; reporting +5 $/domaine [SM1] | Non indiqué [SM1] | Inclus dans le package [SM1] | 25 [SM1] | Jusqu'à 10/jour [SM1] | Non précisé (M365 ou Azure) [SM1] | 24 à 72 h [SM1] | Selon ScaledMail (concurrent), 50 boîtes par domaine augmentent le risque de blocage du tenant [SM2] |
| **Reply.io pre-warmed** (autre acteur connu) | 15 $/boîte/mois + 25 $/domaine/an ; 3 boîtes par domaine [R1] | Non trouvé | 25 $/an [R1] | 3 [R1] | Non trouvé | Microsoft parfois indisponible (« high demand ») [R1] | Pré-chauffé | — |

### Coût pour ~15 inboxes (5 domaines × 3) et ~30 inboxes (10 domaines × 3)

Le coût des domaines est ramené au mois (prix annuel / 12). Les offres « par domaine » (Hypertide, ScaledMail, PlusVibe Azure) sont pénalisées par un schéma à 3 boîtes par domaine. Elles sont donc chiffrées aussi en densité native.

| Fournisseur | 15 inboxes (5 dom.) | 30 inboxes (10 dom.) |
|---|---|---|
| **Zapmail** | 39 $ + 5 × 3,50 $ = 56,50 $ ; domaines 5 × 15 $/12 = 6,25 $. Total **≈ 62,75 $/mois** | Growth 99 $ ; domaines 10 × 15 $/12 = 12,50 $. Total **≈ 111,50 $/mois** |
| **Primeforge** | 15 × 4,50 $ = 67,50 $ ; domaines 5 × 14 $/12 = 5,83 $. Total **≈ 73,33 $/mois** | 30 × 4,50 $ = 135 $ ; domaines 10 × 14 $/12 = 11,67 $. Total **≈ 146,67 $/mois** |
| **PlusVibe M365** | 15 × 4,50 $ = **67,50 $/mois**, plus les domaines (non trouvé) | 30 × 4,50 $ = **135 $/mois**, plus les domaines (non trouvé) |
| **Hypertide Entra** | 5 dom. × 25 $ = **125 $/mois**. En densité native, 1 domaine de 15 boîtes = **25 $/mois** | 10 dom. × 25 $ = **250 $/mois**. En densité native, 2 domaines = **50 $/mois** |
| **ScaledMail Outlook** | 5 dom. × 50 $ = **250 $/mois**. En densité native, 1 domaine = **50 $/mois** (capacité 15 × 10 = 150 emails/jour) | 10 dom. × 50 $ = **500 $/mois**. En densité native, 2 domaines = **100 $/mois** (capacité 300 emails/jour) |
| **Reply.io** | 15 × 15 $ + 5 × 25 $/12 = **≈ 235,42 $/mois** | 30 × 15 $ + 10 × 25 $/12 = **≈ 470,83 $/mois** |
| **Instantly DFY Microsoft** | Non trouvé | Non trouvé |
| Infraforge / Mailforge / Maildoso | Hors sujet : pas d'inbox Microsoft | Hors sujet |

Capacité indicative à 30 emails/inbox/jour (reco Forge) : 15 inboxes donnent ~450 emails/jour, 30 inboxes ~900 emails/jour. Avec la reco Zapmail/Smartlead (15 à 20/jour), on tombe à ~225-300 et ~450-600 emails/jour.

### Recommandation Partie 2
1. **Zapmail** est le meilleur rapport prix/simplicité pour un groupe C en vraies boîtes Microsoft 365, avec 3 boîtes par domaine : ~63 $/mois pour 15, ~112 $/mois pour 30, un workspace isolé par domaine et une installation en quelques minutes.
2. **Primeforge** ou **PlusVibe M365** (4,50 $/boîte) sont des alternatives solides. PlusVibe est pertinent si l'outil d'envoi retenu est PlusVibe : facturation et routage ESP au même endroit.
3. **Hypertide Entra et ScaledMail Outlook** sont très bon marché en haute densité (25 boîtes par domaine) mais reposent sur Azure/Entra ou une infra non précisée. Ils sont à réserver à un test A/B de délivrabilité vers Outlook (GlockApps), pas au groupe C principal. Les offres SMTP (Infraforge, Mailforge, Maildoso) sont exclues.

---

## Sources (toutes lues le 2026-10-28)

- [E1] Emelia pricing : https://emelia.io/pricing
- [E2] Emelia pricing, section crédits : https://emelia.io/pricing
- [E3] Emelia, guide blocklist : https://emelia.io/guide/find-b2b-prospects/blocklist-exclusions
- [E4] MCP Emelia tiers (viaSocket) : https://viasocket.com/mcp/emelia ; listing : https://mcp.so/servers/emelia-mcp
- [P1] PlusVibe plans : https://plusvibe.ai/plans
- [P2] PlusVibe, guide ESP matching : https://help.plusvibe.ai/en/articles/10229396-email-service-provider-esp-matching-guide
- [P3] PlusVibe, préparation délivrabilité : https://help.plusvibe.ai/en/articles/9298690-how-to-prepare-yourself-for-optimal-email-delivery-at-plusvibe
- [P4] PlusVibe, limites Google/Microsoft 2026 : https://plusvibe.ai/blog/google-microsoft-sending-limits
- [I1] Instantly pricing : https://instantly.ai/pricing
- [I2] Instantly, système de crédits SuperSearch : https://help.instantly.ai/en/articles/11381241-supersearch-credit-system
- [I3] Instantly, ESP matching (19/11/2025) : https://instantly.ai/blog/esp-matching/
- [I4] Instantly MCP : https://instantly.ai/blog/mcp-server-vs-api-integration/ ; https://reply.io/blog/instantly-mcp/
- [I5] Instantly, vue d'ensemble des plans : https://help.instantly.ai/en/articles/10273259-instantly-plans-overview
- [I6] Instantly AirMail : https://instantly.ai/airmail
- [L1] lemlist pricing : https://www.lemlist.com/pricing
- [L2] lemlist, Matching ESP : https://help.lemlist.com/en/articles/12750538-use-matching-esp-to-improve-deliverability-in-lemlist
- [L3] lemlist, coût des leads (mis à jour le 24/09/2026) : https://www.lemlist.com/blog/how-much-do-leads-cost-in-lemlist
- [S1] Recherche web « ULTB20OFF1 / SECRET20 » : aucun résultat lié à Instantly
- [Z1] Zapmail pricing : https://zapmail.ai/pricing
- [Z2] Zapmail, accueil et blog (domaines à 15 $/an) : https://zapmail.ai/ ; https://docs.zapmail.ai/purchase-prewarmed-subscription-25774263e0
- [Z3] Smartlead × Zapmail FAQ : https://helpcenter.smartlead.ai/en/articles/280-google-and-outlook-mailboxes-by-zapmail-faqs
- [H1] Hypertide pricing : https://www.hypertide.io/pricing
- [H2] Avis tiers Hypertide : https://woodpecker.co/blog/hypertide/ ; https://coldiq.com/tools/hypertide
- [F1] Infraforge pricing : https://www.infraforge.ai/pricing
- [F2] Mailforge pricing : https://www.mailforge.ai/pricing
- [F3] Primeforge pricing : https://www.primeforge.ai/pricing
- [M1] Maildoso pricing : https://maildoso.ai/pricing
- [SM1] ScaledMail pricing : https://scaledmail.com/pricing
- [SM2] ScaledMail, page « alternative à Hypertide » (source concurrente) : https://www.scaledmail.com/alternatives/hypertide
- [R1] Reply.io, boîtes pré-chauffées : https://support.reply.io/en/articles/15479772-pre-warmed-domains-mailboxes

**Points à vérifier pendant les essais :**
- Le ratio crédits/email de PlusVibe.
- Si les 5 000 crédits Emelia Scale sont mensuels.
- Le plan Instantly requis pour les règles de routage ESP.
- L'incohérence Hypergrowth 97 $ / 358 $ sur la page Instantly.
- Le prix de Zapmail Microsoft après la 1re année.
- Le type de tenant (M365 réel ou Azure) chez Zapmail, Primeforge et ScaledMail.
