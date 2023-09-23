# Adição
print(1 + 1)

# Subtração
print(2 - 1)

# Multiplicação
print(2 * 3)

# Divisão com resultado float
print(10 / 2)

# Divisão com resultado int
print(10 // 2)

# Módulo (resto da divisão)
print(10 % 3)

# Exponenciação (2 * 2 * 2)
print(2 ** 3)
print("..................... \n")

# Ordem de Precedência

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)
print("..................... \n")


# Praticando
produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)
print("..................... \n")

produto = (float(input("Qual o valor do produto? ")))
unidade = (int(input("Vai levar quantas unidades? ")))
valor = (float(produto * unidade))

print(f"O total a pagar é de ${valor} reais.")