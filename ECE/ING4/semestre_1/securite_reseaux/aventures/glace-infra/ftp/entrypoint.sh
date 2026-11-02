#!/bin/sh
set -e
envsubst < /etc/vsftpd.conf.tpl > /etc/vsftpd.conf
: > /var/log/vsftpd/vsftpd.log
chown ftp:ftp /var/log/vsftpd/vsftpd.log
rsyslogd
exec vsftpd /etc/vsftpd.conf
