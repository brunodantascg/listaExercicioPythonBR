# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

infor = str("Informe ")
infoNumero1 = str(" primeira ")
infoNumero2 = str(" segunda ")
infoNota = str(" nota parcial do aluno: ")

nota1 = float(input(infor + infoNumero1 + infoNota))
nota2 = float(input(infor + infoNumero2 + infoNota))

media = (nota1+nota2)/2

if(media >= 7):
    if(media == 10):
        print("Aluno Aprovado com Distinção!")
    else:
        print("Aluno Aprovado!")

elif(media < 7):
    print("Aluno Reprovado!")

