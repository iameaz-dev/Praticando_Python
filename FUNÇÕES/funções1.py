def mensagem(): # é declarada dessa forma, nesse caso não tem parâmetro pois () tá vazio
    print("Minha primeira função!")

def mensagem1(nome): # função com parâmetro sem valor
    print(f"Que legal, {nome}!")

def mensagem2(nome="Iasmim"): # função com parâmetro com valor
    print(f"Que legal, {nome}!")

mensagem() # aqui tá chamando a função
mensagem1(nome="Iasmim") 
mensagem2()
mensagem2(nome="Gabriel") # sobrescreve o parâmetro declarado previamente

# RETORNANDO VALORES
def calcular(numeros):
    return sum(numeros)

print(calcular([1, 2, 3, 4, 5]))

def func_3():
    print("Olá mundo!")

func_3() # retorna Olá mundo!
print(func_3()) # retorna None

# ARGUMENTOS NOMEADOS
def salvar_contato(nome, idade, cidade):
    print(f"Cliente inserido com sucesso! -> {nome} | {idade} | {cidade}")

salvar_contato("Iasmim", 26, "João Pessoa")
salvar_contato(nome="Gabriel", idade=24, cidade="Pipa")
salvar_contato(**{"nome": "Nilda", "idade": 62, "cidade": "Santa Luzia"})

# ARGS E KWARGS
def lista_contatos(data_hj, *contatos, **empresa):
    lista = "\n".join(contatos)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in empresa.items()])
    dados = f"{data_hj}\n\n{lista}\n\n{meta_dados}"
    print(dados)

lista_contatos(
    "Sexta-feira, 15 de Setembro de 2023.",
    "Iasmim Azevedo, 26 anos.",
    "Gabriel Sparke, 24 anos.",
    sobre="Nosso amor é lindo demais!",
    ano=2023,
)


