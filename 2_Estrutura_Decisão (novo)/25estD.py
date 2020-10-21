# 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

r = 0

print("Responda 1-SIM ou 2-NÃO")

r1 = int(input("Telefonou para a vítima? "))
if(r1 == 1):
    r = r + 1

r2 = int(input("Esteve no local do crime? "))
if(r2 == 1):
    r = r + 1

r3 = int(input("Mora perto da vítima? "))
if(r3 == 1):
    r = r + 1

r4 = int(input("Devia para a vítima? "))
if(r4 == 1):
    r = r + 1

r5 = int(input("Já trabalhou com a vítima? "))
if(r5 == 1):
    r = r + 1

if(r == 2):
    print("Suspeito!")

elif(r >= 3 and r <= 4):
    print("Cumplice")

elif(r == 5):
    print("Assassino!")
