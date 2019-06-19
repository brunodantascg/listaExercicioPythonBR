# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe altura: "))

pesoIdealHomens = (72.7 * altura) - 58
pesoIdealMulheres = (62.1 * altura) - 44.7

print("Peso ideal para: Homens {0} | Mulheres {1}.".format(pesoIdealHomens, pesoIdealMulheres))
