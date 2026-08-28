import os,json,base64,time,urllib.request,urllib.parse,urllib.error
AUTH=base64.b64encode(f":{os.environ['LEMLIST_API_KEY']}".encode()).decode()
H={"Authorization":"Basic "+AUTH,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
def html(lines): return "".join("<div><br></div>" if l=="" else f"<div>{l}</div>" for l in lines)
def api(m,u,b=None):
    for a in range(5):
        try:
            rq=urllib.request.Request(u,data=json.dumps(b).encode() if b is not None else None,method=m,headers=H)
            r=urllib.request.urlopen(rq,timeout=40); return json.load(r) if r.length!=0 else {}
        except urllib.error.HTTPError as e:
            if e.code<500: print("ERR",e.code,e.read().decode()[:300]); raise
            time.sleep(2**a)
        except (urllib.error.URLError,ConnectionError): time.sleep(2**a)
    raise SystemExit("api fail")
def find(name):
    for c in api("GET","https://api.lemlist.com/api/campaigns?limit=200"):
        if c.get("name")==name: return c.get("_id") or c.get("id")
    return None

NAME="Décupler · Audit 06 · Expert-comptables (prescripteurs)"
DELAYS=[0,7,11]  # J0 / J+7 / J+18
E1=["{{salutation}},","",
 "{{accroche}}","",
 "J'ai posé la question à ChatGPT et à Perplexity la semaine dernière : « {{requeteTest}} ». Les deux citent trois cabinets. {{constatIA}}","",
 "Ce n'est pas un jugement sur votre travail — c'est un filtre technique, et la plupart des cabinets ignorent qu'il existe. Il se corrige.","",
 "Je dirige Décupler, une agence SEO à Nice. Je vous propose l'audit de {{siteWeb}}, gratuitement et sans contrepartie :","",
 "— votre visibilité réelle dans ChatGPT, Perplexity et les réponses IA de Google, requête par requête, captures à l'appui",
 "— ce qui vous manque techniquement pour être cité, classé par ordre d'impact",
 "— une feuille de route sur 90 jours, chiffrée en temps, que votre prestataire actuel peut exécuter — ou vous-même","",
 "Aucune condition. Vous le lisez, vous en faites ce que vous voulez. Je le fais parce que c'est le meilleur moyen de vous montrer comment on travaille.","",
 "Trois jours de mon côté. Vous me dites juste oui.","",
 "Nathan Fenina","Décupler — https://decupler.com","",
 "— Pour ne plus être contacté, répondez « stop »."]
E2=["{{salutation}},","",
 "Je remonte mon message, il est sûrement passé sous une pile.","",
 "Depuis, j'ai fait tourner le test sur les dix premiers cabinets du 06 : trois seulement sont cités par ChatGPT, et ce ne sont pas les trois plus gros. Je vous mets le détail dans l'audit si vous le voulez.","",
 "Si le sujet ne vous intéresse pas, dites-le-moi franchement — je ne reviendrai pas dessus.","",
 "Nathan"]
E3=["{{salutation}},","",
 "Dernier message de ma part, promis.","",
 "L'audit reste offert et le restera encore quelques semaines. Si un jour ça devient utile, mon adresse ne change pas.","",
 "Bonne continuation, et merci d'avoir lu.","",
 "Nathan"]
SUBJ1="Ce que ChatGPT répond quand on cherche un {{metier}} à {{ville}}"

# accroches rédigées depuis les notes (factuelles, spécifiques)
ACCROCHE={
 "contact@ferrua-ribes.com":"1988, 470 Promenade des Anglais, un second bureau à Mougins et 52 personnes — vous êtes un des rares cabinets du 06 à avoir passé la barre des 50.",
 "cta@trintignac.fr":"Un des plus anciens cabinets du 06, une cinquantaine de personnes au Cannet : la notoriété terrain, vous l'avez — reste à savoir si les moteurs IA la voient aussi.",
 "secretariat@fidex.fr":"Fondé en 2000, sur la zone Menton–Monaco : un secteur frontalier où « expert-comptable » se cherche de plusieurs façons, d'où ma question.",
 "accueil@fiduciaire-wilson.com":"Vous faites déjà du conseil au dirigeant, pas seulement de la tenue — c'est justement le profil de cabinet à qui la visibilité dans les IA rapporte le plus.",
 "contact@jbaudit.com":"Trois implantations : vous avez donc trois fois le problème dont je vais vous parler — un « expert-comptable Nice » qui ne remonte pas partout pareil.",
 "contact@duodecimal.fr":"Avenue Mirabeau, spécialisés dans l'accompagnement à la création d'entreprise — or vos futurs clients démarrent souvent par « à qui confier ma compta ? » posée à une IA.",
 "contact@audelia-nice.fr":"Petite structure niçoise — je vous écris en sachant que c'est vous qui lisez, pas un service com, donc je vais droit au but.",
}

import csv
F="/root/.claude/uploads/a72cc66c-6ba4-5f27-98fd-79167fbf69f8/f1465f78-leadsprescripteurs.csv"
rows=[r for r in csv.DictReader(open(F,encoding="utf-8")) if (r.get("segment") or "").strip()=="prescripteur"]

cid=find(NAME)
if not cid:
    camp=api("POST","https://api.lemlist.com/api/campaigns",{"name":NAME}); cid=camp.get("_id") or camp.get("id"); time.sleep(1)
    seqid=next(iter(api("GET",f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
    for i,(subj,lines) in enumerate([(SUBJ1,E1),("",E2),("",E3)],1):
        api("POST",f"https://api.lemlist.com/api/sequences/{seqid}/steps",
            {"type":"email","subject":subj,"message":html(lines),"delay":DELAYS[i-1],"index":i}); time.sleep(0.4)
    print("CREATED",NAME,cid)
else:
    print("exists",cid)

s=e=0
for r in rows:
    email=r["email"].strip()
    f={"salutation":r.get("salutation","Bonjour"),"companyName":r.get("companyName",""),
       "ville":r.get("ville",""),"metier":r.get("metier","expert-comptable"),
       "effectif":r.get("effectif",""),"siteWeb":r.get("siteWeb",""),
       "requeteTest":r.get("requeteTest",""),"segment":r.get("segment",""),
       "accroche":ACCROCHE.get(email,"A REMPLIR"),"constatIA":"A REMPLIR"}
    url=f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=false"
    try:
        urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(f).encode(),method="POST",headers=H),timeout=20); s+=1
    except urllib.error.HTTPError as ex:
        m=ex.read().decode()
        if "already" in m.lower(): s+=1
        else: e+=1; print("lead err",email,ex.code,m[:150])
    time.sleep=getattr(time,'sleep'); time.sleep(0.2)
print(f"IMPORT prescripteurs sent={s} err={e} cid={cid}")
