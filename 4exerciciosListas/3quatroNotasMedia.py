# Questão 3

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(0,4):
    notas.append(float(input("Informe {0}º nota: ".format(i+1))))

somaNotas = 0
for i in range(0,4):
    n = notas[i]
    somaNotas = somaNotas + n

media = somaNotas / 4

print(" - - - - - ")
print("1º nota - {0} \n2º nota - {1} \n3º nota - {2} \n4º nota - {3} \n".format(notas[0],notas[1],notas[2],notas[3]))
print("Media - {0}".format(media))
print(" - - - - - ")

