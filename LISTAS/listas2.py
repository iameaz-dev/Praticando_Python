# FATIAMENTO DE LISTAS
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # começa no "h"
print(lista[:2]) # vai até o "o"
print(lista[1:3]) # do "y" ao "t" pq diminui um nº
print(lista[0:3:2]) # do "p" ao "t" de 2 em 2 passos
print(lista[::]) # vazio no inicio = caractere 0 | vazio no fim = até o último caractere | vazio passo = pula de 1 em 1
print(lista[::-1]) # só informa o passo -1, então espelha a sequência


# ITERAÇÃO DE LISTAS
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")