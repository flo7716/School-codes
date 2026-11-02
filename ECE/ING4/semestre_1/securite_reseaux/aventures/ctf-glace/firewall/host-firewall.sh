#!/usr/bin/env bash
# Pare-feu hôte (chaîne DOCKER-USER) : seul le port 8080/tcp est joignable depuis l'extérieur,
# avec limitation de débit et journalisation des paquets rejetés.
# Usage : sudo WAN_IF=eth0 ./host-firewall.sh
set -euo pipefail
WAN_IF="${WAN_IF:-eth0}"

iptables -N CTF-FW 2>/dev/null || iptables -F CTF-FW
iptables -A CTF-FW -m conntrack --ctstate ESTABLISHED,RELATED -j RETURN
# anti-flood : max 30 nouvelles connexions/s par IP source (burst 60)
iptables -A CTF-FW -p tcp --dport 8080 -m conntrack --ctstate NEW \
  -m hashlimit --hashlimit-name http --hashlimit-above 30/second --hashlimit-burst 60 \
  --hashlimit-mode srcip -j DROP
iptables -A CTF-FW -p tcp --dport 8080 -j RETURN
iptables -A CTF-FW -m limit --limit 10/min -j LOG --log-prefix "CTF-FW-DROP " --log-level 4
iptables -A CTF-FW -j DROP

iptables -C DOCKER-USER -i "$WAN_IF" -j CTF-FW 2>/dev/null || iptables -I DOCKER-USER -i "$WAN_IF" -j CTF-FW
echo "[+] Règles appliquées sur $WAN_IF (logs : journalctl -k | grep CTF-FW-DROP)"
