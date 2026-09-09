"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

const STATUSES = [
  "À contacter",
  "WhatsApp à envoyer",
  "WhatsApp envoyé",
  "Répondu",
  "Intéressé",
  "RDV",
  "Pas intéressé",
  "Ne pas contacter",
];

const STATUS_CLASS = {
  "À contacter": "st-todo",
  "WhatsApp à envoyer": "st-wa-todo",
  "WhatsApp envoyé": "st-wa-done",
  "Répondu": "st-reply",
  "Intéressé": "st-hot",
  "RDV": "st-rdv",
  "Pas intéressé": "st-dead",
  "Ne pas contacter": "st-nc",
};

function waLink(phone) {
  if (!phone) return null;
  let d = phone.replace(/[^0-9]/g, "");
  if (d.startsWith("0")) d = "33" + d.slice(1);
  return d.length >= 8 ? `https://wa.me/${d}` : null;
}

export default function FacebookRow({ p }) {
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

  const telHref = p.phone ? `tel:${p.phone.replace(/[^0-9+]/g, "")}` : null;
  const wa = waLink(p.phone);
  const mailHref = p.email ? `mailto:${p.email}` : null;

  return (
    <tr>
      <td data-label="Artisan">
        <span className="name cellclip" title={p.company || ""}>
          {p.company || "—"}
        </span>
        {p.job_title && (
          <div className="small cellclip" title={p.job_title}>
            {p.job_title}
          </div>
        )}
      </td>
      <td className="muted" data-label="Zone">
        <span className="cellclip" title={p.location || ""}>
          {p.location || "—"}
        </span>
      </td>
      <td data-label="Téléphone">
        {telHref ? (
          <>
            <a className="lnk" href={telHref}>
              {p.phone}
            </a>
            {wa && (
              <>
                {" · "}
                <a className="lnk wa" href={wa} target="_blank" rel="noreferrer">
                  WhatsApp
                </a>
              </>
            )}
          </>
        ) : (
          "—"
        )}
      </td>
      <td className="muted" data-label="Email">
        {mailHref ? (
          <a className="lnk" href={mailHref}>
            <span className="cellclip">{p.email}</span>
          </a>
        ) : (
          "—"
        )}
      </td>
      <td className="muted" data-label="Contexte">
        <span className="cellclip" title={perso.contexte || ""}>
          {perso.contexte || "—"}
        </span>
        {perso.groupe && <div className="small cellclip" title={perso.groupe}>grp: {perso.groupe}</div>}
      </td>
      <td data-label="Post">
        {perso.lien ? (
          <a className="lnk" href={perso.lien} target="_blank" rel="noreferrer">
            post ↗
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
