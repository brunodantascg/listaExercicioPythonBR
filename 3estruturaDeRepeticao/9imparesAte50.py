# Imprimir números ímpares de 1 até 50

listaImpares = []
listaPares = []

for i in range(1, 51):
    im = i%2
    if(im != 0):
        listaImpares.append(i)
    else:
        listaPares.append(i)

print("Lista Ímpares: ", listaImpares)
print("Lista Pares: ", listaPares)
