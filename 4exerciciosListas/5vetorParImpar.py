# Questão 5

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numInteiros = []
numPar = []
numImpar = []

for i in range(0,20):
    num = int(input("Informe número: "))
    numInteiros.append(num)
    if((num % 2) == 0):
        numPar.append(num)
    else:
        numImpar.append(num)

print("-- VETORES --")
print("Vetor completo: {0}".format(numInteiros))
print("Vetor de Pares: {0}".format(numPar))
print("Vetor de Impares: {0}".format(numImpar))
