"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

const STATUSES = [
  "À contacter",
  "Email envoyé",
  "Relancé",
  "Répondu",
  "Intéressé",
  "RDV",
  "Pas intéressé",
  "Ne pas contacter",
];

const STATUS_CLASS = {
  "À contacter": "st-todo",
  "Email envoyé": "st-sms-done",
  "Relancé": "st-recall",
  "Répondu": "st-reply",
  "Intéressé": "st-hot",
  "RDV": "st-rdv",
  "Pas intéressé": "st-dead",
  "Ne pas contacter": "st-nc",
};

export default function BatimatRow({ p }) {
  const perso = p.personalization || {};
  const [status, setStatus] = useState(p.call_status || "À contacter");
  const [notes, setNotes] = useState(p.notes || "");
  const [pending, start] = useTransition();
  const [flash, setFlash] = useState("");

  function save(patch) {
    start(async () => {
      const r = await updateLeadCrm(p.id, patch);
      setFlash(r.ok ? "ok" : "err");
      setTimeout(() => setFlash(""), 1600);
    });
  }

  const site = perso.website || (p.domain ? `https://${p.domain}` : null);
  const mailHref = p.email ? `mailto:${p.email}` : null;
  const telHref = p.phone ? `tel:${p.phone.replace(/[^0-9+]/g, "")}` : null;

  return (
    <tr>
      <td data-label="Société">
        <span className="name cellclip" title={p.company || ""}>
          {p.company || "—"}
        </span>
        {perso.stand && <div className="small">Stand {perso.stand}</div>}
      </td>
      <td data-label="Site">
        {site ? (
          <a className="lnk" href={site} target="_blank" rel="noreferrer">
            site
          </a>
        ) : (
          "—"
        )}
      </td>
      <td className="muted" data-label="Email">
        {mailHref ? (
          <a className="lnk" href={mailHref} title="Écrire un email">
            <span className="cellclip">{p.email}</span>
          </a>
        ) : (
          "—"
        )}
      </td>
      <td className="muted" data-label="Téléphone">
        {telHref ? (
          <a className="lnk" href={telHref}>
            {p.phone}
          </a>
        ) : (
          "—"
        )}
      </td>
      <td data-label="Statut">
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
      <td className="noteCell" data-label="Remarque">
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
