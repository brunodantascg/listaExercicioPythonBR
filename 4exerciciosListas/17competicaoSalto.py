# Questão 17

# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

texto = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
nomeAtleta = " "
saltos = []
atletas = []

while(nomeAtleta != " "):
    nomeAtleta = str(input("Atleta: ")
    if (nomeAtleta != " "):
        for i in texto:
            saltos.append(float(input("{0} Salto: ".format(texto[i])))
        atletas[nomeAtleta] = saltos

print("\nResultado Final: ")
for(nomeAtleta, saltos) in atletas.items():
    print("Atleta:  {0}".format(nomeAtleta))
    print("Saltos: {0}".format(saltos))
    somaSaltos = 0.0
    for salto in saltos:
        somaSaltos += salto
    print("Média dos Saltos {0}".format(somaSaltos / float(len(textoSaltos))))

                          
