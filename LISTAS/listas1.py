# LISTAS SIMPLES
frutas = ["laranja", "maçã", "uva", "goiaba", "melancia"]
# frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 420000, 2020, 2900, "SP", True]

# ACESSANDO AS LISTAS SIMPLES 
print(frutas[-1])
print(frutas[0])
print(frutas[-2])

# LISTAS ANINHADAS
matriz = [
    [1, "a", 2], # isso é uma linha
    ["b", 3, 4], # nessa matriz temos 3 linhas e 3 colunas
    [6, 5, "c"]  # é uma matriz 3x3
]

# ACESSANDO AS LISTAS ANINHADAS
print(matriz[0]) # linha 0 -> [1, "a", 2]
print(matriz[0][0]) # linha 0, coluna 0 -> [1]
print(matriz[0][-1]) # linha 0, coluna -1 -> [2]
print(matriz[-1][-1]) # linha -1, coluna -1 -> [c]


