#!/usr/bin/env bash
# Sauvegarde logique de srv-db. Cron conseillé : 0 */4 * * * /chemin/scripts/backup.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p backups
F="backups/glace-$(date +%F-%H%M).sql.gz"
docker compose exec -T db sh -c 'mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" --single-transaction glace_db' | gzip > "$F"
sha256sum "$F" > "$F.sha256"
find backups -type f -mtime +14 -delete
echo "[+] Sauvegarde : $F"
