# Exercício Funções - Questão 3

# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma3(x, y, z):
    soma = x + y + z
    return soma
numero = []

for i in range(0, 3, 1):
    num = float(input("Informe {0}ª número: ".format(i+1)))
    numero.append(num)

print("A soma de: {0} + {1} + {2} = {3}".format(numero[0],numero[1],numero[2], soma3(numero[0], numero[1], numero[2])))

