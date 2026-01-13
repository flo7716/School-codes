# Dockerfile for Kali Linux with essential pentest and forensic tools
FROM kalilinux/kali-rolling


# Install essential packages in one layer, clean up afterwards to reduce image size
RUN apt-get update
RUN apt-get install -y ca-certificates apt-transport-https gnupg wget curl nano

# pentest & forensic tools
RUN apt-get install -y nmap wireshark john hydra sqlmap metasploit-framework aircrack-ng binwalk autopsy sleuthkit gdb strace ltrace tcpdump nikto dirb burpsuite zaproxy hashcat steghide foremost exiftool hexedit

# Set nmap to run on this Docker container without root privileges
RUN setcap cap_net_raw,cap_net_admin=eip /usr/bin/nmap



# Set default command to bash
CMD ["/bin/bash"]
