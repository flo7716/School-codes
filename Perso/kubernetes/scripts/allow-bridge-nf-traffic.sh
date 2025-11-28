#!/bin/bash
# This script enables bridge network traffic by setting the appropriate sysctl parameters.
set -e

# check if the br_netfilter module is loaded, load it if not
if ! lsmod | grep -q br_netfilter; then
    modprobe br_netfilter
    echo br_netfilter >> /etc/modules-load.d/br_netfilter.conf
    echo "br_netfilter module loaded."
else
    echo "br_netfilter module is already loaded."
fi

# check if the bridge module is loaded, load it if not
if ! lsmod | grep -q bridge; then
    modprobe bridge
    echo bridge >> /etc/modules-load.d/bridge.conf
    echo "bridge module loaded."
else
    echo "bridge module is already loaded."


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

