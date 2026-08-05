-- ============================================================
-- Module CRM Outbound — Supabase projet "LinkedIn App"
-- Tables préfixées outbound_ (séparées de l'app LinkedIn existante)
-- Appliqué via migration Supabase : outbound_crm_init
-- ============================================================

-- 1) LEADS : source de vérité
create table if not exists public.outbound_leads (
  id            bigint generated always as identity primary key,
  first_name    text,
  last_name     text,
  full_name     text,
  email         text,
  phone         text,
  job_title     text,
  seniority     text,
  company       text,
  domain        text,
  industry      text,
  location      text,
  linkedin      text,
  email_certainty text,
  is_generic_email boolean default false,
  channel       text not null default 'none' check (channel in ('email','call','none')),
  source_file   text,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now()
);
create unique index if not exists outbound_leads_email_uk
  on public.outbound_leads (lower(email)) where email is not null and email <> '';
create index if not exists outbound_leads_channel_ix on public.outbound_leads (channel);
create index if not exists outbound_leads_company_ix on public.outbound_leads (company);

-- 2) CAMPAGNES
create table if not exists public.outbound_campaigns (
  id            bigint generated always as identity primary key,
  name          text not null,
  channel       text not null check (channel in ('email','call')),
  instantly_campaign_id text,
  status        text not null default 'draft',
  created_at    timestamptz not null default now()
);

-- 3) LIEN prospect x campagne (coeur du CRM : 1 ligne = 1 lead dans 1 campagne)
create table if not exists public.outbound_campaign_leads (
  id            bigint generated always as identity primary key,
  campaign_id   bigint not null references public.outbound_campaigns(id) on delete cascade,
  lead_id       bigint not null references public.outbound_leads(id) on delete cascade,
  status        text not null default 'pending'
                check (status in ('pending','sent','opened','replied','interested','bounced','unsubscribed','not_interested')),
  sent_at       timestamptz,
  last_event_at timestamptz,
  notes         text,
  created_at    timestamptz not null default now(),
  unique (campaign_id, lead_id)
);
create index if not exists outbound_campaign_leads_lead_ix on public.outbound_campaign_leads (lead_id);
create index if not exists outbound_campaign_leads_status_ix on public.outbound_campaign_leads (status);

-- Vues : côté email / côté call
create or replace view public.outbound_v_email_leads as
  select * from public.outbound_leads where channel = 'email';
create or replace view public.outbound_v_call_leads as
  select * from public.outbound_leads where channel = 'call';

-- Sécurité : RLS activée, aucune policy => tables non exposées à la clé anon.
alter table public.outbound_leads          enable row level security;
alter table public.outbound_campaigns       enable row level security;
alter table public.outbound_campaign_leads  enable row level security;
