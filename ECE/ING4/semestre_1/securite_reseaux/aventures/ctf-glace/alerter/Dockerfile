FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
RUN useradd -u 10001 -r -s /usr/sbin/nologin app
WORKDIR /app
COPY alerter.py .
USER 10001
CMD ["python", "alerter.py"]
