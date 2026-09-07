import Tabs from "../../components/Tabs";
import TaskRow from "../../components/TaskRow";
import AddTask from "../../components/AddTask";
import { getTasks } from "../../lib/supabase";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";
export const revalidate = 0;

const CAT_ORDER = [
  "CMO",
  "Batimat",
  "Campagnes",
  "À présenter",
  "SMS/Appels",
  "Prospection",
  "Data",
  "App",
  "Délivrabilité",
  "Backlinks",
];

export default async function Taches() {
  let tasks = [];
  let error = null;
  try {
    tasks = await getTasks();
  } catch (e) {
    error = e.message || String(e);
  }

  const done = tasks.filter((t) => t.status === "Fait").length;
  const blocked = tasks.filter((t) => t.status === "Bloqué").length;
  const doing = tasks.filter((t) => t.status === "En cours").length;
  const todo = tasks.filter((t) => t.status === "À faire").length;

  const cats = [...new Set(tasks.map((t) => t.category || "Divers"))].sort((a, b) => {
    const ia = CAT_ORDER.indexOf(a);
    const ib = CAT_ORDER.indexOf(b);
    return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
  });

  return (
    <div className="wrap">
      <div className="top">
        <div className="brand">
          Décupler · Outbound
          <small>Tâches &amp; suivi projet</small>
        </div>
        <div className="totals">
          <span>À faire <b>{todo}</b></span>
          <span>·</span>
          <span>En cours <b>{doing}</b></span>
          <span>·</span>
          <span>Bloqué <b>{blocked}</b></span>
          <span>·</span>
          <span>Fait <b>{done}</b></span>
        </div>
      </div>
      <Tabs />
      <section>
        {error ? (
          <div className="err">Impossible de charger les tâches : {error}</div>
        ) : (
          <>
            <div className="card" style={{ marginBottom: 16, padding: 14 }}>
              <AddTask />
            </div>
            {cats.map((cat) => {
              const rows = tasks.filter((t) => (t.category || "Divers") === cat);
              return (
                <div key={cat} style={{ marginBottom: 22 }}>
                  <div className="sec-h">
                    <h2>{cat}</h2>
                    <span className="hint">
                      {rows.filter((r) => r.status === "Fait").length}/{rows.length} fait
                    </span>
                  </div>
                  <div className="card">
                    <div className="tablewrap">
                      <table className="crm">
                        <thead>
                          <tr>
                            <th>Tâche</th>
                            <th>Statut</th>
                            <th>Remarque</th>
                          </tr>
                        </thead>
                        <tbody>
                          {rows.map((t) => (
                            <TaskRow key={t.id} t={t} />
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              );
            })}
          </>
        )}
      </section>
      <footer>Source : Supabase · table <code>outbound_tasks</code></footer>
    </div>
  );
}
