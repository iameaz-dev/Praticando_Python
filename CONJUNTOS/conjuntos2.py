# métodos da classe set
# union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

# difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# simmetryc_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))

# issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# issubperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# isdisjoint
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 6, 7}
conjunto_c = {8, 9, 10}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_b.isdisjoint(conjunto_c))

# add
sorteio = {1, 23}

sorteio.add(24)
sorteio.add(25)
print(sorteio)

# clear
sorteio = {1, 23}

sorteio.clear()
print(sorteio)

# copy
sorteio = {1, 23}

sorteio.copy()
print(sorteio)

# discard
numeros = {1, 2, 3, 4, 3, 5, 2}

numeros.discard(5)
print(numeros)

# pop
numeros = {1, 2, 3, 4, 3, 5, 2}
numeros.pop()
print(numeros)

# remove
numeros = {1, 2, 3, 4, 3, 5, 2}

numeros.remove(3)
print(numeros)

# len
numeros = {1, 2, 3, 4, 3, 5, 2}
print(len(numeros))

# in
numeros = {1, 2, 3, 4, 3, 5, 2}

print(1 in numeros)
print(23 in numeros)
