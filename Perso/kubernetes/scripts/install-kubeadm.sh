#!/bin/bash
set -e

# Update package lists
apt-get update

# Install required dependencies
apt-get install -y apt-transport-https ca-certificates curl gpg

# Create directory for keyrings
mkdir -p /etc/apt/keyrings

# Download Kubernetes GPG key
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key \
    | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Add Kubernetes repository
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /
EOF

# Update packages again
apt-get update

# Install Kubernetes components
apt-get install -y kubelet kubeadm kubectl

# Prevent automatic updates
apt-mark hold kubelet kubeadm kubectl

echo "Kubernetes components installed successfully."
kubectl version --client --short
