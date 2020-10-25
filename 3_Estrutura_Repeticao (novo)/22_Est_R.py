# 22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = 0
while(num <= 0):
    num = int(input("Informe número: "))
    if (num <= 0):
        print("O numero deve ser positivo!")

primo = True
for i in range(2, num / 2 + 1):
    if (num % i == 0):
        primo = False
        break

if (primo):
    print("O numero eh primo")
else:
    print("O numero nao eh primo")
    print("Ele eh divisivel por")
    for i in range(1, num + 1):
        if (num % i == 0):
            print(i)
