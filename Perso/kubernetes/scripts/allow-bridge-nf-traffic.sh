#!/bin/bash
# This script enables bridge network traffic by setting the appropriate sysctl parameters.
set -e

# Enable bridge-nf-call-iptables
sysctl -w net.bridge.bridge-nf-call-iptables=1

# Enable bridge-nf-call-ip6tables
sysctl -w net.bridge.bridge-nf-call-ip6tables=1

echo "Bridge network traffic settings have been updated:"
sysctl net.bridge.bridge-nf-call-iptables
sysctl net.bridge.bridge-nf-call-ip6tables

# Persist the settings across reboots
if ! grep -q "net.bridge.bridge-nf-call-iptables" /etc/sysctl.conf; then
    echo "net.bridge.bridge-nf-call-iptables = 1" >> /etc/sysctl.conf
fi

if ! grep -q "net.bridge.bridge-nf-call-ip6tables" /etc/sysctl.conf; then
    echo "net.bridge.bridge-nf-call-ip6tables = 1" >> /etc/sysctl.conf
fi

sysctl -p /etc/sysctl.conf
echo "Settings have been persisted in /etc/sysctl.conf"

