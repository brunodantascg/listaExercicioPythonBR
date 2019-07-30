# Questão 21

# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

print("Comparativo de Consumo de Combustivel")

veiculos = []
consumo = []
preco = 2.25

for i in range(1, 6):
    veiculos.append(input("Veiculo {}: ".format(i)))
    consumo.append(float(input("Km por litro: ")))

print("Relatorio Final")

for i in range(0, 5):
    custo = 1000 / consumo[i]
    gasto = custo * preco
    print("{0} - {1} - {2} - {3} litros - R$ {4}".format(i + 1, veiculos[i], consumo[i], custo, gasto))
    if ('menorConsumo' not in vars()) or (consumo[i] > consumo[menorConsumo]):
        menorConsumo = i

print("O menor consumo é do {0}".format(veiculos[menorConsumo])
