# SMS artisans — 3 variantes (site offert)

Message générique « artisan » : vaut pour plombiers, paysagistes, couvreurs… Aucune mention de
métier dans le texte, rien à réécrire d'une verticale à l'autre.

Pourquoi 3 variantes : envoyer 50 fois le même texte depuis la même ligne déclenche les filtres
anti-spam (constaté sur Onoff le 08/09, vers le 50e envoi). On alterne A / B / C.

---

## Versions envoyées aux plombiers (08/09/2026)

> **A** — Bonjour, Nathan de Decupler. Je sais que c'est un peu direct, mais j'ai pris les devants :
> je vous ai préparé un site moderne (offert, 30 premiers artisans) pour signer plus de devis.
> Je vous le montre ? Sinon répondez STOP et j'arrete.

> **B** — Hello, je suis Nathan de Decupler. Je vais être direct pour ne pas vous faire perdre de
> temps : nous sommes partenaires des artisans et je vous ai créé un site moderne — si vous l'aimez,
> vous le gardez. Je vous le montre aujourd'hui ? Sinon répondez STOP.

> **C** — Bonjour, ici Nathan de Decupler. Je me permets ce message un peu direct : j'ai déjà préparé
> pour vous un site internet moderne (offert aux 30 premiers artisans) afin de vous aider à signer
> plus de devis. Ça vous intéresse que je vous le montre ? Sinon répondez STOP et j'arrête

### Coût réel de ces versions (alphabet GSM-7 vs UCS-2)
Un SMS tient sur 160 caractères **seulement** si tout le texte est dans l'alphabet GSM-7. Un seul
caractère hors alphabet (`ê`, `ç` minuscule, tiret cadratin `—`, apostrophe typographique `’`)
bascule le message entier en UCS-2 : **70 caractères par segment** au lieu de 160.

| Variante | Encodage | Segments facturés | Coupable |
|---|---|---|---|
| A | GSM-7 | 2 | — |
| B | UCS-2 | **4** | `ê` (être), `—` |
| C | UCS-2 | **5** | `ê` (arrête) |

Sans importance sur Onoff (forfait). Sur un provider facturé au segment (Brevo…), la variante C
coûte **5x** la version optimisée ci-dessous.

---

## Versions optimisées — 1 seul segment, français correct

Réécrites en GSM-7 pur (é, è, à, ù, Ç majuscule passent ; ê, ç minuscule, — et ’ ne passent pas).
Vérifiées à 153 / 153 / 146 caractères = **1 segment chacune**.

> **A** — Bonjour, Nathan de Decupler. Direct : je vous ai préparé un site moderne, offert aux
> 30 premiers artisans, pour signer plus de devis. Je vous le montre ?

> **B** — Bonjour, Nathan de Decupler. Nous sommes partenaires des artisans : je vous ai créé un
> site moderne. Si vous l'aimez, vous le gardez. Je vous le montre ?

> **C** — Bonjour, Nathan de Decupler. J'ai déjà préparé pour vous un site internet moderne, offert
> aux 30 premiers artisans. Ça vous intéresse de le voir ?

**Mention STOP :**
- **Onoff / envoi manuel** → ajouter ` Sinon répondez STOP.` à la fin (passe à 2 segments, sans
  incidence sur un forfait). Le STOP arrive dans la conversation, on le traite à la main.
- **Brevo / provider marketing** → **ne rien ajouter** : Brevo appose lui-même la mention de
  désinscription réglementaire sur les campagnes SMS marketing FR. Attention, un expéditeur
  alphanumérique (« Decupler ») est **unidirectionnel** : le destinataire ne peut pas répondre,
  ni « STOP » ni « oui ça m'intéresse ». À vérifier dans le compte avant de lancer — sur cette
  offre, la réponse EST la conversion.

---

## Règles de batch (retour terrain 08/09)
- Alterner les 3 variantes dès le premier envoi, pas à partir de l'alerte.
- ~40-50 envois max d'affilée par ligne émettrice, fractionner sur plusieurs demi-journées.
- Mobiles uniquement (`+336` / `+337`) — un fixe ne reçoit pas de SMS.
- Dédoublonner sur le numéro, pas sur le nom : deux fiches peuvent partager une ligne.
- Tout STOP → statut CRM « Ne pas contacter », immédiatement, tous canaux confondus.
