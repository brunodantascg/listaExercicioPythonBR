# Questão 2
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.


num = []

for i in range(0,10):
    num.append(float(input("Informe número: ")))

num.reverse()

print("Lista invertida: {0}".format(num))

for i in range(0,10):
    print(num[i])
