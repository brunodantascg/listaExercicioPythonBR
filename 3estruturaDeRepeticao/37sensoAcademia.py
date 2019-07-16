# Questão 37
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

from decimal import Decimal

class Aluno(object):
    def __init__(self, matricula, peso, altura):
        self.matricula = matricula
        self.peso = peso
        self.altura = altura

def cadastra_aluno(matricula):
    peso = Decimal(input('Peso: '))
    altura = Decimal(input('Altura: '))
    alunos.append(Aluno(matricula, peso, altura))

alunos = []
while(True):
    matricula = int(input('Entre com a matrícula: '))
    if(matricula == 0):
        break
    cadastra_aluno(matricula)

maior_peso = alunos[0].peso
aluno_maior_peso = alunos[0].matricula
menor_peso = alunos[0].peso
aluno_menor_peso = alunos[0].matricula
maior_altura = alunos[0].altura
aluno_maior_altura = alunos[0].matricula
menor_altura = alunos[0].altura
aluno_menor_altura = alunos[0].matricula
soma_peso = 0
soma_altura = 0
for aluno in alunos:
    if(aluno.peso >= maior_peso):
        aluno_maior_peso = aluno.matricula
        maior_peso = aluno.peso
    if(aluno.peso <= menor_peso):
        aluno_menor_peso = aluno.matricula
        menor_peso = aluno.peso
    if(aluno.altura >= maior_altura):
        aluno_maior_altura = aluno.matricula
        maior_altura = aluno.altura
    if(aluno.peso <= menor_altura):
        aluno_menor_altura = aluno.matricula
        menor_altura = aluno.altura
    soma_altura += aluno.altura
    soma_peso += aluno.peso

media_altura = soma_altura / len(alunos)
media_peso = soma_peso / len(alunos)
print(
    'Maior peso: {}, matrícula {}'.format(maior_peso, aluno_maior_peso))
print(
    'Menor peso: {}, matrícula {}'.format(menor_peso, aluno_menor_peso))
print(
    'Maior altura: {}, matrícula {}'.format(maior_altura, aluno_maior_altura))
print(
    'Menor altura: {}, matrícula {}'.format(menor_altura, aluno_menor_altura))
print('Altura média: {}'.format(media_altura))
print('Peso médio: {}'.format(media_peso))
