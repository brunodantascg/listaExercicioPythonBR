# Questão 28
# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.


quant = 0
while(quant <= 0):
    quant = int(input("Informe a quantidade de CDs: "))
    if (quant <= 0):
        print("A quandidade deve ser positiva!")

soma = 0
for i in range(0, quant):
    valor = -1
    while (valor < 0):
        valor = float(input("Informe o valor pago pelo CD: "))
        if (valor < 0):
            print("O valor deve ser maior ou igual a 0")
    soma += valor

media = soma / float(quant)

print("Quantidade de CDs:{0}".format(quant))
print(" A média do valor dos CDs: {0}".format(media))
