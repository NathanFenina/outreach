"""Accès à la base Supabase « Outreach Cold Mail » via la fonction ingest (jeton hors repo)."""
import json, os, urllib.request

URL = "https://teuvlvovgjjlbxdnxdtc.supabase.co/functions/v1/ingest"
TOKEN_FILE = os.environ.get("INGEST_TOKEN_FILE", "/tmp/claude-0/-home-user-outreach/f1faf9d3-6b97-50c2-8cdb-f91bdbcda7ca/scratchpad/ingest_token")


def call(payload):
    tok = os.environ.get("INGEST_TOKEN") or open(TOKEN_FILE).read().strip()
    body = json.dumps(payload).replace("\\u0000", "")  # Postgres refuse le caractère nul (vu dans des noms d'entreprise Lemlist)
    req = urllib.request.Request(URL, data=body.encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-ingest-token": tok})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(e.read().decode())


def upsert(table, rows, on_conflict=None, ignore_duplicates=False, return_rows=False, batch=500):
    out = []
    for i in range(0, len(rows), batch):
        r = call({"action": "upsert", "table": table, "rows": rows[i:i + batch], "on_conflict": on_conflict,
                  "ignore_duplicates": ignore_duplicates, "return_rows": return_rows})
        out += r.get("rows") or []
    return out


def select(table, columns="*", eq=None, page=1000):
    rows, off = [], 0
    while True:
        r = call({"action": "select", "table": table, "columns": columns, "eq": eq or {}, "offset": off, "limit": page})["rows"]
        rows += r
        if len(r) < page:
            return rows
        off += page


def update(table, values, eq):
    return call({"action": "update", "table": table, "values": values, "eq": eq})
