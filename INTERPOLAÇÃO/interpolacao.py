nome = "Iasmim"
idade = 26
profissao = "arquiteta e estudante de ti"

# 1º forma -> %
# ESSA FORMA NÃO É UTILIZADA EM PY3
print("1º - Me chamo %s, tenho %d anos, sou %s." % (nome, idade, profissao))

# 2ª forma -> format
print("2º - Me chamo {}, tenho {} anos e trabalho como {}.".format(nome, idade, profissao))
# pode-se colocar a posição da variável entre as chaves, começando sempre em 0:
print("2º - Me chamo {2}, tenho {1} anos e trabalho como {0}.".format(nome, idade, profissao))
# com a variável entre as chaves:
print("2º - Me chamo {nome}, tenho {idade} anos e trabalho como {profissao}.".format(nome=nome, idade=idade, profissao=profissao))

# 3ª forma -> f strings (mais recomendada)
print(f"3º - Me chamo {nome}, tenho {idade} anos e trabalho como {profissao}.")

# formatando strings com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

