import Tabs from "../../components/Tabs";
import TasksBoard from "../../components/TasksBoard";
import AddTask from "../../components/AddTask";
import { getTasks } from "../../lib/supabase";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";
export const revalidate = 0;

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
            <TasksBoard tasks={tasks} />
          </>
        )}
      </section>
      <footer>Source : Supabase · table <code>outbound_tasks</code></footer>
    </div>
  );
}
