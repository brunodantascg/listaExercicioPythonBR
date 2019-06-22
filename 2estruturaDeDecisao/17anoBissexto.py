# Saber se ano é bissexto

ano = int(input("Informe ano: "))
biAno = ano % 4

if(biAno == 0):
    biAno = ano % 100
    if(biAno == 0):
        biAno = ano % 400
        if(biAno == 0):
            print("{} é um ano BISSEXTO!".format(ano))
        else:
            print("{} não é um ano bissexto".format(ano))
    else:
        print("{} não é um ano bissexto".format(ano))
else:
    print("{} não é um ano bissexto".format(ano))