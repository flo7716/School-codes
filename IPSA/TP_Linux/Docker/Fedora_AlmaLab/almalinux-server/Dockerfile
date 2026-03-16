FROM almalinux:9

RUN dnf -y update && \
    dnf -y install \
    openssh-server \
    sudo \
    iproute \
    iputils \
    nano \
    python3 \
    && dnf clean all

# config ssh simple
RUN ssh-keygen -A

CMD ["/usr/sbin/sshd","-D"]