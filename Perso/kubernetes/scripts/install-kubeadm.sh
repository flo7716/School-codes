#!/bin/bash
# This script installs kubeadm, kubelet, and kubectl on a Linux system.
set -e
# Update package lists
apt-get update
# Install required packages
apt-get install -y apt-transport-https ca-certificates curl
# Add Kubernetes GPG key
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
# Add Kubernetes apt repository
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
# Update package lists again
apt-get update
# Install kubeadm, kubelet, and kubectl
apt-get install -y kubelet kubeadm kubectl
# Hold the packages at their current version to prevent automatic updates
apt-mark hold kubelet kubeadm kubectl
echo "kubeadm, kubelet, and kubectl have been installed successfully."  
kubectl version --client --short
echo "kubectl client version displayed above."