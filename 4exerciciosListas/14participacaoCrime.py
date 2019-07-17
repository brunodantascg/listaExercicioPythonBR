# Questão 14

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a: 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []

print("Responda 1 - SIM ou 2 - NÃO")
print(" ")
for i in range(0,5):
    while(True):
        x = int(input("{0}ª Pergunta: {1} - ".format(i+1, perguntas[i])))
        if((x == 1) or (x == 2)):
            respostas.append(x)
            break
        else:
            print(" ")
            print("A resposta só pode ser 1 - SIM ou 2 - NÃO. Responda novamente!")
            print(" ")    

if(respostas.count(1) == 2):
    print("Suspeito")
elif((respostas.count(1) >= 3) and (respostas.count(1) <= 4)):
    print("Cúmplice")
elif(respostas.count(1) == 5):
    print("Assassino")
else:
    print("Inocente")
