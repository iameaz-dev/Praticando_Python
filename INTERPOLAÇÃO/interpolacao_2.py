nome = "Iasmim"
idade = 26
saldo = 200.00

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

# utilizando dicionários (vamos estudar mais p frente)
dados = {"nome": "Iasmim", "idade": 26}
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
# formatando a string com casas decimais e espaços
print(f"Nome: {nome} Idade: {idade:3} Saldo: {saldo:3.2f}")
