# Questão 4

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetorCaracteres = []
consoantes = []

for i in range(0,10):
    while(True):
        letra = str(input("Informe {0}º caracter: ".format(i+1)))
        if(len(letra) == 1):
            vetorCaracteres.append(letra.upper())
            break
        else:
            print("Informe apenas UM caracter por vez!")

vogal = 0
consoante = 0
for i in range(0,10):
    x = vetorCaracteres[i]    
    if((x == "A") or (x == "E") or (x == "I") or (x == "O") or (x == "U")):
        vogal = vogal + 1
    else:
        consoante = consoante + 1
        consoantes.append(x)

print("Quantidade de Consoantes: {0}".format(consoante))
print("Consoantes: {0}".format(consoantes))
