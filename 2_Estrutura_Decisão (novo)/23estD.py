# 23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Informe um número: "))

x = round(num)

if(num == x):
    print("Número é Inteiro!")

else:
    print("Número é Decimal")
