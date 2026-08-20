# 13 — Campagnes VERTICALES (« rien jeter ») — reste du scrape medspa

> Décision Nathan : **on ne jette rien**. Les ~1292 leads restants du scrape medspa (hors wellness
> A/B déjà publiés) sont **regroupés en 6 verticaux**, chacun avec sa campagne Lemlist et son angle
> (Site-offert ou SEO) **encodé dans le titre**. Séquence 3 mails (J0 / J+2 / J+4 breakup).
> Variables : `{{companyName}}` + `{{ville}}` (name-free, ces fiches Maps ont rarement un prénom).
> Signature : Nathan Fenina / Agence Decupler. Script : `scripts/11_create_vertical_campaigns.py`.

| Groupe | Campagne Lemlist | Angle | Leads |
|---|---|---|---|
| Hôtellerie / hébergement | `Decupler · Hôtellerie · Site-offert` | Site moderne + réservations directes (anti-Booking) | 276 |
| Santé / médical | `Decupler · Santé-Médical · SEO` | Être trouvé par vos patients + RDV en ligne | 323 |
| Commerce local | `Decupler · Commerce-Local · SEO-Maps` | Google/Maps → visites en boutique | 183 |
| Sport / loisirs | `Decupler · Sport-Loisirs · SEO` | Visibilité → inscriptions/adhérents | 27 |
| Services pro / B2B | `Decupler · Services-Pro-B2B · SEO-Leads` | Demandes entrantes via référencement | 92 |
| Institutions / autres (catch-all) | `Decupler · Institutions-Autres · SEO` | Visibilité en ligne (groupe le plus faible) | 391 |

> ⚠️ **Priorité commerciale décroissante.** Hôtellerie = fort potentiel (les hôtels détestent la
> commission Booking). Santé/Commerce/Sport = corrects. Services/Institutions = catch-all « rien jeté » :
> beaucoup de non-acheteurs (mairies, HAS, universités, mutuelles, véto…). À **lancer en dernier**,
> voire à garder en réserve — c'est là que le risque délivrabilité est le plus élevé.

---

## Hôtellerie · Site-offert
- **M1 (J0)** — Objet : `le site de {{companyName}}` — « j'ai regardé votre site… je vous ai préparé une maquette plus moderne, réservations en direct sans Booking. offert, si elle vous plaît vous la gardez. 15 min ? »
- **M2 (J+2)** — remontée Google/Maps à {{ville}} = réservations directes.
- **M3 (J+4)** — breakup, la maquette reste à vous.

## Santé-Médical · SEO
- **M1** — Objet : `vos patients vous trouvent-ils ?` — point de visibilité + prise de RDV en ligne offert.
- **M2** — les recherches où {{companyName}} n'apparaît pas + réglages fiche Google/site.
- **M3** — breakup, le point reste dispo.

## Commerce-Local · SEO-Maps
- **M1** — Objet : `{{companyName}} sur Google Maps` — aperçu visibilité + visites en boutique.
- **M2** — fiche Google + site propre = plus de visites, 3 réglages prioritaires.
- **M3** — breakup.

## Sport-Loisirs · SEO
- **M1** — Objet : `plus d'adhérents pour {{companyName}} ?` — visibilité → inscriptions.
- **M2** — fiche + site = plus d'inscriptions à {{ville}}.
- **M3** — breakup.

## Services-Pro-B2B · SEO-Leads
- **M1** — Objet : `{{companyName}} — plus de demandes entrantes ?` — aperçu leads potentiels.
- **M2** — quel concurrent capte les demandes + comment les récupérer.
- **M3** — breakup.

## Institutions-Autres · SEO
- **M1** — Objet : `la visibilité de {{companyName}}` — point visibilité, actions simples.
- **M2** — où {{companyName}} apparaît (ou pas) + réglages.
- **M3** — breakup.

---

## Reste à faire (côté Nathan, comme pour toutes les campagnes)
- Attacher l'expéditeur + réchauffer les inboxes + **démarrer** dans Lemlist (rien ne part avant).
- Ordre de lancement conseillé : Wellness A/B → Hôtellerie → Santé/Commerce/Sport → Services → Institutions.
