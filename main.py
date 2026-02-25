# Função que calcula a gorjeta:
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    valor_gorjeta = valor_conta * porcentagem_gorjeta / 100
    total_final = valor_conta + valor_gorjeta
    return valor_gorjeta, total_final


# Função que solicita o valor:
def solicitar_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("O valor digitado deve ser maior que 0. Tente novamente.")
        except ValueError:
            print("Valor digitado inválido. Tente novamente.")


# Função principal:
def main():
    print("=" * 65)
    print("Calculadora de Gorjeta")
    print("=" * 65)
    valor_conta = solicitar_valor('Digite o valor da conta: R$')
    porcentagem_gorjeta = solicitar_valor('Digite a porcentagem da gorjeta: ')
    print("=" * 65)
    valor_gorjeta, total_final = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"O valor da gorjeta é de: R${valor_gorjeta:.2f}")
    print(f"O total final da conta do cliente é de: R${total_final:.2f}")
    print("=" * 65)


# Proteção padrão
if __name__ == "__main__":
    main()
