# Questão 50

# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

numero = int(input("Informe o número: "))
a = 1
b = a
for b in range(1, numero + 1):
    print("{0}/{1} = {2}".format(a, b, a/b))

