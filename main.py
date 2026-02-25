# Função que calcula a gorjeta:
def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    valor_gorjeta = valor_conta * porcentagem_gorjeta / 100
    total_final = valor_conta + valor_gorjeta
    return valor_gorjeta, total_final


# Função principal:
def main():
    print("===================== Calculadora de Gorjeta ====================")
    valor_conta = float(input('Digite o valor da conta: R$'))
    porcentagem_gorjeta = float(input('Digite a porcentagem da gorjeta: '))
    print("=" * 65)
    valor_gorjeta, total_final = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"O valor da gorjeta é de: R${valor_gorjeta:.2f}")
    print(f"O total final da conta do cliente é de: R${total_final:.2f}")
    print("=" * 65)


# Proteção padrão
if __name__ == "__main__":
    main()
