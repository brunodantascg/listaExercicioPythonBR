# Data Válida

print("Informe DATA - dd/mm/aaaa")
dd = int(input("Informe dd: "))
mm = int(input("Informe mm: "))
aaaa = int(input("Informe aaaa: "))

def bissexto(aaaa):
    biAno = aaaa % 4
    if (biAno == 0):
        biAno = aaaa % 100
        if (biAno == 0):
            biAno = aaaa % 400
            if (biAno == 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if(aaaa >= 0000 and aaaa <= 9999):
    if(mm > 0 and mm <=12):
        if((dd > 0 and dd <= 31) and (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12)):
            print("A data é válida.")
            if(bissexto(aaaa) == True):
                print("O ano é bissexto")
            else:
                print("O ano não é bissexto")
        elif((dd > 0 and dd <=30) and(mm == 4 or mm == 6 or mm == 9 or mm == 11)):
            print("A data é válida.")
            if(bissexto(aaaa) == True):
                print("O ano é bissexto")
            else:
                print("O ano não é bissexto")
        elif(dd == 28):
            print("A data é válida.")
            if(bissexto(aaaa) == True):
                print("O ano é bissexto")
            else:
                print("O ano não é bissexto")
        elif(dd == 29):
            print("A data é válida.")
            print("O ano é bissexto.")
        else:
            print("{} o dd é inválido.".format(dd))
    else:
        print("{} o mês é inválido.".format(mm))
else:
    print("{} o ano é inválido.".format(aaaa))