# AND -> para ser true tudo tem que ser true
# OR -> para ser true apenas um tem que ser true

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)
print(".................")

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)
print(not saque >= limite and saldo >= saque)
print(".....................................")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp1)
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)

conta_normal_c_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_c_saldo_suficiente = (conta_especial and saldo >= saque)

exp3 = conta_normal_c_saldo_suficiente or conta_especial_c_saldo_suficiente
print(exp3)