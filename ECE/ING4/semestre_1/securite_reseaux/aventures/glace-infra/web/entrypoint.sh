#!/bin/sh
set -e
mkdir -p /var/log/apache2
: > /var/log/apache2/access.log
: > /var/log/apache2/error.log
cat > /var/www/html/db.php <<PHP
<?php
\$DB_HOST = getenv('DB_HOST');
\$DB_NAME = getenv('DB_NAME');
\$DB_USER = getenv('DB_USER');
\$DB_PASSWORD = getenv('DB_PASSWORD');
PHP
rsyslogd
exec apache2-foreground
