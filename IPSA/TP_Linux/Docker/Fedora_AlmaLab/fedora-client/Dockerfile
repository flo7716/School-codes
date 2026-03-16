FROM fedora:40

RUN dnf -y update && \
    dnf -y install \
    openssh-clients \
    iputils \
    iproute \
    nano \
    curl \
    && dnf clean all

CMD ["sleep","infinity"]