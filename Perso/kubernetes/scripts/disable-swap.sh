#!/bin/bash
# This script disables swap on the system to meet Kubernetes requirements.
set -e
# Disable swap immediately
swapoff -a
echo "Swap has been disabled."

# Comment out any swap entries in /etc/fstab to prevent swap from being enabled on reboot
sed -i.bak '/\s*swap\s*/s/^\(.*\)$/#\1/' /etc/fstab
echo "Swap entries in /etc/fstab have been commented out."

echo "Swap has been successfully disabled and will not be re-enabled on reboot."