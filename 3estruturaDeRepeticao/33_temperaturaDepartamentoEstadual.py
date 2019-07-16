# Questão 33
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

quant = 0
while(quant <= 0):
    quant = int(input('Informe a quantidade de temperaturas: '))
    if(quant <= 0):
        print("A quandidade deve ser positiva!")

soma = 0
for i in range(0, quant):
    temperatura = float(input("Informe a temperatura: "))
    if("maior" not in vars()) or (temperatura > maior):
        maior = temperatura
    if("menor" not in vars()) or (temperatura < menor):
        menor = temperatura
    soma += temperatura

media = soma / float(quantidade)

print("Media da temperatura: ".format(media))
print("Maior temperatura: ".format(maior))
print("Menor temperatura: ".format(menor))
