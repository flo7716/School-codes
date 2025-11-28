#!/bin/bash
# This scripts installs and configures containerd on a Linux system.
set -e
# Update package lists
apt-get update
# Install required packages
apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
# Update package lists again
apt-get update
# Install containerd
apt-get install -y containerd.io
# Create default configuration file for containerd
mkdir -p /etc/containerd
containerd config default > /etc/containerd/config.toml
# Restart containerd to apply the new configuration
systemctl restart containerd
# Enable containerd to start on boot
systemctl enable containerd
echo "containerd has been installed and configured successfully."