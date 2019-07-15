# Questão 21
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = 0
while(num <= 0):
    num = int(input("Informe número: "))
    if (num <= 0):
        print("O numero deve ser positivo!")

primo = True
for i in range(2, num / 2 + 1):
    if (num % i == 0):
        primo = False

if (primo):
    print("O numero eh primo")
else:
    print("O numero nao eh primo")
