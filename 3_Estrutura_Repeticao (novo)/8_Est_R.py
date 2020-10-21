# 8 - Faça um programa que leia 5 números e informe a soma e a média dos números.

msn1 = str("Informe ")
msn2 = str(" número :")
soma = 0

for i in range(1, 6, 1):
    n = i
    n = str(n)
    num = float(input(msn1 + n + msn2))

    soma = soma + num

media = soma/5

print("Soma: ", soma)
print("Média: ", media)
