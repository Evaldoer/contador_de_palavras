def calcular():
    while True:
        operacao = input("\nDigite a operação (+, -, *, /) ou 'sair': ").strip().lower()

        if operacao == "sair":
            print("Encerrando calculadora...")
            break

        if operacao not in {"+", "-", "*", "/"}:
            print("Operação inválida!")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = num1 / num2

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Digite apenas números válidos!")


if __name__ == "__main__":
    calcular()