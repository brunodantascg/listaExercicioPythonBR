# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente

msn = str("Informe ")
msn1 = str(" primeiro número: ")
msn2 = str(" segundo número: ")
msn3 = str(" terceiro número: ")

num1 = float(input(msn + msn1))
num2 = float(input(msn + msn2))
num3 = float(input(msn + msn3))

if((num1 < num2)and(num1 < num3)):
    if(num2 < num3):
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)

elif((num2 < num1)and(num2 < num3)):
    if(num1 < num3):
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)

elif((num3 < num1)and(num3 < num2)):
    if(num1 < num2):
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
