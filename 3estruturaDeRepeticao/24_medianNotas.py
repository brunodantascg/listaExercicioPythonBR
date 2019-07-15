# Questão 24
# Faça um programa que calcule o mostre a média aritmética de N notas.


quant = 0
while (quant <= 0):
    quant = int(input("Informe quantas notas: '))
    if (quant <= 0):
        print("A quandidade deve ser positiva!")

soma = 0
for i in range(0, quant):
    nota = -1
    while (nota < 0) or (nota > 10):
        nota = float(input("Informe a nota: "))
        if (nota < 0) or (nota > 10):
            print("A nota deve estar entre 0 e 10")
    soma += nota

print("A media das notas eh ".format(soma/float(quant))
