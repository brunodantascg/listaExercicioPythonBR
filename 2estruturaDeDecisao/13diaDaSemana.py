# Dia da semana

while(True):
    num = int(input("Informe número: "))
    if(num >= 1 and num <= 7):
        break
    else:
        print("Número informado inválido, informe novamente \n")

if(num == 1):
    print("{} - Segunda".format(num))
elif(num == 2):
    print("{} - Terça".format(num))
elif(num == 3):
    print("{} - Quarta".format(num))
elif(num == 4):
    print("{} - Quinta".format(num))
elif(num == 5):
    print("{} - Sexta".format(num))
elif(num == 6):
    print("{} - Sabádo".format(num))
elif(num == 7):
    print("{} - Domingo".format(num))
