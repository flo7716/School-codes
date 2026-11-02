FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        vsftpd rsyslog gettext-base && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /srv/ftp/pub/backup /var/log/vsftpd
COPY pub /srv/ftp/pub
COPY vsftpd.conf.tpl /etc/vsftpd.conf.tpl
COPY rsyslog-client.conf /etc/rsyslog.d/60-forward.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && \
    chown -R ftp:ftp /srv/ftp/pub/backup && chmod 755 /srv/ftp/pub/backup && \
    chmod 644 /srv/ftp/pub/backup/*
EXPOSE 21 21100-21110
ENTRYPOINT ["/entrypoint.sh"]
