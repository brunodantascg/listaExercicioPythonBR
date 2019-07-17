# Questão 42

# Armazenar números em determinados intervalos

# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.


lista25 = []
lista50 = []
lista75 = []
lista100 = []

while(True):
    num = int(input("Informe número: "))
    if(num >= 0 and num <= 25):
        lista25.append(num)
    elif(num > 25 and num <=50):
        lista50.append(num)
    elif(num > 50 and num <= 75):
        lista75.append(num)
    elif(num > 75 and num <=100):
        lista100.append(num)
    elif(num < 0):
        break

print("No intervaldo de 0 - 25  tem {} números".format(len(lista25)))
print("No intervaldo de 26 - 50  tem {} números".format(len(lista50)))
print("No intervaldo de 51 - 75  tem {} números".format(len(lista75)))
print("No intervaldo de 76 - 100  tem {} números".format(len(lista100)))