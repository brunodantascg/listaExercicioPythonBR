# Questão 9

# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetorA = []

for i in range(0,10):
    vetorA.append(int(input("Informe o {}ª número: ".format(i+1))))

somaQuadrados = 0
for numero in vetorA:
    somaQuadrados += (numero * numero)

print("A soma dos quadrados dos numeros lidos é {0}".format(somaQuadrados))
