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

export async function getProspects(channel, limit = 300) {
  const sb = db();
  const { data, error } = await sb
    .from("outbound_leads")
    .select(
      "id,full_name,email,phone,job_title,company,persona,segment,email_certainty,location,company_size"
    )
    .eq("channel", channel)
    .limit(limit);
  if (error) throw error;
  const rows = data || [];
  rows.sort(
    (a, b) =>
      (CERT_ORDER[a.email_certainty] ?? 2) - (CERT_ORDER[b.email_certainty] ?? 2)
  );
  return rows;
}

export async function getTotals() {
  const sb = db();
  const q = (channel) =>
    sb
      .from("outbound_leads")
      .select("id", { count: "exact", head: true })
      .eq("channel", channel);
  const [email, call] = await Promise.all([q("email"), q("call")]);
  return { email: email.count || 0, call: call.count || 0 };
}
