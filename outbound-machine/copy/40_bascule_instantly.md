# 40 · Bascule Lemlist → Instantly (30/10/2026)

## 1. Qui envoie quoi (règle permanente)
| Groupe | Fournisseur | Domaines | Envoie vers | Campagnes Instantly |
|---|---|---|---|---|
| A | PremiumInboxes | 9 domaines (dont decupleragency.com, decupler-search.com) | prospects **Google** uniquement | lots **G** (ex. 104-G-P4-1.1) |
| B | Zapmail | decuplerapp.com, decuplerlabs.com, getdecupler.com, godecupler.com, mydecupler.com, decuplerly.com, decupleroy.com (21 boîtes Google Workspace) | prospects **Outlook / Microsoft** et **autres** | lots **M** et **O** |
- Le lot vient du MX du domaine du prospect (`scripts/mx.py`) : google → G, outlook / microsoft / mimecast / proofpoint → M, le reste → O.
- decupleragency.com et decupler-search.com sont **listés SURBL** (127.0.0.64) : hors campagnes et lemwarm arrêté jusqu'au retrait de la liste (demande sur surbl.org).
- Jamais d'envoi depuis decupler.com.

## 2. Ce qui s'arrête chez Lemlist
- **lemwarm** : déjà en pause sur les 2 boîtes listées ; ne pas le relancer. Couper lemwarm sur toutes les boîtes au moment où elles passent en chauffe Instantly (pas deux chauffes en même temps).
- **Campagnes** : 11 campagnes encore « running » au dernier relevé (relances en cours). Choix de Nathan : les laisser finir jusqu'au 10/11 ou les mettre en pause. Leurs leads sont déjà dans la liste noire : Instantly ne les recontactera pas.
- **Abonnement** : Settings → Billing & Users → Manage → Cancel **avant le 10/11** (+ l'add-on crédits d'enrichissement à part s'il existe). Accès conservé jusqu'au 10/11.
- **Données** : export complet déjà fait (`scripts/52_export_lemlist.py`, 125 campagnes) + historique dans Supabase (liste noire).

## 3. Ce qui part chez Instantly (fait / à faire)
- ✅ Abonnement Hypergrowth.
- ✅ 39 campagnes brouillon (104, 106, 110, 114, 121, 122 × G / M / O), séquences V2, texte seul, sans suivi d'ouverture.
- ✅ ≈ 1 500 leads importés (contrôlés : liste noire, même domaine, un email = une campagne).
- ✅ Blocklist : 6 904 domaines (déjà contactés, répondus, désinscrits, clients).
- ⬜ Boîtes : connexion des groupes A et B (prompt Claude in Chrome ci-dessous).
- ⬜ Chauffe Instantly (API, par Claude) : groupe A d'abord ; groupe B après la fin de la chauffe Zapmail (~6/11) ou dès que Zapmail confirme que sa chauffe s'arrête à l'export.
- ⬜ Rattachement des boîtes aux campagnes (`scripts/56_instantly_accounts.py assign`) : A → G, B → M et O.
- ⬜ Test de placement Outlook sur 2 boîtes Zapmail avant de monter le volume.
- ⬜ Validation des copies par Igor puis go de Nathan → lancement progressif (montée UltB).

## 4. Prompt à coller dans Claude in Chrome
> Tu travailles dans mon Chrome, où je suis connecté à Zapmail, PremiumInboxes, Instantly et Lemlist. Je passe mon cold mail de Lemlist à Instantly. Objectif de cette session : connecter toutes mes boîtes d'envoi à mon espace Instantly. Tu n'envoies aucun email, tu ne lances ni ne modifies aucune campagne.
>
> Contexte à respecter :
> - Groupe A = mes boîtes PremiumInboxes (9 domaines). Elles serviront uniquement à écrire aux prospects qui sont sur Google Workspace / Gmail.
> - Groupe B = mes 21 boîtes Zapmail (domaines decuplerapp.com, decuplerlabs.com, getdecupler.com, godecupler.com, mydecupler.com, decuplerly.com, decupleroy.com). Elles serviront à écrire aux prospects sur Outlook / Microsoft et aux autres fournisseurs.
> - decupleragency.com et decupler-search.com (groupe A) sont listés sur une blacklist : connecte-les quand même mais signale-les à la fin.
>
> Étapes :
> 1. Instantly (app.instantly.ai) → Settings → Integrations / API Keys : récupère ma clé API pour la coller dans les exports ci-dessous (ne la recopie pas dans le chat).
> 2. Zapmail (app.zapmail.ai) : va dans la liste des boîtes, utilise « Export » / « Export to sequencer » → Instantly, colle la clé API, sélectionne les 21 boîtes des 7 domaines du groupe B et valide. S'il n'y a pas d'export direct, télécharge le CSV au format Instantly (email, prénom, nom, mot de passe d'application) et garde-le pour l'étape 4.
> 3. PremiumInboxes : même chose pour toutes les boîtes du groupe A (export direct vers Instantly avec la clé API, ou CSV au format Instantly).
> 4. Si tu as des CSV : Instantly → Email Accounts → Add New → Bulk import (CSV), importe-les. Supprime ensuite les CSV téléchargés de mon ordinateur (ils contiennent des mots de passe).
> 5. Instantly → Email Accounts : vérifie que chaque boîte est connectée sans erreur. Ajoute le tag « groupe-A-google » aux boîtes PremiumInboxes et « groupe-B-outlook-autres » aux boîtes Zapmail si Instantly permet les tags.
> 6. N'active pas la chauffe (warmup) et ne change aucune limite d'envoi : ce sera fait ensuite par l'API.
> 7. Lemlist : ne supprime rien. Va dans lemwarm et note pour chaque boîte si lemwarm est actif ou en pause, sans rien changer.
> 8. À la fin, donne-moi : le nombre de boîtes connectées par domaine et par groupe, les boîtes en erreur avec le message, et l'état lemwarm noté à l'étape 7.
