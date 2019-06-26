# Questão 1
# Faça um programa para imprimir:

def imprimir(n):
    for y in range(1, n + 1):
        for j in range(1, y + 1):
            print(y)
        print()

num = int(input('Informe um numero: '))
imprimir(num)
