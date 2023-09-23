print("Bem-vindo à Calculadora Inteligente!")

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        return "Total = 0"

num1 = float(input("Qual é o primeiro número da operação? "))
num2 = float(input("Qual é o segundo número? "))
print("\n Escolha a operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")

operacao = int(input("Qual operação deseja realizar com os números definidos? "))

resultado = calculadora(num1, num2, operacao)
print("Total = ", resultado)