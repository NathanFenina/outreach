#!/usr/bin/env python3
"""
Pousse les leads d'une campagne (outbound_campaign_leads) vers une campagne Lemlist
via l'API REST. Met à jour le statut ensuite (à faire côté SQL).

Prérequis (env) :
  LEMLIST_API_KEY   clé API Lemlist (Intégrations -> API & Webhooks)
  SUPABASE_URL, SUPABASE_KEY  (pour lire le batch ; ou passe un CSV)

Notes :
- Auth Lemlist = Basic (user vide, password = clé). User-Agent navigateur OBLIGATOIRE
  (sinon Cloudflare renvoie 403 code 1010).
- Endpoint add lead : POST /api/campaigns/{campaignId}/leads/{email}?deduplicate=true
  body = {firstName, companyName, ...customVars}
- Un lead déjà présent dans une AUTRE campagne Lemlist renvoie 500 "Lead already in
  other campaign" -> on le classe 'Déjà en campagne Lemlist' (protection anti-doublon Lemlist).
- ÉCRIRE LE CONTENU DE LA SÉQUENCE : possible via l'API (découvert le 2026-08-11).
    POST  /api/sequences/{seqId}/steps            (crée une étape)
    PATCH /api/sequences/{seqId}/steps/{stepId}   (modifie une étape)
  body = {"type":"email","subject":..., "message":<html>, "delay":<jours>, "index":<n>}
  -> "type" est OBLIGATOIRE et doit valoir "email" (sinon 400 "Type is required" /
     "Invalid request body"). Le seqId s'obtient via GET /api/campaigns/{cid}/sequences.
  Le "message" est du HTML (un <div> par ligne, <div><br></div> pour un saut).
  Variables Lemlist : {{firstName}}, {{companyName}}, {{companyDomain}} (natives) +
  variables custom ({{concurrent}}, {{categorie}}, {{secteur}}...) remplies par lead.
- Attacher un sender / lancer la campagne : se fait dans l'UI Lemlist.
"""
import os, json, time, base64, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
LEM = os.environ["LEMLIST_API_KEY"]
AUTH = base64.b64encode(f":{LEM}".encode()).decode()

def add_lead(campaign_id, email, fields):
    url = f"https://api.lemlist.com/api/campaigns/{campaign_id}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST",
        headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA})
    try:
        urllib.request.urlopen(rq, timeout=30)
        return "sent", ""
    except urllib.error.HTTPError as e:
        msg = e.read().decode()
        if "other campaign" in msg:
            return "dup", msg
        if "already" in msg.lower():
            return "sent", msg
        return "error", msg

def create_campaign(name):
    rq = urllib.request.Request("https://api.lemlist.com/api/campaigns",
        data=json.dumps({"name": name}).encode(), method="POST",
        headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA})
    return json.load(urllib.request.urlopen(rq, timeout=30))

def get_sequence_id(campaign_id):
    """Renvoie le 1er seqId d'une campagne (via GET .../sequences)."""
    rq = urllib.request.Request(f"https://api.lemlist.com/api/campaigns/{campaign_id}/sequences",
        headers={"Authorization": "Basic " + AUTH, "User-Agent": UA})
    seqs = json.load(urllib.request.urlopen(rq, timeout=30))
    return next(iter(seqs))  # les clés du dict sont les seqId

def lines_to_html(lines):
    """['a','', 'b'] -> HTML style éditeur Lemlist (un <div> par ligne)."""
    return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)

def write_step(seq_id, subject, message_html, delay=0, index=1, step_id=None):
    """Crée (POST) ou modifie (PATCH si step_id fourni) une étape email de séquence.
    'type':'email' est obligatoire côté API Lemlist."""
    body = {"type": "email", "subject": subject, "message": message_html,
            "delay": delay, "index": index}
    url = f"https://api.lemlist.com/api/sequences/{seq_id}/steps"
    method = "POST"
    if step_id:
        url += f"/{step_id}"; method = "PATCH"
    rq = urllib.request.Request(url, data=json.dumps(body).encode(), method=method,
        headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA})
    return json.load(urllib.request.urlopen(rq, timeout=30))

if __name__ == "__main__":
    print("Utilitaire Lemlist. Importer add_lead / create_campaign, ou adapter le main.")
