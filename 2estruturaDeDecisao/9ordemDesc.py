# Ordem decrescente

lista = []

n1 = int(input("Informe número "))
n2 = int(input("Informe número "))
n3 = int(input("Informe número "))

lista.append(n1)
lista.append(n2)
lista.append(n3)

lista.sort(reverse=False)

print(lista)