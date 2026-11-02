FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        suricata python3 && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /var/log/suricata
COPY forward.py /forward.py
COPY start.sh /start.sh
RUN chmod +x /start.sh /forward.py
ENTRYPOINT ["/start.sh"]
