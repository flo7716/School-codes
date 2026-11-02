"""Détection d'incidents : interroge Loki toutes les INTERVAL secondes et déclenche des alarmes."""
import json, os, time, urllib.parse, urllib.request

LOKI = os.getenv("LOKI_URL", "http://loki:3100")
WEBHOOK = os.getenv("ALERT_WEBHOOK", "")
INTERVAL = int(os.getenv("INTERVAL", "15"))
COOLDOWN = int(os.getenv("COOLDOWN", "120"))

RULES = [
    {"id": "SQLI",        "sev": "HIGH",     "thr": 1,
     "desc": "Tentative d'injection SQL détectée",
     "q": 'sum(count_over_time({service="web"} |~ `(?i)(union.{1,10}select|or.{1,5}1=1|information_schema|sleep\\(|--\\s)` [1m]))'},
    {"id": "BRUTEFORCE",  "sev": "HIGH",     "thr": 5,
     "desc": "Brute force sur /login (>=5 échecs/min)",
     "q": 'sum(count_over_time({service="web"} |= `event=login_fail` [1m]))'},
    {"id": "SCAN",        "sev": "MEDIUM",   "thr": 15,
     "desc": "Scan de répertoires (>=15 erreurs 404/min)",
     "q": 'sum(count_over_time({service="web"} |= `status=404` [1m]))'},
    {"id": "WAF",         "sev": "MEDIUM",   "thr": 1,
     "desc": "Règle WAF ModSecurity déclenchée",
     "q": 'sum(count_over_time({service="proxy"} |= `ModSecurity` [1m]))'},
    {"id": "BACKUP_LEAK", "sev": "CRITICAL", "thr": 1,
     "desc": "Accès au fichier de sauvegarde sensible /backup",
     "q": 'sum(count_over_time({service="web"} |~ `path=/backup/\\S+` [1m]))'},
    {"id": "WEB_DOWN",    "sev": "CRITICAL", "thr": 1,
     "desc": "Service web sans log depuis 2 min (indisponible ?)",
     "q": 'sum(absent_over_time({service="web"}[2m]))'},
]

last_fired = {}

def query(q):
    url = f"{LOKI}/loki/api/v1/query?" + urllib.parse.urlencode({"query": q})
    with urllib.request.urlopen(url, timeout=5) as r:
        data = json.load(r)
    return sum(float(x["value"][1]) for x in data["data"]["result"])

def notify(rule, value):
    event = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": "ALERT", "rule": rule["id"],
             "severity": rule["sev"], "value": value, "desc": rule["desc"]}
    print(json.dumps(event), flush=True)            # visible dans docker logs + Loki + Grafana
    if WEBHOOK:
        body = json.dumps({"content": f"🚨 [{rule['sev']}] {rule['id']} - {rule['desc']} (valeur={value})"}).encode()
        try:
            urllib.request.urlopen(urllib.request.Request(WEBHOOK, body, {"Content-Type": "application/json"}), timeout=5)
        except Exception as e:
            print(json.dumps({"event": "WEBHOOK_ERROR", "error": str(e)}), flush=True)

print(json.dumps({"event": "ALERTER_STARTED", "rules": [r["id"] for r in RULES]}), flush=True)
time.sleep(20)  # laisse le temps à Loki de démarrer
while True:
    for rule in RULES:
        try:
            v = query(rule["q"])
        except Exception as e:
            print(json.dumps({"event": "QUERY_ERROR", "rule": rule["id"], "error": str(e)}), flush=True)
            continue
        if v >= rule["thr"] and time.time() - last_fired.get(rule["id"], 0) > COOLDOWN:
            last_fired[rule["id"]] = time.time()
            notify(rule, v)
    time.sleep(INTERVAL)
