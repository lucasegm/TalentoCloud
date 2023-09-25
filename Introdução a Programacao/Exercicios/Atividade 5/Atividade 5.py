def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 == 0:
            return "Erro: Divisão por zero"
        else:
            return num1 / num2
    elif operacao == 0:
        return "Sair"
    else:
        return "Operação inválida"

while True:
    print("\nBem-vindo à Calculadora Inteligente! \n Operações disponíveis: \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair ")

    operacao = int(input("Por favor, escolha a operação que deseja realizar: "))

    if operacao == 0:
        print("Fim do programa.")
        break
    elif operacao < 1 or operacao > 4:
        print("Essa opção não existe. Por favor, escolha uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    resultado = calculadora(num1, num2, operacao)

    if resultado == "Erro: Divisão por zero" or resultado == "Operação inválida":
        print(resultado)
    else:
        print(f"O resultado da operação é {resultado}")