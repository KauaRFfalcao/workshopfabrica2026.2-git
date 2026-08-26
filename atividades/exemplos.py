def calcular_total(preco, quantidade):
    return preco * quantidade

total = calcular_total(10 , 2)
print(total)

#collections

usuarios = [{"nome": "alice", "idade": 20},
           {"nome": "bob", "idade": 15},
           {"nome": "luca", "idade": 22}]

for usuario in usuarios:
        print(f"nome: {usuario['nome']}, Idade: {usuario['idade']}")




