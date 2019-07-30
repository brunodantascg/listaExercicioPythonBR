# Exercício Funções - Questão 4

# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def arg(num):
    if(num > 0):
        return "P"
    else:
        return "N"

num = float(input("Informe número: "))

print("O número {0} é {1}".format(num, arg(num)))
