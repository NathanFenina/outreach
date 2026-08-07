-- ============================================================
-- Tagging sectoriel des leads à partir des fichiers de campagne Clay
-- nommés par secteur (SEC__<segment>__<persona>__<effectif>.csv)
--
-- Process (exécuté via MCP + PostgREST, résumé ici) :
--  1. Copie des ~35 fichiers de campagne dans le dossier Drive public,
--     renommés SEC__<segment>__<persona>__<taille>.csv
--  2. Téléchargement (curl) + consolidation locale -> sectors_master.csv
--     (segment / persona / effectif tirés du nom de fichier)
--  3. Staging table outbound_sector_stage, chargée via PostgREST
--  4. Création d'une audience par (segment, persona, effectif)
--  5. Tag des leads existants (match email puis LinkedIn) + insertion des nouveaux
-- ============================================================

-- 1) une audience par combinaison secteur/persona/effectif
insert into public.outbound_audiences (name, channel, segment, persona, size_range, source, status)
select distinct segment||' · '||persona_file||' · '||company_size, 'email', segment, persona_file, company_size, 'clay', 'active'
from public.outbound_sector_stage;

-- 2) tag des leads existants matchés par email
update public.outbound_leads o
  set segment=s.segment, company_size=coalesce(o.company_size,s.company_size), audience_id=s.audience_id
from public.outbound_sector_stage s
where o.email is not null and s.email is not null and lower(o.email)=lower(s.email);

-- 3) tag par LinkedIn les leads restants
update public.outbound_leads o
  set segment=coalesce(o.segment,s.segment), company_size=coalesce(o.company_size,s.company_size),
      audience_id=coalesce(o.audience_id,s.audience_id)
from public.outbound_sector_stage s
where o.segment is null and o.linkedin<>'' and s.linkedin is not null
  and rtrim(lower(o.linkedin),'/')=rtrim(lower(s.linkedin),'/');

-- 4) insertion des nouveaux prospects (non présents en base), dédoublonnés
-- (voir INSERT ... SELECT DISTINCT ON (coalesce(lower(email),lower(linkedin),lower(full_name))) ...)

-- Résultat : 8 606 leads, 4 927 taggés secteur, 14 verticales, 36 audiences email + 1 call.
