# 1 - Faça um Programa que peça dois números e imprima o maior deles.

mensagem1 = str("Informe primeiro número: ")
mensagem2 = str("Informe segundo número: ")

num1 = float(input(mensagem1))
num2 = float(input(mensagem2))

if(num1 > num2):
    print("O número maior é: ", num1)

elif(num2 > num1):
    print("O número maior é: ", num2)

else:
    print(num1," é igual a o número ", num2)
