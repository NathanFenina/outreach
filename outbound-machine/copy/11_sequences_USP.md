# 11 — Séquences complètes par USP (4 messages, cadence Jason J0/J2/J3/J5)

> 2 USP côte à côte (pas A/B, deux propositions de valeur distinctes). Cadence coach Jason :
> **J0 / J2 / J3 / J5** (Fibonacci), campagne finie en ~2 semaines. Structure : TOF (accroche +
> teaser) → MOF (outil / manque de temps) → Offre signature (RDV + cadeau) → Breakup (3 raisons).
> Esprit UltB gardé partout : on offre, "vous gardez tout". Variables Lemlist : `{{firstName}}`,
> `{{companyName}}`, `{{secteur}}`, `{{categorie}}`, `{{concurrent}}` (+ fallbacks).

---

## USP 1 — X-Ray GEO (campagne A) — variables : concurrent, categorie

### Mail 1 · J0 — accroche X-Ray (version validée Nathan)
```
Objet : j'arrive pas à vous trouver
hello {{firstName}}, j'ai testé ce que répondent ChatGPT et Perplexity sur {{categorie}}.
{{concurrent}} ressort, {{companyName}} n'apparaît sur aucun des prompts que j'ai lancés.
j'ai listé les 15 prompts exacts où vous êtes absents + le format de contenu qui fait citer
{{concurrent}} à votre place.
(on a fait ça pour Décathlon entre autres)
seriez-vous contre un échange de 10 min que je vous partage la liste et le plan d'action ?
Nathan
Décupler
PS : 3 de ces prompts sont des requêtes d'achat pures, c'est du cash qui part chez {{concurrent}}.
PPS : si c'est pas vous qui gérez ça, vous me dites vers qui me tourner ?
```

### Mail 2 · J+2 — 2 contenus offerts + RDV (offre signature, version Nathan)
```
Objet : re: j'arrive pas à vous trouver
{{firstName}}, on prend 20 min, on ouvre ensemble ChatGPT/Perplexity, je vous montre quel
concurrent est cité et ce qu'il faut rédiger pour récupérer sa place.
et si on cale ce RDV, je vous écris gratuitement 1 à 2 contenus GEO-friendly, que vous gardez
quoi qu'il arrive.
ça vous dit ?
Nathan, Décupler
```

### Mail 3 · J+3 — outil gratuit + lien (si manque de temps, version Nathan)
```
Objet : re: j'arrive pas à vous trouver
{{firstName}}, si vous manquez de temps, pas besoin d'attendre notre échange : on a développé un
outil interne qui vous sort votre score de visibilité IA sur {{categorie}}.
vous mettez votre URL, il vous donne où vous en êtes + les premières actions. voici le lien :
https://app.decupler.com/audit-geo-gratuit
toutefois, ça ne remplace pas une expertise humaine et un échange humain.
Nathan
```
> Lien = audit GEO (le plus aligné avec l'angle X-Ray). Alternatives dispo :
> `app.decupler.com/cartographie-ia` · `app.decupler.com/audit-eeat`.

### Mail 4 · J+5 — breakup 3 raisons (technique Jason)
```
Objet : je clôture, {{firstName}} ?
{{firstName}}, sans réponse je vais partir du principe que :
1. ce n'est pas vous qui gérez la visibilité (dites-moi vers qui me tourner),
2. vous le lancez déjà en interne (top, je vous laisse),
3. ce n'est pas le moment (on en reparle dans quelques mois ?).
un mot sur la bonne ligne et j'arrête de vous relancer. la liste des 15 prompts reste dispo si vous la voulez.
Nathan
```

---

## USP 2 — Opportunités organiques / Carto (campagne B) — variable : secteur

### Mail 1 · J0 — analyse offerte (version validée Nathan)
```
Objet : petit cadeau {{companyName}}
hello {{firstName}}, je bosse avec des boîtes {{secteur}} qui veulent plus de demandes entrantes via le search.
je vous ai préparé une analyse avec les 10 grandes opportunités organiques prioritaires pour
{{companyName}}, offert, pour vous montrer le niveau : les mots-clés qui rapportent, les prompts IA
à viser, et une projection de leads/mois.
si l'approche vous parle, on vous montre comment on capte plus de leads. sinon vous gardez tout, sans engagement.
seriez-vous contre un échange de 10 min pour vous présenter la carto ?
Nathan Fenina
Décupler
PS : on a travaillé sur l'amélioration de la visibilité organique chez Le Point, Pluxee et Décathlon.
PPS : pas le bon moment ? un « no biz » et je vous laisse tranquille.
```

### Mail 2 · J+2 — "manque de temps ?" + outil (cartographie / audit)
```
Objet : re: petit cadeau {{companyName}}
{{firstName}}, si vous manquez de temps pour qu'on en parle, je peux déjà vous partager la matière :
on a un outil interne qui, à partir de votre URL, sort les opportunités organiques et votre score
de visibilité IA sur {{secteur}}. voici le lien :
https://app.decupler.com/cartographie-ia
toutefois, ça ne remplace pas un regard humain et un échange. on cale 10 min si ça vous parle ?
Nathan
```

### Mail 3 · J+3 — offre signature (cas client + RDV + cadeau)
```
Objet : comme {{secteur}} X ?
{{firstName}}, vous me faites penser à une boîte {{secteur}} qu'on accompagne : elle captait très
peu de demandes entrantes, ses concurrents raflaient les requêtes d'achat. on a priorisé 10 pages
+ le format GEO, résultat : plus de demandes qualifiées, sans dépendre du paid.
on fait le même exercice pour {{companyName}} en 20 min ? et je vous laisse la cartographie + 1 contenu
rédigé gratuitement, que vous gardez.
Nathan, Décupler
```

### Mail 4 · J+5 — breakup 3 raisons
```
Objet : je clôture, {{firstName}} ?
{{firstName}}, sans réponse, je pars du principe que :
1. ce n'est pas vous qui gérez le sujet (vers qui me tourner ?),
2. vous êtes déjà bien couvert en organique (bravo, je vous laisse),
3. ce n'est pas prioritaire là (on en reparle plus tard ?).
un mot et j'arrête. la cartographie des 10 opportunités pour {{companyName}} reste prête si vous la voulez.
Nathan
```

---

## Notes de mise en œuvre

- **Objets** : énigmatiques mais qui parlent (`j'arrive pas à vous trouver`, `petit cadeau {{companyName}}`).
  À A/B tester une fois l'USP validée (Jason : on teste l'objet APRÈS avoir trouvé l'USP qui clique).
- **Liens (mail 2/3)** : Jason recommande de mettre des liens pour **récolter les clics** → le cold call
  devient du **warm call** (on rappelle les cliqueurs d'abord). Outils à brancher : score GEO
  (skill `seo-geo-score`), cartographie, audit E-E-A-T.
- **Fallbacks obligatoires** : `{{concurrent | "vos concurrents"}}`, `{{secteur | "B2B"}}`,
  `{{categorie | "votre marché"}}` — un lead sans la variable ne part pas dans l'USP qui en dépend.
- **Volume cible (coach)** : ~500 leads par USP, batch de 500, sprint de 2 semaines.
