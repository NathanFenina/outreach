"""Classement de la messagerie d'un domaine par son MX (DNS-over-HTTPS, gratuit) : google / microsoft / other / unknown.
Mimecast et Proofpoint sont rangés avec Microsoft (exclus, consigne Igor)."""
import json, urllib.request
from concurrent.futures import ThreadPoolExecutor


def mx(domain):
    try:
        d = json.loads(urllib.request.urlopen(f"https://dns.google/resolve?name={domain}&type=MX", timeout=20).read())
        return sorted([a["data"].split()[-1].rstrip(".").lower() for a in d.get("Answer", []) if a.get("type") == 15])
    except Exception:
        return None


def classify(hosts):
    if hosts is None: return "unknown", ""
    h = " ".join(hosts)
    if not h: return "unknown", ""
    if "google.com" in h or "googlemail.com" in h: return "google", h
    if "outlook.com" in h or "microsoft" in h or "mimecast" in h or "pphosted" in h or "proofpoint" in h: return "microsoft", h
    return "other", h


def classify_many(domains, workers=16):
    with ThreadPoolExecutor(workers) as ex:
        return dict(zip(domains, ex.map(lambda d: classify(mx(d)), domains)))
