import requests

url = 'http://51.159.16.22:8027/'

# Wordlist complète
paths = [
    # PHP files
    'index.php', 'app.php', 'main.php', 'run.php', 'web.php',
    'public/index.php', 'web/index.php', 'www/index.php',
    # Twig templates
    'templates/hello.twig', 'templates/index.twig',
    'templates/hello.html', 'templates/index.html',
    'templates/base.twig', 'templates/main.twig',
    'views/hello.twig', 'views/index.twig',
    'twig/hello.twig', 'twig/index.twig',
    # Config files
    '.htaccess', 'config.php', 'config.yml', 'config.yaml',
    '.env', '.env.local', 'app/config.php',
    # Source exposure
    'phpinfo.php', 'info.php', 'test.php',
    # Docker/container
    'Dockerfile', 'docker-compose.yml', 'docker-compose.yaml',
    # Misc
    'README.md', 'README', 'LICENSE',
    'src/index.php', 'src/app.php', 'src/main.php',
    'public/app.php', 'app/index.php',
]

for path in paths:
    r = requests.get(url + path)
    if r.status_code == 200 and 'Not Found' not in r.text:
        print(f'[FOUND] /{path}')
        print(r.text[:200])
        print('---')
