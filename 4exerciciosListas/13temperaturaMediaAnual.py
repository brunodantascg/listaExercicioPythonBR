# Questão 13

# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturaMedia = []

for i in range(0,12):
    temperaturaMedia.append(float(input("Informe temperatura média de {0}: ".format(mes[i]))))

mediAnual = 0

for i in range(0,12):
    t = temperaturaMedia[i]
    mediAnual = mediAnual + t

media = mediAnual/12

print("Média anual: {0}º".format(media))
print(" ")
print("Meses que a temperatura foi acima da média anual")
print(" ")
for i in range(0,12):
    t1 = temperaturaMedia[i]    
    if(t1 > media):
        print("{0} - {1}º".format(mes[i], temperaturaMedia[i]))
