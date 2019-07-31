# Exercício Funções - Questão 8

# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digitos(x):
    quant = len(str(x))
    return quant

x = int(input("Informe número: "))

print("O número {0}, tem {1} digitos!".format(x, digitos(x)))
