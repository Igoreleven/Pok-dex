from flask import Flask, request
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def homepage():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    poke = request.form.get('pokemon')
    api = f'https://pokeapi.co/api/v2/pokemon/{poke}'
    res = requests.get(api)
    res.raise_for_status()
    hab = res.json()

    #hab
    abilities = hab.get('abilities', []) 
    hab_list = [ability.get('ability', {}).get('name') for ability in abilities]
    hab1 = hab_list[0] if len(hab_list) > 0 else None
    hab2 = hab_list[1] if len(hab_list) > 1 else None

    print("Habilidade 1:", hab1)
    print("Habilidade 2:", hab2)



    #tipo
    res = requests.get(api)
    res.raise_for_status()
    tp = res.json()
    types = tp.get('types', [])

    for tp in types:
        type = tp.get('type', {}).get('name')
        print("Tipo:", type)



    #hp
    res = requests.get(api)
    res.raise_for_status()
    data = res.json()
    stats = data.get('stats', [])

    for stat in stats:
        if stat['stat']['name'] == 'hp':
            hp = stat.get('base_stat')
            print("Hp:", hp)



    #ataque
    res = requests.get(api)
    res.raise_for_status()
    data = res.json()
    stats = data.get('stats', [])

    for stat in stats:
        if stat['stat']['name'] == 'attack':
            attack = stat.get('base_stat')
            print("Ataque:", attack)



    #defesa
    res = requests.get(api)
    res.raise_for_status()
    data = res.json()
    stats = data.get('stats', [])

    for stat in stats:
        if stat['stat']['name'] == 'defense':
            defense = stat.get('base_stat')
            print("Defesas:", defense)



    #special_attack
    res = requests.get(api)
    res.raise_for_status()
    data = res.json()
    stats = data.get('stats', [])

    for stat in stats:
        if stat['stat']['name'] == 'special-attack':
            special_attack = stat.get('base_stat')
            print("special_attack:", special_attack)



    #special-defense
    res = requests.get(api)
    res.raise_for_status()
    data = res.json()
    stats = data.get('stats', [])

    for stat in stats:
        if stat['stat']['name'] == 'special-defense':
            special_defense = stat.get('base_stat')
            print("special_defense:", special_defense)



    #img
    response = requests.get(api)
    response.raise_for_status()
    data = response.json()
    api = data['sprites']['front_default']

    return render_template('/from.html', hab1=hab1, hab2=hab2, type=type, hp=hp, attack=attack, defense=defense, api=api, poke=poke, special_attack=special_attack, special_defense=special_defense)

if __name__ == '__main__':
    app.run(debug=True)