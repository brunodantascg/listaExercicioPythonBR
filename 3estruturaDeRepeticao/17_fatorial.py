# Questão 17
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Informe número: "))
fatorial = 1

while(num > 0):
    fatorial = fatorial * num
    num = num - 1

print(fatorial)
