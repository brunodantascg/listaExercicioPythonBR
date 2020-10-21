# 11 - Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Informe primeiro número: "))
num2 = int(input("Informe segundo número: "))

print("Os números inteiros entre ", num1, " e ", num2, " são: ")

n1 = num1
n2 = num2
soma = 0

for i in range(num1, num2+1, 1):
    if(i > num1)and(i < num2):
        print(i)
        soma = soma + i


print("Soma: ", soma)
