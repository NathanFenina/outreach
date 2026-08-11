"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

const STATUSES = [
  "À appeler",
  "Appelé",
  "RDV",
  "Répondu",
  "Rappeler",
  "Pas intéressé",
  "Mauvais numéro",
  "Ne pas contacter",
];

const STATUS_CLASS = {
  "À appeler": "st-todo",
  Appelé: "st-done",
  RDV: "st-win",
  Répondu: "st-win",
  Rappeler: "st-warn",
  "Pas intéressé": "st-dead",
  "Mauvais numéro": "st-dead",
  "Ne pas contacter": "st-dead",
};

export default function CallRow({ p }) {
  const [status, setStatus] = useState(p.call_status || "À appeler");
  const [notes, setNotes] = useState(p.notes || "");
  const [pending, start] = useTransition();
  const [flash, setFlash] = useState("");

  function save(patch) {
    start(async () => {
      const r = await updateLeadCrm(p.id, patch);
      setFlash(r.ok ? "ok" : "err");
      setTimeout(() => setFlash(""), 1400);
    });
  }

  return (
    <tr>
      <td>
        <span className="name">{p.full_name || p.company || "—"}</span>
      </td>
      <td className="muted">{p.phone || "—"}</td>
      <td className="muted">{p.industry || p.company_size || "—"}</td>
      <td>
        <select
          className={"statusSel " + (STATUS_CLASS[status] || "")}
          value={status}
          onChange={(e) => {
            setStatus(e.target.value);
            save({ call_status: e.target.value });
          }}
        >
          {STATUSES.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
      </td>
      <td className="noteCell">
        <input
          className="noteInput"
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
