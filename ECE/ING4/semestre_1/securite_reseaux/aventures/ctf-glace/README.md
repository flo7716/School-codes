# 🧊 CTF "Le Chemin de la Glace" — Infra Docker (GlaceCorp)

Infrastructure Docker Compose pour le défi en 3 volets : défensif, offensif, réponse à incident.

## 1. Démarrage

```bash
cp .env.example .env            # puis changer les mots de passe
docker compose up -d --build
sudo WAN_IF=eth0 ./firewall/host-firewall.sh   # si exposé publiquement
```

- App web : http://localhost:8080
- Grafana (supervision) : http://127.0.0.1:3000 (admin / voir .env) — **non exposé** hors de l'hôte

## 2. Architecture (segmentation réseau)

```
Internet/attaquant
        │ 8080/tcp uniquement (firewall hôte, chaîne DOCKER-USER)
        ▼
  ┌───────────┐   edge      ┌───────────┐  front (internal)   ┌───────────┐
  │   proxy   │◄───────────►│    web    │◄────────────────────►│    db     │
  │ Nginx+WAF │             │  Flask    │   back (internal)    │  MariaDB  │
  │ ModSecurity              └───────────┘                      └───────────┘
  │ CRS       │                   │
  └───────────┘                   │ logs (stdout)
                                   ▼
                        ┌─────────────────────┐
                        │ monitoring (internal)│
                        │ promtail → loki       │
                        └─────────────────────┘
                                   │
                              mgmt │
                                   ▼
                     grafana (127.0.0.1) + alerter → webhook
```

**Principes appliqués :**
- 5 réseaux Docker isolés ; `front`, `back` et `monitoring` sont `internal: true` (pas de sortie Internet, pas d'accès direct depuis l'extérieur).
- Seul `proxy` est publié (`8080`), seul `grafana` est publié mais bindé à `127.0.0.1` (accès hôte uniquement, jamais réseau).
- `db` n'est joignable que depuis `web`, sur le réseau `back`.
- Conteneurs non-root (`user: 10001:10001`), `cap_drop: ALL` (+ capacités minimales pour MariaDB), `no-new-privileges`, `read_only: true` + `tmpfs` pour `web` et `alerter`.
- Compte MySQL applicatif en **lecture seule** (`GRANT SELECT` uniquement, `init.sql`).
- Limites CPU/RAM par service, `restart: unless-stopped`.
- Pare-feu hôte (`firewall/host-firewall.sh`) : seul 8080/tcp entrant, rate-limiting anti-flood, journalisation des paquets rejetés (`CTF-FW-DROP`).
- Journalisation centralisée : chaque requête HTTP est loguée (IP, méthode, chemin, statut, UA) → Promtail → Loki → Grafana. Un dashboard **"Security Overview"** est provisionné.
- Monitoring/alerting : service `alerter` qui interroge Loki en continu et détecte : injection SQL, brute force, scan de répertoires, déclenchements WAF, accès au fichier de sauvegarde sensible, indisponibilité du service web. Alertes envoyées en log structuré + webhook Discord/Slack optionnel (`ALERT_WEBHOOK`).
- En-têtes de sécurité HTTP (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`), bannière serveur masquée.

## 3. Vulnérabilités volontaires (documentées)

| # | Vulnérabilité | Localisation | CWE | Flag |
|---|---|---|---|---|
| 1 | Injection SQL (concaténation de chaînes, pas de requêtes préparées) | `web/app.py` routes `/search` et `/login` | CWE-89 | `flag{ic3_p4th_sql1_fr0z3n_d4t4}` (table `secrets` en base, accessible via l'injection) |
| 2 | Fichier de sauvegarde exposé publiquement (`/backup/db_config.bak`), référencé dans `robots.txt` | `web/backup/db_config.bak` | CWE-530 / CWE-200 | `flag{b4ckup_l34k_n0_ic3_h3r3}` (en commentaire dans le fichier) |

Vulnérabilités **intentionnelles et cantonnées** à la couche applicative `web` — le reste de l'infra (réseaux internes, moindre privilège DB, firewall) reste durci pour que l'exercice porte uniquement sur ces deux points d'entrée.

Le WAF ModSecurity est volontairement en mode `DetectionOnly` : il journalise et alerte (voir `alerter`) sans bloquer, afin que l'exploitation reste possible pour le volet offensif tout en générant des preuves de détection pour le volet "Réponse à incident".

## 4. Pour le volet offensif (Chemin du Feu)

Pistes attendues (sans tout dévoiler ici) :
- Reconnaissance : `nmap -sV -p- localhost`, `gobuster dir -u http://localhost:8080 -w <wordlist>`.
- `robots.txt` indique un chemin intéressant.
- Le paramètre `q` de `/search` et les champs `u`/`p` de `/login` ne sont pas assainis.
- Script de démonstration (reconnaissance interne) : `scripts/simulate-attack.sh http://localhost:8080`.

## 5. Pour le volet réponse à incident (Chemin du Guerrier)

Voir `docs/plan-continuite-reprise.md` (PCA/PRA, aligné ISO 22301) et `docs/alarmes.md` (règles de détection, procédure d'escalade).

## 6. Limites connues / risques acceptés

- `promtail` monte `/var/run/docker.sock` en lecture seule pour découvrir les conteneurs : c'est un accès sensible à l'hôte Docker, limité au strict nécessaire (RO) et au réseau `monitoring` isolé ; en production on préférerait une solution de collecte sans accès au socket (ex. driver de log distant).
- Le WAF en `DetectionOnly` est un choix pédagogique pour laisser le challenge offensif réalisable ; à passer en `On` en production.
- Secrets gérés via `.env` (non versionné) — en production, utiliser un coffre-fort (Vault, Docker secrets, etc.).
