# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

num1 = int(input("Informe primeiro número inteiro: "))
num2 = int(input("Informe segundo número inteiro: "))
num3 = float(input("Informe número real: "))

a = (2 * num1) * (num2/2)
b = (3 * num1) + num3
c = num3**3

print("a - {0} | b - {1} | c - {2}".format(a, b, c))
