#!/bin/sh
# Routeur / pare-feu du labo : NAT vers le WAN, DNAT SSH vers le bastion,
# filtrage inter-zones. Politique par défaut : tout est refusé.
set -eu

# Docker ne garantit pas l'ordre eth0/eth1/eth2 : on retrouve chaque
# interface à partir de son adresse IP.
iface_for() {
    ip -o -4 addr show | awk -v ip="$1" '{ split($4, a, "/"); if (a[1] == ip) { print $2; exit } }'
}

WAN_IF=$(iface_for "$WAN_IP")
LAN_IF=$(iface_for "$LAN_IP")
ADMIN_IF=$(iface_for "$ADMIN_IP")

for v in WAN_IF LAN_IF ADMIN_IF; do
    eval "val=\${$v}"
    if [ -z "$val" ]; then
        echo "ERREUR : interface introuvable pour $v" >&2
        ip -o -4 addr show >&2
        exit 1
    fi
done
echo "Interfaces : WAN=$WAN_IF  LAN=$LAN_IF  ADMIN=$ADMIN_IF"

# Le routeur est sur 3 réseaux Docker : on force la sortie par le WAN
ip route replace default via "$WAN_GW" dev "$WAN_IF"
echo "Route par défaut : $(ip route show default)"

# On ne fait PAS de "flush ruleset" : Docker a ses propres règles dans ce
# namespace (DNS interne 127.0.0.11). On gère uniquement nos tables.
nft delete table inet labfw 2>/dev/null || true
nft delete table ip labnat 2>/dev/null || true

nft -f - <<EOF
table inet labfw {
    chain input {
        type filter hook input priority filter; policy drop;
        iif "lo" accept
        ct state established,related accept
        ct state invalid drop
        ip protocol icmp accept
        counter comment "input refusé"
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
        ct state established,related accept
        ct state invalid drop

        # LAN -> Internet, mais pas vers les réseaux privés derrière le WAN
        # (réseau de ton laptop / box, autres réseaux Docker)
        iifname "$LAN_IF" oifname "$WAN_IF" ip daddr { 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 } counter drop
        iifname "$LAN_IF" oifname "$WAN_IF" accept

        # Entrée SSH publiée -> bastion (après DNAT)
        iifname "$WAN_IF" oifname "$ADMIN_IF" ip daddr $BASTION_IP tcp dport 22 ct status dnat accept

        # Entrée HTTPS publiée -> reverse proxy (après DNAT)
        iifname "$WAN_IF" oifname "$LAN_IF" ip daddr $PROXY_IP tcp dport 443 ct status dnat accept

        # Bastion -> services du LAN (SSH, HTTP, HTTPS, ping)
        iifname "$ADMIN_IF" oifname "$LAN_IF" ip saddr $BASTION_IP tcp dport { 22, 80, 443 } accept
        iifname "$ADMIN_IF" oifname "$LAN_IF" ip saddr $BASTION_IP icmp type echo-request accept

        # Tout le reste : refusé (LAN -> admin, admin -> Internet, ...)
        counter comment "forward refusé"
    }
}

table ip labnat {
    chain prerouting {
        type nat hook prerouting priority dstnat; policy accept;
        iifname "$WAN_IF" tcp dport $SSH_DNAT_PORT dnat to $BASTION_IP:22
        iifname "$WAN_IF" tcp dport 443 dnat to $PROXY_IP:443
    }

    chain postrouting {
        type nat hook postrouting priority srcnat; policy accept;
        oifname "$WAN_IF" masquerade
        # Connexions entrantes (DNAT) : on remplace la source WAN par l'IP du
        # routeur. Sinon l'hôte applique sa règle MASQUERADE Docker du réseau
        # WAN à ces paquets quand ils traversent le bridge admin/lan, et la
        # réponse du bastion/proxy part vers la mauvaise adresse.
        iifname "$WAN_IF" oifname { "$ADMIN_IF", "$LAN_IF" } masquerade
        # Les services du LAN n'ont pas de route vers le réseau admin :
        # on masque l'IP du bastion derrière l'IP LAN du routeur.
        ip saddr $ADMIN_NET oifname "$LAN_IF" masquerade
    }
}
EOF

echo "Règles nftables chargées :"
nft list table inet labfw
nft list table ip labnat

exec sleep infinity
