# 01
nome = input("Qual o seu nome? ")
saldo_total = (float(input("Quanto você tem na conta? ")))
objetivo_final = (float(input("Você precisa de quanto? ")))
quanto_falta = (objetivo_final - saldo_total)

print(f"Você precisa de mais ${quanto_falta} reais para chegar ao seu objetivo de ${objetivo_final} reais. \n")
print(type(quanto_falta))
print("---------------------------------------------------------------------------------------------- \n")

# 02
produto = (float(input("Qual o valor do produto? ")))
unidade = (int(input("Vai levar quantas unidades? ")))
valor = (float(produto * unidade))

print(f"O total a pagar é de ${valor} reais.")
print("--------------------------------------- \n")
