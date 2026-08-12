"use client";
import { useState, useTransition } from "react";
import { updateLeadCrm } from "../app/actions";

const STATUSES = [
  "À appeler",
  "Appelé",
  "Répondu",
  "RDV",
  "Rappeler",
  "SMS à envoyer",
  "SMS envoyé",
  "Pas intéressé",
  "Mauvais numéro",
  "Ne pas contacter",
];

const STATUS_CLASS = {
  "À appeler": "st-todo",
  Appelé: "st-done",
  Répondu: "st-win",
  RDV: "st-win",
  Rappeler: "st-warn",
  "SMS à envoyer": "st-warn",
  "SMS envoyé": "st-done",
  "Pas intéressé": "st-dead",
  "Mauvais numéro": "st-dead",
  "Ne pas contacter": "st-dead",
};

export default function CallRow({ p }) {
  const perso = p.personalization || {};
  const [status, setStatus] = useState(p.call_status || "À appeler");
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

  const waDigits = (p.phone || "").replace(/[^0-9]/g, "");
  const waText = encodeURIComponent(
    `Bonjour, Nathan de Décupler. Suite à mon appel, je vous envoie la carte des zones autour de Nantes où vous pouvez récupérer des demandes de devis. Je vous partage ça ?`
  );

  return (
    <tr>
      <td>
        <span className="name cellclip" title={p.company || p.full_name || ""}>
          {p.company || p.full_name || "—"}
        </span>
      </td>
      <td className="muted">{p.phone || "—"}</td>
      <td className="muted">
        {perso.rating ? (
          <span>
            ⭐ {perso.rating}
            {perso.reviews ? ` (${perso.reviews})` : ""}
          </span>
        ) : (
          "—"
        )}
      </td>
      <td>
        {perso.website ? (
          <a className="lnk" href={perso.website} target="_blank" rel="noreferrer">
            site
          </a>
        ) : (
          "—"
        )}
        {perso.maps_url && (
          <>
            {" · "}
            <a className="lnk" href={perso.maps_url} target="_blank" rel="noreferrer">
              maps
            </a>
          </>
        )}
        {waDigits && (
          <>
            {" · "}
            <a
              className="lnk wa"
              href={`https://wa.me/${waDigits}?text=${waText}`}
              target="_blank"
              rel="noreferrer"
              title="Ouvrir WhatsApp avec un message pré-rempli"
            >
              WhatsApp
            </a>
          </>
        )}
      </td>
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
