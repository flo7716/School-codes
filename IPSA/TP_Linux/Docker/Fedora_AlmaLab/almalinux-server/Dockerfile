FROM almalinux:9

RUN dnf -y update && \
    dnf -y install \
    freeipa-client \
    openssh-server \
    sudo \
    nano \
    iputils \
    iproute \
    curl-minimal \
    && dnf clean all

RUN ssh-keygen -A

CMD ["sleep","infinity"]