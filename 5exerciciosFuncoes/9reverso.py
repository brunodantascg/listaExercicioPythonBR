# Exercício Funções - Questão 9

# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverte(num):
    y = num
    return y[::-1]

num = str(input("Informe número: "))

print(" {0} ---> {1}.".format(num, inverte(num)))
