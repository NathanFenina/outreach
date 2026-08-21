#!/usr/bin/env python3
"""Publie les agences NON-francophones (Suisse-allemand + Saoudien) sur Lemlist — copy EN white-label.
Lit les leads depuis le fichier résultat Supabase MCP persisté. Variables {{firstName}} + {{companyName}}.
Usage: LEMLIST_API_KEY=... python3 15_publish_agences_en.py <file>"""
import os, sys, json, re, base64, time, urllib.request, urllib.parse, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
AUTH = base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H = {"Authorization": "Basic " + AUTH, "Content-Type": "application/json", "User-Agent": UA}

def api(method, url, body=None):
    last = None
    for attempt in range(5):
        try:
            rq = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=H)
            return json.load(urllib.request.urlopen(rq, timeout=40))
        except (urllib.error.URLError, urllib.error.HTTPError, ConnectionError) as e:
            if isinstance(e, urllib.error.HTTPError) and e.code < 500: raise
            last = e; time.sleep(2 ** attempt)
    raise last
def find_campaign(name):
    for c in api("GET", "https://api.lemlist.com/api/campaigns?limit=200") or []:
        if c.get("name") == name: return c.get("_id") or c.get("id")
    return None
def create_campaign(name): return api("POST", "https://api.lemlist.com/api/campaigns", {"name": name})
def get_seq_id(cid): return next(iter(api("GET", f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
def html(lines): return "".join("<div><br></div>" if l == "" else f"<div>{l}</div>" for l in lines)
def write_step(seq, subj, lines, delay, index):
    return api("POST", f"https://api.lemlist.com/api/sequences/{seq}/steps",
               {"type": "email", "subject": subj, "message": html(lines), "delay": delay, "index": index})
def add_lead(cid, email, fields, dedup="true"):
    url = f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate={dedup}"
    for attempt in range(5):
        rq = urllib.request.Request(url, data=json.dumps(fields).encode(), method="POST", headers=H)
        try:
            urllib.request.urlopen(rq, timeout=20); return "sent"
        except urllib.error.HTTPError as e:
            m = e.read().decode()
            if "other campaign" in m: return "dup"
            if "already" in m.lower(): return "sent"
            if "graveyard" in m.lower() or "blacklist" in m.lower(): return "grave"
            if e.code >= 500: time.sleep(2 ** attempt); continue
            return "error:" + m[:80]
        except (urllib.error.URLError, ConnectionError):
            time.sleep(2 ** attempt)
    return "error:network"

SIG = ["Nathan Fenina", "Decupler Agency"]
STEPS = [
 ("partners?",
  ["hi {{firstName}}, your clients are starting to ask whether they show up in ChatGPT and AI search (Perplexity, Google AI Overviews). most agencies don't have the technical answer yet, and rely on unreliable tools.","",
   "at Decupler that's all we do: we build our own AI systems and agents. and we can deliver it white-label, under {{companyName}}'s name.","",
   "you add an SEO/GEO line to your offering, you keep the margin, we deliver in the background.","",
   "open to 15 min to see our deliverables?","",*SIG,"",
   "PS: even if we don't work together, I'll send you our checklist of what a GEO audit should cover."], 0),
 ("re: partners?",
  ["{{firstName}}, to show you instead of just talking:","",
   "pick ONE of your clients (or a prospect you want to land), and we'll produce their AI-visibility audit — white-label, under your name, free.","",
   "you present it as yours. if it helps you upsell or close, we keep going; if not, you keep the audit, no strings attached.","",
   "15 min so you give me the client and I show you the format of our deliverables?","",*SIG], 2),
 ("we execute, you deliver",
  ["{{firstName}}, put simply: with our AI systems and agents, we build whatever deliverable YOU want — AI-visibility audit, GEO mapping, optimized content, AI monitoring, a ready-to-publish page... you tell us what your clients need, we execute white-label.","",
   "got a moment to discuss?","",*SIG,"",
   "PS: if you've got nothing to delegate right now, just say so and I'll leave you alone.",
   "PS2: we've worked on SEO for large accounts — SG, Le Point, Sodexo."], 1),
 ("closing out, {{firstName}}?",
  ["{{firstName}}, no reply so I'll assume:","1. you already handle SEO/GEO in-house (great, I'll leave you to it),",
   "2. it's not the right time (talk later?),","3. you're not the one handling partnerships (who should I reach out to?).","",
   "one word and I stop. the GEO audit checklist for {{companyName}} is yours if you want it.","",*SIG,"",
   "PPS: a 'no biz' and I'll leave you alone."], 2),
]

def load_leads(path):
    raw = open(path, encoding="utf-8").read().strip()
    text = raw
    try:
        obj = json.loads(raw)
        if isinstance(obj, list) and obj and isinstance(obj[0], dict) and "text" in obj[0]:
            obj = json.loads(obj[0]["text"])
        if isinstance(obj, dict) and "result" in obj: text = obj["result"]
    except Exception:
        text = raw
    m = re.search(r'\[\s*\{\s*"leads"\s*:\s*\[.*\]\s*\}\s*\]', text, re.DOTALL)
    if not m: raise SystemExit("tableau leads introuvable")
    return json.loads(m.group(0))[0]["leads"]

if __name__ == "__main__":
    leads = load_leads(sys.argv[1])
    seen = set(); uniq = []
    for l in leads:
        e = (l.get("email") or "").strip().lower()
        if e and e not in seen: seen.add(e); uniq.append(l)
    print(f"leads agences EN: {len(uniq)}")
    name = "Decupler · Agencies · White-label GEO (EN)"
    cid = find_campaign(name)
    if cid: print("réutilisée (dedup=false):", cid); dedup = "false"
    else:
        camp = create_campaign(name); cid = camp.get("_id") or camp.get("id"); time.sleep(1)
        seq = get_seq_id(cid)
        for i, (subj, lines, d) in enumerate(STEPS, 1): write_step(seq, subj, lines, d, i); time.sleep(0.4)
        print("steps écrits"); dedup = "true"
    print("CAMPAIGN=" + cid)
    s = g = e = 0
    for l in uniq:
        f = {"companyName": l.get("companyName", "")}
        fn = (l.get("firstName") or "").strip()
        if fn: f["firstName"] = fn
        r = add_lead(cid, l["email"].strip(), f, dedup)
        if r in ("sent", "dup"): s += 1
        elif r == "grave": g += 1
        else: e += 1; print("ERR", l["email"], r)
        time.sleep(0.2)
    print(f"STATS ok={s} graveyard={g} err={e}")
