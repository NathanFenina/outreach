# 12 — Séquences campagne WELLNESS / SPA (cold mail)

> Audience **Medical Spa · Bretagne · local** (#47, ~367 leads : instituts de beauté, spas,
> massages, centres bien-être). **Cold mail.** Cible = TPE locales (gérant = destinataire).
> Vocabulaire simple et concret : **réservations, clients, être trouvé sur Google/Maps**.
> Pas de jargon SEO/GEO dans l'objet ni en accroche.
> Cadence J0 / J+2 / J+3 / J+5 (Fibonacci). Variables : `{{firstName}}` + `{{companyName}}` → aucune prépa.
> Signature partout : **Nathan Fenina / Agence Decupler**. Esprit UltB : on offre, vous gardez tout.
>
> **2 approches à A/B tester** (1 campagne Lemlist chacune, ~180 leads / approche) :
> - **Approche A — « Analyse réservations »** : je vous ai préparé une analyse pour capter plus de
>   réservations (SEO/GEO traduit en langage réservations).
> - **Approche B — « Site offert »** : je vous ai préparé un site plus moderne, gratuit, je vous l'offre.

---

## APPROCHE A — « Analyse réservations » (front-end = analyse offerte)

### Mail 1 · J0
```
Objet : vos réservations {{companyName}}
bonjour {{firstName}}, je regarde comment les instituts et spas se font trouver sur Google
et dans les nouvelles recherches (Maps, ChatGPT) au moment où un client cherche « massage »
ou « soin » près de chez lui.
j'ai préparé pour {{companyName}} une petite analyse : où vous apparaissez, où vos concurrents
passent devant, et 3 choses simples qui ramènent plus de réservations.
je vous la partage lors d'un échange de 10 min ?
Nathan Fenina
Agence Decupler
PS : l'analyse est à vous, que vous travailliez avec nous ou pas.
```

### Mail 2 · J+2
```
Objet : re: vos réservations {{companyName}}
{{firstName}}, concrètement je vous montre sur quelles recherches vos futurs clients tombent
sur un concurrent plutôt que sur {{companyName}}, et quoi changer pour récupérer ces réservations.
on prend 15 min quand vous voulez, je vous montre aussi comment on travaille.
Nathan Fenina
Agence Decupler
```

### Mail 3 · J+3 — outil gratuit
```
Objet : re: vos réservations {{companyName}}
{{firstName}}, si vous manquez de temps, pas besoin d'attendre : on a un outil qui, depuis
le nom de votre institut, vous sort votre visibilité et les premières actions à faire.
je vous le lance et je vous renvoie le résultat, c'est offert.
un simple « ok » et je m'en occupe.
Nathan Fenina
Agence Decupler
```

### Mail 4 · J+5 — breakup 3 raisons
```
Objet : je clôture, {{firstName}} ?
{{firstName}}, sans réponse je pars du principe que :
1. ce n'est pas le bon moment (on en reparle plus tard ?),
2. vous êtes déjà complet côté réservations (top, je vous laisse),
3. ce n'est pas vous qui gérez ça (vers qui me tourner ?).
un mot et j'arrête. l'analyse pour {{companyName}} reste à vous si vous la voulez.
Nathan Fenina
Agence Decupler
PPS : pas le bon moment ? un « stop » et je vous laisse tranquille.
```

---

## APPROCHE B — « Site offert » (front-end = maquette de site offerte)

> Même angle que le test BTP : on offre une version modernisée du site pour déclencher le RDV.
> Fort en local (beaucoup d'instituts ont un site daté ou juste une page Facebook).

### Mail 1 · J0
```
Objet : nouveau site {{companyName}}
bonjour {{firstName}}, je suis tombé sur {{companyName}} et je me suis permis de préparer
une version plus moderne de votre site : plus jolie sur mobile, avec la prise de rendez-vous
mise en avant pour transformer les visiteurs en réservations.
souhaitez-vous la voir ? c'est 100% gratuit, je vous l'offre, sans engagement.
Nathan Fenina
Agence Decupler
PS : que vous travailliez avec nous ou non, la maquette est pour vous.
```

### Mail 2 · J+2
```
Objet : re: nouveau site {{companyName}}
{{firstName}}, je vous montre la maquette à l'écran en 10 min : l'accueil, la page soins et
le bouton de réservation. vous gardez tout ce qui vous plaît, même si on n'avance pas ensemble.
ça vous dit ? je m'adapte à vos horaires.
Nathan Fenina
Agence Decupler
```

### Mail 3 · J+3 — preuve + être trouvé
```
Objet : re: nouveau site {{companyName}}
{{firstName}}, au-delà du design, un site propre et bien construit, c'est aussi ce qui vous
fait remonter sur Google et Maps quand quelqu'un cherche un institut près de chez vous.
on regarde ensemble la maquette + les 2-3 réglages qui vous font gagner en visibilité ?
Nathan Fenina
Agence Decupler
```

### Mail 4 · J+5 — breakup 3 raisons
```
Objet : je clôture, {{firstName}} ?
{{firstName}}, sans réponse je pars du principe que :
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
- Variables : `{{firstName}}` + `{{companyName}}` (déjà en base) → **aucune prépa**.
- 2 campagnes Lemlist : `Decupler · Wellness · A Analyse` et `Decupler · Wellness · B Site offert`.
- Split ~50/50 des 367 leads (≈ 180 par approche) pour comparer taux de réponse / RDV.
- ⚠️ Claims à garder VRAIS : pas de chiffre inventé ici (approche volontairement sobre pour du local).
