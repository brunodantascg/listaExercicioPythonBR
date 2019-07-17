# Questão 39

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas

alunos = []
for x in range(0, 10):
    numero = int(input("Número do {0}o. aluno: ".format(x + 1)))
    altura = int(input("Altura em centímetros: "))
    if(x == 0):
        maior_altura = altura
        menor_altura = altura
    if(altura > maior_altura):
        maior_altura = altura
        maior_aluno = numero
    if(altura < menor_altura):
        menor_altura = altura
        menor_aluno = numero

print("Maior aluno Número: {} Altura: {}".format(maior_aluno, maior_altura))
print("Menor aluno Número: {} Altura: {}".format(menor_aluno, menor_altura))
