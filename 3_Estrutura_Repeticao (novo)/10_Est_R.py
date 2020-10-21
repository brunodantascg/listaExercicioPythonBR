# 10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Informe primeiro número: "))
num2 = int(input("Informe segundo número: "))

print("Os números inteiros entre ", num1, " e ", num2, " são: ")

n1 = num1
n2 = num2

for i in range(num1, num2+1, 1):
    if(i > num1)and(i < num2):
        print(i)
