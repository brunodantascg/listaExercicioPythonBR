# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

informativo = str("Informe letra: ")

letra = str(input(informativo))

letra = letra.upper()

if((letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or
   (letra == 'U')):
    print("É uma vogal!")

else:
    print("É uma consoante!")
