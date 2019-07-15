# frase de bom dia

turno = str(input("Informe Turno: "))
turno = turno.upper()

if(turno == 'M'):
    print("M-matutino")
    print("Bom dia!")
elif(turno == 'V'):
    print("V-vespertino")
    print("Bom Tarde!")
elif(turno == 'N'):
    print("N=noturno")
    print("Boa Noite!")
else:
    print("{} valor inválido".format(turno))