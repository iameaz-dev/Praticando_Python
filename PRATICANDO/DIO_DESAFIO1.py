# 01 - equilibrando saldo
# saldo_atual = float(input())
# valor_deposito = float(input())
# valor_retirada = float(input())

# saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

# print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}") # :1.f -> imprime o resultado com uma casa decimal

# # 02 - organizando seus ativos em ordem alfabética
# ativos = []
# quantidadeAtivos = int(input("Digite a quantidade de ativos: "))

# for _ in range(quantidadeAtivos):
#     codigoAtivo = input().strip()  # Use strip() para remover \n
#     ativos.append(codigoAtivo)

# ativos_ordenados = sorted(ativos)

# for alfabetico in ativos_ordenados:
#     print(alfabetico)

# 03 - 
saldo_total = 1000
valor_saque = 200

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
  saldo_total -= valor_saque
  print(f"Saque realizado com sucesso! Novo saldo: {saldo_total}")
else:
  print("Saldo insuficiente. Saque não realizado!")