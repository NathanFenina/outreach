import { createClient } from "@supabase/supabase-js";

// Client Supabase server-side (service_role) — ne jamais l'exposer au navigateur.
export function db() {
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) {
    throw new Error(
      "Config manquante : définis SUPABASE_URL et SUPABASE_SERVICE_ROLE_KEY (voir .env.example)."
    );
  }
  return createClient(url, key, { auth: { persistSession: false } });
}

const CERT_ORDER = { ultra_sure: 0, Verified: 0, probable: 1, "": 2, null: 2 };

export async function getAudiences(channel) {
  const sb = db();
  const { data, error } = await sb
    .from("outbound_audiences_counts")
    .select("*")
    .eq("channel", channel)
    .order("nb_leads", { ascending: false });
  if (error) throw error;
  return data || [];
}

export async function getProspects(channel, { audienceId = null, limit = 500 } = {}) {
  const sb = db();
  let q = sb
    .from("outbound_leads")
    .select(
      "id,full_name,email,phone,job_title,company,persona,segment,email_certainty,location,company_size,lemlist_status,call_status,notes,industry,personalization,demo_url"
    )
    .eq("channel", channel);
  if (audienceId) q = q.eq("audience_id", audienceId);
  const { data, error } = await q.limit(limit);
  if (error) throw error;
  const rows = data || [];
  rows.sort(
    (a, b) =>
      (CERT_ORDER[a.email_certainty] ?? 2) - (CERT_ORDER[b.email_certainty] ?? 2)
  );
  return rows;
}

export async function getAudienceById(id) {
  const sb = db();
  const { data, error } = await sb
    .from("outbound_audiences_counts")
    .select("*")
    .eq("id", id)
    .maybeSingle();
  if (error) throw error;
  return data;
}

export async function getTasks() {
  const sb = db();
  const { data, error } = await sb
    .from("outbound_tasks")
    .select("id,title,category,status,priority,notes,sort_order,updated_at")
    .order("sort_order", { ascending: true })
    .limit(500);
  if (error) throw error;
  return data || [];
}

export async function getTotals() {
  const zero = { email: 0, call: 0, present: 0, batimat: 0, facebook: 0 };
  // Une seule requête (vue agrégée) au lieu de 5 count() -> évite les timeouts.
  // Résilient : si la barre de totaux échoue, on renvoie 0 sans casser la page.
  try {
    const sb = db();
    const { data, error } = await sb.from("outbound_channel_counts").select("channel,n");
    if (error || !data) return zero;
    const out = { ...zero };
    for (const r of data) {
      if (r.channel in out) out[r.channel] = r.n || 0;
    }
    return out;
  } catch {
    return zero;
  }
}
