import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '424e71f2c2386cc5c6dd7502e7517aac'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}

body_registration = {
      "trainer_token" : TOKEN,
      "email" : "maksunov.97@yandex.ru",
      "password" : "S22121970ma"
}      
body_confirmation = {
      "trainer_token" : TOKEN
}
body_create = {
     "name": "Pokemonkod",
     "photo_id": "https://dolnikov.ru/pokemons/albums/007.png"
}
body_change = {
     "pokemon_id": "175459",
     "name": "New Name",
     "photo_id": "https://dolnikov.ru/pokemons/albums/007.png"
}
body_add_pokeball = {
     "pokemon_id": "175459"
}



'''response = requests.post(posturl = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)


response_change = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response_change.text)
message = response_change.json()['message']
print(message)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)
message = response_add_pokeball.json()['message']
print(message)

