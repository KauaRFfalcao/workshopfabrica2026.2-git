import requests

pokemon = print(input("Escolha seu pokemon:"))


resposta = requests.get("https://pokeapi.co/api/v2/pokemon/venusaur")

dados = resposta.json()

print(dados['name'])
print(dados['weight'])
