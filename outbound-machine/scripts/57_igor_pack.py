"""Prépare les onglets de validation pour Igor : « 6c. Copies V3 FR + EN » (modèles V3 en français + traduction anglaise,
colonnes de validation Nathan et Igor) et « 2c. ICP problems (EN) » (5 problèmes de fond + problèmes par sous-ICP, en anglais).
Sortie : ../data/igor_copies_v3.json et ../data/igor_icp_en.json (lignes prêtes pour le Sheet)."""
import json
from copy_v3_models import MODELS, PROBLEMS

head = ["N°", "Famille", "Étape / palier", "Problème porté", "Objet (FR)", "Texte (FR)", "PS (FR)", "Subject (EN)", "Text (EN)", "PS (EN)",
        "Source / retour Nathan", "Validation Nathan", "Commentaire Nathan", "Igor : OK ?", "Igor : comment"]
rows = [head] + [[m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], "", "", "", ""] for m in MODELS]
json.dump(rows, open("../data/igor_copies_v3.json", "w"), ensure_ascii=False)

# Problèmes par sous-ICP, en anglais (traduction des colonnes « Problème 1 à 3 » de l'onglet 2b) + problème de fond principal
ICP_EN = [
 ("1.1", "B2B SaaS publishers", "Buyers build their shortlist in ChatGPT / Perplexity (\"best software for…\"): competitors are cited, they are not", "Pipeline depends on ads (high SaaS CPCs) and SDRs: acquisition cost keeps rising", "Content published with no measurable link to demos / trials", "Invisible in AI answers"),
 ("1.2", "AI and data startups", "Market crowded with new AI players: impossible to stand out on Google or ChatGPT", "Visibility depends on LinkedIn and funding news, no steady inbound demand", "LLMs cite the big players (OpenAI, Mistral…) and comparison sites, not them", "Invisible in AI answers"),
 ("1.3", "IT services and ERP / CRM integrators", "Requests come from network and tenders: few inbound leads", "\"Generalist IT firm\" message: Google and AI don't link them to any expertise (ERP, CRM, cloud…)", "Partner integrators rank better on \"Odoo / Salesforce / Sage integrator + city\"", "A competitor takes the traffic"),
 ("1.4", "Cybersecurity firms", "Trust purchase: CISOs / CIOs check Google and ask AI before reaching out", "Big players and comparison pages dominate \"audit / pentest / SOC\"", "Long cycles: little inbound, dependence on reseller partners", "Invisible in AI answers"),
 ("1.5", "Strategy and management consulting", "Growth through partners' network: irregular pipeline", "Expertise invisible online: Google and AI cite the Big Four and large firms", "Content (white papers, articles) that doesn't generate meetings", "Lack of visibility"),
 ("1.6", "Accounting and outsourced CFO firms", "Clients come by word of mouth, growth is capped", "Strong local competition on \"accountant / outsourced CFO + city\"", "Online platforms and online accounting firms capture searches", "A competitor takes the traffic"),
 ("1.7", "M&A and business transfer advisors", "Sellers and buyers research online, discreetly, before talking to an advisor", "Visibility dominated by business-for-sale platforms and large networks", "Deal flow depends on network and introducers", "Not enough inbound requests"),
 ("1.8", "Wealth managers", "Clients come only through referrals", "Private banks and online platforms dominate Google", "Regulation limits advertising: content is the only lever", "Not enough inbound requests"),
 ("1.9", "Marketing and web agencies (white-label GEO)", "Their clients ask \"what about ChatGPT?\": no GEO offer to sell", "No time or tools to produce GEO in-house", "Competing agencies position themselves on AI", "Invisible in AI answers"),
 ("1.10", "Event and speaker agencies", "Companies search a venue / speaker on Google and ChatGPT, platforms capture demand", "Seasonal seminars", "Dependence on platforms and tenders", "A competitor takes the traffic"),
 ("1.11", "Recruitment and HR firms", "Mandates come from network and LinkedIn", "Job boards and large firms capture searches", "No inbound demand from client companies", "Not enough inbound requests"),
 ("1.12", "Professional training companies", "Enrolments depend on funders (CPF, OPCO) and platforms", "Strong competition on \"training + job\" dominated by large providers", "High acquisition cost through Google Ads", "Expensive ads"),
 ("1.13", "Business law firms", "Business clients only through referrals", "Directories and legaltech capture searches", "Professional conduct rules limit advertising", "A competitor takes the traffic"),
 ("2.1", "Construction and renovation contractors", "Leads bought on platforms and shared between 3 to 5 tradesmen", "A competitor ranks above them on Google Maps and ChatGPT in their area", "Already paid an agency with no result: refuse to pay upfront", "A competitor takes the traffic"),
 ("2.2", "Heat pump and air-con installers", "Short season: empty schedule outside peaks", "Shared and expensive platform leads", "Competitors rank better on \"heat pump + city\"", "Not enough inbound requests"),
 ("2.3", "Solar installers", "Sector damaged by aggressive door-to-door: trust is won online (reviews, website)", "Shared platform leads", "National players dominate Google", "Lack of visibility"),
 ("2.4", "Roller-shutter companies", "Emergency repairs: the first on Google Maps gets the call", "B2B clients (shops) search \"roller shutter repair + city\"", "Little online presence beyond directories", "A competitor takes the traffic"),
 ("2.5", "Stairlift installers", "Purchase triggered by seniors' children searching online", "National brands dominate Google", "Expensive bought leads", "Lack of visibility"),
 ("2.6", "Funeral homes", "Searches made in urgency: the first local result wins", "Large networks (PFG, Roc Eclerc) compete", "Pre-need contracts captured by comparison sites", "A competitor takes the traffic"),
 ("2.7", "Fire safety companies", "Regulated B2B market (annual checks): recurring contracts to win", "National players on \"fire extinguisher maintenance + city\"", "Costly field sales prospecting", "Not enough inbound requests"),
 ("2.8", "Window, door and conservatory installers", "Leads shared on platforms", "Franchise competition (Tryba, Lapeyre…)", "High ticket: one more job matters", "Not enough inbound requests"),
 ("2.9", "Roofing and insulation", "Emergencies (leaks, storms) go to the first on Maps", "Aggressive door-to-door in the sector: trust to win", "Shared leads", "A competitor takes the traffic"),
 ("2.10", "Pool builders", "Season: decisions made in winter / spring", "Networks compete (Desjoyaux, Diffazur…)", "High ticket", "Not enough inbound requests"),
 ("2.11", "Alarm and CCTV installers", "Pros and homeowners compare online", "National monitoring companies compete", "Recurring contracts to win", "Lack of visibility"),
 ("2.12", "Kitchen designers", "Retail brands compete (Schmidt, Mobalpa…)", "Showroom visits come from Google Maps", "Poorly qualified leads", "A competitor takes the traffic"),
 ("2.13", "Removal companies", "Quotes captured by comparison sites", "Season (summer)", "National competition", "A competitor takes the traffic"),
 ("2.14", "Landscapers", "Season (spring)", "High-end clients look for past projects", "Shared leads", "Not enough inbound requests"),
 ("2.15", "Civil engineering and public works", "Public contracts go through tender platforms: 10 bidders, crushed margins", "Private clients (developers, industrials) search Google and find the biggest firms", "Dependence on network and the same contractors", "A competitor takes the traffic"),
 ("4.1", "Independent hotels", "Booking / Expedia commission on every reservation (often 15% or more)", "Few direct bookings from Google and AI", "A competitor comes first on \"hotel + city\"", "Expensive ads"),
 ("4.2", "Spas and wellness centres", "Dependence on booking platforms and gift boxes", "Local competition on \"spa + city\"", "Irregular clientele", "A competitor takes the traffic"),
 ("4.3", "Private senior residences", "Occupancy rate to fill", "Families compare online and on directories", "Large groups compete", "Lack of visibility"),
 ("4.4", "Campsites and holiday parks", "Platform commissions", "Short season", "Few direct bookings", "Expensive ads"),
 ("4.5", "Wellness training schools", "Enrolments depend on word of mouth and fairs", "On \"training + discipline\", platforms and large providers rank first", "Future students compare schools on Google and ChatGPT before asking for a brochure", "Invisible in AI answers"),
]
icp = [["ICP PROBLEMS (EN) · for Igor's review · medical tourism (3.x) on hold"], [],
       ["THE 5 CORE PROBLEMS", "", "Tiers / emails that carry it", "Data source"]]
icp += [[en, fr, tiers, src] for fr, en, tiers, src in PROBLEMS]
icp += [[], ["Code", "Sub-ICP", "Problem 1", "Problem 2", "Problem 3", "Main core problem", "Igor : OK ?", "Igor : comment"]]
icp += [list(x) + ["", ""] for x in ICP_EN]
json.dump(icp, open("../data/igor_icp_en.json", "w"), ensure_ascii=False)
print(len(rows) - 1, "modèles ·", len(ICP_EN), "sous-ICP")
