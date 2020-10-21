# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:


ganhoHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe quantas horas trabalhadas: "))

salarioBruto = ganhoHora * horasTrabalhadas

inss = salarioBruto * 0.08
ir = salarioBruto * 0.11
sin = salarioBruto * 0.05

desconto = inss + ir + sin

print("+ Salário Bruto: R$ ", salarioBruto)
print("- IR: R$ ", ir)
print("- INSS: R$ ", inss)
print("- Sindicato: R$ ", sin)
print("= Salário Liquido: R$ ", salarioBruto - desconto)
