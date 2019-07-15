# Questão 25
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quant = 0
while(quant <= 0):
    quant = int(input("Informe a quantidade de pessoas: "))
    if(quant <= 0):
        print("A quandidade deve ser positiva!")

soma = 0
for i in range(0, quant):
    idade = -1
    while (idade < 0):
        idade = int(input("Informe a idade da pessoa: "))
        if (idade < 0):
            print("A idade nao pode ser negativa")
    soma += idade

media = soma / float(quant)

if (media <= 25):
    print("A turma eh jovem")
elif (media <= 60):
    print("A turma eh adulta")
else:
    print("A turma eh idosa")
