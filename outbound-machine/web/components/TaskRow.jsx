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

export default function TaskRow({ t }) {
  const [status, setStatus] = useState(t.status || "À faire");
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

  return (
    <tr>
      <td data-label="Tâche">
        <span className={"tasktitle" + (done ? " taskdone" : "")}>{t.title}</span>
        {t.category && <span className="chip chip-cat">{t.category}</span>}
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
            <option key={s} value={s}>
              {s}
            </option>
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
