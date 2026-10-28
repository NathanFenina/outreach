# 27 · Synthèse de toutes les campagnes cold mail (N24)

Source : API Lemlist, 119 campagnes lues le 28/10/2026 (`scripts/32_sync_lemlist.py` → `data/synthese_campagnes.csv`, aussi dans Supabase, table `campaigns`, lot `legacy`).
Prospects = leads ayant reçu au moins un message. Réponses = leads dont le dernier état Lemlist est une réponse : **auto-réponses comprises et sous-estimé** (un rebond ou une désinscription après la réponse écrase l'état). Les positives et RDV ne sont pas dans Lemlist : ils viennent du tri manuel (CR Igor).

## 1. Total
- **9509 prospects contactés**, **203 réponses** (2.1 %), 659 rebonds (6.9 %).
- Tri manuel sur 4 semaines (14/09 → 12/10, CR Igor) : 55 réponses humaines, **10 positives** (≈ 18 % des réponses), 2 demandes de RDV, 0 RDV tenu enregistré. Session 2 : ~2 000 prospects, 2,7 % de réponses, 20 % de positives.
- Session 3 (27/10) : 2 accords verbaux sur les appels de vente (1 confirmé, 1 en suspens).

## 2. Par famille de campagnes

| Famille | Prospects | Réponses | Taux | Rebonds |
|---|---:|---:|---:|---:|
| Agences | 1935 | 18 | 0.9 % | 4.9 % |
| Tests de mars (IT, SaaS, SEO) | 1541 | 5 | 0.3 % | 6.2 % |
| Relances webinaire / masterclass (contacts chauds) | 1075 | 87 | 8.1 % | 1.0 % |
| SaaS / IT / levées | 880 | 17 | 1.9 % | 1.8 % |
| Immobilier (agents IA) | 795 | 17 | 2.1 % | 9.1 % |
| E-commerce | 769 | 8 | 1.0 % | 6.9 % |
| BTP / construction | 754 | 19 | 2.5 % | 5.4 % |
| Hôtellerie / santé / local | 708 | 12 | 1.7 % | 16.8 % |
| Conseil / services B2B | 661 | 8 | 1.2 % | 9.4 % |
| Institutions | 391 | 12 | 3.1 % | 24.0 % |

## 3. Par campagne (≥ 50 prospects)

| Campagne | Statut | Prospects | Réponses | Taux | Rebonds |
|---|---|---:|---:|---:|---:|
| 0 Agence_Ads_France_CEO-CMO_2-50 | archived | 870 | 15 | 1.7 % | 2.3 % |
| ⏸️ Agences · White-label GEO (FR) | archived | 504 | 0 | 0.0 % | 10.7 % |
| atimat · Exposants · ChatGPT (GEO) | running | 465 | 14 | 3.0 % | 4.3 % |
| 👍 B2B Dirigeants · SEO+IA (FR) | archived | 425 | 0 | 0.0 % | 13.4 % |
| Immo · Agents IA · Vidéo démo (FR) | running | 398 | 8 | 2.0 % | 9.5 % |
| 👍 Immo · Agents IA · Automatisation (FR) - trop de refus | archived | 397 | 9 | 2.3 % | 8.6 % |
| 0 Agence_Ads_Suisse_CEO-CMO_2-50 | archived | 396 | 0 | 0.0 % | 2.3 % |
| ⏸️ Institutions-Autres · SEO | archived | 391 | 12 | 3.1 % | 24.0 % |
| 0 Email re-engagment SEO AI Systems Mars 26 | archived | 338 | 10 | 3.0 % | 2.4 % |
| ⏸️ Hôtellerie · Site-offert | archived | 251 | 5 | 2.0 % | 16.7 % |
| ⏸️ E-commerce · Ventes+GEO (FR) | archived | 241 | 0 | 0.0 % | 21.6 % |
| Conseil · SEO/GEO · 10 prompts | running | 229 | 8 | 3.5 % | 1.7 % |
| 0TEST IT_Marketing_4 | archived | 220 | 4 | 1.8 % | 5.9 % |
| 3 Invitation webinaire janvier par message | archived | 217 | 19 | 8.8 % | 0.0 % |
| 0TEST IT_Marketing_2 | archived | 186 | 0 | 0.0 % | 6.5 % |
| ⏸️ Commerce-Local · SEO-Maps | archived | 183 | 4 | 2.2 % | 19.1 % |
| 0 WEB TO WEB_ a relancer apres le webinaire | archived | 177 | 11 | 6.2 % | 0.0 % |
| 0TEST Saas_Marketing_3 | archived | 177 | 0 | 0.0 % | 5.6 % |
| 3 E-commerce_bijoux_CEO_France_11-50 | ended | 173 | 1 | 0.6 % | 0.6 % |
| Decupler · Masterclass · relance inscrits | paused | 171 | 25 | 14.6 % | 1.8 % |
| ⏸️ Decupler · Clinique capillaire · Agent (Bretagne) | archived | 168 | 2 | 1.2 % | 13.1 % |
| 👍 Decupler · Levée de fonds · GEO (emails vérifiés) | running | 156 | 3 | 1.9 % | 0.6 % |
| Plombier Nantes · Site offert (mail) - ca n'a pas marché | archived | 151 | 0 | 0.0 % | 9.3 % |
| 0TEST IT_Marketing_3 | archived | 143 | 0 | 0.0 % | 7.0 % |
| 0TEST Saas_Marketing_4 | archived | 142 | 0 | 0.0 % | 4.9 % |
| 3 E-commerce_Fashion_CEO-CMO_France_11-50 | ended | 133 | 2 | 1.5 % | 0.0 % |
| 3 E-commerce_bijoux_CEO_France_2-10_email - Eva | ended | 132 | 4 | 3.0 % | 0.0 % |
| 3 IT-Services_CEO-CMO_FRANCE_11-50 | ended | 132 | 0 | 0.0 % | 0.0 % |
| 0TEST Saas_Marketing_2 | archived | 122 | 0 | 0.0 % | 5.7 % |
| 3 Construction_CEO_CMO_2-50 | ended | 119 | 4 | 3.4 % | 5.0 % |
| IT · ESN + éditeurs · 10 prompts (A1) | running | 115 | 3 | 2.6 % | 1.7 % |
| 0TEST IT_Marketing_1 | archived | 114 | 0 | 0.0 % | 14.0 % |
| 0TEST SEO_France_4 | archived | 105 | 0 | 0.0 % | 6.7 % |
| 3 Agence_Ads_CEO_France_2-10_email_Thomas | ended | 102 | 2 | 2.0 % | 2.0 % |
| 0TEST Saas_Marketing_1 | archived | 101 | 0 | 0.0 % | 6.9 % |
| 👍 Decupler · CMO SaaS FR · KPI (100) | running | 98 | 4 | 4.1 % | 2.0 % |
| 0TEST IT_Marketing_5 | archived | 96 | 0 | 0.0 % | 2.1 % |
| FR · Hiring · Agents IA (recrutement) | running | 94 | 4 | 4.3 % | 1.1 % |
| 0 Saas_CEO_France_2-50 | archived | 81 | 0 | 0.0 % | 2.5 % |
| Decupler · CMO SaaS FR · Pré-audit offert | running | 80 | 2 | 2.5 % | 1.2 % |
| ⏸️ Decupler · Santé · Analyse visibilité (structures) | archived | 79 | 0 | 0.0 % | 22.8 % |
| 0 Campagne SEO 1st connexion | archived | 75 | 7 | 9.3 % | 0.0 % |
| Rappel de webinaire Mars | archived | 74 | 14 | 18.9 % | 0.0 % |
| 3 SaaS_FINTECH_CEO-CMO_France_11-50 | ended | 64 | 0 | 0.0 % | 7.8 % |
| 0TEST SEO_France_3 | archived | 63 | 1 | 1.6 % | 3.2 % |
| ⏸️ Agencies · White-label GEO (EN) | archived | 63 | 1 | 1.6 % | 15.9 % |
| 🆕 Saudi · AI build · Hiring | running | 60 | 1 | 1.7 % | 3.3 % |

## 4. Ce qu'on en tire (et ce qui change à partir de 101)
1. **Les contacts chauds répondent 3 à 10 fois plus** (masterclass 14,6 %, rappels webinaire 19 %, invitations 8,8 %) que le froid (1 à 4 %). → les relances d'inscrits restent un canal à part, à faire à chaque webinaire.
2. **Les rebonds étaient le premier problème** : plusieurs campagnes à 10-24 % (Institutions 24 %, E-commerce 22 %, Santé 23 %, Commerce local 19 %), ce qui a abîmé la réputation des domaines (SURBL). → à partir de 101 : uniquement des emails vérifiés, et exclusion de Microsoft / Mimecast / Proofpoint.
3. **Les meilleurs taux en froid** : CMO SaaS KPI 4,1 %, Hiring agents IA 4,3 %, Conseil 10 prompts 3,5 %, Construction 3,4 %, Batimat 3,0 % (mais 0 positive). Le signal d'intention et la précision du message paient.
4. **Taux de réponse ≠ positives** : Batimat et Immo font des réponses mais pas de RDV (refus, « 2 » au mail 1-2-3). → mesurer réponses humaines, positives et RDV par campagne dans la table `campaigns`, et qualifier chaque réponse à la main jusqu'au passage sur un outil qui le fait.
5. **Trop de petites campagnes** (50 à 200 prospects, beaucoup de tests de 220) : impossible de conclure. → nouvelle règle : 100 minimum, 300 maximum par campagne, une hypothèse écrite avec son critère de succès, lots G / O séparés.
6. **Segments à arrêter ou refaire** : Immo (beaucoup de refus), E-commerce, Institutions, Plombiers (0 réponse). Gardés et refaits : conseil, SaaS / IT, BTP (en partenariat à la performance), hôtellerie.
7. **Ce qui manque dans les données** : le statut « intéressé » n'est jamais renseigné dans Lemlist, et les RDV ne sont pas tracés. → la table `events` de Supabase sert à ça (réponse, positif, RDV), alimentée à chaque réponse traitée.
