# Quetsão 24

# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
    
from random import randrange

def dado():
    numero = randrange(1, 7, 1)
    return numero

lancamentos = []
for x in range(0, 100):
    lancamentos.append(dado())

for x in range(1, 7):
    print('Número {} foi conseguido {} vezes'.format(x, lancamentos.count(x)))
