# loop infinito - executar enquanto for verdade
# nesse caso é sempre verdade pq while True, então dá loop infinito
while True: # tbm poderia ser while 1 == 1
    opcao = int(input("Informe um número: "))

    if opcao == 10: # se digitar 10 ele para
        break

    print(opcao)


# usando RANGE
for numero in range(100):
    if numero == 10: # se n tivesse essa condiçao seria exibido até 99
        break
    print(numero, end=" ")


# CONTINUE
for numero in range(100):
    if numero == 26: #vai pular o numero 26 na contagem
        continue
    print(numero, end=" ")

    