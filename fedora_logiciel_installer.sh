#!/bin/bash

# This script is used to install software on Fedora Linux systems (VS Code, Docker Desktop, Spotify, Keepass and ProtonVPN)

# Update the system
echo "Updating the system..."
sudo dnf update -y

# Install GNOME Tweaks and Extensions
echo "Installing GNOME Tweaks and Extensions..."
sudo dnf install gnome-tweaks gnome-extensions-app -y

# Activate sysrq
echo "Activating sysrq..."
sudo sysctl -w kernel.sysrq=1

# Install VS Code
echo "Installing Visual Studio Code..."
wget https://code.visualstudio.com/sha/download?build=stable&os=linux-rpm-x64 -O vscode.rpm
sudo dnf install ./vscode.rpm -y


# Install Docker Desktop (first install Docker Engine and add user to Docker group)
echo "Installing Docker Engine..."
sudo dnf config-manager addrepo --from-repofile https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker

echo "Adding user to Docker group..."
sudo usermod -aG docker $USER
newgrp docker

echo "Installing Docker Desktop..."
wget https://desktop.docker.com/linux/main/amd64/docker-desktop-x86_64.rpm
sudo dnf install ./docker-desktop-x86_64.rpm -y

# enable auth for Docker Desktop
echo "Enabling authentication for Docker Desktop..."
gpg --generate-key
GPG_ID=$(gpg --list-secret-keys --keyid-format LONG | grep sec | awk '{print $2}' | cut -d'/' -f2)
pass init $GPG_ID


echo "Testing Docker installation..."
docker run hello-world

# Install Keepass
echo "Installing Keepass..."
sudo dnf install keepass -y

# Ajout RPM Fusion pour spotify et codecs
echo "Adding RPM Fusion repositories for Spotify and codecs..."
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm -y
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y


# Install Spotify via RPM Fusion repository
echo "Installing Spotify..."
sudo dnf install lpf-spotify-client -y

# Install codecs for media playback, video and audio
echo "Installing codecs for media playback..."
sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin -y
sudo dnf groupupdate sound-and-video -y 

# Install ProtonVPN
echo "Installing ProtonVPN..."
wget "https://repo.protonvpn.com/fedora-$(cat /etc/fedora-release | cut -d' ' -f 3)-stable/protonvpn-stable-release/protonvpn-stable-release-1.0.4-1.noarch.rpm"
sudo dnf install ./protonvpn-stable-release-1.0.4-1.noarch.rpm && sudo dnf check-update --refresh 
sudo dnf install proton-vpn-gnome-desktop
sudo dnf install libappindicator-gtk3 gnome-shell-extension-appindicator gnome-extensions-app


# Install Anaconda
echo "Installing Anaconda..."
wget https://repo.anaconda.com/archive/Anaconda3-2026.07-1-Linux-x86_64.sh
bash Anaconda3-2026.07-1-Linux-x86_64.sh

# Create a new conda environment for Python 3.12
echo "Creating a new conda environment for Python 3.12..."
conda create -n jpn_florian python=3.12 -y
conda activate jpn_florian
pip install numpy pandas matplotlib seaborn scikit-learn jupyterlab ipynb
conda deactivate
