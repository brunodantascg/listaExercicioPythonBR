# Média de três notas

nota1 = float(input("Informe primeira nota: "))
nota2 = float(input("Informe segunda nota: "))
nota3 = float(input("Informe terceira nota: "))
media = (nota1+nota2+nota3)/3

if(media >= 7 and media <10):
    print("{} - você foi aprovado".format(media))
elif(media <7 and media >=0):
    print("{} - você foi reprovado".format(media))
elif(media == 10):
    print("{} - você foi aprovado com distinção".format(media))
else:
    print("{} - média errada.".format(media))
