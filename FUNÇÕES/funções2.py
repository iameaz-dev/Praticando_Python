# PARÂMETROS ESPECIAIS

def criar_menu1(prato, tipo, preco, /, prato1, tipo1, preco1): # posição
    print(prato, tipo, preco)

def criar_menu2(*, prato2, tipo2, preco2): # nome
    print(prato2, tipo2, preco2)

def criar_menu3(prato3, tipo3, preco3, /, *, prato4, tipo4, preco4): # posição e nome
        print(prato3, tipo3, preco3, prato4, tipo4, preco4)

criar_menu1("Frango", "Carne", 29.99, prato1="Frango", tipo1="Carne", preco1= 29.99)
criar_menu2(prato2="Frango", tipo2="Carne", preco2= 29.99)
criar_menu3("Frango", "Carne", 29.99, prato4="Frango", tipo4="Carne", preco4= 29.99)

# antes da / -> só por posição
# depois da / -> posição ou nome
# depois do * -> só por nome (chave=valor)

# OBJETOS DE PRIMEIRA CLASSE

def subtrair(a, b):
     return a - b

def test(a, b):
     return a*2 + b*3

def resultado(a, b, funcao):
     resultado1 = funcao(a, b)
     print(f"O resultado de é = {resultado1}")
    
resultado(50, 10, subtrair)
resultado(2, 3, test)

# ESCOPO LOCAL E GLOBAL

salario = 3000 # escopo global 


def salario_bonus(bonus, lista): # escopo local
    global salario # utilizando a variável q tá no escopo global

    lista_aux = lista.copy() # cria-se a cópia p não alterar a ref externa
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1] # ref externa
salario_com_bonus = salario_bonus(700, lista) # usando obj mutável por referência
print(salario_com_bonus)
print(lista)


