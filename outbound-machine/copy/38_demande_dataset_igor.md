# 38 · Demande de dataset à Igor (UltB) · cahier des charges

> Pièce jointe au mail 37. Le fichier d'exclusion `data/datasets/DNC-igor.csv` (domaines déjà contactés + clients) est généré par `scripts/49_export_dnc.py` et n'est pas commité (données personnelles).

## Ce qu'on fait nous-mêmes (base Lemlist + Moltsets + FullEnrich)
- ICP 1 B2B en France : 1.1 à 1.13, paliers P1 (levée < 6 mois + recrute), P2 (recrute en marketing), P4 (marché principal).
- ICP 2 BTP et services locaux en France : base Lemlist pour les entreprises de 5 salariés et plus, Google Maps pour les niches.
- ICP 4 hôtels, spas, campings en France.

## Ce qu'on demande à Igor

| # | Cible | Pays | Taille | Contacts | Volume visé |
|---|---|---|---|---|---|
| 1 | SaaS / IA, cabinets de conseil, agences marketing et événementielles | UK, DACH (DE, AT, CH alémanique) | 5 à 500 salariés | CEO / founder, CMO / head of growth, head of SEO / content | 600 entreprises |
| 2 | Cliniques de greffe capillaire, dentaires, esthétiques qui visent des patients francophones | Turquie, Hongrie, Tunisie | toutes | owner / medical director, international patient manager, marketing manager | 300 cliniques |
| 3 | Hôtels indépendants et spas | Belgique, Suisse romande, Maroc | 5 salariés et plus | propriétaire / directeur général, revenue manager, marketing | 300 établissements |

## Règles de livraison
- Séparer **Google** / **autres** (Microsoft dans « autres », on gère l'envoi).
- Pas de catch-all, pas d'emails génériques (contact@, info@) sauf pour les cliniques si pas mieux.
- Exclure les domaines du fichier `DNC-igor.csv`.
- Colonnes souhaitées : prénom, nom, poste, email, statut email, LinkedIn, entreprise, domaine, pays, ville, taille, ESP (MX).
- Format CSV, un fichier par cible.
