#!/bin/bash

# Verification installation ClamAV
if ! command -v clamscan &> /dev/null; then
    echo "ClamAV is not installed. Installing ClamAV..."
    sudo apt-get update
    sudo apt-get install -y clamav clamav-daemon
    sudo freshclam
    sudo systemctl enable clamav-freshclam
else
    echo "ClamAV is already installed."
fi 


# Update ClamAV database
echo "Updating ClamAV database..."
sudo systemctl stop clamav-freshclam
sudo freshclam
if [ $? -ne 0 ]; then
    echo "Failed to update ClamAV database."
    exit 1
fi
sudo systemctl start clamav-freshclam

# Scan the system
echo "Scanning the system with ClamAV..."
sudo clamscan -r --bell -i /
if [ $? -ne 0 ]; then  
    echo "ClamAV scan failed."
    exit 1
fi

echo "ClamAV scan completed successfully."