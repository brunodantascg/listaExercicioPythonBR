# Conceitos sobre notas

nota1 = float(input("Informe primeira nota: "))
nota2 = float(input("Informe segunda nota: "))
media = (nota1+nota2)/2

if(media > 9 and media <= 10):
    print("Sua média foi {}, com conceito A\nAprovado".format(media))
elif(media >= 7.5 and media < 9):
    print("Sua média foi {}, com conceito B\nAprovado".format(media))
elif(media >= 6 and media < 7.5):
    print("Sua média foi {}, com conceito C\nAprovado".format(media))
elif(media >= 4 and media < 6):
    print("Sua média foi {}, com conceito D\nReprovado".format(media))
elif(media >= 0 and media < 4):
    print("Sua média foi {}, com conceito E\nReprovado".format(media))

