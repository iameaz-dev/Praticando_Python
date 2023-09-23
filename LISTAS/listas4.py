# MÉTODOS DA CLASSE LIST
# append - adiciona elementos na lista existente
lista = ["iasmim"]

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)

# clear - limpar a lista
lista = [1, "python", [40, 30, 20]]

lista.clear()
print(lista)

# copy - copiar uma lista
l1 = [1, "python", [40, 30, 20]]

l2 = l1.copy()
print(id(l2), id(l1))

l2[0] = 2
print(l2) # altera o valor da posição 0 apenas de l2

# count - contar quantos elementos iguais tem na lista
idades = ['24', '26', '25', '26', '24']

print(idades.count('24'))
print(idades.count('25'))
print(idades.count('26'))

# extend - juntar listas
nomes = ['iasmim', 'gabriel']
idades = [26, 24]

nomes.extend([idades])
print(nomes)

# index - saber onde é a primeira ocorrência de um objeto
# se houver elementos repetidos, ele ignora e relata só o 1º
letras = ['a', 'd', 'm', 'u', 'p', 'q', 't', 'p']

print(letras.index('p'))

# pop - remove o último elemento da lista
letras = ['a', 'd', 'm', 'u', 'p', 'q', 't', 'p']
print(letras.pop())
print(letras.pop())
print(letras.pop(2))
print(letras)

# remove - remove elementos da lista
letras = ['a', 'd', 'm', 'u', 'p', 'q', 't', 'p']
letras.remove('p')
print(letras)

# reverse - espelhar a lista  
letras = ['a', 'd', 'm', 'u', 'p', 'q', 't', 'p']
letras.reverse()
print(letras)

# sort - ordenar a lista em ordem alfabética
letras = ['m', 'u', 'a', 'd', 'p', 'q', 't', 'b']
letras.sort()
print(letras)

letras.sort(reverse=True) # ordena do z ao a
print(letras)

letras = ['mmm', 'uu', 'aaaaaaaa', 'd'] # ordena por tamanho (menor p maior)
letras.sort(key=lambda x: len(x)) 
print(letras)

letras.sort(key=lambda x: len(x), reverse=True) # maior pro menor
print(letras)

# len - diz o tamanho das coisas
letras = ['m', 'u', 'a', 'd', 'p', 'q', 't', 'b']
print(len(letras))

# sorted - ordenar iteráveis
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))                
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
 