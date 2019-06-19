# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# =  Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe quantas horas trabalhadas: "))
salarioBruto = ganhoHora * horasTrabalhadas
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = ir + inss + sindicato
salarioLiquido = salarioBruto - descontos

print("+ Salário Bruto: R$ {0} \n- IR (11%): R$ {1} \n- INSS (8%): R$ {2} \n- Sindicato (5%): R$ {3} \n= Salário Líquido: R$ {4}".format(salarioBruto, ir, inss, sindicato, salarioLiquido))
