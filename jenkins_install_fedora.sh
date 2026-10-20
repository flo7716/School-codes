#!/bin/bash

sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/rpm-stable/jenkins.repo
sudo dnf upgrade
# Add required dependencies for the Jenkins package
sudo dnf install fontconfig java-21-openjdk
sudo dnf install jenkins
sudo systemctl daemon-reload


sudo systemctl enable jenkins --now