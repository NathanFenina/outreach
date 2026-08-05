# Outbound Machine — Décupler

Machine d'acquisition B2B : consolider les bases de contacts existantes, les nettoyer,
les enrichir (email + téléphone), puis les splitter en cohortes pour tester **cold email**
(via Instantly) et **cold call** (via un dialer à définir) sur la même audience — sans
qu'une même personne soit contactée par les deux canaux.

## Stack

| Outil | Rôle | Statut session |
|-------|------|----------------|
| Clay | Bases de contacts existantes (anciennes campagnes) | Connecté, mais **Audiences désactivé** → export CSV manuel obligatoire |
| FullEnrich | Enrichissement waterfall email + téléphone | Connecté — **0 crédit** (recharge nécessaire pour tout nouvel enrichissement) |
| Instantly | Envoi cold email | À connecter |

## Pipeline

1. **Sourcing** — export CSV manuel des tables Clay (sectorielles) → `data/00_raw/`
2. **Nettoyage** — fusion, dédoublonnage (email + entreprise), retrait des emails
   génériques/invalides, sélection du bon interlocuteur → `data/01_clean/`
3. **Enrichissement** — FullEnrich waterfall (email + téléphone), par lots de 50 max
4. **Split A/B** — 50/50 randomisé, **seed = 42** (reproductible), exclusion mutuelle
5. **Push** — cohorte email → Instantly ; cohorte call → dialer (format international)

## Arborescence

```
outbound-machine/
├── data/
│   ├── 00_raw/          exports bruts (Clay CSV, FullEnrich CSV) tels quels
│   ├── 01_clean/        base fusionnée + nettoyée + dédoublonnée
│   ├── 02_cohorte_email.csv   leads avec email valide → Instantly
│   └── 02_cohorte_call.csv    leads avec téléphone → dialer (format international)
└── logs/
    └── nettoyage.log    trace des fusions / suppressions / dédoublonnages
```

## Règles de split (par défaut)

- Split **A/B 50/50 randomisé, seed fixe = 42** → reproductible.
- **Aucune personne dans les deux cohortes** simultanément.
- Cohorte email = email valide uniquement ; cohorte call = téléphone valide uniquement.
- Alternative possible : split **par secteur** (dossiers Clay) au lieu de A/B — au choix.

## Règles de sécurité

- Aucun appel MCP simulé : si un serveur manque, on s'arrête et on le signale.
- Aucune action d'écriture réelle (push Instantly, envoi) sans **récapitulatif + validation explicite**.
- Traitement par lots (jamais toute la liste en un seul appel) + logs pour reprise propre.

## Statut courant

- [x] Arborescence de travail créée
- [x] Exports Clay reçus (39 CSV via Drive) + liste call FullEnrich (157 contacts, 100 % tel)
- [x] Consolidation : 39 fichiers -> **7 574 leads uniques** (767 doublons retirés)
      - 4 551 avec email (60 %), 3 023 sans email (à ré-enrichir)
- [x] CRM Supabase — projet "LinkedIn App", tables `outbound_*` (schéma `db/schema.sql`)
      - `outbound_leads` chargée : **7 574 leads** (4 551 côté email, 3 023 sans email)
      - RLS activée, tables verrouillées
- [ ] Charger la liste call (157 tel) en `channel='call'` + exclusion mutuelle
- [ ] Split cohortes email / call
- [ ] Connecter Instantly + push cohorte email
- [ ] Webhook Instantly -> maj statuts dans `outbound_campaign_leads`

## CRM Outbound (Supabase)

Modèle en 3 tables (voir `db/schema.sql`) :
- `outbound_leads` — source de vérité (qui contacter).
- `outbound_campaigns` — campagnes email/call (+ `instantly_campaign_id`).
- `outbound_campaign_leads` — 1 ligne = 1 lead dans 1 campagne, avec `status`
  (`pending → sent → opened → replied → interested / bounced / unsubscribed`).

Vues `outbound_v_email_leads` / `outbound_v_call_leads` = vue côté email / côté call.
Chargement des leads : `scripts/02_load_supabase.py` (env `SUPABASE_URL`, `SUPABASE_KEY`).

> Données (PII) stockées hors Git : voir `.gitignore`. Le repo ne contient que le code.
> `scripts/01_consolidate.py` régénère `data/01_clean/master_leads.csv` depuis `data/00_raw/`.
