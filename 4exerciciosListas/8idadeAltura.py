# Questão 8

# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(0,5):
    idade.append(int(input("Informe {}ª idade: ".format(i+1))))
    altura.append(float(input("Informe {}ª altura: ".format(i+1))))

print("-- Lista Inicial --")
print("Idade: {0}".format(idade))
print("Altura: {0}".format(altura))

idade.reverse()
altura.reverse()

print("-- Lista Inversar --")
print("Idade: {0}".format(idade))
print("Altura: {0}".format(altura))
