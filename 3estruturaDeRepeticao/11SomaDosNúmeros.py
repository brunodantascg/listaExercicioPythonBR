# Mostrar números inteiros do intervalo e mostrar a soma

num1 = int(input("Informe número um: "))
num2 = int(input("Informe número dois: "))
listaNum = []
num = num1
numm = num2
soma = 0

for i in range(num1, num2+1, 1):
    listaNum.append(i)

listaNum.remove(num)
listaNum.remove(numm)

print(listaNum)

while(len(listaNum) > 0):
    soma = listaNum.pop() + soma

print("A soma dos números: ", soma)