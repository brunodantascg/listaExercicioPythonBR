# Maior número de três

num1 = float(input("Informe primeiro número: "))
num2 = float(input("Informe segundo número: "))
num3 = float(input("Informe terceiro número: "))

if(num1 > num2 and num1 > num3):
    print("O maior número é {}".format(num1))
elif(num2 > num1 and num2 > num3):
    print("O maior número é {}".format(num2))
else:
    print("O maior número é {}".format(num3))
