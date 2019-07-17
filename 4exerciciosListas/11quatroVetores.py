# Questão 11

# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetorA = []
vetorB = []
vetorC = []
vetorABC = []

for i in range(0,10):
    vetorA.append(float(input("Informe número para vetor A: ")))
    vetorB.append(float(input("Informe número para vetor B: ")))
    vetorC.append(float(input("Informe número para vetor C: ")))

for i in range(0,10):
    vetorABC.append(vetorA[i])
    vetorABC.append(vetorB[i])
    vetorABC.append(vetorC[i])    

print(vetorABC)
