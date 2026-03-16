FROM fedora:40

RUN dnf -y update && \
    dnf -y install \
    freeipa-client \
    openssh-clients \
    sudo \
    nano \
    iputils \
    iproute \
    && dnf clean all

CMD ["sleep","infinity"]