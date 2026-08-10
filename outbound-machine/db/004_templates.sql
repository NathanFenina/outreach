-- ============================================================
-- Bibliothèque de copies réutilisables : outbound_templates
-- Un template = un mail (ou script call) réutilisable, versionné.
-- Flux : templates -> campagne -> perso par lead -> import Lemlist.
-- ============================================================
create table if not exists public.outbound_templates (
  id            bigint generated always as identity primary key,
  name          text not null,
  channel       text not null default 'email' check (channel in ('email','call')),
  segment       text,            -- SaaS/IT, E-commerce, BTP, Reactivation, Agence-Ads...
  angle         text,            -- X-Ray GEO, Comparaison, Echantillon carto, Reactivation...
  sequence_step int not null default 1,   -- 1 = J0, 2 = relance J+3/4, 3 = J+7/10
  subject_a     text,
  subject_b     text,            -- variante A/B d'objet
  body          text,            -- corps avec {variables}
  cta           text,
  ps            text,
  pps           text,
  variables     text[],          -- {prenom},{entreprise},{concurrent},{categorie}...
  lang          text not null default 'fr',
  status        text not null default 'to_test' check (status in ('draft','to_test','active','winner','archived')),
  notes         text,
  created_at    timestamptz not null default now()
);
create index if not exists outbound_templates_seg_ix on public.outbound_templates (segment, angle, sequence_step);
alter table public.outbound_templates enable row level security;

-- Contenu inséré (résumé) : voir copy/04_copies_par_audience.md et copy/05_cold_call_playbook.md
-- SaaS/IT: X-Ray GEO, Comparaison, Echantillon carto (mail 1) + script call.
-- E-commerce: Visibilité IA (mail 1).
-- Reactivation: séquence 3 mails (J0 / J+4 / J+10 breakup soft).
