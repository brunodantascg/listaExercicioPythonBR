# Questão 19
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

soma = 0

while(True):
    n = int(input("Informa quantos números deseja verificar: "))
    if((n >= 0) and (n <=1000)):
        break
    print("Desculpe! Só podemos verificar entre 0 - 1000.")
    print()
    
nQuantidade = n

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
