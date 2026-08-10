# 03 — Infra, délivrabilité & volume

> Comment envoyer sans finir en spam, et à quel rythme monter.

## Setup de départ recommandé (Décupler)

| Élément | Départ | Cible |
|---|---|---|
| Domaine principal `decupler.fr` | ❌ jamais pour le cold | réservé site/clients/inbound |
| Domaines de prospection dédiés | 3-5 (ex : `decupler-growth.com`, `getdecupler.fr`) | jusqu'à 10 |
| Inboxes par domaine | 2 | 2-3 |
| Inboxes totales | 6 | ~20 |
| Volume / inbox / jour | 5-10 (warm-up) → 20-25 | 20-30 max |
| Volume total / jour | — (warm-up) | 300-400 |
| Warm-up | 3-4 semaines avant tout envoi réel | — |
| Auth | SPF + DKIM + DMARC sur CHAQUE domaine | obligatoire |
| Identité expéditeur | 1 principale : Nathan (photo LK, signature Décupler) | — |

Les autres boîtes servent à **répartir le volume** (rotation) et protéger la réputation,
pas à inventer une fausse équipe.

## Providers

- Mix **Google Workspace + Microsoft 365** (~60/40) : Google→Google et Outlook→Outlook passent mieux les filtres.
- Option avancée (école "haute sécurité") : **aged domains** (GoDaddy Auctions, Odys) + SMTP dédié — vérifier l'historique (Wayback, blacklists) avant achat. Plus technique (à confier à Mahdi).
- Séquenceur : **Lemlist** (choix Nathan) — warm-up, rotation d'inboxes, Unibox, séquences.

## Montée en charge (ne PAS brancher 400/jour demain)

- Semaine 1 : 5-10 mails/j/inbox.
- Semaine 2 : 10-15/j/inbox (si bounces & plaintes très faibles).
- Semaine 3 : 15-20/j/inbox.
- Ensuite : 20-25/j/inbox, plafond 30. Pas de pics brutaux.
- **Mois 1 opérationnel** : 500-1000 prospects, 1 ICP, 2 angles. On optimise AVANT de scaler.

## Délivrabilité (garde-fous)

- Vérification des emails **obligatoire** avant import (réduit les bounces).
- Bounces < 2% (idéal < 1%). Plaintes spam < 0,1% (jamais 0,3%).
- Étaler les envois sur les **heures ouvrées** du fuseau ciblé.
- Surveiller au niveau **domaine**, pas juste par inbox.
- Pas de lien/pièce jointe au mail 1 (protège la délivrabilité).

## Benchmarks (pour juger une campagne)

| Indicateur | Faible | Correct | Très bon |
|---|---|---|---|
| Réponse totale | < 3% | 3-5% | 5-10%+ |
| Réponse **positive** | < 0,5% | 1-3% | 3-5%+ |
| RDV / emails | < 0,3% | 0,5-1,5% | 2-4%+ |
| Bounce | > 3% | < 2% | < 1% |

KPI Décupler : viser **1 RDV qualifié / 100-200 contacts ultra-ciblés**, et identifier quel
angle (visibilité IA / pages comparaison / cluster manquant / local) sort les meilleurs RDV.

## Économie de l'analyse (rappel — 3 niveaux)

Sur 1000 prospects : ~700 signal léger (campagne segmentée), ~250 insight enrichi, ~50 ABM
(Loom/carto/maquette). L'agent doit pouvoir renvoyer **SKIP**. Pas d'audit long avant intérêt
si compte < ~3-5 K€ de valeur.

## Le lead magnet "outil d'audit" (simulateurs Décupler)

- ❌ Pas le meilleur **1er CTA** en cold (lien = friction + risque délivrabilité).
- ✅ Usage : "j'ai déjà lancé une analyse, je vous l'envoie ?" → page de résultat perso **après** réponse/relance.
- ✅ Bon pour **inbound / LinkedIn / retargeting** : outil "Score SEO + visibilité IA" avec résultat immédiat, puis email pro pour le rapport détaillé, téléphone en **optionnel** ("préférez-vous le rapport par mail ou une explication de 10 min ?").
- Ne pas cacher la récupération du numéro derrière l'audit (dégrade la confiance en B2B FR).

## Chaîne cible (pour l'automatisation, plus tard)

`data → signal → angle → email → campagne Lemlist`, avec niveau de recherche variable selon
la valeur du compte. Source de vérité = **Supabase** (déjà en place), enrichissement FullEnrich,
activation Lemlist. Réponses Lemlist → retour CRM → statut mis à jour.
