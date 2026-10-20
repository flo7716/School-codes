import requests

url = 'http://51.159.16.22:8027/'

# Tester d'autres paramètres
params_to_test = ['name', 'template', 'input', 'q', 'search', 
                  'page', 'id', 'user', 'data', 'text', 'msg',
                  'content', 'value', 'str', 'twig', 'var',
                  'param', 'test', 'hello', 'world']

for param in params_to_test:
    r = requests.get(url, params={param: 'TESTUNIQUE123'})
    if 'TESTUNIQUE123' in r.text:
        print(f'[FOUND] param={param} → {r.text.strip()}')
    else:
        print(f'[FAIL]  param={param} → {r.text.strip()}')
