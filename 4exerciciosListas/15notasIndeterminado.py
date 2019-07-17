# Questão 15

# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

num = 0
valores = []

while(num != -1):
    while(True):
        notas = float(input("Informe nota: "))
        if((notas >= -1) and (notas <=10) ):
            if(notas == -1):
                print(" ")
                print("Armazenamento encerrado!")
                print(" ")
                break
            valores.append(notas)
        else:
            print("Valor da nota errado (0 - 10). Informe Novamente!\n")

    if(notas == -1):
        break

print("a. Foram informados {0} valores.".format(len(valores))) # a. Mostre a quantidade de valores que foram lidos;
print("b. Valores informados: {0}".format(valores)) # b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;

# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("c. Valores inverso: ")
valores.reverse()
for i in range(0, len(valores)):
    print(valores[i])

# d. Calcule e mostre a soma dos valores;
print("d. Soma dos Valores: {0}".format(sum(valores)))

# e. Calcule e mostre a média dos valores;
print("e. Média dos Valores: {0}".format(sum(valores)/len(valores)))

# f. Calcule e mostre a quantidade de valores acima da média calculada;
media = sum(valores)/len(valores)
valorAcima = []
for i in range(0, len(valores)):
    va = valores[i]
    if(va > media):
        valorAcima.append(va)        

print("f. Valores acima da média: {0}".format(valorAcima))

# g. Calcule e mostre a quantidade de valores abaixo de sete;
valorAbaixo = []
for i in range(0, len(valores)):
    vb = valores[i]
    if(vb < 7):
        valorAbaixo.append(vb)  

print("f. Valores abaixo de 7: {0}".format(valorAbaixo))

# h. Encerre o programa com uma mensagem;
print(" ")
print("Programa Encerrado!")


