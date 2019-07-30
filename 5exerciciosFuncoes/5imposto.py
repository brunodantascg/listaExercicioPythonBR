# Exercício Funções - Questão 5

# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

from decimal import Decimal

def somaImposto(taxaImposto, custo):
    valorTotal = custo + (custo / Decimal ("100") * taxaImposto)
    return valorTotal

custo = Decimal(input("Custo: "))
taxaImposto = Decimal(input("Taxa de imposto: "))
valor = somaImposto(taxaImposto, custo)
print("Valor com imposto: R$ {0}".format(valor))
