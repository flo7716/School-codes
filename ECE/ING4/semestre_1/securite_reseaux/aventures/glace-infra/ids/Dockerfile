FROM ubuntu:22.04
# NB : contrairement à Debian bookworm, le paquet "suricata" n'est pas disponible
# dans les dépôts Debian stable amd64 (il faudrait bookworm-backports ou compiler
# depuis les sources). Ubuntu 22.04 l'a directement dans le dépôt "universe".
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        suricata python3 && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/log/suricata
COPY forward.py /forward.py
COPY start.sh /start.sh
RUN chmod +x /start.sh /forward.py
ENTRYPOINT ["/start.sh"]
