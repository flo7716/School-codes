import requests

url = 'http://51.159.16.22:8027/'

# Lire le composer.lock complet pour la version Twig exacte
r = requests.get(url + 'composer.lock')
# Trouver la version twig
import json
data = json.loads(r.text)
for pkg in data['packages']:
    if 'twig' in pkg['name']:
        print(f"[TWIG] {pkg['name']} version: {pkg['version']}")

# Chercher d'autres fichiers PHP
files = [
    'app.php', 'hello.php', 'template.php', 'view.php',
    'src/index.php', 'templates/hello.html.twig',
    'templates/index.html.twig', 'templates/hello.twig',
    'views/hello.twig', 'views/index.twig',
]

for f in files:
    r = requests.get(url + f)
    if r.status_code == 200 and 'Not Found' not in r.text:
        print(f'[FOUND] {f}')
        print(r.text[:300])
        print('---')
    else:
        print(f'[FAIL]  {f}')
