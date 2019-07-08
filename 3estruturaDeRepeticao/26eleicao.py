# Questão 26
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

quant = 0
while(quant <= 0):
    quant = int(input("Informe a quantidade de eleitores: "))
    if (quant <= 0):
        print("A quandidade deve ser positiva!")

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
for i in range(0, quant):
    voto = 0
    while(voto < 1) or (voto > 3):
        voto = int(input("Voce quer votar no candidato 1, 2 ou 3: "))
        if (voto < 1) or (voto > 3):
            print("Candidato invalido! Vote novamente")
    if (voto == 1):
        votosCandidato1 += 1
    elif (voto == 2):
        votosCandidato2 += 1
    else:
        votosCandidato3 += 1

print("Resultado:")
print("Candidato 1: {0}".format(votosCandidato1))
print("Candidato 2: {0}".format(votosCandidato2))
print("Candidato 3: {0}".format(votosCandidato3))
