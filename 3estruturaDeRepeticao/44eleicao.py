# Questão 44

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

from decimal import Decimal

class Candidato():
    def __init__(self, nome):
        self.nome = nome
        self.votos = 0
        
    def vota(self):
        self.votos += 1

dantas = Candidato("Dantas")
cardoso = Candidato("Cardoso")
joao = Candidato("João")
jesus = Candidato("Jesus")
nulo = Candidato("Voto nulo")
branco = Candidato("Voto em branco")
candidatos = {1: dantas, 2: cardoso, 3: joao, 4: jesus, 5: nulo, 6: branco}
totalVotos = 0
votacao = True
votoInvalido = True

while(votacao):
    for candidato in candidatos:
        print("{} - {}".format(candidato, candidatos[candidato].nome))
    print("0 - Encerra")
    voto = int(input("Entre com o voto: "))
    if(voto == 0):
        votacao = False
    elif(voto in candidatos):
        candidatos[voto].vota()
        totalVotos += 1
    else:
        print("Voto inválido!")

for candidato in candidatos:
    print("{}: {}".format(candidatos[candidato].nome, candidatos[candidato].votos))

percentualNulo = 100 / totalVotos * candidatos[5].votos
percentualBranco = 100 / totalVotos * candidatos[6].votos
print("Percentual de votos nulos: {0}".format(percentualNulo))
print("Percentual de votos em branco: {0}".format(percentualBranco))
