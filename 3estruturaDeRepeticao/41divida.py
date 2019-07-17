# Questão 41

# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

from decimal import *
getcontext().prec = 2

valorDivida = Decimal(input("Informe o valor da dívida: "))
print("Valor da dívida Valor dos Juros Quantidade de parcelas Valor da parcela")
print('{0}             0               1                      {1}'.format(valorDivida, valorDivida))
quantidadeParcelas = 0
porcentagemJuros = 0
for x in range(0,4):
    quantidadeParcelas += 3
    porcentagemJuros += 5
    valorJuros = valorDivida / 100 * porcentagemJuros
    valorDividaJuros = valorDivida + valorJuros
    valorParcela = valorDividaJuros / quantidadeParcelas
    print("{0}             {1}               {2}                      {3}".format(valorDividaJuros, valorJuros, quantidadeParcelas, valorParcela))
    
