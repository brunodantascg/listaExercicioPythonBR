# Calcular raízes de uma equação

print("Informe os três valores da equaaçao - ax2 + bx + c!")
a = float(input("Informe o valor de ax2"))
if(a != 0):
    b = float(input("Informe o valor de bx"))
    c = float(input("Informe o valor de c"))
    delta = b**2 - (4*a*c)
    if(delta >= 0):
        if(delta == 0):
            print("A equação possuí apenas uma raíz!")
        else:
            print("A equação possuí duas raízes!")
    else:
        print("Programa Encerrado! - Não possuí raizes reais.")
else:
    print("Programda Encerrado! - a igual a {}".format(a))