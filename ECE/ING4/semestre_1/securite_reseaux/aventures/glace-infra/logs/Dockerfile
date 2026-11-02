FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        rsyslog fail2ban iptables && \
    rm -rf /var/lib/apt/lists/*
COPY rsyslog-server.conf /etc/rsyslog.d/10-server.conf
COPY jail.local /etc/fail2ban/jail.local
COPY filters/ /etc/fail2ban/filter.d/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && mkdir -p /var/log/remote
EXPOSE 514/udp 514/tcp
ENTRYPOINT ["/entrypoint.sh"]
