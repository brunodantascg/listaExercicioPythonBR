# Valor positivo, dois números

num1 = int(input("Informe número: "))

if(num1 > 0):
    print("O número {} é positivo".format(num1))
elif(num1 < 0):
    print("O número {} é negativo".format(num1))
else:
    print("{} é neutro".format(num1))
    