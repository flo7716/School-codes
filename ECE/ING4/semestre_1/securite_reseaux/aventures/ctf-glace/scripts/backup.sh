#!/usr/bin/env bash
# Sauvegarde logique de la base + rétention 14 jours. Cron : 0 */4 * * * /chemin/scripts/backup.sh
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p backups
F="backups/glace-$(date +%F-%H%M).sql.gz"
docker compose exec -T db sh -c 'mariadb-dump -uroot -p"$MARIADB_ROOT_PASSWORD" --single-transaction glace' | gzip > "$F"
sha256sum "$F" > "$F.sha256"
find backups -type f -mtime +14 -delete
echo "[+] Sauvegarde : $F"
