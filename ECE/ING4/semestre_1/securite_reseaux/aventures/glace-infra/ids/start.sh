#!/bin/sh
set -e
mkdir -p /var/log/suricata
exec "$@" &
SURICATA_PID=$!
python3 /forward.py &
wait $SURICATA_PID
