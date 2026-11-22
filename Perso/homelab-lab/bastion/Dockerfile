FROM alpine:3.22
# Le sed rend le compte "admin" déverrouillé mais sans mot de passe
# (un compte verrouillé "!" est refusé par sshd, même avec une clé).
RUN apk add --no-cache openssh-server \
 && adduser -D -s /bin/sh admin \
 && sed -i 's/^admin:!/admin:*/' /etc/shadow \
 && install -d -o admin -g admin -m 700 /home/admin/.ssh \
 && install -d -m 700 /etc/ssh/hostkeys
COPY sshd_config /etc/ssh/sshd_config
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
