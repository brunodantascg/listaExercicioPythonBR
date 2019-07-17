# Questão 49

# Faça um programa que mostre os n termos da Série a seguir:

#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

# Imprima no final a soma da série.


numero = int(input("Informe o número: "))
for i in range(1, numero + 1):
    if(i == 1):
        y = 1
    print("{0}/{1} = {2}".format(i, y, i/y))
    y += 2
