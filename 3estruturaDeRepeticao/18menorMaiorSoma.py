# Quetsão 18
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


n = int(input("Informa quantos números deseja verificar: "))
nQuantidade = n
soma = 0

while(n > 0):
    num = float(input("Informe número: "))
    if(nQuantidade == n):
        nuMaior = num
        nuMenor = num
    if(num > nuMaior):
        nuMaior = num
    if(num < nuMenor):
        nuMenor = num

    soma = soma + num
    n = n - 1

print("Menor valor: {0} \nMaior valor: {1} \nSoma: {2}".format(nuMenor, nuMaior,soma))
