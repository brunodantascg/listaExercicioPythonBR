# Questão 24
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a - par ou ímpar;
# b - positivo ou negativo;
# c - inteiro ou decimal.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação que deseja realizar: + | - | / | *: ")


def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")
        if resultado_operacao % 2 == 0:
            print("Par")
            if resultado_operacao > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")


if operacao == '+':
    resultado_operacao = num1 + num2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = num1 - num2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = num1 / num2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = num1 * num2
    print("Resultado: ", resultado_operacao)
    checar()
else:
    print("Valor Invalido")
