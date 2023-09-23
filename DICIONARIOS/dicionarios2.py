# métodos da classe dict

# clear -> apaga o conteúdo do dicionário
contatos = {
    "iasmimmm@gmail.com": {"nome": "Iasmim", "tel": "83998034558"},
    "gabrielsparke66@gmail.com": {"nome": "Gabriel", "tel": "84996581036"}
}
#contatos.clear()
print(contatos)

# copy -> copiar um dict existente
copia = contatos.copy()
copia = {"nome": "Ias", "idade": 26}
print(copia)

# fromkeys -> criar chaves e valores
dicionario = dict.fromkeys(["nome", "idade"])
print(dicionario)
dicionario = dict.fromkeys(["nome", "idade"], "vazio")
print(dicionario)

# get -> acessar valores dentro do dict
resultado = contatos.get(
    "iasmimmm@gmail.com", {}
)  
print(resultado)

# items -> retorna a lista de tuplas
resultado = contatos.items()
print(resultado)

for chave, valor in contatos.items():
    print(chave, valor)

# keys -> retorna só as chaves do dict
novo_dict = {"a": 100, 1: "teste", "b": "python"}
print(novo_dict.keys())

# pop -> remove valores do dict e retorna o valor removido
resultado = copia.pop("nome", {})  
print(resultado)
print(copia)

# popitem -> remove valores na sequência
resultado = novo_dict.popitem()  
print(resultado)

# setdefault -> add valores sem sobrescreve-los
dados = {"nome": "iasmim", "idade": 26}
dados.setdefault("nome", "gabriel")
print(dados)
dados.setdefault("Nome", "gabriel")
print(dados)

# update -> atualiza o dict
dados = {
    "iameaz.dev": {"nome": "iasmim", "idade": 26}
}
dados.update({"iameaz.dev": {"nome": "iaxmeni"}})
print(dados)

# values -> retorna só os valores do dict
dados1 = {"nome": "iasmim", "idade": 26}
print(dados1.values())

# in -> verificar se uma chave existe ou não no dict
resultado = "nome" in dados1 
print(resultado)
# in no dict aninhado
resultado1 = "telefone" in dados["iameaz.dev"] 
print(resultado1)

# del -> remover valores do dict
dados = {
    "iameaz.dev": {"nome": "iasmim", "idade": 26},
    "gabrielsparke": {"nome": "gabriel", "idade": 24}
}
del dados["iameaz.dev"]["idade"]
print(dados)
del dados["gabrielsparke"]
print(dados)


