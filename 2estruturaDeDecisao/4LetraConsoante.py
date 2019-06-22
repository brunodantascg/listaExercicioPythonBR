# Verificar se a letra é vogal

letra = str(input("Informe a letra: "))
letra = letra.upper()

if(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
    print("a letra {} é uma vogal".format(letra))
else:
    print("A letra {} é uma consoante".format(letra))
