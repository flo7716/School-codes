#!/usr/bin/env bash
# Pare-feu hôte (chaîne DOCKER-USER) : seuls 80/tcp (srv-web) et 21/tcp + 21100-21110/tcp
# (srv-ftp, contrôle + PASV) sont joignables depuis l'extérieur. Tout le reste est rejeté
# et journalisé. Respecte la règle du jeu : "seuls les ports 80 et 21 sont exposés".
# Usage : sudo WAN_IF=eth0 ./host-firewall.sh
set -euo pipefail
WAN_IF="${WAN_IF:-eth0}"

iptables -N CTF-FW 2>/dev/null || iptables -F CTF-FW
iptables -A CTF-FW -m conntrack --ctstate ESTABLISHED,RELATED -j RETURN

# Anti-flood (n'empêche pas un scan nmap raisonnable, bloque le bourrinage/DoS - interdit par les règles du jeu)
iptables -A CTF-FW -p tcp -m multiport --dports 80,21,21100:21110 -m conntrack --ctstate NEW \
  -m hashlimit --hashlimit-name http-ftp --hashlimit-above 50/second --hashlimit-burst 100 \
  --hashlimit-mode srcip -j DROP

iptables -A CTF-FW -p tcp -m multiport --dports 80,21,21100:21110 -j RETURN
iptables -A CTF-FW -m limit --limit 20/min -j LOG --log-prefix "CTF-FW-DROP " --log-level 4
iptables -A CTF-FW -j DROP

iptables -C DOCKER-USER -i "$WAN_IF" -j CTF-FW 2>/dev/null || iptables -I DOCKER-USER -i "$WAN_IF" -j CTF-FW
echo "[+] Règles appliquées sur $WAN_IF (logs : journalctl -k | grep CTF-FW-DROP)"
