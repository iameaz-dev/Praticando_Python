# declaração de tuplas
frutas = ("melancia", "banana", "manga", "goiaba",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

# acesso aos dados
print(frutas[-2])
print(letras[2])
print(numeros[-1])
print(pais[0])

# tupla aninhada -> idêntica a lista aninhada
matriz = [
    [2, "i", 6], 
    ["g", 2, 4], 
    [7, 5, "a"],  
]

print(matriz[0]) 
print(matriz[0][0]) 
print(matriz[0][-1]) 
print(matriz[-1][-1]) 

# fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # começa no "h"
print(lista[:2]) # vai até o "o"
print(lista[1:3]) # do "y" ao "t" pq diminui um nº
print(lista[0:3:2]) # do "p" ao "t" de 2 em 2 passos
print(lista[::]) # vazio no inicio = caractere 0 | vazio no fim = até o último caractere | vazio passo = pula de 1 em 1
print(lista[::-1]) # só informa o passo -1, então espelha a sequênciao de tuplas

# fatiamento, iteração e os métodos count, index e lex
# são 100% iguais as listas! 

carros=("gol")
print(isinstance(carros, tuple))
