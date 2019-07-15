# Questão 21 
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# + Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# + Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import math

valorSaque = int(input("Informe valor para sacar R$: "))

notas100 = valorSaque / 100
notas100Correto = math.floor(notas100)
restoNotas100 = (notas100 - notas100Correto) * 100

notas50 = valorSaque / 50
notas50Correto = math.floor(notas50)
restoNotas50 = (notas50 - notas50Correto) * 50

notas10 = valorSaque / 10
notas10Correto = math.floor(notas10)
restoNotas10 = (notas100 - notas10Correto) * 10

notas5 = valorSaque / 5
notas5Correto = math.floor(notas5)
notas1 = (notas5 - notas5Correto) * 5

print("Notas de 100: R${0}, Notas de 50: R${1}, Notas de 10: R${2}, Notas de 5: R${3}, Notas de 1: R${4}".format(notas100Correto, notas50Correto, notas10Correto, notas5Correto, notas1))

