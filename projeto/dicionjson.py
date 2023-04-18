import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': '25',
    },
    'Pessoa 2': {
        'nome': 'Lucas',
        'idade': '15',
    }
}

d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+', encoding='utf-8') as file:
    file.write(d1_json)
