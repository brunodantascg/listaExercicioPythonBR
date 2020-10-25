# 25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

pessoas = int(input("Informe a quantidade de pessoas da turma: "))
msn1 = str("Infome idade da ")
msn2 = str("ª pessoa: ")
idadet = 0

for i in range(1, pessoas+1, 1):
    s = str(i)
    idade = int(input(msn1 + s + msn2))
    idadet = idadet + idade

medidade = idadet/pessoas

print("Média de idade da turma: ", medidade)

if(medidade > 0 and medidade <= 25):
    print("Média de idade é entre 0 e 25 anos")
    print("Turma Jovem!")

elif(medidade > 25 and medidade <= 60):
    print("Média de idade é entre 25 e 60 anos")
    print("Turma Adulta!")

else:
    print("Maior de 60 anos")
    print("Turma Idosa!")
