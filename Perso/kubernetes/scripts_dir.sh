#!/bin/bash

#creation dossier scripts
mkdir -p scripts

#creation scripts vides pour Vagrant
touch scripts/disable-swap.sh \
      scripts/install-essential-tools.sh \
      scripts/allow-bridge-nf-traffic.sh \
      scripts/install-containerd.sh \
      scripts/install-kubeadm.sh \
      scripts/update-kubelet-config.sh

#changement permissions pour execution
chmod +x scripts/*.sh

