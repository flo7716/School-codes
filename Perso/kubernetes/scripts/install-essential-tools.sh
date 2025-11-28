#!/bin/bash
# This script installs essential tools required for Kubernetes setup on a Linux system.
set -e
# Update package lists
apt-get update
# Install essential tools
apt-get install -y \
    curl \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    gnupg \
    lsb-release \
    vim \
    net-tools \
    wget \
    git

#installation des dependances pour sysctl
apt-get install -y procps

#installation des dependances pour le reseau (bridge-utils et iptables)
apt-get install -y bridge-utils iptables-nft
echo "Essential tools have been installed successfully."