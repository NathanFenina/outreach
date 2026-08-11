"use server";

import { db } from "../lib/supabase";

// Met à jour le statut d'appel / la remarque d'un lead (CRM cold call), server-side.
export async function updateLeadCrm(leadId, patch) {
  const allowed = {};
  if (typeof patch.call_status === "string") allowed.call_status = patch.call_status;
  if (typeof patch.notes === "string") allowed.notes = patch.notes;
  if (Object.keys(allowed).length === 0) return { ok: false, error: "rien à mettre à jour" };
  allowed.updated_at = new Date().toISOString();
  try {
    const sb = db();
    const { error } = await sb.from("outbound_leads").update(allowed).eq("id", leadId);
    if (error) return { ok: false, error: error.message };
    return { ok: true };
  } catch (e) {
    return { ok: false, error: e.message || String(e) };
  }
}
