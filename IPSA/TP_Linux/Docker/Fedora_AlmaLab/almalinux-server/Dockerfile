FROM almalinux:9

RUN dnf -y update && \
    dnf -y install \
    freeipa-server \
    freeipa-server-dns \
    openssh-server \
    sudo \
    nano \
    iproute \
    iputils \
    && dnf clean all

RUN ssh-keygen -A

CMD ["/usr/sbin/init"]