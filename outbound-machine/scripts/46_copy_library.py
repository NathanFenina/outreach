"""Bibliothèque de toutes les copies de Nathan, numérotées :
L-xx = campagnes Lemlist réellement envoyées (mail 1 + chiffres réels), B-xx = mails de la Base Copy (artifact),
F-xx = séquences des fichiers copy/ (titre + objet + début du mail 1). Sortie : ../data/copy_library.json"""
import base64, csv, html, json, os, re, sys, time, urllib.request
from bs4 import BeautifulSoup

H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode()}
BASE_COPY = sys.argv[1] if len(sys.argv) > 1 else "base_copy.html"


def get(p):
    for i in range(5):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request("https://api.lemlist.com/api" + p, headers=H), timeout=60).read())
        except Exception:
            time.sleep(2 ** i)
    return None


def text(h):
    h = re.sub(r"<br\s*/?>|</div>|</p>", "\n", h or "")
    return re.sub(r"\n{3,}", "\n\n", html.unescape(re.sub(r"<[^>]+>", "", h))).strip()


lib = []
# 1. Lemlist : campagnes avec des envois réels
rows = [r for r in csv.DictReader(open("../data/synthese_campagnes.csv")) if int(r["launched"] or 0) > 0]
rows.sort(key=lambda r: -int(r["launched"]))
for i, r in enumerate(rows, 1):
    seqs = get(f"/campaigns/{r['id']}/sequences") or {}
    steps = [s for seq in (seqs.values() if isinstance(seqs, dict) else seqs) for s in (seq.get("steps") or [])]
    mail = next((s for s in steps if s.get("type") == "email"), None)
    if not mail: continue
    launched, replied = int(r["launched"]), int(r["replied"] or 0)
    lib.append(dict(id=f"L-{i:02d}", source="Lemlist (envoyée)", titre=r["name"], objet=mail.get("subject") or "",
                    corps=text(mail.get("message"))[:1500], etapes=sum(1 for s in steps if s.get("type") == "email"),
                    resultat=f"{launched} contactés · {replied} réponses ({100 * replied / launched:.1f} %)" if launched else ""))
    time.sleep(0.3)

# 2. Base Copy : tous les mails (formats .mail et .n-mail)
soup = BeautifulSoup(open(BASE_COPY).read(), "html.parser")
n = 0
for sec in soup.find_all("section"):
    sid = sec.get("id")
    for m in sec.select(".mail, .n-mail"):
        n += 1
        art = m.find_parent("article")
        if art and art.select_one(".n-id"):
            titre = f"{art.select_one('.n-id').get_text(strip=True)} · {art.find('h3').get_text(' ', strip=True)}"
        else:
            lbl = m.select_one(".lbl"); titre = lbl.get_text(" ", strip=True) if lbl else sid
        subj = m.select_one(".n-subj") or m.select_one(".subj .val") or m.select_one(".subj")
        objet = subj.get_text(" ", strip=True) if subj else ""
        body = m.select_one(".body")
        if body is None:
            if subj: subj.extract()
            body = m
        lib.append(dict(id=f"B-{n:02d}", source=f"Base Copy · #{sid}", titre=titre, objet=objet.replace("Objet :", "").strip(),
                        corps=body.get_text("\n", strip=False).strip()[:1500], etapes="", resultat=""))

# 3. Fichiers copy/ : un enregistrement par séquence / mail titré (### ou ##)
n = 0
for fn in sorted(os.listdir("../copy")):
    if not re.match(r"(0\d|1\d)_.*\.md$", fn): continue
    txt = open(f"../copy/{fn}").read()
    for m in re.finditer(r"^#{2,4} (.+)$", txt, re.M):
        start = m.end(); nxt = re.search(r"^#{2,4} ", txt[start:], re.M)
        block = txt[start:start + (nxt.start() if nxt else len(txt))].strip()
        if not re.search(r"(?i)objet|subject|bonjour|hello|hi \{|\{\{firstName", block): continue
        n += 1
        obj = re.search(r"(?i)(?:objet|subject)\s*[:：]\s*\**(.+)", block)
        lib.append(dict(id=f"F-{n:03d}", source=f"copy/{fn}", titre=m.group(1).strip()[:160], objet=(obj.group(1).strip("* ") if obj else ""),
                        corps=block[:1200], etapes="", resultat=""))

json.dump(lib, open("../data/copy_library.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(lib), Counter(x["id"][0] for x in lib))
