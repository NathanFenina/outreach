"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

// Toutes les issues possibles : on peut faire avancer OU refroidir un lead depuis ce board.
const STATUSES = [
  "Rappeler",
  "Répondu",
  "Intéressé",
  "RDV",
  "RDV pris",
  "Vidéo envoyée",
  "Présenté",
  "À relancer",
  "Signé",
  "Perdu",
  "Pas intéressé",
  "Ne pas contacter",
];

const STATUS_CLASS = {
  Rappeler: "st-recall",
  "Répondu": "st-reply",
  "Intéressé": "st-hot",
  RDV: "st-rdv",
  "RDV pris": "st-rdv",
  "Vidéo envoyée": "st-sms-done",
  "Présenté": "st-reply",
  "À relancer": "st-recall",
  "Signé": "st-win",
  "Perdu": "st-dead",
  "Pas intéressé": "st-dead",
  "Ne pas contacter": "st-nc",
};

const CANAL = {
  call: "Cold Call",
  facebook: "Facebook",
  present: "À présenter",
  batimat: "Batimat",
  email: "Cold Mail",
  levee: "Levée",
  cmo: "CMO",
};

export default function HotRow({ p }) {
  const perso = p.personalization || {};
  const [status, setStatus] = useState(p.call_status || "Intéressé");
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
  let wa = (p.phone || "").replace(/[^0-9]/g, "");
  if (wa.startsWith("0")) wa = "33" + wa.slice(1);
  const waHref = wa.length >= 8 ? `https://wa.me/${wa}` : null;
  const site = p.demo_url || perso.website || null;
  const contact = p.full_name || p.first_name;

  return (
    <tr>
      <td data-label="Lead">
        <span className="name cellclip" title={p.company || contact || ""}>
          {p.company || contact || "—"}
        </span>
        {contact && p.company && contact !== p.company && (
          <div className="small cellclip" title={contact}>
            {contact}
            {p.job_title ? ` · ${p.job_title}` : ""}
          </div>
        )}
        {(!p.company || contact === p.company) && p.job_title && (
          <div className="small cellclip" title={p.job_title}>{p.job_title}</div>
        )}
      </td>
      <td data-label="Canal">
        <span className="badge b-none">{CANAL[p.channel] || p.channel}</span>
      </td>
      <td data-label="Téléphone">
        {telHref ? (
          <>
            <a className="lnk" href={telHref}>
              {p.phone}
            </a>
            {waHref && (
              <>
                {" · "}
                <a className="lnk wa" href={waHref} target="_blank" rel="noreferrer">
                  WA
                </a>
              </>
            )}
          </>
        ) : (
          "—"
        )}
      </td>
      <td data-label="Site">
        {site ? (
          <a className="lnk" href={site} target="_blank" rel="noreferrer">
            site ↗
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
