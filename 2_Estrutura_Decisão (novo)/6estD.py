# 6 - Faça um Programa que leia três números e mostre o maior deles.

msn = str("Informe ")
msn1 = str(" primeiro número: ")
msn2 = str(" segundo número: ")
msn3 = str(" terceiro número: ")

num1 = float(input(msn + msn1))
num2 = float(input(msn + msn2))
num3 = float(input(msn + msn3))

if((num1 > num2) and (num1 > num3)):
    print(num1, " é maior número")

elif((num2 > num1)and(num2 > num3)):
    print(num2, " é maior número")

else:
    print(num3, " é o maior número")
