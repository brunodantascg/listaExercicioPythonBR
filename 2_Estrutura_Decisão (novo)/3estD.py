# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

informativo = str("Informe sexo: ")

sexo = str(input(informativo))

if((sexo == 'F') or (sexo == 'f')):
    print("O sexo informato é F - Feminino")

elif((sexo == 'M') or (sexo == 'm')):
    print("O sexo informato é M - Masculino")

else:
    print("Sexo inválido")
