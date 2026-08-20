# 12 — Séquences campagne WELLNESS / SPA (cold mail)

> Audience **Medical Spa · Bretagne · local** (#47, **367 leads**). **Cold mail.**
> Cible = TPE locales (le gérant lit le mail). Vocabulaire simple : réservations, avis, être trouvé.
> Cadence J0 / J+2 / J+3 / J+5. Signature partout : **Nathan Fenina / Agence Decupler**. Esprit UltB : on offre, vous gardez tout.
>
> ### 🎯 Principe « un template, zéro déchet »
> Au lieu de découper l'audience par micro-secteur (et jeter ce qu'on a scrapé), **une seule campagne
> par approche** + une **variable `{{secteur}}`** qui adapte le texte. Rempli en base pour les 367 :
> `institut` (136) · `cabinet de massage` (105) · `spa` (66) · `centre de bien-être` (46) · `établissement` (14).
> Le mail dit « votre {{secteur}} » → il sonne juste pour chaque fiche, sans copy séparée.
>
> **Variables utilisées :** `{{companyName}}` · `{{secteur}}` · `{{ville}}` (= city, déjà en base) → aucune prépa manuelle.
> ⚠️ **Pas de `{{firstName}}`** : seulement 23/367 leads ont un prénom (fiches Maps = nom d'entreprise).
> Les openers s'appuient donc sur `{{companyName}}` / « bonjour, » — jamais sur un prénom vide.
>
> ### On lance les 2 en A/B
> - **A — « Analyse / 10 recherches où vous êtes absent »** (angle SEO/GEO, primaire pour les spas).
> - **B — « Maps + avis + site offert »** (on repère la fiche Google, on offre une maquette de site moderne).

---

## APPROCHE A — « 10 recherches où vous êtes absent » (analyse offerte)

### Mail 1 · J0
```
Objet : votre {{secteur}} sur Google
bonjour, je regarde comment les instituts et spas se font trouver quand un client
tape « massage » ou « soin » près de chez lui — sur Google comme dans les IA (ChatGPT, Maps).
j'ai préparé une analyse pour {{companyName}} : j'ai repéré 10 recherches à {{ville}} où c'est un
concurrent qui ressort à votre place, et les 3 choses simples qui vous font récupérer ces réservations.
je vous la partage lors d'un échange de 10 min ?
Nathan Fenina
Agence Decupler
PS : l'analyse est à vous, que vous travailliez avec nous ou pas.
```

### Mail 2 · J+2
```
Objet : re: votre {{secteur}} sur Google
concrètement je vous montre les recherches où vos futurs clients tombent sur un
concurrent plutôt que sur {{companyName}}, et quoi changer pour reprendre ces places.
on prend 15 min quand vous voulez — je vous montre aussi comment on travaille.
Nathan Fenina
Agence Decupler
```

### Mail 3 · J+3 — outil gratuit
```
Objet : re: votre {{secteur}} sur Google
si vous manquez de temps, pas besoin d'attendre : on a un outil qui, depuis le nom
de votre {{secteur}}, sort votre visibilité et les premières actions à faire.
je le lance pour {{companyName}} et je vous renvoie le résultat — c'est offert.
un simple « ok » et je m'en occupe.
Nathan Fenina
Agence Decupler
```

### Mail 4 · J+5 — breakup 3 raisons
```
Objet : je clôture, {{companyName}} ?
sans réponse je pars du principe que :
1. ce n'est pas le bon moment (on en reparle plus tard ?),
2. vous êtes déjà complet côté réservations (top, je vous laisse),
3. ce n'est pas vous qui gérez ça (vers qui me tourner ?).
un mot et j'arrête. l'analyse pour {{companyName}} reste à vous si vous la voulez.
Nathan Fenina
Agence Decupler
PPS : pas le bon moment ? un « stop » et je vous laisse tranquille.
```

---

## APPROCHE B — « Maps + avis + site offert »

> Hook demandé par Nathan : on repère la fiche Google Maps, on complimente les avis, on pointe le
> site perfectible et on **offre une maquette de site moderne** — « si vous l'aimez, vous la gardez ».
> ⚠️ On n'invente pas de chiffre d'avis (pas la donnée en base) → formulation sans nombre.
> *(Option : si tu veux dire « vos X avis », je re-parse le xlsx d'origine pour ajouter une variable `{{avis}}`.)*

### Mail 1 · J0
```
Objet : votre fiche {{companyName}}
bonjour, je suis tombé sur la fiche Google de {{companyName}} et j'ai vu vos avis
clients — ils donnent vraiment envie de pousser la porte.
du coup je me suis permis de regarder votre site : il est bien, mais on peut le rendre plus moderne
et surtout transformer plus de visiteurs en réservations. je vous ai préparé une maquette.
si elle vous plaît, vous la gardez — c'est offert, sans engagement.
on cale 15 min la semaine prochaine pour que je vous la partage à l'écran ?
Nathan Fenina
Agence Decupler
PS : que vous travailliez avec nous ou non, la maquette est à vous.
```

### Mail 2 · J+2
```
Objet : re: votre fiche {{companyName}}
je vous montre la maquette en 10 min : l'accueil, la page soins et le bouton de
réservation mis en avant. vous repartez avec, même si on n'avance pas ensemble.
quel créneau vous arrange la semaine prochaine ?
Nathan Fenina
Agence Decupler
```

### Mail 3 · J+3 — être trouvé (pont vers Maps/Google)
```
Objet : re: votre fiche {{companyName}}
au-delà du design, un site propre c'est aussi ce qui fait remonter votre {{secteur}}
sur Google et Maps à {{ville}} quand quelqu'un cherche autour de lui.
on regarde ensemble la maquette + les 2-3 réglages qui vous rendent plus visible ?
Nathan Fenina
Agence Decupler
```

### Mail 4 · J+5 — breakup 3 raisons
```
Objet : je clôture, {{companyName}} ?
sans réponse je pars du principe que :
1. votre site actuel vous convient (parfait, je vous laisse),
2. ce n'est pas le moment (on en reparle plus tard ?),
3. ce n'est pas vous qui gérez ça (vers qui me tourner ?).
un mot et j'arrête. la maquette pour {{companyName}} reste à vous.
Nathan Fenina
Agence Decupler
PPS : pas le bon moment ? un « stop » et je vous laisse tranquille.
```

---

## Prêt à pousser
- Variables déjà en base : `{{companyName}}` · `{{secteur}}` · `{{ville}}` → **aucune prépa** (pas de `{{firstName}}`).
- 2 campagnes Lemlist : `Decupler · Wellness · A Analyse-10recherches` et `Decupler · Wellness · B Site-offert`.
- Split ~50/50 des 367 (≈ 183 / approche) pour comparer réponse & RDV.
- Reste à faire côté Lemlist : attacher l'expéditeur + démarrer (rien ne part avant).
