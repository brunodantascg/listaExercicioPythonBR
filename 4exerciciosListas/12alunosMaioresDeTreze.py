# Questão 12

# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


alunos = []
totAlunos = 5

for i in range(0, totAlunos):
    aluno = []
    aluno.append(int(input("Informe a idade do aluno: ")))
    aluno.append(float(input("Informe a altura do aluno: ")))
    alunos.append(aluno)

somaAltura = 0.0
for aluno in alunos:
    somaAltura += aluno[1]

mediaAltura = somaAltura / float(totAlunos)

totAlunosAltos = 0
for aluno in alunos:
    if (aluno[0] >= 13) and (aluno[1] >= mediaAltura):
        totAlunosAltos += 1

print"Existem {0} alunos com mais de 13 anos acima da media de altura".format(totAlunosAltos))
