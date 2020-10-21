# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Informe quanto você ganha por hora: R$"))

horasTrabalhadas = int(input("Informe quantas horas trabalhas: "))

salario = ganhoHora * horasTrabalhadas

print("Seu salário é R$", salario)
