import Link from "next/link";
import Tabs from "./Tabs";
import {
  getAudiences,
  getProspects,
  getTotals,
  getAudienceById,
} from "../lib/supabase";

function CertBadge({ c }) {
  if (c === "ultra_sure" || c === "Verified")
    return <span className="badge b-ultra">ultra sûr</span>;
  if (c === "probable") return <span className="badge b-prob">probable</span>;
  return <span className="badge b-none">n/a</span>;
}

function StatusBadge({ s }) {
  const imported = s && s.toLowerCase().includes("import") && !s.toLowerCase().includes("à ");
  return (
    <span className={"badge " + (imported ? "b-ultra" : "b-none")}>
      {s || "À importer"}
    </span>
  );
}

export default async function Dashboard({ channel, audienceId }) {
  const isEmail = channel === "email";
  const base = isEmail ? "/cold-mail" : "/cold-call";
  let totals = { email: 0, call: 0 },
    error = null;

  try {
    if (audienceId) {
      const [audience, prospects, t] = await Promise.all([
        getAudienceById(audienceId),
        getProspects(channel, { audienceId }),
        getTotals(),
      ]);
      totals = t;
      return (
        <Shell channel={channel} totals={totals}>
          <div className="crumb">
            <Link href={base}>← Toutes les audiences</Link>
          </div>
          <div className="sec-h">
            <h2>{audience ? audience.name : "Audience"}</h2>
            <span className="hint">
              {prospects.length} prospect{prospects.length > 1 ? "s" : ""}
              {prospects.length >= 500 ? " (500 premiers)" : ""}
            </span>
          </div>
          <ProspectTable rows={prospects} isEmail={isEmail} />
        </Shell>
      );
    }

    const [audiences, t] = await Promise.all([getAudiences(channel), getTotals()]);
    totals = t;
    return (
      <Shell channel={channel} totals={totals}>
        <div className="sec-h">
          <h2>Audiences {isEmail ? "email" : "call"}</h2>
          <span className="hint">
            {audiences.length} audience{audiences.length > 1 ? "s" : ""} · clique pour voir les prospects
          </span>
        </div>
        {audiences.length === 0 ? (
          <div className="card">
            <div className="empty">Aucune audience pour ce canal.</div>
          </div>
        ) : (
          <div className="aud-grid">
            {audiences.map((a) => (
              <Link className="aud" key={a.id} href={`${base}?audience=${a.id}`}>
                <div className="nm">{a.name}</div>
                <div className="n">{Number(a.nb_leads).toLocaleString("fr-FR")}</div>
                <div className="sub">
                  {isEmail
                    ? `${Number(a.nb_email).toLocaleString("fr-FR")} avec email`
                    : `${Number(a.nb_phone).toLocaleString("fr-FR")} avec téléphone`}
                </div>
                <div className="chips">
                  {a.segment && <span className="chip">{a.segment}</span>}
                  {a.persona && <span className="chip">{a.persona}</span>}
                  {a.size_range && <span className="chip">{a.size_range}</span>}
                </div>
              </Link>
            ))}
          </div>
        )}
      </Shell>
    );
  } catch (e) {
    error = e.message || String(e);
    return (
      <Shell channel={channel} totals={totals}>
        <div className="err">
          Impossible de charger les données : {error}
          <br />
          Vérifie SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY.
        </div>
      </Shell>
    );
  }
}

function Shell({ channel, totals, children }) {
  return (
    <div className="wrap">
      <div className="top">
        <div className="brand">
          Décupler · Outbound
          <small>Audiences &amp; prospects — CRM Supabase</small>
        </div>
        <div className="totals">
          <span>
            Cold mail <b>{totals.email.toLocaleString("fr-FR")}</b>
          </span>
          <span>·</span>
          <span>
            Cold call <b>{totals.call.toLocaleString("fr-FR")}</b>
          </span>
        </div>
      </div>
      <Tabs />
      <section>{children}</section>
      <footer>
        Source : Supabase · tables <code>outbound_*</code> · lecture server-side.
      </footer>
    </div>
  );
}

function ProspectTable({ rows, isEmail }) {
  return (
    <div className="card">
      <div className="tablewrap">
        <table>
          <thead>
            <tr>
              <th>Nom</th>
              <th>{isEmail ? "Email" : "Téléphone"}</th>
              <th>Poste</th>
              <th>Entreprise</th>
              <th>Effectif</th>
              {isEmail ? <th>Qualité</th> : <th>Persona</th>}
              <th>Statut Lemlist</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((p) => (
              <tr key={p.id}>
                <td>
                  <span className="name">{p.full_name || "—"}</span>
                </td>
                <td className="muted">{isEmail ? p.email || "—" : p.phone || "—"}</td>
                <td className="muted">{p.job_title || "—"}</td>
                <td>{p.company || "—"}</td>
                <td className="muted">{p.company_size || "—"}</td>
                {isEmail ? (
                  <td>
                    <CertBadge c={p.email_certainty} />
                  </td>
                ) : (
                  <td className="muted">{p.persona || "—"}</td>
                )}
                <td>
                  <StatusBadge s={p.lemlist_status} />
                </td>
              </tr>
            ))}
            {rows.length === 0 && (
              <tr>
                <td colSpan={7} className="empty">
                  Aucun prospect dans cette audience.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
