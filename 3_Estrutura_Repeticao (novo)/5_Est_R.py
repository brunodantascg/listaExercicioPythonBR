# 5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

cresA = float(input("Informe taxa de crescimento da cidade A: "))
cresB = float(input("Informe taxa de crescimento da cidade B: "))

popuA = int(input("Informe população da cidade A: "))
popuB = int(input("Informe população da cidade B: "))

ano = 0

while (popuA < popuB):
    taxaA = popuA * cresA
    taxaB = popuB * cresB

    popuA = popuA + taxaA
    popuB = popuB + taxaB
    
    ano = ano + 1


print(ano)
