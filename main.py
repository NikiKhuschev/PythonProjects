import requests

token = '9fde3c4e897a6cf0351e94fd6de72bed'
host = 'https://api.pokemonbattle.me' # хост для покемонов

'''response = requests.post('https://api.pokemonbattle.me/pokemons', json = { 
    "name": "generate",
    "photo": "generate",
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response.text)''' # создание покемона

'''response = requests.put('https://api.pokemonbattle.me/pokemons', json = {
    "pokemon_id": "13161",
    "name": "Круговорот",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png",
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_izmenenie.json())''' # изменение покемона


response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', 
                                  json= {"pokemon_id" : "13161"}, 
                                  headers = {'trainer_token' : token, 
                                  'Content-Type' : 'application/json'})

print(response_add_pokeball.json())