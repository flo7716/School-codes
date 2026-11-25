#!/usr/bin/env bash
# Vérifie le routage, le DNS filtrant et la segmentation du labo.
set -uo pipefail
cd "$(dirname "$0")" || exit 1

# timeout : si le port 2222 répond mais que le bastion est injoignable,
# ssh attendrait la bannière indéfiniment (ConnectTimeout ne couvre pas ce cas)
SSH=(timeout 15 ssh -F ssh_config -o BatchMode=yes -o ConnectTimeout=5 lab-bastion)
pass=0; fail=0

ok()  { printf '  \033[32m✔\033[0m %s\n' "$1"; pass=$((pass+1)); }
ko()  { printf '  \033[31m✘\033[0m %s\n' "$1"; fail=$((fail+1)); }

# expect <ok|fail> <description> <commande...>
expect() {
    local want=$1 desc=$2; shift 2
    if "$@" >/dev/null 2>&1; then got=ok; else got=fail; fi
    if [[ $got == "$want" ]]; then ok "$desc"; else ko "$desc"; fi
}

lan() { docker exec lab-lan-client "$@"; }
dns_resolves() { lan dig +short +time=3 @10.10.10.10 example.com | grep -q .; }
dns_blocked()  { lan dig +short +time=3 @10.10.10.10 blocked.lab.test | grep -qx 0.0.0.0; }
nc_installed() { "${SSH[@]}" 'wget -q -T5 -O- http://10.10.10.20/status.php' | grep -q '"installed":true'; }

# shellcheck disable=SC1091
source .env
DOMAIN=${NEXTCLOUD_DOMAIN:-nextcloud.localhost}
PORT=${HTTPS_PUBLIC_PORT:-443}
TARGET=${BIND_IP:-127.0.0.1}; [[ $TARGET == 0.0.0.0 ]] && TARGET=127.0.0.1
# Depuis le laptop, comme un navigateur (CA récupérée dans le conteneur Caddy)
docker cp lab-proxy:/data/caddy/pki/authorities/local/root.crt /tmp/homelab-ca.crt >/dev/null 2>&1
https_nc() { curl -sf --max-time 5 --cacert /tmp/homelab-ca.crt --resolve "$DOMAIN:$PORT:$TARGET" "https://$DOMAIN:$PORT/status.php" | grep -q '"installed":true'; }
https_dav() { curl -s -o /dev/null -w '%{http_code}' --max-time 5 --cacert /tmp/homelab-ca.crt --resolve "$DOMAIN:$PORT:$TARGET" "https://$DOMAIN:$PORT/.well-known/caldav" | grep -q '^30[17]$'; }

echo "== Routeur"
expect ok   "règles nftables chargées"                docker exec lab-router nft list table inet labfw

echo "== Client LAN"
# "bloqué" = le vrai netcat (OpenBSD) est installé ET la connexion échoue.
# (le nc de busybox ne connaît pas -z : il échouerait toujours, à tort)
blocked() { lan sh -c 'nc -h 2>&1 | grep -q OpenBSD' && ! lan nc -z -w3 "$1" "$2"; }

if ! docker exec lab-lan-client true 2>/dev/null; then
    ko "conteneur lab-lan-client arrêté (voir : docker logs lab-lan-client)"
    echo "  Tests LAN ignorés."
else
    expect ok "accès Internet via le routeur (NAT)"     lan ping -c1 -W3 9.9.9.9
    expect ok "outils de test installés (apk via NAT)"  lan sh -c "command -v dig && command -v nc"
    expect ok "résolution DNS via Pi-hole"              dns_resolves
    docker exec lab-pihole sh -c 'pihole deny blocked.lab.test || pihole -b blocked.lab.test' >/dev/null 2>&1
    expect ok "domaine bloqué par Pi-hole -> 0.0.0.0"   dns_blocked
    expect ok "LAN -> bastion SSH refusé"               blocked 10.10.20.10 22
    expect ok "LAN -> base de données (backend) refusé" blocked 10.10.30.10 3306
    expect ok "LAN -> réseaux privés derrière le WAN"   blocked 172.31.0.1 22
fi

echo "== Bastion"
expect ok   "connexion SSH par clé via 127.0.0.1"     "${SSH[@]}" true
expect fail "connexion par mot de passe refusée"      timeout 15 ssh -F ssh_config -o BatchMode=yes -o PubkeyAuthentication=no -o PreferredAuthentications=password lab-bastion true
expect ok   "bastion -> Pi-hole (HTTP)"               "${SSH[@]}" 'wget -q -T5 -O /dev/null http://10.10.10.10/admin/'
cockpit_up() { "${SSH[@]}" "wget -q -T5 --no-check-certificate -O /dev/null https://10.10.20.1:9090/"; }
if systemctl is-active --quiet cockpit.socket 2>/dev/null; then
    expect ok "bastion -> Cockpit de l'hôte (10.10.20.1:9090)" cockpit_up
fi
expect fail "bastion -> Internet refusé"              "${SSH[@]}" 'wget -q -T5 -O /dev/null http://1.1.1.1'

printf '  … attente de Nextcloud'
for _ in $(seq 1 30); do
    nc_installed 2>/dev/null && break
    printf '.'; sleep 5
done
echo
expect ok   "bastion -> Nextcloud installé"           nc_installed

echo "== Accès utilisateur (HTTPS depuis le laptop)"
expect ok   "https://$DOMAIN répond, certificat valide" https_nc
expect ok   "redirection CalDAV/CardDAV (GNOME)"        https_dav

echo
echo "Résultat : $pass OK, $fail échec(s)"
[[ $fail -eq 0 ]]
