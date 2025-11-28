#!/bin/bash
# This script updates the kubelet configuration on a Linux system.
set -e
KUBELET_CONFIG_FILE="/var/lib/kubelet/config.yaml"
if [ ! -f "$KUBELET_CONFIG_FILE" ]; then
    echo "Kubelet configuration file not found at $KUBELET_CONFIG_FILE"
    exit 1
fi
# Backup the existing kubelet configuration file
cp "$KUBELET_CONFIG_FILE" "${KUBELET_CONFIG_FILE}.bak"
echo "Backup of kubelet configuration created at ${KUBELET_CONFIG_FILE}.bak"
# Update kubelet configuration settings
# Example: Set the cgroup driver to systemd
sed -i 's/^cgroupDriver: .*/cgroupDriver: systemd/' "$KUBELET_CONFIG_FILE"
# Example: Set the evictionHard memory threshold
if grep -q '^evictionHard:' "$KUBELET_CONFIG_FILE"; then
    sed -i 's/^evictionHard: .*/evictionHard: memory.available<500Mi/' "$KUBELET_CONFIG_FILE"
else
    echo "evictionHard: memory.available<500Mi" >> "$KUBELET_CONFIG_FILE"
fi
echo "Kubelet configuration has been updated."
# Restart kubelet to apply the new configuration
systemctl restart kubelet
echo "Kubelet service has been restarted to apply the new configuration."
echo "Kubelet configuration update script completed successfully."
