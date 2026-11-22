#!/bin/sh
set -eu

# Clé d'hôte persistante (volume) : pas d'alerte "host key changed" à chaque rebuild
if [ ! -f /etc/ssh/hostkeys/ssh_host_ed25519_key ]; then
    ssh-keygen -q -t ed25519 -N '' -f /etc/ssh/hostkeys/ssh_host_ed25519_key
fi

# Copie de la clé publique avec le bon propriétaire (StrictModes)
install -o admin -g admin -m 600 /run/authorized_keys /home/admin/.ssh/authorized_keys

/usr/sbin/sshd -t
exec /usr/sbin/sshd -D -e
