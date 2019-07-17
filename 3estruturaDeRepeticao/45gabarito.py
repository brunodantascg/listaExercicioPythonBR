# Questão 45

# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A Média das Notas da Turma.

# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
possiveis_respostas = ['A', 'B', 'C', 'D', 'E']
alunos = []
continua = "S"
while(continua == "S"):
    print("{}o. aluno".format(len(alunos) + 1))
    acertos = 0
    for x in range(0, 10):
        resposta = "X"
        while(resposta not in possiveis_respostas):
            resposta = input("{}a. resposta: ".format(x + 1)).upper()
            if(resposta not in possiveis_respostas):
                print("Entre com uma resposta válida! A, B, C, D ou E")
            else:
                if(resposta == gabarito[x]):
                    acertos += 1
    alunos.append(acertos)
    continua = input("Continua? s/n: ").upper()

print("Maior acerto: {}".format(max(alunos)))
print("Menor acerto: {}".format(min(alunos)))
print("Total de alunos: {}".format(len(alunos)))
print("Média de acertos: {}".format(sum(alunos) / len(alunos)))
