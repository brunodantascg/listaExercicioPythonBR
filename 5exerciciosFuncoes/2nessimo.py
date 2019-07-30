# Exercício Funções - Questão 2

# Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir(numero):
    if isinstance(numero, int):
        x = 1
        while x <= numero:
            y = 1
            texto = " "
            while y <= x:                
                texto += str(y) + "\t"
                y += 1
            print(texto)
            x += 1

numero = int(input("Informe número: "))

print(imprimir(numero))
