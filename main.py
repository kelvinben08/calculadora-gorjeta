print('----------------------------- Calculadora de Gorjeta -----------------------------')

# Entradas do usuário:
valor_conta = float(input("Digite o valor da conta: R$"))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

# Cálculo do valor da gorjeta:
valor_gorjeta = valor_conta * porcentagem_gorjeta / 100
total_final = valor_conta + valor_gorjeta

print('----------------------------------------------------------------------------------')

# Impressão do resultado:
print(f"O valor da gorjeta é de: R${valor_gorjeta:.2f}")
print(f"O total final da conta do cliente é de: R${total_final:.2f}")

print('----------------------------------------------------------------------------------')
