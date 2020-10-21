# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

msn = str("Informe ")
msn1 = str(" primeiro número.")
msn2 = str(" segundo número.")
msn3 = str(" terceiro número.")

num1 = float(input(msn + msn1))
num2 = float(input(msn + msn2))
num3 = float(input(msn + msn3))

if((num1 > num2)and(num1 > num3)):
    if((num2 > num3)):
        print(num1, " é o maior número, ", num2, " é o segundo maior número e ", num3, " é o menor número")
    else:
        print(num1, " é o maior número, ", num3, " é o segundo maior número e ", num2, " é o menor número")

elif((num2 > num1)and(num2 > num3)):
    if((num1 > num3)):
        print(num2, " é o maior número, ", num1, " é o segundo maior número e ", num3, " é o menor número")
    else:
        print(num2, " é o maior número, ", num3, " é o segundo maior número e ", num1, " é o menor número")

elif((num3 > num1)and(num3 > num2)):
    if((num2 > num1)):
        print(num3, " é o maior número, ", num2, " é o segundo maior número e ", num1, " é o menor número")
    else:
        print(num3, " é o maior número, ", num1, " é o segundo maior número e ", num2, " é o menor número")
