# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Informe quanto você ganha por hora: "))
horasTrabalhadas = int(input("Informe quantas horas trabalhadas: "))
salario = ganhoHora * horasTrabalhadas

print("Salário: R$ {0}".format(salario))
