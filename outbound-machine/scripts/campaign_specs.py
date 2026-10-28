"""Définition des campagnes (convention N°-LOT-H). Chaque campagne existe en 2 lots : G (prospects Google, ancienne infra)
et O (autres messageries, infra Zapmail, envoi après la chauffe ~6/11). Microsoft exclu."""
DECIDERS = ["Ownership / Firm Leadership", "Executive Leadership", "Department Leadership"]
SPECS = {
    "101": dict(name="ICP 2.2 · PAC et clim · FR · partenariat performance", icp_code="2.2", hypothesis=9, lang="fr", tier=3,
                countries=["FR"], keywords=["pompe à chaleur", "climatisation", "génie climatique"],
                headcount=["1-10", "11-50", "51-200"], seniority=DECIDERS, per_company=2, max_companies=2000, max_pages=33),
    "102": dict(name="ICP 1.x · B2B FR · recrute en marketing (palier 2)", icp_code="1.5", hypothesis=7, lang="fr", tier=2,
                countries=["FR"], keywords=["logiciel SaaS", "éditeur de logiciel", "SaaS", "ESN", "intégrateur ERP", "intégrateur CRM", "cybersécurité",
                                            "cabinet de conseil", "conseil en stratégie", "conseil en management", "fusions acquisitions", "M&A",
                                            "organisme de formation", "formation professionnelle"],
                headcount=["1-10", "11-50", "51-200", "201-500"], seniority=DECIDERS, per_company=3, max_companies=260, max_pages=15,
                extra=[("jobPostingTitle", ["marketing", "SEO", "growth", "contenu", "content", "acquisition", "communication"]), ("jobPostingDate", ["Last 90 days"])],
                signals={"I2": "recrute en marketing (offre < 90 j)"}),
    "103": dict(name="ICP 1.7 · M&A et transmission · FR (palier 3)", icp_code="1.7", hypothesis=7, lang="fr", tier=3,
                countries=["FR"], keywords=["fusions acquisitions", "M&A", "cession d'entreprise", "transmission d'entreprise"],
                headcount=["1-10", "11-50", "51-200"], seniority=DECIDERS, per_company=2, max_companies=330, max_pages=20),
}

# ICP 2 regroupé (lot G trop petit par niche) : un message par niche via variables de lead
SPECS["101b"] = dict(name="ICP 2.3 solaire · FR", icp_code="2.3", hypothesis=9, lang="fr", tier=3, countries=["FR"],
                     keywords=["photovoltaïque", "panneaux solaires"], headcount=["1-10", "11-50", "51-200"], seniority=DECIDERS,
                     per_company=2, max_companies=2000, max_pages=25)
SPECS["101c"] = dict(name="ICP 2.7 sécurité incendie · FR", icp_code="2.7", hypothesis=9, lang="fr", tier=3, countries=["FR"],
                     keywords=["sécurité incendie", "extincteurs", "désenfumage"], headcount=["1-10", "11-50", "51-200"], seniority=DECIDERS,
                     per_company=2, max_companies=2000, max_pages=25)
SPECS["102"]["assign"] = [("1.7", ["fusion", "acquisition", "m&a", "cession", "transmission"]), ("1.4", ["cybersécurité", "cybersecurity", "sécurité informatique", "pentest"]),
                          ("1.12", ["formation", "qualiopi"]), ("1.3", ["esn", "intégrateur", "erp", "crm", "salesforce", "odoo", "sage"]),
                          ("1.1", ["saas", "logiciel", "software", "plateforme"]), ("1.5", ["conseil", "consulting", "cabinet"])]
SPECS["102b"] = dict(SPECS["102"], name="ICP 1.x · B2B FR · palier 3 (sans signal)", tier=3, extra=[], signals={}, per_company=2, max_companies=700, max_pages=12,
                     headcount=["11-50", "51-200", "201-500"])
SPECS["102c"] = dict(SPECS["102b"], name="ICP 1.x · B2B FR · palier 3 (suite)", start_page=13, max_pages=18)
SPECS["101d"] = dict(SPECS["101b"], name="ICP 2.9 toiture et isolation · FR", icp_code="2.9", keywords=["couverture", "toiture", "isolation"], max_pages=8)
SPECS["101e"] = dict(SPECS["101b"], name="ICP 2.8 menuiseries, fenêtres, vérandas · FR", icp_code="2.8", keywords=["menuiserie", "fenêtres", "véranda"], max_pages=8)
