# Questão 32
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = 0
while(num <= 0):
    num = int(input('Informe o fatorial: '))
    if(num <= 0):
        print("O fatorial que ser positivo!")

fatorial = 1
print("Fatorial de {0}".format(num))

for i in reversed(range(2, num + 1)):
    print("{0} * {1}".format(i, i-1))
    fatorial *= i

print("1 = {0}".format(fatorial))
