#!/bin/bash

# Vagrant + VirtualBox setup for a Linux Kubernetes cluster
# This script sets up a basic Kubernetes cluster using Vagrant and VirtualBox.

# Detect OS and install necessary packages (using the appropriate package manager)
# check if the OS is Debian-based or RedHat-based
if [ -f /etc/debian_version ]; then
    PACKAGE_MANAGER="apt-get"
    UPDATE_CMD="sudo $PACKAGE_MANAGER update"
    INSTALL_CMD="sudo $PACKAGE_MANAGER install -y"
elif [ -f /etc/redhat-release ]; then
    PACKAGE_MANAGER="dnf"
    UPDATE_CMD="sudo $PACKAGE_MANAGER update -y"
    INSTALL_CMD="sudo $PACKAGE_MANAGER install -y"
else
    echo "Unsupported OS. This script supports Debian-based and RedHat-based distributions."
    exit 1
fi

# Install Vagrant and VirtualBox
$UPDATE_CMD
$INSTALL_CMD vagrant virtualbox
