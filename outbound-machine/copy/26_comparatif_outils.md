# 26 — Comparatif outils outbound (envoi, data, signaux SEO, MX)

> Recherche web publique, sans inscription. **Toutes les sources ont été lues le 2026-10-28.** Prix en USD HT, sauf mention contraire.
> « non trouvé » = l'info n'est pas publiée sur la source consultée. Rien n'est deviné. Les calculs (marqués *calc.*) sont faits à partir des prix publiés.
> Hypothèse de volume : ~40 boîtes d'envoi, 7 500 prospects/mois, 3 à 4 emails par prospect, donc **22 500 à 30 000 emails/mois**, et environ **7 500 emails vérifiés à trouver/mois**.

---

## A. Outils d'envoi

### A1. Lemlist (outil actuel, renouvellement le 2026-11-10)
Source : https://www.lemlist.com/pricing (lue le 2026-10-28, y compris les données de prix JSON intégrées à la page)

| Élément | Valeur publiée |
|---|---|
| Plan **Email** | 69 $/mois (mensuel), 55 $/mois (annuel, -20 %), trimestriel -10 %. **Utilisateurs et expéditeurs illimités**, 50 000 emails/mois |
| Paliers de volume du plan Email | 50k emails = 69 $ · 100k = 89 $ · 200k = 159 $ · 500k = 359 $ · 1M = 659 $ (mensuel) |
| Plan Multichannel | 109 $/mois (87 $ en annuel) par utilisateur, 5 expéditeurs par utilisateur, **+9 $/mois par expéditeur supplémentaire** |
| lemwarm | « included in all plans » (FAQ) |
| API / MCP / CLI | Inclus (« lemlist MCP & CLI », « CRM integrations & API ») |
| Base People | « 650M+ leads database », recherche dans la base incluse |
| Crédits | « $1 in credits covers 20 emails or 5 phone numbers » (5 crédits par email, 20 par téléphone). Facturés seulement sur résultat. **Les crédits non utilisés sont reportés tant que l'abonnement est actif** |
| Paliers de crédits (mensuel / trimestriel / annuel, par mois) | 2k : 20 / 18 / 16 $ · 5k : 49 / 44 / 39 $ · 10k : 94 / 85 / 75 $ · 25k : 225 / 203 / 180 $ · 50k : 441 / 397 / 353 $ · 100k : 833 / 750 / 666 $ · 200k : 1 568 / 1 411 / 1 254 $ |
| Signaux d'intention (add-on) | 29 $/mois (21 $ en annuel) pour 100 signaux |
| Routage selon l'ESP du destinataire | non trouvé sur la page de prix |

**Coût pour notre usage (*calc.*)** : 7 500 emails × 5 crédits = 37 500 crédits, donc palier 50k. Il est impossible de savoir si plusieurs paliers se cumulent (non trouvé).
- Mensuel : 69 $ + 441 $ = **510 $/mois**. Cela donne 0,044 $ par email trouvé, avec une marge de 2 500 emails.
- Annuel : 55 $ + 353 $ = **408 $/mois**.

### A2. Instantly
Sources : https://instantly.ai/pricing · https://help.instantly.ai/en/articles/11381241-supersearch-credit-system · https://help.instantly.ai/en/articles/11364248-supersearch · https://api.instantly.ai/openapi/api_v2.json · https://developer.instantly.ai/llms.txt · https://developer.instantly.ai/mcp/introduction.md · https://instantly.ai/blog/esp-matching/ (toutes lues le 2026-10-28)

| Plan Outreach | Mensuel | Annuel (par mois) | Emails/mois | Contacts importés | Boîtes / warmup |
|---|---|---|---|---|---|
| Growth | 47 $ | 37,6 $ | 5 000 | 1 000 | Illimitées / illimité |
| **Hypergrowth** | **97 $** | **77,6 $** | 125 000 | 25 000 | Illimitées / illimité |
| Light Speed | 358 $ | 286,3 $ | 500 000 | 100 000 | Illimitées |

La page propose aussi des bundles qui regroupent envoi et crédits : Starter 94 $ (85 $), avec 5 000 emails, 1 000 contacts et 1 500 crédits · **Scale 194 $ (175 $), avec 100 000 emails, 25 000 contacts et 5 000 crédits** · Agency 555 $ (500 $), avec 500 000 emails, 100 000 contacts et 10 000 crédits.
→ **Growth ne suffit pas** pour notre volume (5 000 emails et 1 000 contacts). Le minimum est Hypergrowth ou le bundle Scale.

**Crédits SuperSearch / Leads** (help center, page « mise à jour hier ») :
- Email pro : **1 crédit** s'il est trouvé par Instantly, **2 crédits ou plus** via un partenaire, **environ 1,5 crédit en moyenne**. Gratuit si rien n'est trouvé.
- Enrichissement : profil complet 0,5 · Job listings / Technologies / News / Funding 0,5 crédit chacun · vérification de lead 0,25.
- Plans de crédits (prix mensuels) : Nano 9 $ (150) · Growth 47 $ (1 500) · Growth 2 77 $ (2 000) · Supersonic 97 $ (5 000) · Supersonic 2 147 $ (7 500) · **Hyper 197 $ (10 000)** · **Hyper 2 300 $ (20 000)** · Hyper 3 500 $ (45 000) · Hyper 4 997 $ (100 000). Les crédits mensuels expirent 2 mois après l'achat.
- Base : « 450M+ B2B leads ». Filtres disponibles : localisation, technologies, offres d'emploi (hiring), type de financement, CA, mots-clés, signaux. « Live buying signals on 85% of companies ».
- Couverture par pays : **non trouvé**. Méthode de vérification et gestion des catch-all : **non trouvé**.
- Incohérence sur la page de prix : le plan Supersonic apparaît à la fois à 97 $ et à 197 $ pour 5 000 crédits. Il faut vérifier au checkout.

**Matching ESP et blocklist** (schéma API v2 officiel) :
- Chaque lead porte un champ `esp_code`, **détecté automatiquement par Instantly** : 1 = Google, 2 = Microsoft, 3 = Zoho, 9 = Yahoo, 999 = Other, 1000 = Not Found. Un champ `esg_code` signale aussi la passerelle de filtrage (Barracuda, Mimecast, Proofpoint, Cisco). Les leads se filtrent par `esp_code`. **La colonne ESP existe donc bien.**
- Au niveau de la campagne : `match_lead_esp` (matching ESP) et `provider_routing_rules`, avec action `send` ou `do_not_send`, `recipient_esp` [google / outlook / other] et `sender_esp`. **Exclure les destinataires Microsoft est donc natif** (règle do_not_send avec recipient_esp = outlook).
- Blocklist : endpoints `block-list-entries` (création, création en masse, suppression, export CSV).
- **MCP officiel** : « exposes the full Instantly V2 API as MCP tools » (developer.instantly.ai/mcp).
- API v2 sur le plan Growth : **non confirmé**. Plusieurs sources tierces indiquent Hypergrowth au minimum (https://feedback.featurebase.app/p/api-access-on-growth-plan, demande toujours « In Review »).
- Remises : le code **SECRET20 est introuvable** dans les sources publiques. Les 20 % de l'affiliation Igor n'ont pas été vérifiés.

**Coût pour notre usage (*calc.*)** : 7 500 emails × 1,5 crédit = 11 250 crédits.
- Option 1 : Hypergrowth 97 $ + Hyper 2 300 $ (20 000 crédits) = **397 $/mois**, soit environ 0,0225 $ par email.
- Option 2 (serrée) : Hypergrowth 97 $ + Hyper 197 $ (10 000 crédits, soit 6 700 à 10 000 emails) = **294 $/mois**, en complétant avec le reliquat FullEnrich.
- Option 3 : bundle Scale 194 $ (5 000 crédits) + Supersonic 2 147 $ (7 500) = 341 $/mois, soit 12 500 crédits. Rien n'indique publiquement que le cumul est possible.
- Avec 20 % de remise affiliée, si elle s'applique : Option 2 ≈ 235 $, Option 1 ≈ 318 $ (non vérifié).

### A3. PlusVibe
Source : https://plusvibe.ai/plans (lue le 2026-10-28)

| Plan | Mensuel | Annuel (par mois) | Crédits d'enrichissement/mois | Emails/mois | Leads actifs |
|---|---|---|---|---|---|
| Personal | 37 / 45 / 52 / 58 $ | 30,8 / 37,5 / 43,3 / 48,3 $ | 1k / 3k / 5k / 7k | 25 000 | 30 000 |
| **Business** | 77 / 92 / **119** / 165 / 220 $ | 64,2 / 76,7 / **99,2** / 137,5 / 183,4 $ | 3k / 7k / **15k** / 30k / 50k | 150 000 | 100 000 |
| Agency | à partir de 497 $ | 415 $ | sur mesure | 500 000+ | 1M+ |

- Valeur d'un crédit : d'après les équivalences affichées, 1k crédits = « 1000 Business Emails Found OR 2000 Email Verifications OR 5000 Websites Scraped ». On en déduit **1 crédit ≈ 1 email pro trouvé** (*calc.* à partir des ratios). Coût unitaire publié : non trouvé.
- Warmup : pool privé « 350k+ » sur tous les plans. Warmup « Basic » sur Personal, « Advanced » sur Business.
- Matching ESP : « Basic » sur Personal, « Advanced » sur Business et Agency. Le détail du fonctionnement est **non trouvé** (pas de description d'une règle « ne pas envoyer à Microsoft »).
- API : « API Access » listé dans le plan Business. Le tableau comparatif semble l'indiquer absent de Personal. « Custom MCP Server » est cité dans les intégrations.
- Nombre de boîtes connectables sur les plans payants : **non trouvé** sur la page. Le plan gratuit est limité à 3 boîtes. Des sources tierces parlent d'« illimité ».
- Base de leads intégrée (recherche ICP) : **non trouvé** sur la page. L'outil fonctionne en « email finder » à partir d'un nom et d'un domaine.
- Services annexes : création de boîtes Google Workspace 4 $/boîte/mois, Microsoft 365 4,5 $.

**Coût pour notre usage (*calc.*)** : Business 15k = **119 $/mois** (99,2 $ en annuel). 7 500 emails trouvés consomment 7 500 crédits, et les 7 500 restants servent à environ 15 000 vérifications. **Une source de prospects reste nécessaire**, puisque PlusVibe ne fournit pas de base de recherche.

### A4. Synthèse envoi (40 boîtes, 7 500 prospects, 7 500 emails trouvés)

| Outil | Plan | Coût mensuel | Annuel (par mois) | Coût par email trouvé | Matching ESP / exclusion Microsoft | API / MCP |
|---|---|---|---|---|---|---|
| Lemlist | Email + 50k crédits | 510 $ | 408 $ | 0,044 $ | non trouvé | Oui / Oui |
| Instantly | Hypergrowth + Hyper (10k) | 294 $ | ~255 $ | ~0,02–0,03 $ | **Oui, natif** (`esp_code` et règles de routage) | Oui / Oui |
| Instantly | Hypergrowth + Hyper 2 (20k) | 397 $ | ~348 $ | ~0,0225 $ | idem | idem |
| PlusVibe | Business 15k | 119 $ | 99 $ | ~0,016 $ (*calc.*) | « Advanced », détail non trouvé | Oui / MCP cité |

---

## B. Fournisseurs de données

| Source | Prix | Prix par email vérifié | Prix par entreprise | Signaux | Pays | API / MCP | Source (lue le 2026-10-28) |
|---|---|---|---|---|---|---|---|
| **Moltsets** | Free 0 $ (1k appels à vie) · Solo 27 $ · **Pro 97 $** (15k enrichissements et 7,5k recherches par 5 h) · Team 397 $ · Max 997 $. « Unlimited data », avec politique de fair use | non publié. Inclus dans le forfait, emails classés A–F, échecs retirés, pas de match = 0 | non publié (recherche par industrie, taille, CA, plus IP→entreprise) | **hiring / funding / tech / trafic : non trouvé** | **non trouvé** (seul l'email perso US-only est mentionné) | REST + **MCP**, même clé | https://moltsets.com/our-data/ · https://moltsets.com/pricing |
| **Monid** | Agrégateur pay-per-call, 2 800+ outils et 90+ fournisseurs (Apollo, PDL, Ahrefs…), 1 $ offert, exemple affiché « $0.0013 » par appel | dépend du fournisseur appelé : non trouvé | non trouvé | selon le fournisseur | non trouvé | **MCP**, Skill, CLI | https://monid.ai (page /pricing vide) |
| **Treg** | Passerelle pay-per-call, 117 fournisseurs et 4 000+ endpoints, 1 $ offert, sans marge sur les tarifs fournisseurs | Hunter : « from $0.0005/call » (prix d'appel, pas d'email trouvé garanti) | Crunchbase funding : 0,01 $/appel | hiring/headcount, funding, news (via fournisseurs) | non trouvé | API (docs, llms.txt). Le terme MCP n'est pas cité | https://treg.to |
| **Instantly SuperSearch** | voir A2 | ~1,5 crédit, soit 0,0225 $ (Hyper 2) à 0,09 $ (Nano) | profil complet 0,5 crédit, local business 2 crédits | Tech, Hiring, Funding, News à 0,5 crédit chacun, plus signaux | non trouvé | API v2 + MCP | voir A2 |
| **Lemlist People DB** | voir A1 | 5 crédits, soit 0,044 $ (palier 50k) à 0,05 $ | recherche gratuite | add-on intent 29 $ pour 100 signaux | non trouvé (650M+ leads) | API + MCP | voir A1 |
| **FullEnrich** | Pro 1k crédits = 55 $/mois (0,055 $/crédit) · 15k = 720 $/mois (0,048 $). Prix des paliers 5k et 10k : non trouvé | 1 crédit (email pro), 3 (email perso), 10 (mobile). Facturé seulement si trouvé | 0,25 crédit si demandé seul | non | non trouvé (waterfall 25+ sources, 800M personnes) | API + MCP (connecteur déjà installé) | https://fullenrich.com/pricing |
| **Apollo** (référence) | La page officielle ne publie ni prix ni crédits. Sources tierces : Basic 49 $, Professional 79 $ par utilisateur et par mois en annuel | 1 crédit par email (tiers) | non trouvé | non trouvé sur la page officielle | non trouvé | API seulement en Custom (page officielle) | https://www.apollo.io/pricing · https://www.zeliq.com/blog/apolloio-pricing |

Igor juge les emails Apollo peu fiables. Ce point n'a pas été vérifié publiquement. Apollo reste à exclure par prudence.

---

## C. Signaux d'intention SEO, coût par entreprise

### C1. Trafic organique et chute de trafic
| Outil | Endpoint / plan | Prix | Coût pour 7 500 domaines (*calc.*) | Par entreprise |
|---|---|---|---|---|
| **DataForSEO Labs** | Tarif standard Labs, applicable à tous les endpoints sauf exceptions (bulk traffic estimation, domain rank overview…) | 0,012 $/tâche + 0,00012 $/item, jusqu'à 1 000 domaines par tâche | ~0,99 $ | 0,00013 $ |
| **DataForSEO Labs** | **Historical Bulk Traffic Estimation** (historique d'ETV, pour détecter une chute) | 0,12 $/tâche + 0,0012 $/domaine | ~9,96 $ | **0,0013 $** |
| DataForSEO Labs | Historical Rank Overview | 0,12 $/tâche + 0,0012 $/mois de données | — | — |
| | Option `include_clickstream_data=true` | double le coût | | |
| OpenSEO | Base 10 $/mois (10 $ d'usage inclus) · Pro 30 $ (36 $) · Agency 200 $ (240 $). Coût de la donnée + 28 %, environ 0,05 $ par recherche de mot-clé | > DataForSEO direct | — | — |
| Semrush API | add-on du plan Business, unités vendues par 2M/5M/10M/20M, **prix des unités non publié**. Trends API sur devis | non trouvé | — | — |
| Ahrefs API | semble réservée au plan Enterprise, **prix non trouvé** | non trouvé | — | — |
| SimilarWeb API | Data Credits, **prix sur devis** | non trouvé | — | — |

Sources : https://dataforseo.com/pricing/dataforseo-labs/dataforseo-google-api · https://openseo.so/pricing · https://www.semrush.com/kb/5-api · https://docs.ahrefs.com/ · https://docs.similarweb.com/api-v5/guides/data-credits-calculations (toutes lues le 2026-10-28). Le dépôt minimum DataForSEO n'est pas indiqué sur ces pages (non trouvé).

### C2. API SERP (quel concurrent se classe au-dessus du prospect)
| API | Prix | Coût pour 1 000 vérifications (top 10) | Source |
|---|---|---|---|
| **DataForSEO SERP, file Standard** | 0,0006 $/SERP (profondeur 10). Priority 0,0012 $, Live 0,002 $ | **0,60 $** (Priority 1,20 $, Live 2,00 $) | https://dataforseo.com/pricing/serp/google-organic-serp-api |
| Serper.dev | 50 $ pour 50k requêtes · 375 $ pour 500k · 1 250 $ pour 2,5M. Crédits valables 6 mois, 2 500 gratuits | 1,00 $ (0,75 à 0,30 $ en volume) | https://serper.dev/ |
| Scrapingdog | Lite 40 $/mois pour 200 000 crédits, 5 crédits par requête Google (tiers) | ~1,00 $ | https://www.scrapingdog.com/pricing/ · https://www.scrapingdog.com/integration/ |
| ValueSERP | 50 $/mois pour 25 000 recherches (vendeur, via une recherche) · PAYG 2,50 $/1k | 2,00 $ (PAYG 2,50 $) | https://trajectdata.com/serp/value-serp-api/pricing/ (page 404 lors de la lecture, chiffres issus des extraits de recherche) |
| SerpApi | Starter 25 $ pour 1 000 · Developer 75 $ pour 5 000 · Production 150 $ pour 15 000 · 250 gratuites/mois | 25 $ / 15 $ / 10 $ | https://serpapi.com/pricing |
| Google Custom Search JSON API | **fermée aux nouveaux clients, arrêt le 1er janvier 2027**. 5 $/1 000, 100 requêtes/jour gratuites | 5 $ (inaccessible) | https://developers.google.com/custom-search/v1/overview |

**Coût par entreprise (*calc.*)** : 1 historique de trafic (0,0013 $) + 3 SERP Standard (0,0018 $) = **≈ 0,003 $ par entreprise**. Même avec 10 mots-clés, on arrive à environ 0,007 $, **bien sous l'objectif de 1 à 2 centimes fixé par le coach**. Pour 7 500 entreprises/mois : **environ 23 $/mois**.

---

## D. Lookup MX gratuit (Google / Microsoft / autre)

- **Méthode gratuite** : DNS-over-HTTPS, sans clé.
  - `https://dns.google/resolve?name=DOMAINE&type=MX`
  - ou `https://cloudflare-dns.com/dns-query?name=DOMAINE&type=MX` avec l'en-tête `accept: application/dns-json`
  - Ou en local avec `dig MX` / Python `dnspython`.
  - Testé le 2026-10-28 : decupler.com renvoie `smtp.google.com`, lemlist.com renvoie `aspmx.l.google.com`.
- **Règles de classement** :
  - Google : `aspmx.l.google.com`, `*.googlemail.com`, `smtp.google.com`.
  - Microsoft : `*.mail.protection.outlook.com`, plus le nouveau format DNSSEC `*.mx.microsoft`, déployé pour les nouveaux domaines (MC1048624, date annoncée 1er juillet 2026, à confirmer). Sources : https://c7solutions.com/2024/02/what-is-mx-microsoft · https://mc.merill.net/message/MC1048624
  - Autre : tout le reste.
  - Proofpoint, Mimecast ou Barracuda en MX : ESP réel inconnu, à classer en « autre » ou à exclure.
- **Alternative sans code** : le champ `esp_code` d'Instantly fait ce classement automatiquement à l'import. Il existe aussi des actors Apify à environ 1–2 $ pour 1 000 domaines (https://apify.com/ataism/dns-records), utilisables avec les 5 $/mois gratuits.

---

## Recommandation (au 2026-10-28)

1. **Outil d'envoi après le 2026-11-10 : passer à Instantly et ne pas renouveler Lemlist.**
   - **Pourquoi :** matching ESP natif. Chaque lead reçoit un `esp_code` détecté automatiquement, et des règles de routage `do_not_send` permettent d'exclure Microsoft, ce qui correspond exactement à notre convention de campagnes. Boîtes et warmup illimités. API v2 avec blocklist, et MCP officiel. Pour le même volume, Instantly coûte environ 40 % de moins que Lemlist (294 à 397 $ contre 510 $).
   - **PlusVibe** est moins cher (119 $), mais trois points restent non trouvés : la limite de boîtes, la base de prospects et le fonctionnement exact du matching ESP. À tester seulement en essai gratuit de 14 jours, pas comme outil principal.
2. **Enrichissement : crédits Instantly SuperSearch** (recherche ICP, emails, signaux tech, hiring et funding).
   - Écouler les 1 045 crédits FullEnrich en fallback sur les non-trouvés et les catch-all.
   - Tester Moltsets avec le plan gratuit (1k appels) : « unlimited » à 97 $, mais la couverture pays et les signaux sont non trouvés.
   - Avant de basculer, faire un test de bounce sur 500 leads FR via GlockApps ou la vérification Instantly.
3. **API intention SEO : DataForSEO** (compte déjà ouvert), avec Labs Historical Bulk Traffic Estimation et SERP en file Standard. Environ 0,003 $ par entreprise, soit **environ 25 $/mois** pour 7 500 entreprises. Le lookup MX passe par DoH gratuit ou par `esp_code`.
4. **Coût mensuel estimé :** Instantly 294 $ + DataForSEO ~25 $ + Outscraper/Apify (offerts) = **environ 320 $/mois**, contre environ 535 $ en restant sur Lemlist.

**Achats exacts à faire avant le 2026-11-10 :**
- **Instantly Outreach « Hypergrowth »** : 97 $/mois en mensuel (77,6 $/mois en annuel). Appliquer le lien affilié d'Igor ou essayer SECRET20 au checkout (remise non vérifiée).
- **Instantly « Hyper Credits »** : 197 $/mois pour 10 000 crédits. Passer à « Hyper Credits 2 » (300 $ pour 20 000) si le ratio réel dépasse 1,33 crédit par email.
- **DataForSEO** : recharge pay-as-you-go (montant minimum non trouvé). 25 $/mois suffisent pour 7 500 entreprises.
- **Lemlist** : désactiver le renouvellement avant le 2026-11-10, après avoir exporté les campagnes, la blocklist et les leads. Les crédits ne restent reportés que tant que l'abonnement est actif : les consommer avant cette date.
