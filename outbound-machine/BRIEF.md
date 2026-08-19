# BRIEF — Outbound Machine Décupler (fil de reprise)

> Document vivant : où on en est, ce qui bloque, les décisions en attente. À relire après chaque pause.
> Dernière MàJ : reprise après 4 jours de pause.

## Où on en est (fait ✅)

- **CRM Supabase** : 7 574 leads, app web Next.js (onglets Cold Mail / Cold Call), 45 audiences.
- **Audience 32 (SaaS-Fintech A/B)** : **195 envoyés Lemlist** (136 + 59 re-poussés), 5 emails morts. **Complète.**
- **Campagnes Lemlist A (X-Ray) et B (Carto)** : existent, leads dedans. ⚠️ à vérifier : sont-elles *running* ?
- **Base copy** : docs `copy/00→11` + présentation artifact (montrable au coach).
- **Leads sans email** (~830) : marqués « Pas d'email — à enrichir » dans l'appli (dont audience 41 IT-Services 51-200).
- **Débrief coach Jason** capturé (`copy/10`).
- **Branche mergée sur `main`** : on travaille sur main.

## ⏳ Ce qui BLOQUE / en attente de TOI

1. **Valider la copy des 2 USP** (`copy/11`) → tant que non validée, on ne prépare pas les variables ni l'import.
2. **CSV medical spa Bretagne** (Outscraper, cold mail) → à uploader ici.
3. **Audience paysagistes Nantes** (cold call) → à uploader ici.
4. **Clé Lemlist** : à mettre dans les variables d'env Claude Code (Settings → Environnement) pour ne plus la recoller.
5. **Vérifier que les campagnes A/B Lemlist sont bien lancées** + inboxes « au vert » (warm-up).

## 🔜 Prochaines étapes (une fois la copy validée)

- **IT-Services (272 leads emailables, audience 16)** : préparer les variables (secteur cheap, concurrent = recherche),
  créer 2 campagnes Lemlist taguées, importer (~136 par USP). Process = **agents remplissent la base D'ABORD, puis import**.
- Scaler par batch de 500 / USP (reco Jason), sprints de 2 semaines, cadence J0/J2/J3/J5.

## 🧭 Décisions en discussion (avis donnés, à trancher)

- **Structure repo** : garder l'orga par fonction (copy/scripts/web/db) vs séparer par canal. → reco : garder par fonction.
- **SMS bouton** : `sms:` link gratuit (comme WhatsApp) vs API (Twilio/Brevo). OnOff = API limitée.
- **Cold call = CRM** : déjà un CRM manuel (statut + notes). Click-to-call + logging = Twilio.
- **Transcripts d'appels OnOff** : ajouter un champ `call_transcript` en base ; source = export OnOff ou Twilio/Fireflies.

## Copy — statut

- **2 USP** (X-Ray GEO / Opportunités organiques) : séquences 4 messages prêtes, **en attente validation**.
- **BTP** : 2 promesses (site / audit) + 5 angles + script cold call. Attente d'une 1re campagne de leads.
- **Réactivation** : séquence 3 mails (base Clay).
- Règle d'or : esprit UltB (on offre, vous gardez tout) ; objets énigmatiques mais qui parlent ; 1 angle par USP.

## Canaux
- **Cold mail** : Lemlist (variables), 20 inboxes (10 domaines × 2).
- **Cold call** : OnOff (à venir), CRM web éditable, audiences #44 Couvreurs / #45 Plombiers Nantes.
- **Cold SMS / WhatsApp** : bouton WhatsApp (gratuit) déjà en place ; SMS à décider.
