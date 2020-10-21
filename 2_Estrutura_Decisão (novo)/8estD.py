# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


msn = str("Informe o preço ")
msn1 = str(" do primeiro produto: ")
msn2 = str(" do segundo produto: ")
msn3 = str(" do terciro produto: ")

pro1 = float(input(msn + msn1))
pro2 = float(input(msn + msn2))
pro3 = float(input(msn + msn3))

if((pro1 < pro2)and(pro1 < pro3)):
    print("O primeiro produto é a melhor opção de compra, R$", pro1)

elif((pro2 < pro1)and(pro2 < pro3)):
    print("O segundo produto é a melhor opção de compra, R$", pro2)

else:
    print("O terceiro produto é a melhor opção de compra, R$", pro3)
