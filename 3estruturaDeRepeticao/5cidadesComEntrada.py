# População entre cidades

a = int(input("Informe população da cidade A: "))
b = int(input("Informe população da cidade B: "))
taxaA = float(input("Informe a taxa de crescimento da população A: "))
taxaA = taxaA / 100
taxaB = float(input("Informe a taxa de crescimento da população B: "))
taxaB = taxaB / 100
ano = 0
print(a)
print(b)

while(a != b):
    a = a + (a*taxaA)
    print(a)
    b = b + (b*taxaB)
    print(b)
    ano = ano + 1

print("Com {0} anos, a População A {1} será igual a População da B {2}".format(ano, a, b))