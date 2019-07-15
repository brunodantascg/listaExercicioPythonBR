# População entre cidades

a = int(80000)
b = int(200000)
ano = 0
print(a)
print(b)

while(a != b):
    a = a + (a*0.03)
    print(a)
    b = b + (b*0.015)
    print(b)
    ano = ano + 1

print("Com {0} anos, a População A {1} será igual a População da B {2}".format(ano, a, b))