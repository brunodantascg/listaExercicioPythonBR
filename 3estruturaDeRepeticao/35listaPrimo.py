# Questão 35
# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


div = 0

def eh_primo(numero, div):
    primo = True
    for x in range(2, numero):
        div += 1
        if(numero % x == 0):
            primo = False
    return primo, div

primos = []
numero = int(input('Entre com um número: '))
for x in range(1, numero):
    primo, div = eh_primo(x, div)
    if(primo):
        primos.append(x)

print('Números primos entre 1 e {0}: {1}'.format(numero, primos))
print('Total de divisões: {0}'.format(div))
