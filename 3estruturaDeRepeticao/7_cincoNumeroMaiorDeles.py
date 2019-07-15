# Informar cinco número e informar o maior deles

lista = []

for i in range(1, 6, 1):
    num = int(input("Informe número: "))
    lista.append(num)

lista.sort()
print(lista.pop())
