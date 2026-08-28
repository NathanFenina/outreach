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
            if e.code<500: print('ERR',e.code,e.read().decode()[:300]); raise
            time.sleep(2**a)
        except (urllib.error.URLError,ConnectionError): time.sleep(2**a)
    raise SystemExit("api fail")
def find(name):
    for c in api("GET","https://api.lemlist.com/api/campaigns?limit=200"):
        if c.get("name")==name: return c.get("_id") or c.get("id")
    return None

SIG=["Nathan Fenina","Agence Decupler"]; DELAYS=[0,3,4,5]
NAME="Decupler · Plombier Nantes · Site offert (mail)"
# Version live (validée Nathan) : site moderne OFFERT + offre 30 premiers + J7 en demande de référence
STEPS=[
 ("un site moderne offert pour {{companyName}} ?",
  ["bonjour,","",
   "{{avisphrase}}","",
   "je vous ai préparé un site moderne pour {{companyName}} — pensé pour signer plus de devis : demande de devis en ligne, avis Google mis en avant, rapide et impeccable sur mobile.","",
   "on l'offre en ce moment aux 30 premiers artisans de la région — une offre de lancement.","",
   "seriez-vous contre un échange de 15 min pour que je vous le partage ?","",*SIG,"",
   "PS : aucun engagement — si ça ne vous parle pas, un mot et j'arrête."]),
 ("re: un site moderne offert pour {{companyName}} ?",
  ["on cherche 30 artisans à qui offrir un site moderne ce mois-ci — et on en a déjà aidé plusieurs à décrocher plus de chantiers.","",
   "ça ne vous engage à rien : 15 min, je vous montre le site pour {{companyName}} à l'écran. s'il vous plaît, vous le gardez.","",*SIG]),
 ("pas pour vous, {{companyName}} ?",
  ["si ce n'est pas le bon moment pour {{companyName}}, aucun souci.","",
   "par contre — connaissez-vous un artisan (plombier, élec, couvreur…) à qui ça rendrait service ? je lui prépare son site aussi.","",
   "un prénom + un numéro et je m'occupe du reste.","",*SIG]),
 ("je clôture, {{companyName}} ?",
  ["sans réponse je pars du principe que : 1. ce n'est pas le moment ; 2. votre site vous convient déjà ; 3. ce n'est pas vous qui gérez ça. un mot et j'arrête.","",
   "le site pour {{companyName}} reste offert pour les 30 premiers si vous voulez le voir.","",*SIG,"",
   "PPS : un « no biz » et je vous laisse tranquille."]),
]

cid=find(NAME)
if not cid:
    camp=api("POST","https://api.lemlist.com/api/campaigns",{"name":NAME}); cid=camp.get("_id") or camp.get("id"); time.sleep(1)
    seqid=next(iter(api("GET",f"https://api.lemlist.com/api/campaigns/{cid}/sequences")))
    for i,(subj,lines) in enumerate(STEPS,1):
        api("POST",f"https://api.lemlist.com/api/sequences/{seqid}/steps",{"type":"email","subject":subj,"message":html(lines),"delay":DELAYS[i-1],"index":i}); time.sleep(0.4)
    print("CREATED",NAME,cid)
else:
    print("exists",cid)

leads=json.load(open('/tmp/claude-0/-home-user-outreach/a72cc66c-6ba4-5f27-98fd-79167fbf69f8/scratchpad/plombier_nantes_push.json'))
s=e=g=0
for l in leads:
    email=l['email'].strip(); rv=l.get('reviews')
    if rv and rv>0:
        avis=f"je vous contacte depuis votre fiche Google, d'ailleurs bravo pour les {rv} avis positifs."
    else:
        avis="je vous contacte depuis votre fiche Google — on voit tout de suite le sérieux de votre travail."
    f={"companyName":l['company'],"ville":l.get('city',''),"avisphrase":avis}
    if l.get('first_name'): f["firstName"]=l['first_name']
    url=f"https://api.lemlist.com/api/campaigns/{cid}/leads/{urllib.parse.quote(email)}?deduplicate=true"
    for a in range(4):
        try:
            urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(f).encode(),method="POST",headers=H),timeout=15); s+=1; break
        except urllib.error.HTTPError as ex:
            m=ex.read().decode()
            if "already" in m.lower(): s+=1; break
            if "graveyard" in m.lower() or "blacklist" in m.lower(): g+=1; break
            if ex.code>=500: time.sleep(2**a); continue
            e+=1; break
        except (urllib.error.URLError,ConnectionError): time.sleep(2**a)
    time.sleep(0.12)
open('/tmp/claude-0/-home-user-outreach/a72cc66c-6ba4-5f27-98fd-79167fbf69f8/scratchpad/plombier_mail_result.txt','w').write(f"cid={cid} sent={s} dup/graveyard={g} err={e} total={len(leads)}")
print(f"PLOMBIER MAIL DONE cid={cid} sent={s} graveyard={g} err={e}")
