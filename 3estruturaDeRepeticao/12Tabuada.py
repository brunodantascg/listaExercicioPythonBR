# Gerador de Tabuada

while(True):
    num = int(input("Informe número: "))

    for i in range(0, 11, 1):
        mul = i * num
        print("{0} x {1} = {2}".format(num, i, mul))

    con = str(input('Deseja continuar sim - não: '))
    con = con.upper()
    if(con == 'NÃO'):
        break
    else:
        print('Ok!')

print('Ótimo!')