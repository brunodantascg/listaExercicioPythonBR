# nota válida

while(True):
    nota = float(input("Informe uma nota de 0 - 10: "))
    if(nota >= 0 and nota <= 10):
        break
    else:
        print("A nota informada é inválida! Digite novamente.")

