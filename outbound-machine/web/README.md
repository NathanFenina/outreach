# Outbound — app Audiences (Next.js)

Petite app interne : 2 onglets **Cold Mail** / **Cold Call**, affichant les
**audiences** (registre `outbound_audiences`) et les **prospects**
(`outbound_leads`), lus en direct depuis Supabase **côté serveur**.

## Sécurité
Les données (emails, téléphones) sont lues **server-side** avec la clé
`service_role`. Elles ne transitent jamais par le navigateur, et la clé n'est
jamais exposée (pas de préfixe `NEXT_PUBLIC_`).

## Variables d'environnement
| Variable | Où la trouver |
|---|---|
| `SUPABASE_URL` | Supabase → Project Settings → API → Project URL |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase → Project Settings → API → `service_role` (secret) |

Voir `.env.example`.

## Déploiement Vercel (le plus simple)
1. Sur https://vercel.com → **Add New… → Project** → importe le repo `NathanFenina/outreach`.
2. **Root Directory** : `outbound-machine/web`.
3. Framework : **Next.js** (auto-détecté).
4. **Environment Variables** : ajoute `SUPABASE_URL` et `SUPABASE_SERVICE_ROLE_KEY`.
5. **Deploy**. Vercel te donne l'URL — tu ouvres, tu vois tes audiences/prospects en live.

## Lancer en local
```bash
cd outbound-machine/web
cp .env.example .env    # puis renseigne la service_role key
npm install
npm run dev             # http://localhost:3000
```
