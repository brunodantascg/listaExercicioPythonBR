# Ler número menor que mil (centenas dezenas unidades)

while(True):
    num = int(input("Informe número menor do que 1000: "))
    if(num >= 0 and num <=1000):
        break
    else:
        print("Número menor ou igual a 1000")

num1 = str(num)
num1 = len(num1)

#centenas dezenas unidades

if(num1 == 4):
    centenas = num//100
    if(centenas > 1):
        print("{} centenas.".format(centenas))
    else:
        print("{} centena.".format(centenas))
    dezenasR = num%100
    dezenas = dezenasR//10
    if(dezenas > 1):
        print("{} Dezenas.".format(dezenas))
    else:
        print("{} Dezena.".format(dezenas))
    unidadesR = dezenas%10
    unidade = unidadesR
    if(unidade > 1):
        print("{} Unidades".format(unidade))
    else:
        print("{} Unidade".format(unidade))

elif(num1 == 3):
    centenas = num//100
    if(centenas > 1):
        print("{} centenas.".format(centenas))
    else:
        print("{} centena.".format(centenas))
    dezenasR = num%100
    dezenas = dezenasR//10
    if(dezenas > 1):
        print("{} Dezenas.".format(dezenas))
    else:
        print("{} Dezena.".format(dezenas))
    unidadesR = dezenasR%10
    unidade = unidadesR
    if(unidade > 1):
        print("{} Unidades".format(unidade))
    else:
        print("{} Unidade".format(unidade))

elif(num1 == 2):
    centenas = num//100
    if(centenas > 1):
        print("{} centenas.".format(centenas))
    else:
        print("{} centena.".format(centenas))
    dezenas = num//10
    if(dezenas > 1):
        print("{} Dezenas.".format(dezenas))
    else:
        print("{} Dezena.".format(dezenas))
    unidadesR = num%10
    unidade = unidadesR
    if(unidade > 1):
        print("{} Unidades".format(unidade))
    else:
        print("{} Unidade".format(unidade))

elif(num1 == 1):
    centenas = num//100
    if(centenas > 1):
        print("{} centenas.".format(centenas))
    else:
        print("{} centena.".format(centenas))
    dezenas = num//10
    if(dezenas > 1):
        print("{} Dezenas.".format(dezenas))
    else:
        print("{} Dezena.".format(dezenas))
    unidadesR = num%10
    unidade = unidadesR
    if(unidade > 1):
        print("{} Unidades".format(unidade))
    else:
        print("{} Unidade".format(unidade))