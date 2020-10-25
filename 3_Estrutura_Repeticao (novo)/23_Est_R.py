# 23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

quant = 0
while(quant <= 0):
    quant = int(input("Informe os primeiros quantos numeros: "))
    if (quantidade <= 0):
        print("A quandidade deve ser positiva!")

quantDivisoes = 0
for num in range(1, quant + 1):
    primo = True
    for i in range(2, num / 2 + 1):
        quantDivisoes += 1
        if (num % i == 0):
            primo = False
            break

    if (primo):
        print num,

print ("\nQuantidade de divisoes: {0}".format(quantDivisoes))
