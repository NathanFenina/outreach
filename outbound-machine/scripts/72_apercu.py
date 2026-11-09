"""Aperçu HTML à valider : pour chaque campagne de 66_instantly_v5.py, les 3 mails rendus sur de vrais leads, tels
qu'Instantly les enverra (variables remplacées). Mail 3 : un exemple A (cartographie) et un exemple B (concurrent) quand il
existe, + la liste des leads B à contrôler à la main sur Google. Sortie : ../copy/48_apercu_mails.html"""
import datetime, html, re, sys

src = open("66_instantly_v5.py").read().split('if __name__ == "__main__":')[0]
g = {"__name__": "x"}; exec(compile(src, "66_instantly_v5.py", "exec"), g)
PLAN, SEQ, leads = g["PLAN"], g["SEQ"], g["leads"]
WHEN = ["Mail 1 · J0 · nouveau fil", "Mail 2 · J+3 · même fil (relance)", "Mail 3 · J+8 · nouveau fil (relance)"]


def render(t, lead):
    v = dict(lead["custom_variables"], firstName=lead["first_name"], lastName=lead["last_name"], companyName=lead["company_name"])
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(v.get(m.group(1), m.group(0))), t)


def mail(i, subj, body, lead, tag=""):
    s = render(subj, lead) if subj else "(même fil, pas d'objet)"
    lines = "".join(f"<p>{html.escape(render(l, lead)).replace(chr(10), '<br>')}</p>" for l in body)
    return f"<div class='m'><div class='h'>{WHEN[i]}{tag} · objet : <b>{html.escape(s)}</b></div>{lines}</div>"


L = leads()
out, btable = [], []
stats = []
for code, (name, seq, ps3, _) in PLAN.items():
    ls = L[code]
    if not ls: continue
    A = [l for l in ls if l["custom_variables"].get("m3_variant", "A") != "B"]
    B = [l for l in ls if l["custom_variables"].get("m3_variant") == "B"]
    ex = next((l for l in A if l["custom_variables"].get("ai_absent")), A[0] if A else ls[0])
    stats.append((code, name, len(ls), len(B)))
    s = SEQ[seq]
    blk = [f"<h2>{html.escape(code)} · {html.escape(name)}</h2><p class='n'>{len(ls)} leads · mail 3 concurrent (B) : {len(B)} · "
           f"cartographie (A) : {len(ls) - len(B)}. Exemple : {html.escape(ex['company_name'])} ({ex['website']})</p>"]
    for i, (subj, body) in enumerate(s):
        blk.append(mail(i, subj, body, ex, " · version A cartographie" if i == 2 and "{{m3s}}" in subj else ""))
    if B and "{{m3s}}" in s[2][0]:
        b = B[0]
        blk.append(f"<p class='n'>Version B, exemple : {html.escape(b['company_name'])} ({b['website']})</p>" + mail(2, s[2][0], s[2][1], b, " · version B concurrent"))
        for l in B:
            c = l["custom_variables"]
            btable.append((code, l["company_name"], l["website"], c.get("niche"), c.get("m3s", "").split(" plutôt")[0].split(" instead")[0]))
    import random
    smp = random.Random(code).sample(ls, min(15, len(ls)))
    smp = sorted(smp, key=lambda l: l["custom_variables"].get("m3_variant", "A"))
    blk.append("<p class='n'>15 autres leads tirés au hasard (niche, phrase d'ouverture, objet du mail 3) :</p><table><tr><th>Entreprise</th><th>Niche</th><th>Ouverture mail 1</th><th>Objet mail 3</th></tr>"
               + "".join(f"<tr><td>{html.escape(l['company_name'])}<br><span class='n'>{l['website']}</span></td><td>{html.escape(l['custom_variables'].get('niche') or '')}</td>"
                         f"<td>{html.escape(render(next((x for x in s[0][1] if '{{l1}}' in x or '{{s4a}}' in x), s[0][1][1]), l))}</td><td>{html.escape(render(s[2][0], l))}</td></tr>" for l in smp)
               + "</table>")
    out.append("".join(blk))

seen, rows = set(), []
for r in btable:
    if r[2] in seen: continue
    seen.add(r[2]); rows.append(r)
tab = "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td><td>{html.escape(d or '')}</td><td>{html.escape(e)}</td>"
              f"<td><a href='https://www.google.com/search?q={html.escape(d or '')}'>chercher</a></td></tr>" for a, b, c, d, e in rows)
summary = "".join(f"<tr><td>{a}</td><td>{html.escape(b)}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in stats)
page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aperçu des mails</title><style>
:root{{--bg:#fff;--fg:#1d1d1f;--mut:#6e6e73;--card:#f5f5f7;--line:#d2d2d7;--acc:#0b57d0}}
@media (prefers-color-scheme:dark){{:root{{--bg:#111;--fg:#f2f2f2;--mut:#a1a1a6;--card:#1c1c1e;--line:#38383a;--acc:#8ab4f8}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;max-width:860px;margin:0 auto;padding:16px}}
h2{{margin-top:40px;border-top:1px solid var(--line);padding-top:20px}} .n{{color:var(--mut)}}
.m{{background:var(--card);border-radius:10px;padding:12px 16px;margin:12px 0}} .m p{{margin:6px 0}} .h{{color:var(--mut);font-size:13px;margin-bottom:6px}}
table{{border-collapse:collapse;width:100%;font-size:13px;display:block;overflow-x:auto}} td,th{{border-bottom:1px solid var(--line);padding:6px;text-align:left}}
a{{color:var(--acc)}}</style></head><body>
<h1>Aperçu des mails · vrais leads, rendu final</h1>
<p class="n">{datetime.date.today():%d/%m/%Y}. Un lead réel par campagne, tel qu'Instantly l'enverra. Rien n'est envoyé.</p>
<p><b>Où est quoi :</b> mail 1 = ChatGPT + 3 quick wins (premier message). Mail 2 = « envoyez-moi une page » (relance, même fil).
Mail 3 = relance dans un nouveau fil : <b>B « concurrent »</b> si le concurrent est validé strictement (même métier, même type de client, page d'accueil des deux sites lue),
sinon <b>A « cartographie »</b>. S3a (agences marque blanche) garde son propre mail 3.</p>
<table><tr><th>Campagne</th><th>Nom</th><th>Leads</th><th>Mail 3 B</th></tr>{summary}</table>
{''.join(out)}
<h2>Mail 3 B · à contrôler sur Google</h2><p class="n">{len(rows)} entreprises. Google varie selon le lieu et la personne : vérifier un échantillon avant le lancement.</p>
<table><tr><th>Campagne</th><th>Entreprise</th><th>Site</th><th>Recherche</th><th>Concurrent cité</th><th></th></tr>{tab}</table>
</body></html>"""
if "--igor" in sys.argv:  # version courte pour Igor : 1 exemple par campagne, sans les tableaux internes
    page = re.sub(r"<p class='n'>15 autres leads[\s\S]*?</table>", "", page)
    page = page[:page.index("<h2>Mail 3 B")] + "</body></html>" if "<h2>Mail 3 B" in page else page
    page = page.replace("Aperçu des mails · vrais leads, rendu final", "Décupler · wave 1 preview (real leads, final render)")
    page = re.sub(r"<p><b>Où est quoi :</b>[\s\S]*?</p>", "<p><b>Sequence:</b> mail 1 = ChatGPT check + 3 quick wins (the 'didn't come up' line is only written when verified on real ChatGPT for that lead). "
                  "Mail 2 (day 3, same thread) = 'send me one page, I'll optimise it for free'. Mail 3 (day 8, new thread) = map of organic opportunities + 3-min video. "
                  "S3a (white-label agencies) keeps its own mail 3. One real lead per campaign below, exactly as Instantly will send it.</p>", page)
    open("../copy/49_apercu_igor.html", "w").write(page)
else:
    open("../copy/48_apercu_mails.html", "w").write(page)
print("ok", [(a, c, d) for a, b, c, d in stats], "B uniques", len(rows))
