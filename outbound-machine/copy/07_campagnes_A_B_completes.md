# 07 — Campagnes A/B complètes (variables Lemlist, prêtes à envoyer)

> Audience de test : **#32 SaaS-Fintech · CEO-CMO · 11-50** (200 leads, split A=120 / B=80).
> A = **X-Ray GEO** (`cam_4vqWGAztL9Lir4ac6`) · B = **Échantillon Carto** (`cam_edt7pdBJjn6e7uzoD`).
> Objectif du test : quelle promesse d'actif immédiat convertit le mieux à froid.
> Règles maison respectées : pas de cadratins, objets minuscules type "camouflage interne",
> 1er mail = permission facile (« je vous l'envoie ? »), jamais de call de 30 min au 1er contact,
> 1 preuve max par mail, breakup soft (pause, pas fin).

---

## Variables Lemlist (source = `scripts/07_push_with_vars.py`)

Le script pousse ces champs pour chaque lead. **Toujours prévoir un fallback** pour qu'aucune
balise vide ne fuite dans le mail.

| Variable Lemlist        | Champ poussé   | Source base            | Exemple A (Nicolas)          | Exemple B (Maxime)              |
|-------------------------|----------------|------------------------|------------------------------|---------------------------------|
| `{{firstName}}`         | firstName      | `first_name`           | Nicolas                      | Maxime                          |
| `{{companyName}}`       | companyName    | `company`              | Entrepreneurs et Finance     | HelloPrêt                       |
| `{{companyDomain}}`     | companyDomain  | `domain`               | entrepreneurs-finance.fr     | hellopret.fr                    |
| `{{secteur}}`           | secteur        | `personalization`      | conseil M&A PME              | courtage crédit immobilier      |
| `{{categorie}}`         | categorie      | `personalization`      | les cabinets de conseil M&A  | les courtiers crédit immo       |
| `{{concurrent}}`        | concurrent     | `personalization`      | In Extenso Finance           | Pretto                          |

**Syntaxe fallback Lemlist** : `{{firstName | "bonjour"}}`, `{{concurrent | "vos concurrents"}}`.
Si `concurrent`, `categorie` ou `secteur` est vide pour un lead => il **ne doit pas** partir dans la
campagne qui utilise cette variable (filtre `qa_status='ok'` avant push).

---

## CAMPAGNE A — X-Ray GEO (`cam_4vqWGAztL9Lir4ac6`)

Promesse : « voici les prompts IA exacts où **{{concurrent}}** sort et où **vous** êtes absent ».
Actif immédiat = la **liste des prompts + le format de contenu** qui fait citer le concurrent.

### A · Mail 1 — J0 (accroche X-Ray)
```
Objet (A) : visibilité ia
Objet (B) : {{concurrent | "vos concurrents"}} vous devance

hello {{firstName | "bonjour"}}, j'ai testé ce que répondent ChatGPT et Perplexity sur {{categorie | "votre marché"}} :
{{concurrent | "vos concurrents"}} ressort, {{companyName}} n'apparaît sur aucun des prompts que j'ai lancés.
j'ai listé les 15 prompts exacts où vous êtes absents, plus le format de contenu qui fait citer
{{concurrent | "vos concurrents"}} à votre place.
(on a fait ça pour Décathlon entre autres)
seriez-vous contre que je vous partage la liste ?
Nathan, Décupler
PS : 3 de ces prompts sont des requêtes d'achat pures, c'est du cash qui part chez {{concurrent | "le concurrent"}}.
```

### A · Mail 2 — J+3 (preuve + micro-teaser, relance curiosité)
```
Objet : re: 15 prompts

{{firstName | "bonjour"}}, petit complément sur ma liste.
ce n'est pas « faites plus de contenu » : sur {{categorie | "votre catégorie"}}, il y a 3 prompts d'achat
où la marque citée gagne la vente avant même le moindre clic sur Google.
{{companyName}} peut devenir la réponse par défaut sur ces 3 prompts, c'est rapide à corriger.
je vous envoie la liste + le plan pour y ranker ?
Nathan
```

### A · Mail 3 — J+7 (offre d'actif, breakup soft)
```
Objet : je vous laisse la liste ?

{{firstName | "bonjour"}}, je mets le sujet en pause de mon côté, sans souci si ce n'est pas le moment.
la liste des prompts GEO pour {{companyName}} est déjà prête : où {{concurrent | "vos concurrents"}} est cité,
où vous ne l'êtes pas, et le contenu à créer pour inverser ça.
si vous la voulez, répondez juste « prompts » et je vous l'envoie.
Nathan, Décupler
PPS : si ce n'est pas vous qui gérez la visibilité, vous me dites vers qui me tourner ?
```

---

## CAMPAGNE B — Échantillon Carto (`cam_edt7pdBJjn6e7uzoD`)

Promesse (mécanique Elena/UltB) : « je vous prépare **déjà** la cartographie des 3 opportunités,
offert, pour vous montrer le niveau. satisfait => on va plus loin. sinon vous gardez tout ».
Actif immédiat = mini-carto (mots-clés qui rapportent + prompts IA + projection de demandes/mois).

### B · Mail 1 — J0 (offre échantillon)
```
Objet (A) : carto {{secteur | "seo"}}
Objet (B) : petit cadeau pour {{companyName}}

hello {{firstName | "bonjour"}}, je bosse avec des boîtes {{secteur | "B2B"}} qui veulent plus de demandes
entrantes via le search.
je vous prépare déjà la cartographie des 3 opportunités organiques prioritaires pour {{companyName}},
offert, pour vous montrer le niveau : les mots-clés qui rapportent, les prompts IA à viser,
et une projection de demandes par mois.
si l'approche vous parle, on vous montre comment on capte ça. sinon vous gardez tout, sans engagement.
seriez-vous contre un échange de 10 min pour vous présenter la carto ?
Nathan, Décupler
PS : on a fait +20% de pipeline sur le canal organique pour Le Point, Pluxee et Décathlon.
```

### B · Mail 2 — J+3 (aperçu concret, preuve visuelle)
```
Objet : re: carto {{secteur | "seo"}}

{{firstName | "bonjour"}}, pour vous donner un aperçu concret : la carto ne parle pas de « plus de trafic »,
mais des requêtes à intention commerciale de {{categorie | "votre marché"}} que {{concurrent | "vos concurrents"}}
capte déjà et pas vous.
j'ai aussi une projection du nombre de demandes par mois que ça peut représenter (estimation, pas une promesse).
je vous envoie la première version ?
Nathan
```

### B · Mail 3 — J+7 (offre d'actif, breakup soft)
```
Objet : je vous laisse la carto ?

{{firstName | "bonjour"}}, je clôture simplement le sujet.
la 1re version de la cartographie SEO/GEO pour {{companyName}} est déjà prête : contenus prioritaires,
requêtes visées, et les sources à travailler pour gagner en visibilité sur Google et dans les réponses IA.
si ce n'est pas prioritaire, aucun souci. si vous la voulez, répondez juste « carto ».
Nathan, Décupler
PPS : pas le bon moment ? un « no biz » et je vous laisse tranquille.
```

---

## QA avant envoi (checklist)

- [ ] Aucun lead sans `concurrent` / `categorie` / `secteur` dans A (variable au coeur du mail).
- [ ] `qa_status='ok'` filtré (167/200 aujourd'hui, 33 à finir).
- [ ] Fallbacks présents sur chaque variable (test « lead sans concurrent » => le mail reste lisible).
- [ ] Objets en minuscules, pas de cadratins, pas de jargon (`robots.txt`, `schema`...).
- [ ] 1 seule preuve par mail (Décathlon en A, +20% pipeline en B).
- [ ] Signature identique partout : « Nathan, Décupler ».
- [ ] Reste à pousser : **64 leads** sur 200 (136 déjà « Envoyé Lemlist »).

## État live (2026-08-12)

| Groupe | Leads | qa_ok | Envoyés Lemlist | Reste à pousser |
|--------|-------|-------|-----------------|-----------------|
| A (X-Ray)  | 120 | — | — | — |
| B (Carto)  | 80  | — | — | — |
| **Total**  | **200** | **167** | **136** | **64** |

> Push du reste via `scripts/07_push_with_vars.py` (coût token nul, voir doctrine point « variables »).
