# 14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

m1 = str("Informe ")
m2 = str(" número: ")
par = 0
impar = 0

for i in range(1, 11, 1):
    n = str(i)
    num = int(input(m1 + n + m2))
    if(num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

print("Quantidade de números PARES: ", par)
print("Quantidade de números IMPARES: ", impar)
