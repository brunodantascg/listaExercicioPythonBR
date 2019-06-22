# saber se é um triangulo

lado1 = float(input("Informe lado: "))
lado2 = float(input("Informe lado: "))
lado3 = float(input("Informe lado: "))

if(lado1 + lado2 > lado3 or lado3 + lado2 > lado1 or lado1 + lado3 > lado2):
    print("É um triângulo")
    if(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
        print("Equilátero.")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um Triângulo!")