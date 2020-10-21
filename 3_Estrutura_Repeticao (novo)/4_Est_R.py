# 4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

cresA = 0.03
cresB = 0.015

popuA = 80000
popuB = 200000

ano = 0

while (popuA < popuB):
    taxaA = popuA * cresA
    taxaB = popuB * cresB

    popuA = popuA + taxaA
    popuB = popuB + taxaB
    
    ano = ano + 1


print(ano)
