# 🧊 CTF "Le Chemin de la Glace" — Infrastructure Docker

Implémente exactement la topologie décrite dans *Le Chemin de la Glace – Documentation des
vulnérabilités et des flags* (@ila) : les deux vulnérabilités, les deux flags et le plan
d'adressage y sont détaillés ; ce dépôt construit l'infrastructure qui les porte.

## 1. Démarrage

```bash
cp .env.example .env          # DB_PASSWORD doit rester Gl4c3_App_2026 (cf. .env.example)
# PASV_ADDRESS=<IP LAN ou publique de la machine hôte> si vous testez le FTP en PASV
docker compose up -d --build
sudo WAN_IF=eth0 ./firewall/host-firewall.sh    # si l'infra est exposée hors du poste local
```

- Web : `http://localhost/` (ou `recherche.php?q=...`)
- FTP : `ftp://localhost/` (anonyme)

## 2. Topologie (conforme au document)

| Machine | Zone | IP | Service | Rôle |
|---|---|---|---|---|
| srv-ftp | DMZ | 10.0.10.20 | vsftpd, port 21 | Vulnérabilité 1 + flag 1 |
| srv-web | DMZ | 10.0.10.10 | Apache + PHP, port 80 | Vulnérabilité 2 (point d'entrée) |
| srv-db | LAN | 10.0.20.10 | MySQL, port 3306 | Flag 2 (cible finale) |
| srv-logs | ADMIN | 10.0.30.10x | rsyslog, Suricata, fail2ban | Détection |

```
Internet / attaquant
     │  80, 21 (+21100-21110 PASV) uniquement — firewall hôte (DOCKER-USER)
     ▼
 ┌─────────┐          dmz           ┌─────────┐
 │ srv-ftp │◄─────────────────────► │ srv-web │
 └────┬────┘                        └────┬────┘
      │ admin (one-way : logs)           │ lan (SEUL flux autorisé vers srv-db)
      │                                  ▼
      │                            ┌─────────┐
      │                            │ srv-db  │   (LAN, aucun accès direct depuis Internet)
      │                            └─────────┘
      ▼
 ┌──────────┐   admin (logs)
 │ srv-logs │◄───────────────────────────────── ids-ftp / ids-web (netns partagé)
 └──────────┘
```

- `dmz` : seul réseau joignable depuis l'extérieur (ports 80/21 publiés).
- `lan` : `internal: true` — relie uniquement `srv-web` à `srv-db`. C'est le flux que la
  vulnérabilité 2 détourne : l'attaquant ne touche jamais le LAN, c'est `srv-web` qui
  interroge la base pour lui.
- `admin` : `internal: true` — `srv-web` et `srv-ftp` y expédient leurs logs vers
  `srv-logs` (rsyslog) ; les sondes IDS `ids-ftp`/`ids-web` (voir §4) y relaient aussi
  leurs alertes.

## 3. Les deux vulnérabilités (résumé technique — détails et exploitation dans la
documentation fournie)

| # | Vulnérabilité | Fichier | Flag |
|---|---|---|---|
| 1 | FTP anonyme (`anonymous_enable=YES`) exposant `pub/backup/config.php.bak` | `ftp/vsftpd.conf.tpl`, `ftp/pub/backup/config.php.bak` | `flag{ftp_4n0nym0us_l34k}` |
| 2 | Injection SQL par concaténation dans `recherche.php`, aggravée par un compte `glace_app` ayant `SELECT` sur toute la base | `web/src/recherche.php`, `db/init.sql` | `flag{sql1_d4ns_l4_gl4c3}` |

`login.php` est volontairement **saine** (requêtes préparées) : elle sert uniquement de
cible réaliste pour démontrer la détection de brute force par fail2ban, sans ouvrir une
troisième vulnérabilité non documentée.

## 4. Détection (IDS + logs centralisés + fail2ban)

- Deux sondes **Suricata** (`ids-ftp`, `ids-web`) partagent le namespace réseau de
  `srv-ftp`/`srv-web` (`network_mode: "service:..."`) pour avoir une **visibilité réelle**
  du trafic reçu par chaque machine DMZ — un simple rattachement au réseau `dmz` ne
  suffirait pas (un bridge Docker se comporte comme un switch : pas de sniffing du trafic
  unicast d'un tiers). Règles personnalisées : `ids/custom.rules`.
- **rsyslog** centralise les logs de `srv-ftp` et `srv-web` (et les alertes Suricata) sur
  `srv-logs`, rangés par hôte dans `/var/log/remote/<hôte>/`.
- **fail2ban**, sur `srv-logs`, surveille ces logs centralisés (scan FTP répété, tentative
  d'injection SQL, brute force sur `/login.php`).

Détail des règles et de leurs limites : `docs/alarmes.md`. Plan de réponse à incident :
`docs/plan-continuite-reprise.md`.

## 5. Scripts

- `scripts/simulate-attack.sh <cible>` : rejoue la chaîne complète (nmap → FTP anonyme →
  injection SQL) et affiche les deux flags — utile pour valider l'infra et déclencher les
  alertes de test.
- `scripts/backup.sh` / `scripts/restore.sh` : sauvegarde/restauration de `srv-db`.
- `firewall/host-firewall.sh` : n'autorise que 80/tcp et 21+21100-21110/tcp en entrée,
  journalise le reste (conforme à la règle du jeu "seuls les ports 80 et 21 sont
  exposés").

## 6. Limites connues / risques acceptés

- La plage de ports PASV FTP (21100-21110) est publiée en plus du 21 : c'est une nécessité
  technique du mode passif derrière une NAT Docker, documentée comme faisant partie du
  même service FTP (et non une 3e porte d'entrée).
- fail2ban tournant **dans un conteneur** ne peut pas modifier le pare-feu de l'hôte : ses
  bannissements sont, dans cette démo, journalisés mais pas appliqués réseau (voir
  `docs/alarmes.md` §limites). Une version production ferait tourner fail2ban côté hôte.
- Secrets gérés via `.env` (non versionné). Le mot de passe `glace_app` est volontairement
  identique au secret fuité par la vulnérabilité 1 : c'est le fil rouge du CTF, pas un
  oubli.
