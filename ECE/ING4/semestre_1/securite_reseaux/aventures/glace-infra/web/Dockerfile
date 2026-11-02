FROM php:8.2-apache
RUN docker-php-ext-install mysqli && \
    apt-get update && apt-get install -y --no-install-recommends rsyslog && \
    rm -rf /var/lib/apt/lists/*
COPY rsyslog-client.conf /etc/rsyslog.d/60-forward.conf
COPY apache-log.conf /etc/apache2/conf-enabled/z-log-format.conf
COPY src/ /var/www/html/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown -R www-data:www-data /var/www/html
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
