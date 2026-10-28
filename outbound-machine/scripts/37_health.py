"""Santé des domaines d'envoi, gratuit (remplace GlockApps au quotidien) : MX/SPF/DKIM/DMARC, listes noires SURBL et
Spamhaus DBL (DNS), redirection HTTP. Écrit sending_domains + health_checks (Supabase). À lancer chaque semaine.
Le taux de réponse humaine par boîte (métrique n° 1 d'Igor) est suivi dans la synthèse des campagnes."""
import json, urllib.request, datetime
import outreach_db as db

GROUP_A = ["decupler-agency.com", "decupler-digital.com", "decupler-geo.com", "decupler-ia.com", "decupler-leads.com",
           "decupler-search.com", "decupler-seo.com", "decupleragency.com", "decuplerdigital.com"]
GROUP_B = ["decuplerapp.com", "decuplerlabs.com", "getdecupler.com", "godecupler.com", "mydecupler.com", "decuplerly.com", "decupleroy.com"]


def q(name, t):
    try:
        return [a["data"] for a in json.loads(urllib.request.urlopen(f"https://dns.google/resolve?name={name}&type={t}", timeout=20).read()).get("Answer", [])]
    except Exception:
        return None


def http(d):
    try:
        r = urllib.request.urlopen(urllib.request.Request(f"https://{d}", method="HEAD"), timeout=15)
        return r.geturl()
    except Exception as e:
        return f"erreur {e}"[:80]


now = datetime.datetime.utcnow().isoformat()
rows, checks = [], []
for grp, doms in (("A", GROUP_A), ("B", GROUP_B)):
    for d in doms:
        txt = q(d, "TXT") or []
        res = dict(mx=q(d, "MX"), spf=any("v=spf1" in t for t in txt), dkim=bool(q(f"google._domainkey.{d}", "TXT")),
                   dmarc=(q(f"_dmarc.{d}", "TXT") or [""])[0][:60], surbl=q(f"{d}.multi.surbl.org", "A"),
                   spamhaus_dbl=q(f"{d}.dbl.spamhaus.org", "A"), url=http(d) if grp == "B" else None)
        sp = res["spamhaus_dbl"] or []
        rows.append(dict(domain=d, provider="PremiumInboxes" if grp == "A" else "Zapmail", grp=grp,
                         esp_target="google" if grp == "A" else "other", surbl=bool(res["surbl"]),
                         spamhaus=bool(sp) and not any(x.startswith("127.255.255") for x in sp),
                         redirect_ok=(res["url"] or "").startswith("https://decupler.com") if grp == "B" else None,
                         status="ok" if res["spf"] and res["dkim"] and res["dmarc"] else "dns incomplet", checked_at=now,
                         notes="Spamhaus refuse les résolveurs publics : résultat 127.255.255.x = non vérifiable" if any(x.startswith("127.255.255") for x in sp) else None))
        checks.append(dict(domain=d, check_type="dns_blacklist", result=res))
        print(grp, d, "SURBL" if res["surbl"] else "-", "spf" if res["spf"] else "NOSPF", "dkim" if res["dkim"] else "NODKIM", res["url"] or "")
db.upsert("sending_domains", rows, "domain")
db.upsert("health_checks", checks)
