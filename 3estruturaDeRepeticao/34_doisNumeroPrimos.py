# Questão 34
# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Informe o número: '))
primo = True
for x in range(2, numero):
    if(numero % x == 0):
        primo = False

if(primo):
    print('O número {} é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))
