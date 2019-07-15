# Maior e Menor número

num1 = float(input("Informe número: "))
num2 = float(input("Informe número: "))
num3 = float(input("Informe número: "))

if(num1 > num2 and num1 > num3):
    print("{} é o maior número".format(num1))
    if(num2 > num3):
        print("E {} é o menor número".format(num3))
    else:
        print("E {} é o menor número".format(num2))
elif(num2 > num1 and num2 > num3):
    print("{} é o maior número".format(num2))
    if(num1 > num3):
        print("E {} é o menor número".format(num3))
    else:
        print("E {} é o menor número".format(num1))
else:
    print("{} é o maior número".format(num3))
    if(num2 > num1):
        print("E {} é o menor número".format(num1))
    else:
        print("E {} é o menor número".format(num2))
