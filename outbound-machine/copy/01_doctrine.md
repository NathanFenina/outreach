# 01 — Doctrine Cold Mail Décupler (synthèse world-class)

> Ma synthèse d'expert : ce qu'on retient, ce qu'on jette, et POURQUOI.
> Objectif d'un cold mail Décupler = **déclencher une conversation** (pas vendre),
> en **prouvant la valeur avant le RDV** via un actif tangible.

## 1. Le principe central : Reverse Lead Magnet + X-Ray

Tous les experts convergent sur un point (2026) : **l'audit générique est mort**, la
**personnalisation "j'ai vu votre profil" est morte** (AI slop repérable). Ce qui gagne :

> Une **observation unique, spécifique et vérifiable** (la "radiographie") →
> une **offre d'actif tangible et gratuit** → un **CTA à friction quasi nulle**.

Décupler a un **avantage déloyal** : ses **simulateurs** (GEO, E-E-A-T, cartographie IA)
SONT le reverse lead magnet. On ne "propose un audit", on **offre un morceau de solution**.

## 2. Résolution des 6 hésitations de Nathan

| Hésitation | Décision d'expert |
|---|---|
| Mettre "j'ai vu que vous avez bossé avec X" ? | ❌ en tant que perso (générique). ✅ UNE observation business vérifiable (relevance). |
| "J'ai préparé une analyse, seriez-vous contre que je la partage ?" | ✅✅ **C'est le cœur.** Reverse lead magnet + CTA orienté "non". À garder. |
| Balancer le lien du simulateur dans le mail 1 ? | ❌ Pas de lien au mail 1 (friction + délivrabilité). On **teaser**, on livre après réponse. |
| Mettre les quick wins dans le mail 1 ? | ❌ Non. On **teaser UN** insight (la faille), on livre le reste après le "oui". Sinon plus aucune raison de répondre. |
| Attaquer un pain ("15 prompts où vous n'êtes pas cité") ? | ✅✅ Excellent (GEO). Concret, chiffrable, nouveau mécanisme. |
| Mettre l'audit complet + lien dès le mail 1 ? | ❌ "trop", tue la curiosité. On garde la découverte pour après le oui. |

**Règle d'or Décupler** : le mail 1 **montre la faille, ne la répare pas**. La réparation
(la valeur complète) se livre APRÈS la permission. C'est ce qui crée la conversation.

## 3. Reconciliation du débat "volume" (les 2 écoles)

- École A (ton 1er expert) : 25/inbox, aged domains, SMTP dédié, anti-Apollo, petit volume chirurgical.
- École B (Lucero/Igor) : volume horizontal massif (100k/mois), 20/inbox, l'offre prime.

**Ils sont d'accord sur l'infra** : scaling **horizontal** (beaucoup d'inboxes, ~20-30/j
chacune, warm-up). Le désaccord = ambition de volume brut.

**Position Décupler** : notre edge, c'est la **qualité de la data** (listes sectorielles
déjà curées + enrichissement FullEnrich) et l'**offre** (simulateurs). Donc :
- ✅ Infra horizontale (10 domaines / ~20 inboxes) — voir `03_infra_setup.md`.
- ✅ Volume **medium**, ICP serré, offre forte. On ne fait PAS du spray Apollo 100k.
- ✅ On **monte en volume seulement après** avoir validé qu'un angle convertit.
- On ne juge jamais un angle sous ~200-300 envois ("volume negates luck").

## 4. Principes de copy (non négociables)

1. **Objet camouflage** : 1-2 mots, **minuscules**, style collègue interne. Pas de promesse marketing.
   - Ex : `visibilité ia`, `carto seo`, `question site`, `prompts [secteur]`.
2. **Longueur** : 80-120 mots, **< 15 sec de lecture**. Test à voix basse.
3. **Structure** (4 temps) :
   - (a) 1 ligne de **relevance** (observation vérifiable, pas "j'espère que vous allez bien").
   - (b) Le **problème/valeur** en 1 phrase **non technique**.
   - (c) 1 **preuve** (Decathlon / Top 20 FR / 500K€) — une seule.
   - (d) **CTA orienté "non"** offrant l'actif : "seriez-vous contre que je vous envoie… ?".
4. **Écrire comme un humain** : minuscules ok, pas de jargon (robots.txt, etc.), pas de salutations pompeuses, pas de "AI slop".
5. **1 ICP + 1 problème + 1 offre par campagne.** Jamais "SEO + GEO + contenu + technique" en même temps.
6. **PS** utile (preuve additionnelle) + **porte de sortie** ("répondez 'stop' et je vous laisse tranquille").

## 5. Le mail NE VEND PAS — il qualifie

Objectif unique du mail 1 = obtenir la **permission** de livrer l'actif (analyse / simulateur /
Loom). La vente se fait plus tard (à la livraison de l'actif, ou au call). Ne jamais pitcher
l'infra complète (back-end) au mail 1.

## 6. L'économie de l'analyse (ne pas se ruiner en IA)

On NE prépare PAS un audit complet pour chaque prospect. Machine à **micro-insights** :
- **Niveau 1 (~70%)** : signal léger auto (secteur, page/angle manquant, concurrent, ville) → campagne segmentée, 1ʳᵉ ligne légèrement adaptée.
- **Niveau 2 (~25%)** : insight enrichi (1-3 pages, 1-2 concurrents, 1 opportunité précise) → meilleure 1ʳᵉ ligne.
- **Niveau 3 (~5% ABM)** : Loom / mini-cartographie / maquette → gros comptes ou répondants chauds.
- L'agent doit pouvoir répondre **SKIP** s'il ne trouve pas d'insight solide (sinon il invente → tue la crédibilité).
- Règle : pas d'analyse longue avant intérêt si le compte vaut < ~3-5 K€ de valeur client.

## 7. Où la copy vivra (app)

- Stockage repo : ce dossier `copy/` (versionné, jamais perdu).
- App (plus tard) : table `outbound_templates` (framework, objet, corps, séquence, segment,
  variante géo/langue, statut A/B, taux de réponse) + onglet "Copy". On branche Lemlist ensuite.
- Statut prospect : colonne `lemlist_status` déjà en base (À importer → Importé → Répondu…).
