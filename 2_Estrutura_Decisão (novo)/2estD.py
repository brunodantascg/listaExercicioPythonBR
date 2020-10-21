# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

informativo = str("Informe número: ")

num = float(input(informativo))

if(num >= 0):
    if(num > 0):
        print("O número é positivo")
    else:
        print("O número é neutro")
else:
    print("O número é negativo")
