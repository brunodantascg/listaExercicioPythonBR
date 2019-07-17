# Questão 10

# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorA = []
vetorB = []
vetorAB = []

for i in range(0,10):
    vetorA.append(float(input("Informe número para vetor A: ")))
    vetorB.append(float(input("Informe número para vetor B: ")))

for i in range(0,10):
    vetorAB.append(vetorA[i])
    vetorAB.append(vetorB[i])

print(vetorAB)
