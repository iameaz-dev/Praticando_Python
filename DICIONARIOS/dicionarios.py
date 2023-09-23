# forma 1
pessoa = {"nome": "Iasmim", "idade": 26}

# forma 2
pessoa = dict(nome="Iasmim", idade=26)
print(pessoa)

# adicionar uma nova chave em um dicionário existente
pessoa["genero"] = "feminino"
print(pessoa)

# acessando os dados
print(pessoa["nome"])

# sobrescrever um valor
pessoa["nome"] = "Gabriel"
pessoa["idade"] = "24"
pessoa["genero"] = "masculino"
print(pessoa)

# dicionários aninhados
contatos = {
    "iasmimmm@gmail.com": {"nome": "Iasmim", "tel": "83998034558"},
    "gabrielsparke66@gmail.com": {"nome": "Gabriel", "tel": "84996581036"}
}
# acessando um valor 
print(contatos["iasmimmm@gmail.com"]["tel"])
print("------------------------")

# iteração de dicionários
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items(): # melhor forma
    print(chave, valor)

