# Mostrar números inteiros do intervalo

num1 = int(input("Informe número um: "))
num2 = int(input("Informe número dois: "))
listaNum = []
num = num1
numm = num2

for i in range(num1, num2+1, 1):
    listaNum.append(i)

listaNum.remove(num)
listaNum.remove(numm)

print(listaNum)