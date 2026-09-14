"use client";
import { useState, useMemo } from "react";
import TaskRow from "./TaskRow";

const PRIO_LABEL = { 1: "Haute", 2: "Medium", 3: "Basse" };

function uniq(arr) {
  return [...new Set(arr.filter(Boolean))];
}

export default function TasksBoard({ tasks }) {
  const [fType, setFType] = useState("all");
  const [fCanal, setFCanal] = useState("all");
  const [fStatus, setFStatus] = useState("open"); // open = pas Fait/Abandonné
  const [fPrio, setFPrio] = useState("all");
  const [q, setQ] = useState("");

  const types = useMemo(() => uniq(tasks.map((t) => t.category)).sort(), [tasks]);
  const canaux = useMemo(() => uniq(tasks.map((t) => t.channel)).sort(), [tasks]);

  const rows = useMemo(() => {
    return tasks.filter((t) => {
      if (fType !== "all" && (t.category || "") !== fType) return false;
      if (fCanal !== "all" && (t.channel || "") !== fCanal) return false;
      if (fPrio !== "all" && String(t.priority || 2) !== fPrio) return false;
      if (fStatus === "open" && (t.status === "Fait" || t.status === "Abandonné")) return false;
      if (fStatus !== "all" && fStatus !== "open" && t.status !== fStatus) return false;
      if (q && !(`${t.title} ${t.notes || ""}`.toLowerCase().includes(q.toLowerCase()))) return false;
      return true;
    });
  }, [tasks, fType, fCanal, fStatus, fPrio, q]);

  const sel = "statusSel";
  return (
    <div>
      <div className="card" style={{ padding: 12, marginBottom: 14 }}>
        <div className="addtask">
          <input
            className="noteInput"
            placeholder="🔍 chercher…"
            value={q}
            onChange={(e) => setQ(e.target.value)}
            style={{ width: 180 }}
          />
          <select className={sel} value={fType} onChange={(e) => setFType(e.target.value)}>
            <option value="all">Type : tous</option>
            {types.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
          <select className={sel} value={fCanal} onChange={(e) => setFCanal(e.target.value)}>
            <option value="all">Canal : tous</option>
            {canaux.map((c) => (
              <option key={c} value={c}>{c}</option>
            ))}
          </select>
          <select className={sel} value={fStatus} onChange={(e) => setFStatus(e.target.value)}>
            <option value="open">Statut : à traiter</option>
            <option value="all">Statut : tous</option>
            <option value="À faire">À faire</option>
            <option value="En cours">En cours</option>
            <option value="Bloqué">Bloqué</option>
            <option value="Fait">Fait</option>
            <option value="Abandonné">Abandonné</option>
          </select>
          <select className={sel} value={fPrio} onChange={(e) => setFPrio(e.target.value)}>
            <option value="all">Prio : toutes</option>
            <option value="1">Haute</option>
            <option value="2">Medium</option>
            <option value="3">Basse</option>
          </select>
          <span className="small">{rows.length} tâche{rows.length > 1 ? "s" : ""}</span>
        </div>
      </div>

      <div className="card">
        <div className="tablewrap tallscroll">
          <table className="crm tasks">
            <thead>
              <tr>
                <th>Tâche</th>
                <th>Type</th>
                <th>Canal</th>
                <th>Prio</th>
                <th>Statut</th>
                <th>Remarque</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((t) => (
                <TaskRow key={t.id} t={t} />
              ))}
              {rows.length === 0 && (
                <tr>
                  <td colSpan={6} className="empty">Aucune tâche pour ce filtre.</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
