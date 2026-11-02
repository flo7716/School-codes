import os
from urllib.parse import unquote
import pymysql
from flask import Flask, request, render_template_string, send_from_directory, abort, Response

app = Flask(__name__)

LAYOUT = """
<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>GlaceCorp</title>
<style>body{font-family:Calibri,Arial;max-width:760px;margin:40px auto;background:#0b1e33;color:#e8f1fa}
a{color:#7cc4ff}input{padding:6px}button{padding:6px 12px}.box{background:#12304f;padding:16px;border-radius:8px;margin:12px 0}</style>
</head><body><h1>❄️ GlaceCorp - Catalogue</h1>
<p><a href="/">Accueil</a> | <a href="/login">Connexion</a></p>{{ body|safe }}</body></html>
"""

def db():
    return pymysql.connect(
        host=os.environ["DB_HOST"], user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"], database=os.environ["DB_NAME"],
        connect_timeout=3)

def client_ip():
    return request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()

def page(body):
    return render_template_string(LAYOUT, body=body)

@app.after_request
def log_and_headers(resp):
    path = unquote(request.full_path.rstrip("?"))
    ua = request.headers.get("User-Agent", "-").replace('"', "'")
    print(f'event=http ip={client_ip()} method={request.method} path={path} status={resp.status_code} ua="{ua}"', flush=True)
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "no-referrer"
    resp.headers.pop("Server", None)
    return resp

@app.route("/health")
def health():
    return "ok"

@app.route("/")
def index():
    return page("""<div class="box"><form action="/search">
    <input name="q" placeholder="Rechercher un produit"><button>Chercher</button></form></div>""")

# ---- VULNÉRABILITÉ n°1 : injection SQL (requête construite par concaténation) ----
@app.route("/search")
def search():
    q = request.args.get("q", "")
    sql = f"SELECT name, description FROM products WHERE name LIKE '%{q}%'"   # VOLONTAIREMENT VULNÉRABLE
    try:
        with db() as conn, conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
    except Exception as e:
        return page(f"<div class='box'>Erreur SQL : {e}</div>"), 500          # fuite d'erreur volontaire
    items = "".join(f"<div class='box'><b>{n}</b><br>{d}</div>" for n, d in rows) or "<p>Aucun résultat.</p>"
    return page(items)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = """<div class="box"><form method="post">
    <input name="u" placeholder="Utilisateur"> <input name="p" type="password" placeholder="Mot de passe">
    <button>Connexion</button></form></div>"""
    if request.method == "GET":
        return page(form)
    u, p = request.form.get("u", ""), request.form.get("p", "")
    sql = f"SELECT id, username FROM users WHERE username='{u}' AND password='{p}'"   # VOLONTAIREMENT VULNÉRABLE
    try:
        with db() as conn, conn.cursor() as cur:
            cur.execute(sql)
            row = cur.fetchone()
    except Exception:
        return page(form + "<p>Erreur serveur.</p>"), 500
    if row:
        print(f"event=login_ok ip={client_ip()} user={row[1]}", flush=True)
        return page(f"<div class='box'>Bienvenue {row[1]} 👋</div>")
    print(f"event=login_fail ip={client_ip()}", flush=True)
    return page(form + "<p>Identifiants invalides.</p>"), 401

# ---- VULNÉRABILITÉ n°2 : fichier de sauvegarde exposé et référencé dans robots.txt ----
@app.route("/robots.txt")
def robots():
    return Response("User-agent: *\nDisallow: /backup/\n", mimetype="text/plain")

@app.route("/backup/")
def backup_index():
    return page("<div class='box'>Index of /backup<br><a href='/backup/db_config.bak'>db_config.bak</a></div>")

@app.route("/backup/<path:name>")
def backup_file(name):
    return send_from_directory("backup", name, mimetype="text/plain")
