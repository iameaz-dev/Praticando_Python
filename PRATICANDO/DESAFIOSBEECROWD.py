# 01
print("Hello World!")

# 02
A = (int(input("Valor de A: ")))
B = (int(input("Valor de B: ")))
X = A + B
print(f"X = {X}")

# 03
R = float(input("Digite um valor: "))
A = 3.14159 * (R * R)
print(f"A={A:.4f}")

# 04
A = int(input())
B = int(input())
SOMA = A + B
print(f"SOMA = {SOMA}")

# 05
A = 5.0
B = 7.1
nota_A = A * 3.5
nota_B = B * 7.5
media = (nota_A + nota_B) / 2
print(f"MEDIA = {media:.5f}")

# 06
code1, units1, price1 = map(float, input().split())
code2, units2, price2 = map(float, input().split())
amount1 = units1 * price1
amount2 = units2 * price2
amount_total = amount1 + amount2
print(f"VALOR A PAGAR: R$ {amount_total:.2f}")
