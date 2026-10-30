# Copies V2.2 à valider (30/10, après audit)

Générées par scripts/47_copies_v2.py depuis scripts/copy_v2.py. Validation dans le Sheet, onglet « 6b. Copies V2 à valider ».
Chaque mail 1 existe en variante A (livrable, ci-dessous) et B (dernière phrase remplacée par « Ça vaut 15 minutes pour en parler cette semaine ? »).

## Hypothèses par palier (HADI)
- **P1** : Une levée + un recrutement = budget et urgence : ≥ 5 % de réponses, ≥ 30 % positives (petit volume).
- **P2** : Un recrutement marketing / commercial = objectif de pipeline : ≥ 4 % de réponses sur ≥ 150 prospects.
- **P3** : Un constat chiffré sur leur propre visibilité (concurrent n°1, citations IA) : ≥ 4 % de réponses sur ≥ 300 prospects.
- **P4** : Marché principal, problème du métier + livrable offert : ≥ 3 % de réponses, ≥ 20 % positives sur ≥ 300 prospects.
- **A/B** : Livrable (A) contre rendez-vous (B) au mail 1 : on garde la variante avec le plus de « oui » sur ≥ 250 prospects par variante.


## 1.1 éditeurs SaaS

### V2-001 · P1 · a levé + recrute
**Objet :** après la levée

Félicitations pour la levée, {{firstName}}. Recruter juste après, c'est le signe que le pipeline est la priorité des prochains mois.

La moitié des acheteurs de logiciels commencent maintenant leur recherche dans un chatbot plutôt que sur Google (G2, 2026).

Seriez-vous contre que je vous envoie, en vidéo de 3 minutes, les 10 questions où vos acheteurs ne vous trouvent pas ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-002 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

La moitié des acheteurs de logiciels commencent maintenant leur recherche dans un chatbot plutôt que sur Google (G2, 2026).

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-003 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

La moitié des acheteurs de logiciels commencent maintenant leur recherche dans un chatbot plutôt que sur Google (G2, 2026).

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-004 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-005 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-006 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-007 · P4 · marché principal
**Objet :** shortlist

{{firstName}}, quand un acheteur demande à ChatGPT « {{prompt}} », c'est là que se joue la shortlist, avant même votre site.

Un sur trois finit par acheter à un éditeur qu'il ne connaissait pas (G2, 2026) : la place est encore à prendre.

Seriez-vous contre que je vous envoie les 10 questions de votre catégorie, et qui y est cité ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-008 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-009 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-010 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-011 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-012 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-013 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.2 startups IA

### V2-014 · P1 · a levé + recrute
**Objet :** après la levée

Félicitations pour la levée, {{firstName}}. Recruter juste après, c'est le signe que le pipeline est la priorité des prochains mois.

On compte plus de 1 100 startups IA en France (France Digitale 2026) : se faire citer devient plus dur que lever.

Seriez-vous contre que je vous envoie, en vidéo de 3 minutes, les 10 questions où vos acheteurs ne vous trouvent pas ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-015 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

On compte plus de 1 100 startups IA en France (France Digitale 2026) : se faire citer devient plus dur que lever.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-016 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

On compte plus de 1 100 startups IA en France (France Digitale 2026) : se faire citer devient plus dur que lever.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-017 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-018 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-019 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-020 · P4 · marché principal
**Objet :** 1 100 startups IA

{{firstName}}, il y a plus de 1 100 startups IA en France (France Digitale). Quand un client demande à ChatGPT un outil pour « {{prompt}} », il en cite trois.

La différence se joue sur ce que les IA savent de vous : cas d'usage, preuves, entités.

Seriez-vous contre que je vous envoie où en est {{companyName}} sur ces questions ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-021 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-022 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-023 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-024 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-025 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-026 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.3 ESN et intégrateurs

### V2-027 · P1 · a levé + recrute
**Objet :** après la levée

Félicitations pour la levée, {{firstName}}. Recruter juste après, c'est le signe que le pipeline est la priorité des prochains mois.

Sur « intégrateur + éditeur + ville », ce sont les partenaires les mieux référencés qui reçoivent les demandes entrantes.

Seriez-vous contre que je vous envoie, en vidéo de 3 minutes, les 10 questions où vos acheteurs ne vous trouvent pas ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-028 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Sur « intégrateur + éditeur + ville », ce sont les partenaires les mieux référencés qui reçoivent les demandes entrantes.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-029 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Sur « intégrateur + éditeur + ville », ce sont les partenaires les mieux référencés qui reçoivent les demandes entrantes.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-030 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-031 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-032 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-033 · P4 · marché principal
**Objet :** {{motcle}}

{{firstName}}, « {{motcle}} » est cherché environ {{volume}} fois par mois, et c'est {{concurrent}} qui récupère ces demandes.

Pour une ESN, c'est souvent le seul contact entrant qui n'est ni un appel d'offres ni une recommandation.

Seriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-034 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-035 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-036 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-037 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-038 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-039 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.4 sociétés de cybersécurité

### V2-040 · P1 · a levé + recrute
**Objet :** après la levée

Félicitations pour la levée, {{firstName}}. Recruter juste après, c'est le signe que le pipeline est la priorité des prochains mois.

Un RSSI vérifie toujours avant d'appeler : sur Google, et de plus en plus dans ChatGPT, où ce sont les gros acteurs qui sont cités.

Seriez-vous contre que je vous envoie, en vidéo de 3 minutes, les 10 questions où vos acheteurs ne vous trouvent pas ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-041 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Un RSSI vérifie toujours avant d'appeler : sur Google, et de plus en plus dans ChatGPT, où ce sont les gros acteurs qui sont cités.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-042 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Un RSSI vérifie toujours avant d'appeler : sur Google, et de plus en plus dans ChatGPT, où ce sont les gros acteurs qui sont cités.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-043 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-044 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-045 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-046 · P4 · marché principal
**Objet :** audit de sécurité

{{firstName}}, avant de contacter un prestataire pour un audit ou un pentest, un RSSI se renseigne seul, sur Google et de plus en plus dans ChatGPT.

Sur « {{prompt}} », la réponse cite {{concurrent}}. Pas {{companyName}}.

Seriez-vous contre que je vous envoie les questions où vous pourriez être la référence citée ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-047 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-048 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-049 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-050 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-051 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-052 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.5 cabinets de conseil

### V2-053 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Les IA citent d'abord McKinsey, BCG et Bain ; les petits cabinets ne remontent que sur les questions de niche (test Consultor, 2026).

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-054 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Les IA citent d'abord McKinsey, BCG et Bain ; les petits cabinets ne remontent que sur les questions de niche (test Consultor, 2026).

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-055 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-056 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-057 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-058 · P4 · marché principal
**Objet :** grands cabinets

{{firstName}}, quand un dirigeant demande à ChatGPT un cabinet pour « {{prompt}} », il cite d'abord les grands noms. Sur les questions de niche, en revanche, les petits cabinets passent devant (test Consultor, 2026).

C'est là que se fait votre shortlist.

Seriez-vous contre que je vous envoie les 10 questions de votre spécialité, et qui y est cité ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-059 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-060 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-061 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-062 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-063 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-064 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.6 cabinets d'expertise comptable

### V2-065 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Depuis le 1er septembre 2026, la réception des factures électroniques est obligatoire : les dirigeants cherchent un cabinet qui les accompagne.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-066 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Depuis le 1er septembre 2026, la réception des factures électroniques est obligatoire : les dirigeants cherchent un cabinet qui les accompagne.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-067 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-068 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-069 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-070 · P4 · marché principal
**Objet :** facture électronique

{{firstName}}, depuis le 1er septembre, les dirigeants cherchent un cabinet qui les accompagne sur la facture électronique.

Sur « expert-comptable {{ville}} », c'est {{concurrent}} qui sort, pas {{companyName}}.

Seriez-vous contre que je vous envoie ce qui lui donne cette place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-071 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-072 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-073 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-074 · FU2 · J+11 · relance sobre
**Objet :** (même fil)

{{firstName}}, une question simple : la visibilité de {{companyName}} sur Google et dans ChatGPT est-elle un sujet pour vous cette année ?

Un « oui » ou un « non » me suffit.

Nathan

### V2-075 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-076 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.7 conseils en M&A et transmission

### V2-077 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

7 cédants sur 10 à plus d'un an de la vente se renseignent seuls (Bpifrance Le Lab), sur les simulateurs et les plateformes d'annonces.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-078 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

7 cédants sur 10 à plus d'un an de la vente se renseignent seuls (Bpifrance Le Lab), sur les simulateurs et les plateformes d'annonces.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-079 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-080 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-081 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-082 · P4 · marché principal
**Objet :** vos futurs cédants

{{firstName}}, 7 dirigeants sur 10 qui pensent à céder dans plus d'un an se renseignent encore seuls (Bpifrance Le Lab).

Ils posent leurs questions à Google et à ChatGPT, et tombent sur les simulateurs et les plateformes d'annonces, rarement sur un conseil comme {{companyName}}.

Seriez-vous contre que je vous envoie ces questions, et qui y répond aujourd'hui ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-083 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-084 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-085 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-086 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-087 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-088 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.8 cabinets de gestion de patrimoine

### V2-089 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

44 % des épargnants décident seuls, et près d'un jeune sur cinq consulte une IA avant de placer (AMF 2025).

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-090 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

44 % des épargnants décident seuls, et près d'un jeune sur cinq consulte une IA avant de placer (AMF 2025).

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-091 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-092 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-093 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-094 · P4 · marché principal
**Objet :** vos futurs clients

{{firstName}}, depuis le 11 août, plus d'appel sans consentement préalable. Et 44 % des épargnants décident déjà seuls (AMF).

Quand on demande à ChatGPT « {{prompt}} », il cite {{concurrent}}, pas {{companyName}}.

Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-095 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-096 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-097 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-098 · FU2 · J+11 · relance sobre
**Objet :** (même fil)

{{firstName}}, une question simple : la visibilité de {{companyName}} sur Google et dans ChatGPT est-elle un sujet pour vous cette année ?

Un « oui » ou un « non » me suffit.

Nathan

### V2-099 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-100 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.9 agences

### V2-101 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Vos clients vous demandent « et ChatGPT ? », et peu d'agences ont une réponse technique à leur donner.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-102 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Vos clients vous demandent « et ChatGPT ? », et peu d'agences ont une réponse technique à leur donner.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-103 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-104 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-105 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-106 · P4 · marché principal
**Objet :** vos clients et ChatGPT

{{firstName}}, question directe : quand un client vous demande s'il ressort dans ChatGPT, vous refusez, vous sous-traitez ou vous gérez en interne ?

On produit le GEO en marque blanche pour quelques agences : vous gardez le client et la marge, on exécute.

Seriez-vous contre que je fasse l'audit GEO d'un de vos clients, sous votre marque ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-107 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : l'audit sous votre marque est offert, vous jugez sur pièce.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-108 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-109 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-110 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-111 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-112 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.10 agences événementielles et de conférenciers

### V2-113 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Les entreprises cherchent un lieu ou un conférencier sur Google et ChatGPT, et ce sont les plateformes qui captent la demande.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-114 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Les entreprises cherchent un lieu ou un conférencier sur Google et ChatGPT, et ce sont les plateformes qui captent la demande.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-115 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-116 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-117 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-118 · P4 · marché principal
**Objet :** séminaire {{ville}}

{{firstName}}, quand une entreprise cherche « {{motcle}} », ce sont les plateformes et {{concurrent}} qui récupèrent la demande.

Un devis qui arrive en direct, c'est une commission en moins et un client à vous.

Seriez-vous contre que je vous envoie ce qui vous manque pour être choisi en direct ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-119 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour l'Académie Madelrieux, +46 % de clics Google en 3 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-120 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-121 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-122 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-123 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-124 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.11 cabinets de recrutement

### V2-125 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Les mandats viennent du réseau et de LinkedIn ; les DRH qui cherchent un cabinet par métier tombent sur les jobboards et les gros réseaux.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-126 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Les mandats viennent du réseau et de LinkedIn ; les DRH qui cherchent un cabinet par métier tombent sur les jobboards et les gros réseaux.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-127 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-128 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-129 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-130 · P4 · marché principal
**Objet :** cabinet {{motcle}}

{{firstName}}, quand une DRH cherche « {{motcle}} », elle tombe sur les jobboards et sur {{concurrent}}, rarement sur un cabinet spécialisé comme {{companyName}}.

C'est pourtant le mandat que vous voulez : celui qui arrive sans prospection.

Seriez-vous contre que je vous envoie comment le capter ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-131 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-132 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-133 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-134 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-135 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-136 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.12 organismes de formation

### V2-137 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Les inscriptions dépendent des financeurs et des plateformes ; sur « formation + métier », les gros organismes prennent la place.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-138 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Les inscriptions dépendent des financeurs et des plateformes ; sur « formation + métier », les gros organismes prennent la place.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-139 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-140 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-141 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-142 · P4 · marché principal
**Objet :** vos inscriptions

{{firstName}}, sur « {{motcle}} », ce sont les gros organismes et les plateformes qui récupèrent les inscriptions.

Pour l'Académie Madelrieux, un organisme comme vous, on a obtenu +46 % de clics Google en 3 mois, sans publicité.

Seriez-vous contre que je vous envoie ce qu'on ferait pour {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-143 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-144 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-145 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-146 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro, que je sache quoi faire.

Nathan

### V2-147 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-148 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 1.13 cabinets d'avocats d'affaires

### V2-149 · P2 · recrute en marketing
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute en marketing, {{firstName}}. J'imagine que le pipeline entrant fait partie de ses objectifs.

Les dossiers viennent de la recommandation ; les annuaires et les legaltech captent les recherches.

Pour une fraction du coût d'un recrutement, seriez-vous contre que je vous envoie les questions où vos concurrents sont cités à votre place ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-150 · P2b · recrute des commerciaux
**Objet :** votre recrutement

J'ai vu que {{companyName}} recrute des commerciaux, {{firstName}}. Il va falloir leur donner des demandes à traiter.

Les dossiers viennent de la recommandation ; les annuaires et les legaltech captent les recherches.

Seriez-vous contre que je vous envoie les questions où vos futurs clients trouvent vos concurrents plutôt que vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-151 · P3a · baisse de trafic (si baisse > 10 %)
**Objet :** trafic {{companyName}}

{{firstName}}, d'après les outils SEO, le trafic Google de {{companyName}} a baissé d'environ {{baisse}} % en un an (estimation).

Ce n'est pas forcément de votre fait : depuis l'arrivée des réponses IA de Google en France, une partie des clics ne descend plus jusqu'aux sites.

Seriez-vous contre que je vous envoie le plan pour reprendre ces demandes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-152 · P3b · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-153 · P3c · concurrent cité par les IA (chiffré)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-154 · P4 · marché principal
**Objet :** avocat {{motcle}}

{{firstName}}, quand un dirigeant cherche « avocat {{motcle}} {{ville}} », ce sont les annuaires et {{concurrent}} qui sortent.

Dans le respect de vos règles déontologiques, votre expertise peut y apparaître : contenu de fond, pages par domaine, présence dans les réponses IA.

Seriez-vous contre que je vous envoie où {{companyName}} en est ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-155 · Champion (SEO / contenu / marketing)
**Objet :** « {{motcle}} »

{{firstName}}, « {{motcle}} » est cherché {{volume}} fois par mois, et {{concurrent}} y passe devant {{companyName}}, sur Google comme dans ChatGPT.

Il vous manque moins que vous ne pensez : surtout les entités et les données structurées que les IA lisent pour citer une source.

Seriez-vous contre que je vous en envoie la liste ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour Cloudtech, +17 % de leads issus du SEO et des IA en 6 mois.
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-156 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message au cas où il serait passé sous la pile.

Toujours partant pour que je vous l'envoie ? Un « oui » suffit.

Nathan

### V2-157 · VP2 · J+8 · nouvel objet
**Objet :** 1 levier sur 7

{{firstName}}, pas de rendez-vous cette fois : un levier que votre équipe peut activer seule.

En haut de votre page la plus importante, une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent.

J'ai les 6 autres pour {{companyName}}, classés par impact. Seriez-vous contre que je vous les envoie ?

Nathan
PS : ce levier est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-158 · FU2 · J+11 · relance sobre
**Objet :** (même fil)

{{firstName}}, une question simple : la visibilité de {{companyName}} sur Google et dans ChatGPT est-elle un sujet pour vous cette année ?

Un « oui » ou un « non » me suffit.

Nathan

### V2-159 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée de ma part.

Donnez-moi la page de {{companyName}} qui compte le plus : je la travaille pour qu'elle soit citée par les IA (50 critères), et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Je vous l'envoie sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-160 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, je ne veux pas encombrer votre boîte, c'est mon dernier message.

Si la visibilité de {{companyName}} sur Google et ChatGPT remonte un jour dans vos priorités, je serai content d'en parler. Et si quelqu'un d'autre gère ce sujet chez vous, dites-moi à qui écrire.

Bonne continuation,
Nathan


## 2.1 entreprises du BTP et de la rénovation

### V2-161 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « rénovation {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-162 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleure entreprise de rénovation à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-163 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-164 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 chantiers de plus ?

Question directe, {{firstName}} : si 20 chantiers de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques entreprises du BTP et de la rénovation {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-165 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« rénovation {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-166 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « rénovation {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-167 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-168 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-169 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.2 installateurs de pompes à chaleur et de clim

### V2-170 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « pompe à chaleur {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-171 · P2 · saison (métiers saisonniers)
**Objet :** avant la saison

{{firstName}}, les PAC air-air font +31 % au second semestre avec les canicules (Uniclima). C'est cet hiver que se prépare la visibilité de l'été prochain.

Je cherche quelques installateurs de pompes à chaleur et de clim {{zone}} prêts à prendre 20 installations de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-172 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur installateur de pompe à chaleur à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-173 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-174 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 installations de plus ?

Question directe, {{firstName}} : si 20 installations de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques installateurs de pompes à chaleur et de clim {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-175 · P4 · marché principal C · interdiction de prospecter (rénovation énergétique)
**Objet :** prospecter, c'est fini

{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.

Il ne reste que les clients qui vous cherchent, sur Google et dans ChatGPT.

Seriez-vous contre que je vous envoie comment en recevoir 20 de plus par mois, payé à la performance ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-176 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« pompe à chaleur {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-177 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « pompe à chaleur {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-178 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-179 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-180 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.3 installateurs photovoltaïques

### V2-181 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « panneaux solaires {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-182 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur installateur de panneaux solaires à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-183 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-184 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 installations de plus ?

Question directe, {{firstName}} : si 20 installations de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques installateurs photovoltaïques {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-185 · P4 · marché principal C · interdiction de prospecter (rénovation énergétique)
**Objet :** prospecter, c'est fini

{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.

Il ne reste que les clients qui vous cherchent, sur Google et dans ChatGPT.

Seriez-vous contre que je vous envoie comment en recevoir 20 de plus par mois, payé à la performance ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-186 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« panneaux solaires {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-187 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « panneaux solaires {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-188 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-189 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-190 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.4 entreprises de rideaux métalliques

### V2-191 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « dépannage rideau métallique {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-192 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleure entreprise de rideaux métalliques à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-193 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-194 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 interventions de plus ?

Question directe, {{firstName}} : si 20 interventions de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques entreprises de rideaux métalliques {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-195 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« dépannage rideau métallique {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-196 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « dépannage rideau métallique {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-197 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-198 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-199 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.5 installateurs de monte-escaliers

### V2-200 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « monte-escalier {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-201 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur installateur de monte-escalier à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-202 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-203 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 installations de plus ?

Question directe, {{firstName}} : si 20 installations de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques installateurs de monte-escaliers {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-204 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« monte-escalier {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-205 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « monte-escalier {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-206 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-207 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-208 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.6 entreprises de pompes funèbres

### V2-209 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « pompes funèbres {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-210 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « quelles pompes funèbres choisir à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-211 · P4 · marché principal · version sobre (2.6)
**Objet :** familles à {{ville}}

{{firstName}}, quand une famille doit organiser des obsèques à {{ville}}, elle cherche dans l'urgence, souvent sur son téléphone.

Sur « pompes funèbres {{ville}} », c'est {{concurrent}} qui apparaît en premier.

Seriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-212 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« pompes funèbres {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-213 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « pompes funèbres {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-214 · FU2 · J+11 · relance sobre (2.6 pompes funèbres)
**Objet :** (même fil)

{{firstName}}, une question simple : est-ce que la visibilité de {{companyName}} sur Google auprès des familles de {{ville}} est un sujet pour vous cette année ?

Un « oui » ou un « non » me suffit.

Nathan

### V2-215 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-216 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.7 entreprises de sécurité incendie

### V2-217 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « maintenance extincteurs {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-218 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleure entreprise de sécurité incendie à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-219 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-220 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 contrats de plus ?

Question directe, {{firstName}} : si 20 contrats de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques entreprises de sécurité incendie {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-221 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« maintenance extincteurs {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-222 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « maintenance extincteurs {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-223 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-224 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-225 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.8 menuisiers et poseurs de fenêtres

### V2-226 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « fenêtres {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-227 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur menuisier pour changer ses fenêtres à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-228 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-229 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 chantiers de plus ?

Question directe, {{firstName}} : si 20 chantiers de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques menuisiers et poseurs de fenêtres {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-230 · P4 · marché principal C · interdiction de prospecter (rénovation énergétique)
**Objet :** prospecter, c'est fini

{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.

Il ne reste que les clients qui vous cherchent, sur Google et dans ChatGPT.

Seriez-vous contre que je vous envoie comment en recevoir 20 de plus par mois, payé à la performance ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-231 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« fenêtres {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-232 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « fenêtres {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-233 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-234 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-235 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.9 couvreurs et entreprises d'isolation

### V2-236 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « couvreur {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-237 · P2 · saison (métiers saisonniers)
**Objet :** avant la saison

{{firstName}}, après chaque tempête, le premier couvreur visible sur Google Maps prend les appels, et avec les arnaques, les clients vérifient les avis avant d'appeler.

Je cherche quelques couvreurs et entreprises d'isolation {{zone}} prêts à prendre 20 chantiers de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-238 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur couvreur à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-239 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-240 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 chantiers de plus ?

Question directe, {{firstName}} : si 20 chantiers de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques couvreurs et entreprises d'isolation {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-241 · P4 · marché principal C · interdiction de prospecter (rénovation énergétique)
**Objet :** prospecter, c'est fini

{{firstName}}, depuis la loi du 30 juin 2025, impossible de démarcher un particulier pour de la rénovation énergétique, même par SMS ou par mail.

Il ne reste que les clients qui vous cherchent, sur Google et dans ChatGPT.

Seriez-vous contre que je vous envoie comment en recevoir 20 de plus par mois, payé à la performance ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-242 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« couvreur {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-243 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « couvreur {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-244 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-245 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-246 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.10 piscinistes

### V2-247 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « pisciniste {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-248 · P2 · saison (métiers saisonniers)
**Objet :** avant la saison

{{firstName}}, les projets de piscine se décident entre janvier et avril : c'est maintenant qu'il faut être visible.

Je cherche quelques piscinistes {{zone}} prêts à prendre 20 chantiers de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-249 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur pisciniste à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-250 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-251 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 chantiers de plus ?

Question directe, {{firstName}} : si 20 chantiers de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques piscinistes {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-252 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« pisciniste {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-253 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « pisciniste {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-254 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-255 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-256 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.11 installateurs d'alarmes et de vidéosurveillance

### V2-257 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « alarme maison {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-258 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur installateur d'alarme à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-259 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-260 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 contrats de plus ?

Question directe, {{firstName}} : si 20 contrats de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques installateurs d'alarmes et de vidéosurveillance {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-261 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« alarme maison {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-262 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « alarme maison {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-263 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-264 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-265 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.12 cuisinistes

### V2-266 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « cuisiniste {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-267 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur cuisiniste à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-268 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-269 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 projets de plus ?

Question directe, {{firstName}} : si 20 projets de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques cuisinistes {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-270 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« cuisiniste {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-271 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « cuisiniste {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-272 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-273 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-274 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.13 entreprises de déménagement

### V2-275 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « déménageur {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-276 · P2 · saison (métiers saisonniers)
**Objet :** avant la saison

{{firstName}}, les devis de l'été se demandent au printemps.

Je cherche quelques entreprises de déménagement {{zone}} prêts à prendre 20 déménagements de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-277 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur déménageur à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-278 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-279 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 déménagements de plus ?

Question directe, {{firstName}} : si 20 déménagements de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques entreprises de déménagement {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-280 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« déménageur {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-281 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « déménageur {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-282 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-283 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-284 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.14 paysagistes

### V2-285 · P1 · concurrent devant sur Google Maps
**Objet :** {{concurrent}} devant

{{firstName}}, sur « paysagiste {{ville}} », {{concurrent}} sort avant {{companyName}} sur Google Maps. Ces appels-là, c'est lui qui les reçoit.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-286 · P2 · saison (métiers saisonniers)
**Objet :** avant la saison

{{firstName}}, les chantiers du printemps se décident en hiver.

Je cherche quelques paysagistes {{zone}} prêts à prendre 20 chantiers de plus par mois, en partenariat à la performance : vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-287 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleur paysagiste à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-288 · P4 · marché principal A · plateformes de devis (commentaire Nathan)
**Objet :** vos devis

{{firstName}}, les plateformes de devis facturent jusqu'à 90 € HT un prospect, et le partagent souvent entre 4 ou 5 artisans.

Nous, on aide nos clients à recevoir leurs demandes en direct, sur leur site et leur fiche Google, sans payer chaque contact.

Seriez-vous contre que je vous envoie comment ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-289 · P4 · marché principal B · capacité + performance (validée par Nathan)
**Objet :** 20 chantiers de plus ?

Question directe, {{firstName}} : si 20 chantiers de plus arrivaient chaque mois, vous auriez l'équipe pour les faire ?

Je cherche quelques paysagistes {{zone}} pour un partenariat à la performance : on travaille votre site et votre fiche Google, vous payez sur les résultats, pas avant.

Seriez-vous contre que je vous envoie comment ça marche ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : à la performance, si les demandes n'arrivent pas, vous ne payez pas.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-290 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« paysagiste {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-291 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « paysagiste {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-292 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-293 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-294 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 2.15 entreprises de travaux publics et de génie civil

### V2-295 · P3 · absent de ChatGPT
**Objet :** ChatGPT et {{ville}}

{{firstName}}, j'ai demandé à ChatGPT « meilleure entreprise de travaux publics à {{ville}} ». Il cite {{concurrent}}, pas {{companyName}}.

De plus en plus de clients posent la question comme ça avant d'appeler.

Seriez-vous contre que je vous envoie pourquoi il est cité, et ce qu'il faudrait pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-296 · P4 · marché principal D · maîtres d'ouvrage privés (2.15)
**Objet :** vos marchés privés

{{firstName}}, les marchés publics passent par les plateformes d'appel d'offres. Les maîtres d'ouvrage privés, eux, cherchent sur Google « travaux publics {{zone}} », et c'est {{concurrent}} qu'ils trouvent.

Un marché privé qui arrive en direct, c'est un dossier sans mise en concurrence à 10.

Seriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-297 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« travaux publics {{ville}} » est cherché environ {{volume}} fois par mois, et les premiers de la carte reçoivent l'essentiel des appels.

Toujours partant pour que je vous envoie ce qui vous sépare d'eux ?

Nathan

### V2-298 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}} sur « travaux publics {{ville}} ».

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-299 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. votre planning est plein jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-300 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre site qui compte le plus : je la travaille pour que Google et ChatGPT la recommandent, et je vous dis ce qui vous manque. C'est offert.

Vous gardez le résultat. Sur quelle page je travaille ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-301 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message, je ne veux pas vous encombrer.

Si un jour vous voulez plus de demandes en direct, sans payer chaque contact, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 4.1 hôtels indépendants

### V2-302 · P1 · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « hôtel {{ville}} », {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-303 · P3 · ChatGPT cite un concurrent
**Objet :** {{concurrent}} sur ChatGPT

{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.

Un Français sur trois a déjà utilisé une IA pour préparer un voyage (KAYAK-Ipsos), et ces IA s'appuient surtout sur Booking, pas sur votre site.

Seriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-304 · P4 · marché principal
**Objet :** vos commissions

{{firstName}}, chaque réservation Booking coûte de 15 à 25 % de commission (UMIH), et un hôtel sur deux voit une OTA vendre ses chambres moins cher que son propre site (HOTREC 2026).

Seriez-vous contre que je vous envoie combien de recherches « hôtel {{ville}} » pourraient arriver en direct chez {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-305 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« hôtel {{ville}} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?

Nathan

### V2-306 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-307 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. vous êtes complets jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-308 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.

Vous gardez le résultat. Sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-309 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message.

Si un jour vous voulez plus de réservations en direct, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 4.2 spas et instituts

### V2-310 · P1 · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « spa {{ville}} », {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-311 · P3 · ChatGPT cite un concurrent
**Objet :** {{concurrent}} sur ChatGPT

{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.

Seriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-312 · P4 · marché principal
**Objet :** vos nouvelles clientes

{{firstName}}, vos fidèles restent, mais les nouvelles clientes qui cherchent « spa {{ville}} » tombent sur {{concurrent}} avant vous, ou passent par une plateforme qui prend sa commission.

Une cliente qui vous trouve sur Google Maps ne vous coûte rien.

Seriez-vous contre que je vous envoie comment la récupérer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-313 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« spa {{ville}} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?

Nathan

### V2-314 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-315 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. vous êtes complets jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-316 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.

Vous gardez le résultat. Sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-317 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message.

Si un jour vous voulez plus de nouvelles clientes, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 4.3 résidences seniors

### V2-318 · P1 · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « résidence seniors {{ville}} », {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-319 · P3 · ChatGPT cite un concurrent
**Objet :** {{concurrent}} sur ChatGPT

{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.

Seriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-320 · P4 · marché principal
**Objet :** familles à {{ville}}

{{firstName}}, quand une famille cherche une résidence pour un parent, elle compare en ligne, sur Google et les annuaires, avant d'appeler.

Sur « résidence seniors {{ville}} », c'est {{concurrent}} qui est vu en premier.

Seriez-vous contre que je vous envoie ce qui le place devant {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PPS : si ce n'est pas le sujet, répondez simplement « non merci ».

### V2-321 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« résidence seniors {{ville}} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?

Nathan

### V2-322 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-323 · FU2 · J+11 · relance sobre (4.3)
**Objet :** (même fil)

{{firstName}}, une question simple : est-ce que la visibilité de {{companyName}} sur Google auprès des familles de {{ville}} est un sujet pour vous cette année ?

Un « oui » ou un « non » me suffit.

Nathan

### V2-324 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.

Vous gardez le résultat. Sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-325 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message.

Si un jour vous voulez plus de familles, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 4.4 campings et résidences de tourisme

### V2-326 · P1 · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « camping {{lieu}} », {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-327 · P3 · ChatGPT cite un concurrent
**Objet :** {{concurrent}} sur ChatGPT

{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.

Un Français sur trois a déjà utilisé une IA pour préparer un voyage (KAYAK-Ipsos), et ces IA s'appuient surtout sur Booking, pas sur votre site.

Seriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-328 · P4 · marché principal
**Objet :** 900 € de séjour

{{firstName}}, sur un séjour de 900 €, entre 135 et 180 € partent chez la plateforme selon le contrat.

Les recherches « camping {{lieu}} » arrivent surtout sur Booking et sur les grands groupes, pas sur votre site.

Seriez-vous contre que je vous envoie où ces réservations directes vous échappent ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-329 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« camping {{lieu}} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?

Nathan

### V2-330 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-331 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. vous êtes complets jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-332 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.

Vous gardez le résultat. Sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-333 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message.

Si un jour vous voulez plus de réservations en direct, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 4.5 écoles et formations bien-être

### V2-334 · P1 · concurrent devant sur Google
**Objet :** {{concurrent}} devant

{{firstName}}, sur « formation {{motcle}} {{ville}} », {{concurrent}} sort avant {{companyName}}.

Je peux vous dire pourquoi il passe devant, et ce qui vous manque pour le dépasser.

Seriez-vous contre que je vous l'explique dans une vidéo de 3 minutes ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-335 · P3 · ChatGPT cite un concurrent
**Objet :** {{concurrent}} sur ChatGPT

{{firstName}}, j'ai demandé à ChatGPT « {{prompt}} ». Il recommande {{concurrent}}, pas {{companyName}}.

Seriez-vous contre que je vous envoie pourquoi {{concurrent}} est cité, et ce qu'il faut changer pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-336 · P4 · marché principal
**Objet :** vos inscriptions

{{firstName}}, quand quelqu'un cherche « formation {{motcle}} », il compare les écoles sur Google et de plus en plus dans ChatGPT, et c'est {{concurrent}} qui est cité.

Pour l'École Humaniste de Gestalt, on a fait passer la position moyenne Google de 18 à 10.

Seriez-vous contre que je vous envoie ce qu'on ferait pour {{companyName}} ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : le plan est offert, vous le gardez même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-337 · FU1 · J+3 · même fil
**Objet :** (même fil)

{{firstName}}, je remonte mon message.

« formation {{motcle}} {{ville}} » est cherché environ {{volume}} fois par mois. Toujours partant pour que je vous envoie combien de ces recherches vous reviennent ?

Nathan

### V2-338 · VP2 · J+8 · nouvel objet
**Objet :** pourquoi {{concurrent}}

{{firstName}}, pas de rendez-vous cette fois.

Je regarde votre fiche Google, votre site et vos avis, et je vous dis en 3 minutes de vidéo ce qui vous manque face à {{concurrent}}.

Je vous l'envoie ?

Nathan
PS : la vidéo est à vous, même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-339 · FU2 · J+11 · relance 1-2-3
**Objet :** (même fil)

Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :

1. vos promotions sont complètes jusqu'en 2028 ;
2. ce n'est pas le sujet et vous voulez que j'arrête ;
3. Claude Code a pris le contrôle de votre PC et ne vous laisse plus répondre.

Répondez juste le numéro.

Nathan

### V2-340 · VP3 · J+21 · nouvel objet
**Objet :** votre page

{{firstName}}, dernière idée.

Donnez-moi la page de votre choix : je la rends citable par les IA, pas seulement par Google (50 critères), et je vous ajoute les données structurées qui vous manquent. C'est offert.

Vous gardez le résultat. Sur quelle page ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-341 · FU3 · J+24 · rupture
**Objet :** (même fil)

{{firstName}}, c'est mon dernier message.

Si un jour vous voulez plus de nouveaux inscrits, répondez simplement « oui » et je reviens vers vous.

Bonne continuation,
Nathan


## 1.x intent SEO / GEO (tous)

### V2-342 · P3b · n°1 sur le mot-clé business + roadmap
**Objet :** {{motcle}}

{{firstName}}, sur « {{motcle}} » ({{volume}} recherches par mois), c'est {{concurrent}} qui est n°1 {{part}}.

Je peux vous partager la roadmap pour le rattraper : ce qu'il a, ce qui vous manque, dans l'ordre où ça rapporte.

Seriez-vous contre que je la monte pour vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
{{ps}} (preuve du sous-ICP)
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-343 · P3c · visibilité IA (ChatGPT + Perplexity + Google IA)
**Objet :** {{concurrent}} cité, pas vous

{{firstName}}, j'ai posé la question que vos clients posent, « {{prompt}} », à ChatGPT, Perplexity et Google.

Sur {{n_reponses}} réponses, {{concurrent}} est cité {{n_concurrent}} fois. {{companyName}} : {{n_vous}}.

C'est là que se fait la shortlist. Seriez-vous contre que je vous envoie ce qui le fait citer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
{{ps}} (preuve du sous-ICP)
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-344 · P3d · réponse IA de Google (AI Overview)
**Objet :** la réponse de Google

{{firstName}}, quand on cherche « {{motcle}} » sur Google, la réponse IA tout en haut cite {{concurrent}}. Pas {{companyName}}.

Cette réponse passe avant les liens, et beaucoup ne regardent plus ceux d'en dessous.

Seriez-vous contre que je vous envoie comment y entrer ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
{{ps}} (preuve du sous-ICP)
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-345 · VP2 variante · roadmap de rattrapage
**Objet :** votre roadmap

{{firstName}}, on prépare des roadmaps SEO et IA pour des entreprises comme {{companyName}} : où vous perdez des demandes, qui les récupère, et les 3 actions qui rapportent le plus.

Seriez-vous contre que je monte la vôtre ? Je vous l'envoie, vous gardez le résultat.

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-346 · VP3 variante · cas client et process
**Objet :** comment on travaille

{{firstName}}, dernière idée de ma part.

Je peux vous envoyer un cas client proche de {{companyName}} et notre process, étape par étape : audit, pages, citations par les IA, suivi des demandes.

Je vous l'envoie ?

Nathan
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.


## 2.x intent SEO / GEO (tous)

### V2-347 · P3b · n°1 sur Google Maps + roadmap
**Objet :** {{concurrent}} devant

{{firstName}}, sur « {{metier}} {{ville}} » ({{volume}} recherches par mois), c'est {{concurrent}} qui est n°1 {{part}}.

Je peux vous partager la roadmap pour passer devant lui : fiche Google, avis, pages du site, dans l'ordre.

Seriez-vous contre que je la monte pour vous ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.

### V2-348 · P3c · ChatGPT + Google IA
**Objet :** {{concurrent}} recommandé

{{firstName}}, j'ai demandé à ChatGPT et à Google « {{pro}} à {{ville}} ». Les deux recommandent {{concurrent}}. {{companyName}} n'apparaît dans aucune réponse.

De plus en plus de clients choisissent comme ça avant d'appeler.

Seriez-vous contre que je vous envoie ce qui le fait recommander ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : pour L'Artisan d'à côté, une entreprise du bâtiment, on est allé chercher 20 nouveaux clients par mois.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.


## 4.x intent SEO / GEO (tous)

### V2-349 · P3c · ChatGPT + Google IA (hébergements)
**Objet :** {{concurrent}} recommandé

{{firstName}}, j'ai demandé à ChatGPT et à Google « {{prompt}} ». Les deux recommandent {{concurrent}}. {{companyName}} n'apparaît pas.

Un Français sur trois a déjà utilisé une IA pour préparer un voyage (KAYAK-Ipsos), et ces IA s'appuient surtout sur Booking, pas sur votre site.

Seriez-vous contre que je vous envoie ce qui le fait recommander, et la roadmap pour l'être aussi ?

Nathan Fenina, fondateur de Décupler (SEO + IA)
PS : c'est offert, vous gardez le résultat même si on ne travaille jamais ensemble.
PPS : pas le bon moment ? Répondez « bye bye » et je vous laisse tranquille.
