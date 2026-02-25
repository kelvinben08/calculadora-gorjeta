"""
Calculadora de Gorjeta

Programa que calcula o valor da gorjeta e o total final.
Versão: 1.3
"""
TAMANHO_LINHA = 78
TITULO = "Calculadora de Gorjeta"


def calcular_gorjeta(valor_conta: float,
                     porcentagem_gorjeta: float) -> tuple[float, float]:
    """
    Calcula o valor da gorjeta e o total final da conta.

    Args:
        valor_conta (float): Valor original da conta.
        porcentagem_gorjeta (float): Porcentagem da gorjeta.

    Returns:
        tuple[float, float]: Valor da gorjeta e total final.
    """

    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    total_final = valor_conta + valor_gorjeta

    return valor_gorjeta, total_final


def solicitar_valor(mensagem: str) -> float:
    """
    Solicita um valor numérico ao usuário.

    Garante que o valor digitado:
    - Seja um número válido
    - Não seja negativo

    Args:
        mensagem (str): Texto exibido para o usuário.

    Returns:
        float: Valor validado pelo usuário.
    """

    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("O valor digitado não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Valor digitado inválido. Tente novamente.")


def main():
    """
    Função principal que executa o fluxo do programa.
    """

    print("=" * TAMANHO_LINHA)
    print(TITULO.center(TAMANHO_LINHA))
    print("=" * TAMANHO_LINHA)
    valor_conta = solicitar_valor('Digite o valor da conta: R$')
    porcentagem_gorjeta = solicitar_valor('Digite a porcentagem da gorjeta: ')
    print("=" * TAMANHO_LINHA)
    valor_gorjeta, total_final = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"O valor da gorjeta é de: R${valor_gorjeta:.2f}")
    print(f"O total final da conta do cliente é de: R${total_final:.2f}")
    print("=" * TAMANHO_LINHA)


# Proteção padrão:
if __name__ == "__main__":
    main()
