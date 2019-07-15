# Cinco Perguntas - Polícia

q = 0
print('Responda Sim ou Não')

res1 = str(input("Telefonou para a vítima? "))
res1 = res1.upper()
if(res1 == 'SIM'):
    q = q + 1
res2 = str(input("Esteve no local do crime? "))
res2 = res2.upper()
if(res2 == 'SIM'):
    q = q + 1
res3 = str(input("Mora perto da vítima? "))
res3 = res3.upper()
if(res3 == 'SIM'):
    q = q + 1
res4 = str(input("Devia a vítima? "))
res4 = res4.upper()
if(res4 == 'SIM'):
    q = q + 1
res5 = str(input("Já trabalhou com a vítima? "))
res5 = res5.upper()
if(res5 == 'SIM'):
    q = q + 1

def particicao(q):
    if(q == 1):
        return 'Inocente'
    elif(q == 2):
        return 'Suspeito'
    elif(q >= 3 and q <= 4):
        return 'Cúmplice'
    elif(q == 5):
        return 'Assassino'

print(particicao(q))