# Folha de pagamento

valorHora = float(input("Informe valor da sua hora R$: "))
quantHoraT = int(input("Informe quantas horas trabalhadas: "))
salarioBruto = valorHora * quantHoraT

if(salarioBruto > 900 and salarioBruto <= 1500):
    if(salarioBruto <=900):
        print("Isento")
    else:
        des = '5%'
        descontoIr = salarioBruto * 0.05
elif(salarioBruto > 1500 and salarioBruto <= 2500):
    des = '10%'
    descontoIr = salarioBruto * 0.10
elif(salarioBruto > 2500):
    descontoIr = salarioBruto * 0.20
    des = '20%'

fgts = salarioBruto * 0.11
inss = salarioBruto * 0.10
descontos = descontoIr + inss
salario = salarioBruto - descontos

print("Salário Bruto: R${}".format(salarioBruto))
print("(-) IR {0}: R${1}".format(des, descontoIr))
print("(-) INSS (10%): R${}".format(inss))
print("FGTS (11%): R${}".format(fgts))
print("Total de descontos: R${}".format(descontos))
print("Salário Líquido: R${}".format(salario))
