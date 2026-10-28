"""Séquences cold mail (format Igor : (VP + FU) x 3, délais 0/3/5/3/10/3, texte brut, aucun lien,
CTA de permission orienté « non », « stop » en PS). Jetons remplacés par segment au chargement :
[SEG] libellé du sous-ICP, [UNIT] unité (chantiers, patients…), [PROOF] preuve réelle,
[HUMOR3] option 3 drôle de la tactique 1-2-3, [ORIGIN] pays d'origine des patients (ICP 3).
Variables Lemlist {{...}} remplies par lead à l'import ; un lead dont une variable manque
ne part pas dans la campagne qui en dépend.
"""

DELAYS = [0, 3, 5, 3, 10, 3]
SIGN_FR = "Nathan Fenina, fondateur de Décupler"
SIGN_EN = "Nathan Fenina, founder of Décupler"

# H6 · B2B décideur · R.E.P.L.Y. · question ChatGPT + concurrent cité (LM1 en deux temps)
# variables : icebreaker (jamais vide), prompt, competitor
H6 = {
 "fr": [
  ("chatgpt et {{companyName}}",
   "{{icebreaker}}\n\nQuand on demande à ChatGPT « {{prompt}} », il recommande {{competitor}}, pas {{companyName}}.\n\nPour beaucoup de [SEG], c'est là que se fait la shortlist, avant même Google.\n\nJ'ai relevé 9 autres questions de ce type sur votre marché.\n\nSeriez-vous contre que je vous les montre en 15 min, avec ce qui fait citer {{competitor}} ?\n\n" + SIGN_FR + "\nPS : [PROOF]. Pas le sujet ? Répondez « stop »."),
  (None, "{{firstName}}, je me permets de remonter mon message.\n\nLa question où {{competitor}} passe devant vous est la moins grave des 10.\n\nSeriez-vous contre 15 min pour voir les autres ?\n\nNathan"),
  ("une idée pour {{companyName}}",
   "Bonjour {{firstName}},\n\nPas de rendez-vous cette fois : une action que votre équipe peut faire seule cette semaine.\n\nSur votre page la plus importante, ajoutez en haut une réponse de 2 phrases à la question que vos clients posent le plus, avec un chiffre. C'est le format que ChatGPT et Google reprennent le plus souvent.\n\nJ'ai 6 autres actions de ce type pour {{companyName}}, dans l'ordre où elles rapportent.\n\nCe serait une mauvaise idée d'en parler 15 min ?\n\nNathan\nPS : répondez « stop » et je n'écris plus."),
  (None, "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. {{companyName}} est cité partout dans ChatGPT et vous refusez des clients ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. vous avez demandé à ChatGPT de me répondre, et il a recommandé {{competitor}}.\n\nRépondez juste le numéro, que je sache quoi faire.\n\nNathan"),
  ("je clos le sujet",
   "Bonjour {{firstName}},\n\nJe ne veux pas encombrer votre boîte : c'est mon dernier message sur le sujet.\n\nSi la visibilité de {{companyName}} sur ChatGPT et Google remonte un jour dans vos priorités, j'ai un outil gratuit qui donne votre score en 2 minutes. Répondez « outil » et je vous envoie le lien.\n\nBonne continuation,\nNathan"),
  (None, "{{firstName}}, dernière chose : si quelqu'un d'autre gère ce sujet chez {{companyName}}, à qui puis-je écrire ?\n\nMerci d'avance,\nNathan"),
 ],
 "en": [
  ("chatgpt and {{companyName}}",
   "{{icebreaker}}\n\nWhen you ask ChatGPT \"{{prompt}}\", it recommends {{competitor}}, not {{companyName}}.\n\nFor many [SEG], that's where the shortlist gets made, before Google.\n\nI found 9 more questions like this in your market.\n\nWould you be against me walking you through them in 15 minutes, with what gets {{competitor}} cited?\n\n" + SIGN_EN + "\nPS: [PROOF]. Not relevant? Just reply \"stop\"."),
  (None, "{{firstName}}, bumping this up.\n\nThe question where {{competitor}} beats you is the least serious of the 10.\n\nWould you be against 15 minutes to see the others?\n\nNathan"),
  ("an idea for {{companyName}}",
   "Hi {{firstName}},\n\nNo meeting this time: one thing your team can do on its own this week.\n\nOn your most important page, add a 2-sentence answer at the top to the question your clients ask most, with a number. That's the format ChatGPT and Google quote most often.\n\nI have 6 more actions like this for {{companyName}}, ranked by what they bring in.\n\nWould it be a bad idea to go through them in 15 minutes?\n\nNathan\nPS: reply \"stop\" and I won't write again."),
  (None, "I haven't heard back, {{firstName}}, which means one of 3 things:\n\n1. {{companyName}} is cited everywhere on ChatGPT and you're turning clients away;\n2. it's not a priority and you'd like me to stop;\n3. you asked ChatGPT to reply to me, and it recommended {{competitor}}.\n\nJust reply with the number so I know what to do.\n\nNathan"),
  ("closing the loop",
   "Hi {{firstName}},\n\nI don't want to clutter your inbox, so this is my last message on this.\n\nIf {{companyName}}'s visibility on ChatGPT and Google ever becomes a priority, I have a free tool that gives you your score in 2 minutes. Reply \"tool\" and I'll send the link.\n\nAll the best,\nNathan"),
  (None, "{{firstName}}, one last thing: if someone else handles this at {{companyName}}, who should I write to?\n\nThanks,\nNathan"),
 ],
}

# H7 · B2B · AAA sans recherche (palier 3, marché principal) · permission d'envoyer une vidéo de 2 min
H7 = {
 "fr": [
  ("intro : {{companyName}} x décupler",
   "{{icebreaker}}\n\nLes entreprises que nous accompagnons reçoivent une partie de leurs demandes via Google et ChatGPT, sans publicité. [PROOF].\n\nJe pense qu'on peut faire pareil pour {{companyName}}.\n\nSeriez-vous contre que je vous envoie une vidéo de 2 minutes qui montre comment ?\n\n" + SIGN_FR + "\nPS : pas le sujet ? Répondez « stop »."),
  (None, "{{firstName}}, des nouvelles de mon dernier message ?\n\nLa vidéo fait 2 minutes, je vous l'envoie ?\n\nNathan"),
  H6["fr"][2],
  (None, "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. vos clients vous trouvent déjà tout seuls sur ChatGPT et vous n'avez plus de place ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. vous attendez que ChatGPT vous recommande de lui-même (il est un peu lent).\n\nRépondez juste le numéro, que je sache quoi faire.\n\nNathan"),
  H6["fr"][4], H6["fr"][5],
 ],
 "en": [
  ("intro: {{companyName}} x décupler",
   "{{icebreaker}}\n\nThe companies we work with get part of their inbound from Google and ChatGPT, without ads. [PROOF].\n\nI think we can do the same for {{companyName}}.\n\nWould you be against me sending a 2-minute video showing how?\n\n" + SIGN_EN + "\nPS: not relevant? Just reply \"stop\"."),
  (None, "{{firstName}}, any thoughts on my last message?\n\nThe video is 2 minutes, shall I send it?\n\nNathan"),
  H6["en"][2],
  (None, "I haven't heard back, {{firstName}}, which means one of 3 things:\n\n1. clients already find you on ChatGPT and you're fully booked;\n2. it's not a priority and you'd like me to stop;\n3. you're waiting for ChatGPT to recommend you on its own (it's a bit slow).\n\nJust reply with the number so I know what to do.\n\nNathan"),
  H6["en"][4], H6["en"][5],
 ],
}

# H8 · B2B champion · feuille de route qui le fait briller (LM4 en deux temps) · variables : keyword, volume, competitor
H8 = {
 "fr": [
  ("10 mots-clés, {{firstName}}",
   "Bonjour {{firstName}},\n\nVous gérez l'acquisition chez {{companyName}}, c'est bien ça ?\n\n« {{keyword}} » est cherché {{volume}} fois par mois, et {{competitor}} est devant vous.\n\nJ'ai listé 9 autres recherches de ce type, avec la page à créer pour chacune : de quoi présenter une feuille de route chiffrée à votre direction.\n\nCe serait une mauvaise idée que je vous les montre en 15 min ?\n\n" + SIGN_FR + "\nPS : répondez « stop » et je n'écris plus."),
  (None, "{{firstName}}, je remonte mon message.\n\n« {{keyword}} » est la plus simple des 10 à récupérer.\n\nSeriez-vous contre 15 min pour voir les autres ?\n\nNathan"),
  H6["fr"][2], H6["fr"][3], H6["fr"][4], H6["fr"][5],
 ],
 "en": [
  ("10 keywords, {{firstName}}",
   "Hi {{firstName}},\n\nYou handle acquisition at {{companyName}}, right?\n\n\"{{keyword}}\" gets {{volume}} searches a month, and {{competitor}} ranks above you.\n\nI listed 9 more searches like this, with the page to create for each: a costed roadmap you can take to leadership.\n\nWould it be a bad idea to walk you through them in 15 minutes?\n\n" + SIGN_EN + "\nPS: reply \"stop\" and I won't write again."),
  (None, "{{firstName}}, bumping this up.\n\n\"{{keyword}}\" is the easiest of the 10 to win back.\n\nWould you be against 15 minutes to see the others?\n\nNathan"),
  H6["en"][2], H6["en"][3], H6["en"][4], H6["en"][5],
 ],
}

# H9 · ICP 2/3/4 · partenariat à la performance (Nathan N22) · variable : zone (« à Lyon », « au Maroc »)
H9 = {
 "fr": [
  ("[UNIT] en plus, {{firstName}} ?",
   "Bonjour {{firstName}},\n\nVous seriez prêt à prendre 10 [UNIT] de plus par mois ?\n\nJe cherche quelques [SEG] {{zone}} pour un partenariat à la performance : on travaille votre visibilité sur Google et ChatGPT, directement sur votre site[ORIGIN], et vous payez sur les résultats.\n\n[PROOF_LINE]Seriez-vous contre que je vous explique comment ça marche ?\n\n" + SIGN_FR + "\nPS : pas intéressé ? Répondez « stop »."),
  (None, "{{firstName}}, question honnête : avez-vous l'équipe pour absorber 10 [UNIT] de plus par mois ?\n\nSi oui, je vous explique le modèle en 10 minutes.\n\nNathan"),
  ("vidéo pour {{companyName}}",
   "Bonjour {{firstName}},\n\nAutre idée, sans rendez-vous : je regarde votre site, votre fiche Google et vos avis, et je vous montre en 3 minutes de vidéo ce qui fait partir des clients chez vos concurrents.\n\nLa vidéo montre les problèmes. Pour les solutions, on en parle si vous le souhaitez.\n\nJe vous l'envoie ?\n\nNathan\nPS : répondez « stop » et je n'écris plus."),
  (None, "Je n'ai pas eu de nouvelles, {{firstName}}, ce qui veut dire une de ces 3 choses :\n\n1. votre planning est plein jusqu'en 2028 ;\n2. ce n'est pas le sujet et vous voulez que j'arrête ;\n3. [HUMOR3].\n\nRépondez juste le numéro, que je sache quoi faire.\n\nNathan"),
  ("je clos le sujet",
   "Bonjour {{firstName}},\n\nDernier message de ma part sur le sujet.\n\nSi un jour vous voulez plus de [UNIT] sans payer d'avance, répondez simplement « partenariat » et je reviens vers vous.\n\nBonne continuation,\nNathan"),
  (None, "{{firstName}}, dernière chose : si quelqu'un d'autre s'occupe des nouveaux clients chez {{companyName}}, à qui puis-je écrire ?\n\nMerci d'avance,\nNathan"),
 ],
 "en": [
  ("more [UNIT], {{firstName}}?",
   "Hi {{firstName}},\n\nWould you be open to 10 more [UNIT] a month?\n\nI'm looking for a few [SEG] {{zone}} for a performance-based partnership: we work on your visibility on Google and ChatGPT, directly on your own website[ORIGIN], and you pay on results.\n\n[PROOF_LINE]Would you be against me explaining how it works?\n\n" + SIGN_EN + "\nPS: not interested? Just reply \"stop\"."),
  (None, "{{firstName}}, honest question: does your team have room for 10 more [UNIT] a month?\n\nIf so, I can explain the model in 10 minutes.\n\nNathan"),
  ("video for {{companyName}}",
   "Hi {{firstName}},\n\nAnother idea, no meeting needed: I look at your website, your Google profile and your reviews, and show you in a 3-minute video what sends clients to your competitors.\n\nThe video shows the problems. We can talk solutions if you want.\n\nShall I send it?\n\nNathan\nPS: reply \"stop\" and I won't write again."),
  (None, "I haven't heard back, {{firstName}}, which means one of 3 things:\n\n1. you're fully booked until 2028;\n2. it's not a priority and you'd like me to stop;\n3. [HUMOR3].\n\nJust reply with the number so I know what to do.\n\nNathan"),
  ("closing the loop",
   "Hi {{firstName}},\n\nMy last message on this.\n\nIf you ever want more [UNIT] without paying upfront, just reply \"partnership\" and I'll get back to you.\n\nAll the best,\nNathan"),
  (None, "{{firstName}}, one last thing: if someone else handles new clients at {{companyName}}, who should I write to?\n\nThanks,\nNathan"),
 ],
}

# FU2 sobre (pompes funèbres : pas d'humour)
SOBER_FU2 = {
 "fr": (None, "{{firstName}}, je ne veux pas insister.\n\nSi le sujet ne vous concerne pas, un simple « non » me suffit et je n'écris plus.\n\nNathan"),
 "en": (None, "{{firstName}}, I don't want to push.\n\nIf this isn't for you, a simple \"no\" is enough and I won't write again.\n\nNathan"),
}

HUMOR3 = {
 2: ("vous êtes sur un chantier et vous lirez ce mail ce soir", "you're on a job site and will read this tonight"),
 3: ("vous êtes au bloc et vous lirez ce mail entre deux patients", "you're in surgery and will read this between two patients"),
 4: ("vous êtes en plein service et vous lirez ce mail ce soir", "you're in the middle of a shift and will read this tonight"),
}
ORIGIN = {3: (", pour les patients qui vous cherchent depuis la France, la Belgique et la Suisse",
              ", for patients searching from the UK, Ireland and the rest of Europe")}

# H12 · variante de VP1 (tous ICP) · hack Igor : concurrent classé au-dessus (objet + corps) · variables : keyword, competitor
H12_VP1 = {
 "fr": ("{{competitor}} devant vous",
        "Bonjour {{firstName}},\n\nQuand on cherche « {{keyword}} » sur Google, {{competitor}} sort avant {{companyName}}.\n\nLe premier résultat prend environ un clic sur trois : ces demandes partent chez lui.\n\nJe sais comment inverser l'ordre, et je peux vous montrer le plan en 15 minutes.\n\nSeriez-vous contre ?\n\n" + SIGN_FR + "\nPS : [PROOF]. Pas le sujet ? Répondez « stop »."),
 "en": ("{{competitor}} ahead of you",
        "Hi {{firstName}},\n\nWhen people search \"{{keyword}}\" on Google, {{competitor}} shows up before {{companyName}}.\n\nThe top result takes roughly one click in three: those enquiries go to them.\n\nI know how to flip the order, and I can show you the plan in 15 minutes.\n\nWould you be against that?\n\n" + SIGN_EN + "\nPS: [PROOF]. Not relevant? Just reply \"stop\"."),
}

# icebreakers par signal (jamais vide)
ICEBREAKER = {
 "fr": {"I1": "Félicitations pour la levée de fonds de {{companyName}}.",
        "I2": "J'ai vu que {{companyName}} recrute en marketing : j'imagine que la croissance des demandes entrantes est un objectif.",
        "I4": "Félicitations pour votre arrivée chez {{companyName}}.",
        "default": "Je regarde de près les [SEG] en ce moment.",
        "H7default": "{{firstName}}, vous pilotez la croissance de {{companyName}}, c'est bien ça ?",
        "H7I2": "{{firstName}}, j'ai vu que {{companyName}} recrute en marketing : j'imagine que la croissance des demandes entrantes est un objectif."},
 "en": {"I1": "Congrats on {{companyName}}'s funding round.",
        "I2": "I saw {{companyName}} is hiring in marketing, so I guess growing inbound is a goal.",
        "I4": "Congrats on your new role at {{companyName}}.",
        "default": "I've been looking closely at [SEG] lately.",
        "H7default": "{{firstName}}, you're driving growth at {{companyName}}, right?",
        "H7I2": "{{firstName}}, I saw {{companyName}} is hiring in marketing, so I guess growing inbound is a goal."},
}

HYPOTHESES = [
 (1, None, "I7", "LM3", "R.E.P.L.Y.", "ICP 1 · extrait de l'Opportunity Map (3 requêtes où un concurrent est cité)", "historique (25_convention_campagnes)"),
 (2, None, "I6", "LM4", "AAA", "ICP 1 · top 10 mots-clés qui font perdre des leads", "historique"),
 (3, None, "I6", "LM6", "R.E.P.L.Y.", "ICP 1 · objet « concurrent mieux placé » + vidéo 3 min", "historique"),
 (4, None, None, "LM6", "AAA", "ICP 2 · « je cherche des boîtes BTP qui veulent plus de clients » (commission)", "historique, remplacée par H9"),
 (5, None, None, None, "AAA", "ICP 2 · site offert + 97 €/mois", "historique"),
 (6, None, "I7", "LM1", "R.E.P.L.Y.", "B2B décideur · question ChatGPT où un concurrent est cité, 1 dans le mail, 9 en appel ; VP2 = 1 action offerte (LM2)", "paliers 1-2 (signal)"),
 (7, None, "I13", "LM13", "AAA", "B2B · AAA sans recherche + vidéo 2 min (marché principal)", "palier 3"),
 (8, None, "I6", "LM4", "R.E.P.L.Y.", "B2B champion · feuille de route chiffrée qui le fait briller (1 mot-clé dans le mail, 9 en appel)", "champions"),
 (9, None, "I13", "LM6", "AAA", "ICP 2/3/4 · partenariat à la performance « 10 [unités] de plus par mois ? », VP2 = vidéo 3 min des problèmes", "Nathan N22"),
 (12, None, "I6", "LM5", "R.E.P.L.Y.", "Tous ICP · variante VP1 : « {{concurrent}} devant vous » (objet + corps), hack Igor", "à tester après H6/H9"),
]
SUCCESS = "≥ 3 % de réponses humaines / prospects uniques et ≥ 20 % de positives / réponses, sur au moins 100 prospects"
