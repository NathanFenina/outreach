"use client";
import { useState, useTransition } from "react";
import { updateTask } from "../app/actions";

const STATUSES = ["À faire", "En cours", "Bloqué", "Fait", "Abandonné"];
const STATUS_CLASS = {
  "À faire": "st-todo",
  "En cours": "st-recall",
  "Bloqué": "st-vm",
  "Fait": "st-rdv",
  "Abandonné": "st-nc",
};

const TYPES = ["Prospection", "Contenu", "Stratégie", "Reliquat", "Sécurité", "Campagnes", "App", "Data"];
const CANAUX = ["—", "Cold mail", "SMS", "Appel", "LinkedIn", "App"];
const PRIOS = [
  { v: 1, label: "Haute" },
  { v: 2, label: "Medium" },
  { v: 3, label: "Basse" },
];

export default function TaskRow({ t }) {
  const [status, setStatus] = useState(t.status || "À faire");
  const [type, setType] = useState(t.category || "Prospection");
  const [canal, setCanal] = useState(t.channel || "—");
  const [prio, setPrio] = useState(t.priority || 2);
  const [notes, setNotes] = useState(t.notes || "");
  const [pending, start] = useTransition();
  const [flash, setFlash] = useState("");

  function save(patch) {
    start(async () => {
      const r = await updateTask(t.id, patch);
      setFlash(r.ok ? "ok" : "err");
      setTimeout(() => setFlash(""), 1600);
    });
  }

  const done = status === "Fait" || status === "Abandonné";
  const typeOpts = TYPES.includes(type) ? TYPES : [type, ...TYPES];

  return (
    <tr>
      <td data-label="Tâche">
        <span className={"tasktitle" + (done ? " taskdone" : "")}>{t.title}</span>
      </td>
      <td data-label="Type">
        <select
          className="statusSel"
          value={type}
          onChange={(e) => {
            setType(e.target.value);
            save({ category: e.target.value });
          }}
        >
          {typeOpts.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </td>
      <td data-label="Canal">
        <select
          className="statusSel"
          value={canal}
          onChange={(e) => {
            setCanal(e.target.value);
            save({ channel: e.target.value === "—" ? "" : e.target.value });
          }}
        >
          {CANAUX.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </td>
      <td data-label="Prio">
        <select
          className={"statusSel " + (prio === 1 ? "st-hot" : "")}
          value={prio}
          onChange={(e) => {
            const v = Number(e.target.value);
            setPrio(v);
            save({ priority: v });
          }}
        >
          {PRIOS.map((p) => (
            <option key={p.v} value={p.v}>{p.label}</option>
          ))}
        </select>
      </td>
      <td data-label="Statut">
        <select
          className={"statusSel " + (STATUS_CLASS[status] || "")}
          value={status}
          onChange={(e) => {
            setStatus(e.target.value);
            save({ status: e.target.value });
          }}
        >
          {STATUSES.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </td>
      <td className="noteCell" data-label="Remarque">
        <input
          className="noteInput noteInput-wide"
          defaultValue={notes}
          placeholder="remarque…"
          onBlur={(e) => {
            if (e.target.value !== notes) {
              setNotes(e.target.value);
              save({ notes: e.target.value });
            }
          }}
        />
        <span className="savemark">
          {pending ? "…" : flash === "ok" ? "✓" : flash === "err" ? "⚠︎" : ""}
        </span>
      </td>
    </tr>
  );
}
