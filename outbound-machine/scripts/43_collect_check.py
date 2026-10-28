"""Collecte tous les fichiers de résultats FullEnrich sauvegardés et liste les lots manquants."""
import glob, json, subprocess, sys
T = "/root/.claude/projects/-home-user-outreach/f1faf9d3-6b97-50c2-8cdb-f91bdbcda7ca/tool-results/"
files = glob.glob(T + "mcp-FullEnrich-get_enrichment_results-*.txt") + glob.glob(T + "toolu_*.json")
names = {}
for f in files:
    try:
        d = json.load(open(f)); d = json.loads(d[0]["text"]) if isinstance(d, list) else d
        if d.get("status") == "FINISHED": names[d["enrichment_name"]] = f
    except Exception: pass
subprocess.run([sys.executable, "40_collect_enrich.py"] + list(names.values()))
print(len(names), "lots terminés :", sorted(names))
