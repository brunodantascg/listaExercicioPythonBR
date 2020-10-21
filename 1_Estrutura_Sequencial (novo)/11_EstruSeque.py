# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

int1 = int(input("Informe primeiro número inteiro: "))
int2 = int(input("Informe segundo número inteiro: "))
rea = float(input("Informe primeiro número real: "))

# a - o produto do dobro do primeiro com metade do segundo .

a = (2*int1)+(int2/2)
print("resultado a - ", a)

# b - a soma do triplo do primeiro com o terceiro.

b = (int1*3)+(3*rea)
print("resultado b - ", b)

# C - o terceiro elevado ao cubo.

c = (rea**3)
print("resultado c - ", c)
