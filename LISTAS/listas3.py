# COMPREENSÃO DE LISTAS

# for - filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # append = add novos valores
print(pares)

# for - modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2) 
print(quadrado) # gera uma nova lista com os valores modificados
print(numeros)  # não altera a lista numeros

# comprehension - filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# comprehension - modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

