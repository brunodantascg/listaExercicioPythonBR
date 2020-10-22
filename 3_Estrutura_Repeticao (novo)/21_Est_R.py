# 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input('Entre com um número: '))
primo = True
for x in range(2, numero):
    if(numero % x == 0):
        primo = False

if(primo):
    print('O número {} é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))
