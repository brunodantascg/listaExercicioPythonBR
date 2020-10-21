# 13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


base = int(input("Informe base: "))
exp = int(input("Informe expoente: "))
cal = 1

for i in range(1, exp+1, 1):
    cal = cal * base

print(base, "^", exp, " = ", cal)
    
