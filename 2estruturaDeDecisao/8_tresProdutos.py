# Valores de 3 produtos e saber qual o menor

p1 = float(input("Informe preço do primeiro produto: "))
p2 = float(input("Informe preço do segundo produto: "))
p3 = float(input("Informe preço do terceiro produto: "))

if(p1 < p2 and p1 < p3):
    print("O primeiro produto, por R${} é a melhor opção".format(p1))
elif(p2 < p1 and p2 < p3):
    print("O primeiro produto, por R${} é a melhor opção".format(p2))
else:
    print("O primeiro produto, por R${} é a melhor opção".format(p3))
