-- ============================================================
-- Migration : registre d'audiences + rattachement des leads
-- Appliqué via migration Supabase : outbound_audiences_registry
-- ============================================================

create table if not exists public.outbound_audiences (
  id            bigint generated always as identity primary key,
  name          text not null,
  channel       text not null check (channel in ('email','call')),
  segment       text,            -- verticale : Construction, IT, Infogérance...
  persona       text,            -- poste : CMO, Dirigeant, DAF...
  size_range    text,            -- effectif : 11-50, 50-200...
  revenue_range text,            -- CA : 1-5M, 5-20M...
  source        text,            -- clay / fullenrich
  status        text not null default 'active',
  created_at    timestamptz not null default now()
);

alter table public.outbound_leads add column if not exists company_size text;
alter table public.outbound_leads add column if not exists revenue_range text;
alter table public.outbound_leads add column if not exists audience_id bigint
  references public.outbound_audiences(id) on delete set null;
create index if not exists outbound_leads_audience_ix on public.outbound_leads (audience_id);

-- Vue : audiences avec comptes en direct
create or replace view public.outbound_audiences_counts as
  select a.*, count(l.id) as nb_leads,
         count(l.id) filter (where l.email is not null) as nb_email,
         count(l.id) filter (where l.phone is not null) as nb_phone,
         -- "in Lemlist" = pushed OK OR déjà présent dans une autre campagne Lemlist
         count(l.id) filter (where l.lemlist_status in ('Envoyé Lemlist','Déjà en campagne Lemlist')) as nb_lemlist,
         -- cold call : lead traité = statut différent de "À appeler"
         count(l.id) filter (where l.channel = 'call' and l.call_status <> 'À appeler') as nb_called
  from public.outbound_audiences a
  left join public.outbound_leads l on l.audience_id = a.id
  group by a.id;

alter table public.outbound_audiences enable row level security;
