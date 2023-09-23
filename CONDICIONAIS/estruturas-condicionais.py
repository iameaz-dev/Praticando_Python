# IF
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque.")
    print("Retire o seu dinheiro!")
if saldo < saque:
    print("Saldo insuficiente.")
print("..........................")


# IF ELSE
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque.")
    print("Retire o seu dinheiro!")
else:
    print("Saldo insuficiente.")
print("..........................")


# IF ELIF ELSE
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato\n"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida, tente novamente:")
    opcao = int(input("[1] Sacar \n[2] Extrato\n"))
