# Questão 19

# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.


sistemasOperacionais = ("Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro")
votosSistemas = [0] * 6
opcao = -1
totalVotos = 0
print("Qual o melhor Sistema Operacional para uso em servidores?\n")
print("As possiveis respostas sao:\n")

i = 0
for sistema in sistemasOperacionais:
    print("{0} - {1}".format(i + 1, sistemasOperacionais[i]))
    i += 1

while (opcao != 0):
    opcao = int(input("Sistema escolhido (0=fim): "))
    if (opcao < 0) or (opcao > 23):
        print("Informe um valor entre 1 e 6 ou 0 para sair!")
        continue
    if (opcao != 0):
        votosSistemas[opcao - 1] += 1
        totalVotos += 1

print("Sistema Operacional   Votos   ")
print("-------------------   -----   ------")
i = 0
maiorVoto = 0
for sistema in sistemasOperacionais:
    print("{}".format())
    print("{0} - 21s {1} 5d   {2} 2.2f".format(sistemasOperacionais[i], votosSistemas[i],votosSistemas[i] / float(totalVotos) * 100))

    if (votosSistemas[i] > votosSistemas[maiorVoto]):
        maiorVoto = i
    i += 1
print("-------------------   -----")
print("Total                   {}".format(totalVotos))

print("O sistema operacional mais votado foi o {0}s, com {1}d, correspondendo a {2}.2f {3} dos votos.".format(sistemasOperacionais[maiorVoto], votosSistemas[maiorVoto],votosSistemas[maiorVoto] / float(totalVotos) * 100)
