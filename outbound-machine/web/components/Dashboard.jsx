import Tabs from "./Tabs";
import { getAudiences, getProspects, getTotals } from "../lib/supabase";

function CertBadge({ c }) {
  if (c === "ultra_sure" || c === "Verified")
    return <span className="badge b-ultra">ultra sûr</span>;
  if (c === "probable") return <span className="badge b-prob">probable</span>;
  return <span className="badge b-none">n/a</span>;
}

export default async function Dashboard({ channel }) {
  const isEmail = channel === "email";
  let audiences = [],
    prospects = [],
    totals = { email: 0, call: 0 },
    error = null;
  try {
    [audiences, prospects, totals] = await Promise.all([
      getAudiences(channel),
      getProspects(channel),
      getTotals(),
    ]);
  } catch (e) {
    error = e.message || String(e);
  }

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

      {error ? (
        <div className="err">
          Impossible de charger les données : {error}
          <br />
          Vérifie les variables SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY.
        </div>
      ) : (
        <>
          <section>
            <div className="sec-h">
              <h2>Audiences {isEmail ? "email" : "call"}</h2>
              <span className="hint">
                {audiences.length} audience{audiences.length > 1 ? "s" : ""} ·
                comptées en direct
              </span>
            </div>
            {audiences.length === 0 ? (
              <div className="card">
                <div className="empty">Aucune audience pour ce canal.</div>
              </div>
            ) : (
              <div className="aud-grid">
                {audiences.map((a) => (
                  <div className="aud" key={a.id}>
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
                      {a.revenue_range && <span className="chip">{a.revenue_range}</span>}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </section>

          <section>
            <div className="sec-h">
              <h2>Prospects {isEmail ? "email" : "call"}</h2>
              <span className="hint">
                {prospects.length} affichés{" "}
                {isEmail && prospects.length >= 300 ? "(300 premiers, triés par qualité)" : ""}
              </span>
            </div>
            <div className="card">
              <div className="tablewrap">
                <table>
                  <thead>
                    <tr>
                      <th>Nom</th>
                      <th>{isEmail ? "Email" : "Téléphone"}</th>
                      <th>Poste</th>
                      <th>Entreprise</th>
                      <th>Persona</th>
                      {isEmail ? <th>Qualité</th> : <th>Effectif</th>}
                    </tr>
                  </thead>
                  <tbody>
                    {prospects.map((p) => (
                      <tr key={p.id}>
                        <td>
                          <span className="name">{p.full_name || "—"}</span>
                        </td>
                        <td className="muted">
                          {isEmail ? p.email || "—" : p.phone || "—"}
                        </td>
                        <td className="muted">{p.job_title || "—"}</td>
                        <td>{p.company || "—"}</td>
                        <td className="muted">{p.persona || "—"}</td>
                        {isEmail ? (
                          <td>
                            <CertBadge c={p.email_certainty} />
                          </td>
                        ) : (
                          <td className="muted">{p.company_size || "—"}</td>
                        )}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        </>
      )}

      <footer>
        Source : Supabase · projet LinkedIn App · tables <code>outbound_*</code>.
        Lecture server-side (service_role) — aucune donnée exposée au navigateur.
      </footer>
    </div>
  );
}
