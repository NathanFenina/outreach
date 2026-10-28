"""Recherche gratuite dans la base People / Companies de Lemlist (quota de recherches : champ « limitation »)."""
import base64, json, os, time, urllib.request
from icp_catalog import COUNTRIES
H = {"Authorization": "Basic " + base64.b64encode((":" + os.environ["LEMLIST_API"]).encode()).decode(), "Content-Type": "application/json"}
CNAME = {c: n for c, n, *_ in COUNTRIES}
BIG = ["11-50", "51-200", "201-500", "501-1000"]
SMALL = ["1-10"]


def f(fid, values, out=None):
    return {"filterId": fid, "in": values, "out": out or []}


def search(kind, filters, page=1, size=100):
    body = json.dumps({"filters": filters, "page": page, "size": size}).encode()
    for i in range(5):
        try:
            r = urllib.request.urlopen(urllib.request.Request(f"https://api.lemlist.com/api/database/{kind}", data=body, headers=H, method="POST"), timeout=120)
            return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500: time.sleep(3 * (i + 1)); continue
            raise RuntimeError(e.read().decode()[:300])
    raise RuntimeError("lemlist db: échec")


def seg_filters(s, countries, headcount):
    kws = s["kw_fr"] + s["kw_en"]
    return [f("currentCompanyCountry", [CNAME[c] for c in countries]), f("keywordInCompany", kws), f("currentCompanyHeadcount", headcount)]
