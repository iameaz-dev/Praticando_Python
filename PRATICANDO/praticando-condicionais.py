MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
IDADE_EUA = 16
nome = str(input("Qual o seu nome? "))
idade = int(input("Digite a sua idade: "))

if idade >= MAIOR_IDADE:
    print(f"{nome}, você pode tirar sua CNH! :)")
elif idade == IDADE_ESPECIAL:
    print(f"{nome}, você pode fazer as aulas teóricas e práticas, mas a sua CNH só irá ser liberada quando completar 18 anos.")
elif idade == IDADE_EUA:
    print(f"{nome}, você pode fazer as aulas teóricas, mas a sua CNH só sai quando completar os 18 anos.")
else:
    print(f"{nome}, você ainda não tem idade para dirigir.")
 
