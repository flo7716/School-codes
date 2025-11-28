#!/bin/bash
set -e

# ------------------------------
# Install Kubernetes components
# ------------------------------

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
kubectl version --client

# ------------------------------
# Initialize Kubernetes cluster
# ------------------------------

# Only run kubeadm init if not already initialized
if [ ! -f /etc/kubernetes/admin.conf ]; then
    echo "Initializing Kubernetes cluster..."
    kubeadm init --pod-network-cidr=10.244.0.0/16

    # Setup kubeconfig for vagrant user
    mkdir -p /home/vagrant/.kube
    cp -i /etc/kubernetes/admin.conf /home/vagrant/.kube/config
    chown vagrant:vagrant /home/vagrant/.kube/config

    echo "Cluster initialized. kubeconfig copied to /home/vagrant/.kube/config"

    # Apply Flannel CNI network
    su - vagrant -c "kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml"
else
    echo "Kubernetes cluster is already initialized."
fi
