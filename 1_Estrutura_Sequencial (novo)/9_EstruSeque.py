# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Informe temperatura em Fahrenheit: "))

celsius = 5 * ((fahrenheit-32)/9)

print("A temperatura ", fahrenheit, " graus Fahrenheit é equivalente a ", celsius, " graus Celsius.")
