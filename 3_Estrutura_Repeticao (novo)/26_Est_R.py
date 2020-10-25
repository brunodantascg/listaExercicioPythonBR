# 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input("Qual o número total de eleitores: "))
msn1 = str("Eleitor nº ")
msn2 = str(" informe seu voto: ")

candi1 = str(" Candidato 1 ")
candi2 = str(" Candidato 2 ")
candi3 = str(" Candidato 3 ")
votoB = str(" Voto em Branco 4 ")

voto1 = 0
voto2 = 0
voto3 = 0
votoBranco = 0

for i in range(1, eleitores+1, 1):
    s = str(i)
    print(candi1)
    print(candi2)
    print(candi3)
    print(votoB)
    while True:
        voto = int(input(msn1 + s + msn2))
        if(voto > 0 and voto <=4):
            break
        else:
            print("Informe voto correto!")

    if(voto == 1):
        voto1 = voto1 + 1
    if(voto == 2):
        voto2 = voto2 + 1
    if(voto == 3):
        voto3 = voto3 + 1
    if(voto == 4):
        votoB = votoB + 1

print(" VOTOS CONTABILIZADOS ")
print("Candidato 1: ", voto1)
print("Candidato 2: ", voto2)
print("Candidato 3: ", voto3)
print("Votos em Branco: ", votoB)
