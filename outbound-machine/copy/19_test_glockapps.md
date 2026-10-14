# 19 · Test de délivrabilité GlockApps (devoir Igor : 3 tests)

> But : savoir **où arrivent vraiment nos mails** (boîte principale, onglet Promotions, spam) chez
> Google, Outlook et les serveurs privés, au lieu de deviner. Igor : « GlockApps est le seul fournisseur
> fiable ; les scores de délivrabilité Lemlist ne le sont pas. »

## Coût (page tarifs GlockApps, relevée le 14/10/2026)
- **Free : 0 $, 2 crédits de test de spam.** Ça suffit pour démarrer.
- Essential 59 $/mois (360 crédits), Growth 99 $/mois, Enterprise 129 $/mois : prix en **facturation annuelle** ; le mensuel est plus cher (≈ 85 $ vu par Nathan).
- Il existe aussi des **packs de crédits** sans abonnement (Igor les conseille). Prix non affichés sur la page : à vérifier dans l'onglet « Spam Test Credit Packs ».
- **Recommandation :** compte gratuit (2 tests) + le plus petit pack de crédits pour le 3e. Pas d'abonnement tant qu'on n'a pas les résultats.
- ⚠️ Vérifier dans la FAQ « What does 1 Email Spam Test entail? » combien de crédits consomme un test.

## Les 3 tests
On garde **le même texte que la vraie campagne** (sinon le test ne veut rien dire), texte brut, sans tracking.

| # | Boîte d'envoi | Contenu | Ce qu'on apprend |
|---|---|---|---|
| 1 | `nathan@decupler-agency.com` | Mail 1 de la campagne **Conseil · 10 prompts** (notre meilleure campagne), tel qu'en production | Placement actuel de notre meilleur copy |
| 2 | `nathan.fenina@decupler-seo.com` (autre domaine) | Mail 1 **Batimat** tel qu'en production | Si le domaine ou le contenu Batimat est le problème |
| 3 | même boîte que le test 1 | Mail Conseil réécrit façon Igor : objet camouflage `chatgpt`, aucun lien, CTA de permission, **PS désinscription** | Si les changements d'Igor améliorent le placement |

Les 10 domaines d'envoi sont sur SURBL : si les 3 tests sont mauvais partout, c'est le domaine ; si seul le contenu varie, c'est le copy.

## Pas à pas
1. Créer le compte sur glockapps.com (gratuit), aller dans **Inbox Insight → Spam Test → New test → Manual**.
2. GlockApps donne une **liste d'adresses témoins** (seed list) et un **identifiant de test** à mettre dans le mail (en général dans l'objet ou le corps : suivre leur consigne).
3. Envoyer le mail **depuis la vraie boîte Google Workspace** de l'expéditeur (connexion Gmail de la boîte), à toutes les adresses témoins, en texte brut. Lemlist envoie par la même boîte Gmail, donc le résultat est représentatif.
   *Option plus fidèle :* une campagne Lemlist de test avec les adresses témoins comme leads. Je peux la créer par API, **uniquement avec le GO de Nathan** (ce sont des envois réels).
4. Attendre le rapport (quelques minutes à 1 h), exporter la capture.
5. Noter les résultats ici :

| Test | Google boîte principale | Google spam | Outlook boîte principale | Outlook spam | SMTP privés boîte principale | Remarques (SpamAssassin, blacklists) |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

## Lecture des résultats (règles Igor)
- Cible : **≈ 100 % en boîte principale chez Google et SMTP privés.**
- **~50 % = on est en spam** → on corrige avant de renvoyer du volume.
- **Outlook mauvais = acceptable** : on peut exclure Outlook / Microsoft 365 du cold.
- En continu : **le taux de réponse humaine** est la métrique de suivi (s'il chute, c'est un signe de spam).
