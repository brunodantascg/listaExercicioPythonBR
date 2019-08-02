# Questão 10

# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randrange

def joga_dados():
    return randrange(1, 7, 1)

def obtem_valor():
    valor = 0
    for x in range(0, 2):
        valor += joga_dados()
    print("Valor obtido: {0}".format(valor))
    return valor

natural = [7, 11]
craps = [2, 3, 12]

valor = obtem_valor()
if(valor in natural):
    print("Natural")
    print("Ganhou!")
    exit()
elif(valor in craps):
    print("Craps")
    print("Perdeu!")
    exit()
else:
    ponto = valor
    print("Ponto")
    while(True):
        valor = obtem_valor()
        if(valor == ponto or valor == 7):
            if(valor == ponto):
                print("Ganhou!")
            elif(valor == 7):
                print("Perdeu!")
            brea
