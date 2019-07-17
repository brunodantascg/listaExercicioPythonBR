# Questão 40

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidadesMenosDe2000 = 0
somaDeAcidentes = 0
totalDeVeiculos = 0
totalDeAcidentes = 0

for x in range(0, 5):
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos em 1999: "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas em 1999: "))
    if(x == 0):
        maiorIndice = acidentes
        menorIndice = acidentes
        codigoMaiorIndice = codigo
        codigoMenorIndice = codigo
    if(acidentes > maiorIndice):
        maiorIndice = acidentes
        codigoMaiorIndice = codigo
    if(acidentes < menorIndice):
        menorIndice = acidentes
        codigoMenorIndice = codigo
    if(veiculos < 2000):
        totalDeAcidentes += acidentes
        cidadesMenosDe2000 += 1
    totalDeVeiculos += veiculos

if(cidadesMenosDe2000 != 0):
    mediaAcidentes = totalDeAcidentes / cidadesMenosDe2000
else:
    mediaAcidentes = 0

mediaVeiculos = totalDeVeiculos / 5

print("Maior índice de acidente de trânsito Código: {0} Quantidade de veículos: {1}".format(codigoMaiorIndice, maiorIndice))
print("Menor índice de acidente de trânsito Código: {0} Quantidade de veículos: {1}".format(codigoMenorIndice, menorIndice))
print("Média de veículos: {0}".format(mediaVeiculos))
print("Média de acidentes em cidades com menos de 2000 veículos: {0}".format(mediaAcidentes))
