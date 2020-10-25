# 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

v = 0
nume = 0

while True:
    num = float(input("Informe número: "))
    v = v + 1
    nume = nume + num
    var = str(input("Deseja informar outro número? S - sim e N - não"))
    if(var == 's'):
        print("ok")
    else:
        break

media = nume/v

print("Média: ", media)

