FROM fedora:40

RUN dnf -y update && \
    dnf -y install \
    freeipa-client \
    openssh-clients \
    sudo \
    nano \
    iputils \
    iproute \
    curl \
    && dnf clean all

CMD ["sleep","infinity"]