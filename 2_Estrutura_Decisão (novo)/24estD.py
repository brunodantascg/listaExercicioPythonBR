# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input("Informe primeiro número: "))
num2 = float(input("Informe segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

ope = int(input("Informe qual operação deseja fazer: "))

if((ope == 1)or(ope == 2)or(ope == 3)or(ope == 4)):
    if(ope == 1):
        soma = num1 + num2
        print("Resultado da soma: ",soma)

        if((soma // 1) == soma):
            print("inteiro")
            if((soma % 2) == 0):
                print("par")
            else:
                print("impar")
        else:
            print("decimal")

        if(soma >= 0):
            print("positivo")
        else:
            print("negativo")


    elif(ope == 2):
        sub = num1 - num2
        print("Resultado da Subtração: ", sub)

    elif(ope == 3):
        div = num1/num2
        print("Resultado da Divisão: ", div)

    else:
        mul = num1 * num2
        print("Resultado da Multiplicação: ", mul)
        
else:
    print("Operação ERRADA")

