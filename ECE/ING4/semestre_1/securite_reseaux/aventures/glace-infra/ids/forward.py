#!/usr/bin/env python3
"""Relaye en continu les alertes Suricata (eve.json) vers srv-logs (rsyslog, UDP/514)."""
import json, os, socket, time

LOG_HOST = os.environ.get("LOG_HOST", "10.0.30.100")
IDS_NAME = os.environ.get("IDS_NAME", "ids")
EVE_PATH = "/var/log/suricata/eve.json"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def tail(path):
    while not os.path.exists(path):
        time.sleep(1)
    f = open(path, "r")
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

for line in tail(EVE_PATH):
    try:
        ev = json.loads(line)
    except json.JSONDecodeError:
        continue
    if ev.get("event_type") != "alert":
        continue
    msg = f"<13>{IDS_NAME}: ALERT sig=\"{ev['alert']['signature']}\" src={ev.get('src_ip')} dst={ev.get('dest_ip')}:{ev.get('dest_port')} sev={ev['alert'].get('severity')}"
    try:
        sock.sendto(msg.encode(), (LOG_HOST, 514))
    except OSError:
        pass
