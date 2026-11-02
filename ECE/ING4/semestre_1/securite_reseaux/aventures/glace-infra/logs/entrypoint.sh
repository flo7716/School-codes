#!/bin/sh
set -e
mkdir -p /var/log/remote
touch /var/log/fail2ban.log
rsyslogd
sleep 2
fail2ban-server -xf start &
wait
