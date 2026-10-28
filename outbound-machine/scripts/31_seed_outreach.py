"""Charge le catalogue (pays, sous-ICP, personas, intentions, lead magnets, hypothèses, modèles de
séquences) dans Supabase « Outreach Cold Mail ». Idempotent (upsert)."""
import outreach_db as db
from icp_catalog import COUNTRIES, SEGMENTS, PERSONAS, INTENTS, LEAD_MAGNETS
import sequences as S

db.upsert("countries", [dict(code=c, name=n, language=l, wave=w, priority=w, rationale=r) for c, n, l, w, r in COUNTRIES], "code")
db.upsert("icp_segments", [dict(code=s["code"], icp=s["icp"], name=s["name"], family=s["family"], countries=s["countries"],
    priority=s["priority"], pains=s["pains"], kw_fr=s["kw_fr"], kw_en=s["kw_en"], keywords=s["kw_fr"] + s["kw_en"],
    industries=s["industries"], seg_fr=s["seg_fr"], seg_en=s["seg_en"],
    unit_fr=(s["unit"] or (None, None))[0], unit_en=(s["unit"] or (None, None))[1],
    proof_fr=(s["proof"] or (None, None))[0], proof_en=(s["proof"] or (None, None))[1], proof=(s["proof"] or ("aucune preuve sectorielle",))[0],
    offer="partenariat à la performance" if s["family"] == "PERF" else "visibilité Google + IA qui génère des demandes (OVI)",
    size_min=5, notes=s["notes"], status="propose") for s in SEGMENTS], "code")
pers = []
for s in SEGMENTS:
    for grp, rank, titles, angle in PERSONAS[s["family"]]:
        pers.append(dict(icp_code=s["code"], grp=grp, rank=rank, titles=titles, angle=angle))
existing = db.select("personas", "id")
if not existing:
    db.upsert("personas", pers)
db.upsert("intents", [dict(code=c, name=n, description=d, how_detect=h, tool=t, cost_per_company_usd=cost, pyramid_tier=tier)
                      for c, n, d, h, t, cost, tier in INTENTS], "code")
db.upsert("lead_magnets", [dict(code=c, name=n, effort=e, cost_note=cn, funnel_stage=fs, email_part=ep, call_part=cp,
                                sequence_step=st, icp_codes=[x.strip() for x in ic.split(",")]) for c, n, e, cn, fs, ep, cp, st, ic in LEAD_MAGNETS], "code")
db.upsert("hypotheses", [dict(code=c, intent_code=i, lead_magnet_code=lm, framework=f, angle=a, success_criteria=S.SUCCESS, status=st)
                         for c, _, i, lm, f, a, st in S.HYPOTHESES], "code")
msgs = []
for fam, hyp, seq in (("B2B", 6, S.H6), ("B2B", 7, S.H7), ("B2B", 8, S.H8), ("PERF", 9, S.H9)):
    for lang, steps in seq.items():
        for i, (subj, body) in enumerate(steps):
            msgs.append(dict(family=fam, hypothesis_code=hyp, language=lang, step=i + 1, delay_days=S.DELAYS[i], subject=subj, body=body,
                             persona_grp="champion" if hyp == 8 else "decideur" if fam == "B2B" else "tous", status="propose"))
for lang, (subj, body) in S.H12_VP1.items():
    msgs.append(dict(family="TOUS", hypothesis_code=12, language=lang, step=1, delay_days=0, subject=subj, body=body, persona_grp="tous", status="propose"))
if not db.select("messages", "id"):
    db.upsert("messages", msgs)
print(len(SEGMENTS), "segments,", len(pers), "personas,", len(msgs), "modèles")
