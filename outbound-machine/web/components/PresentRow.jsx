"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

const STATUSES = [
  "À présenter",
  "RDV pris",
  "Présenté",
  "Signé",
  "Perdu",
];

const STATUS_CLASS = {
  "À présenter": "st-todo",
  "RDV pris": "st-warn",
  "Présenté": "st-done",
  "Signé": "st-win",
  "Perdu": "st-dead",
};

export default function PresentRow({ p }) {
  const perso = p.personalization || {};
  const [status, setStatus] = useState(p.call_status || "À présenter");
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

  const digits = (p.phone || "").replace(/[^0-9+]/g, "");
  const waDigits = (p.phone || "").replace(/[^0-9]/g, "");
  // SMS / WhatsApp de rappel de RDV — sans accents (GSM-7)
  const rappel = `Bonjour, Nathan de Decupler. Petit rappel : je vous ai prepare un site moderne, je vous le montre 10 min a l'ecran ? Dites-moi quand ca vous arrange. Sinon repondez STOP.`;
  const txt = encodeURIComponent(rappel);
  const telHref = p.phone ? `tel:${digits}` : null;
  const smsHref = p.phone ? `sms:${digits}?body=${txt}` : null;

  return (
    <tr>
      <td data-label="Entreprise">
        <span className="name cellclip" title={p.company || ""}>
          {p.company || "—"}
        </span>
        {p.industry && <div className="muted small">{p.industry}</div>}
      </td>
      <td className="muted" data-label="Téléphone">
        {telHref ? (
          <a className="lnk" href={telHref} title="Appeler">
            {p.phone}
          </a>
        ) : (
          "—"
        )}
      </td>
      <td data-label="Site à présenter">
        {p.demo_url ? (
          <a className="lnk" href={p.demo_url} target="_blank" rel="noreferrer" title="Ouvrir le site construit">
            ▶ voir le site
          </a>
        ) : (
          "—"
        )}
        {perso.website && (
          <>
            {" · "}
            <a className="lnk" href={perso.website} target="_blank" rel="noreferrer" title="Site actuel du prospect">
              actuel
            </a>
          </>
        )}
      </td>
      <td data-label="Rappel">
        {smsHref && (
          <a className="lnk" href={smsHref} title="SMS de rappel pré-rempli (OnOff / téléphone)">
            SMS
          </a>
        )}
        {waDigits && (
          <>
            {smsHref ? " · " : ""}
            <a
              className="lnk wa"
              href={`https://wa.me/${waDigits}?text=${txt}`}
              target="_blank"
              rel="noreferrer"
              title="Rappel via WhatsApp"
            >
              WA
            </a>
          </>
        )}
        {!smsHref && !waDigits && "—"}
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
          placeholder="RDV, retour, objection…"
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
