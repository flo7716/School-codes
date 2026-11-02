#!/usr/bin/env bash
# Restauration : ./scripts/restore.sh backups/glace-AAAA-MM-JJ-HHMM.sql.gz
set -euo pipefail
cd "$(dirname "$0")/.."
F="${1:?fichier de sauvegarde requis}"
sha256sum -c "$F.sha256"
docker compose up -d db
until docker compose exec -T db mysqladmin ping -h localhost >/dev/null 2>&1; do sleep 2; done
gunzip -c "$F" | docker compose exec -T db sh -c 'mysql -uroot -p"$MYSQL_ROOT_PASSWORD" glace_db'
docker compose up -d
echo "[+] Restauration terminée"
