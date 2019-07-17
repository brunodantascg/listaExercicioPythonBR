# Quetsão 6

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
media = []

# Pedir notas de alunos
for a in range(0,4):
    soma = 0
    alunos.append(str(input("Informe nome do {}ª aluno: ".format(a+1))))
    for n in range(0,4):
        notas = float(input("Informe {}ª nota: ".format(n+1)))
        soma = soma + notas
    medias = soma/4
    media.append(medias)

mediaConta = 0

for i in range(0,4):
    m = media[i]
    if(m >= 7):
        mediaConta = mediaConta + 1
        # print("Aluno: {0}".format(alunos[i]))
        # print("Média: {}".format(media[i]))

print(" - - - - - ")
print("Número de alunos >= 7: {0}".format(mediaConta))
print(" - - - - - ")
