# Questão 13

# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.


linhas = int(input("Informe número de linhas (1-20): ")
try:
    linhas = int(linhas)
    if(linhas > 20):
        raise Exception
except:
    linhas = 1
colunas = int(input("Informe número de colunas (1-20): ")
try:
    colunas = int(colunas)
    if(colunas > 20):
        raise Exception
except:
    colunas = 1
print(linhas, colunas)

tabela = []
for x in range(0, linhas + 2):
    if(x == 0 or x == linhas + 1):
        tabela.append("+")
    else:
        tabela.append("|")
for linha in range(0, linhas + 2):
    for coluna in range(0, colunas):
        if(linha == 0 or linha == linhas + 1):
            tabela[linha] += "-"
            if(coluna == colunas - 1):
                tabela[linha] += "+"
        else:
            tabela[linha] += " "
            if(coluna == colunas - 1):
                tabela[linha] += "|"

for linha in tabela:
    print(linha)
