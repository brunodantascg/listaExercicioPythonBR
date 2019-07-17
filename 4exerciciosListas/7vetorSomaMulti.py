# Questão 7

# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []

for i in range(0,5):
    vetor.append(float(input("Informe {0}ª número: ".format(i+1))))

soma = 0
multi = 1

for i in range(0,5):
    num = vetor[i]
    soma = soma + num
    multi = multi * num

print("Soma: {0}".format(soma))
print("Multiplicação: {0}".format(multi))
print("Números: {0}".format(vetor))
