# 7 - Faça um programa que leia 5 números e informe o maior número.

msn1 = str("Informe ")
msn2 = str(" número :")
nuMa = 0

for i in range(1, 6, 1):
    n = i
    n = str(n)
    num = float(input(msn1 + n + msn2))

    if((num > nuMa)or(i == 1)):
        nuMa = num
        

print(nuMa)
