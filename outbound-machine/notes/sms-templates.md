# Templates SMS / WhatsApp — Décupler

> Variables entre `{}` : à remplacer (l'app remplit `{nomBoite}` automatiquement).
> Règle : SMS de masse à froid = **sans accents** (GSM-7, 160 car/segment, moins cher).
> SMS chaud 1:1 (rappel de RDV) = accents tolérés, peu de volume.
> Toujours finir un envoi à froid par une sortie STOP (RGPD).

---

## 1. Cold SMS — Site offert (paysagistes / BTP local) ✅ VALIDÉ, convertit bien

> Bonjour {nomBoite}, Nathan de Decupler. Je sais que c'est un peu direct, mais j'ai pris les devants: je vous ai prepare un site moderne (offert, 30 premiers paysagistes) pour signer plus de devis. Je vous le montre? Sinon repondez STOP et j'arrete.

- Statut : **testé, ça marche** (premier contact à froid).
- Personnalisation : `{nomBoite}` = nom de la boîte. Fallback si vide : « Bonjour, ».
- Adapter « 30 premiers paysagistes » au métier ciblé (couvreurs, élagueurs…).

---

## 2. Rappel générique — présentation à l'écran (dans l'app, onglet « À présenter »)

> Bonjour, Nathan de Decupler. Petit rappel : je vous ai prepare un site moderne, je vous le montre 10 min a l'ecran ? Dites-moi quand ca vous arrange. Sinon repondez STOP.

- Sans date/lien précis — pour relancer un prospect chaud pas encore calé.

---

## 3. Rappel RDV visio (Google Meet) — le jour J ✅ à utiliser

**Version recommandée (avec accroche « donner envie ») :**

> Bonjour {nomBoite}, Nathan de Decupler. Petit rappel de notre RDV a {heure} : je vous montre EN DIRECT le site que j'ai prepare pour vous — vos prestations, vos avis Google, pret a recevoir des demandes de devis. 15 min, pas plus.
> Lien : {lienMeet}
> Depuis le telephone c'est ok, idealement au calme. A tout a l'heure !

- L'accroche = on **tease le livrable** (« votre site EN DIRECT, avec vos avis, prêt à capter des devis ») → ça crée l'envie de se connecter.
- `{heure}` ex. « 14h30 », `{lienMeet}` = lien Google Meet.
- Envoyer ~1-2 h avant le call.

**Variante courte (si tu veux moins de texte) :**

> Bonjour {nomBoite}, on se voit a {heure} : je vous montre votre nouveau site (avis Google + demandes de devis) en 15 min. Lien : {lienMeet}. Au calme si possible, a tout a l'heure ! — Nathan, Decupler

---

## Idées d'accroches « donner envie » (à piocher pour le rappel)

- « votre site EN DIRECT, avec vos vrais avis Google » → concret, ils veulent voir leur nom.
- « prêt à recevoir des demandes de devis dès aujourd'hui » → bénéfice immédiat.
- « je vous montre comment un client vous trouve sur Google et vous contacte » → mise en scène.
- « 15 min, pas plus » → lève l'objection temps (celle qu'ils citent le plus).
- Éviter : « pour vous présenter mon offre » (ça sent la vente) → dire « je vous montre CE QUE J'AI FAIT pour vous » (c'est un cadeau, pas un pitch).
