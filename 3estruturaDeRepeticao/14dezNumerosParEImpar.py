# Pedir 10 números e calcular ser é par ou ímpar

listaImpar = []
listaPar = []

for i in range(1, 11, 1):
    num = int(input('Informe {} número: '.format(i)))
    if(num % 2 == 0):
        listaPar.append(num)
    else:
        listaImpar.append(num)

print('Números ímpares', listaImpar)
print('Números pares', listaPar)

