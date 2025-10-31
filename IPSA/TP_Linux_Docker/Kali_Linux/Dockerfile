## Dockerfile for Kali Linux with essential pentest and forensic tools

# Use the official Kali Linux base image
FROM kalilinux/kali-rolling

# Update and upgrade the system
RUN apt-get update && apt-get -y upgrade

# Install essential pentest and forensic tools
RUN apt-get install -y \
    nmap \
    wireshark \
    john \
    hydra \
    sqlmap \
    metasploit-framework \
    aircrack-ng \
    binwalk \
    volatility \
    autopsy \
    sleuthkit \
    gdb \
    strace \
    ltrace \
    tcpdump \
    netcat \
    nikto \
    dirb \
    burpsuite \
    zaproxy \
    hashcat \
    steghide \
    foremost \
    exiftool \
    hexedit \
    && apt-get clean

# Set the default command to bash
CMD ["/bin/bash"]
# End of Dockerfile 