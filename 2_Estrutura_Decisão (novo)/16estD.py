# 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print("Informe valores de a, b,c para ax2+bx+c")

a = float(input("Informe o valor de a: "))

if(a != 0):
    b = float(input("Informe o valor de b: "))
    c = float(input("Iforme o valor de c: "))
    delta = ((b**2)-(4-a*c))
    if(delta < 0):
        print("Delta negativo! Não possui raízes reais!")

    elif((delta < 0)and(delta == 0)):
        print("A equação possui apenas uma raiz real!")

        equma = (-b)/2*a

        print("A Raíz é: ",equma)
        
    elif(delta > 0):
        print("A equação possui duas raízes reias!")

        eqdua1 = (-b+delta)/2*a
        eqdua2 = (-b-delta)/2*a

        print("A primeira Raíz é: ",eqdua1)
        print("A primeira Raíz é: ",eqdua2)

else:
    print("A equação não é do segundo grau!")

print("FIM!")
