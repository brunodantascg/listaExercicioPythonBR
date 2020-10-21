# 3 - Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


while True:
    nome = str(input("Informe Nome: "))
    if(len(nome) <= 3):
        print("Nome com mais de 3 caracteres!")
    else:
        print("Nome ok!")
        break

while True:
    idade = int(input("Informe Idade: "))
    if((idade > 0)and(idade <=150)):
        print("Idade ok!")
        break
    else:
        print("Idade entre 0 e 150 anos")

while True:
    salario = float(input("Informe Salário R$:"))
    if(salario > 0):
        print("Salário ok!")
        break
    else:
        print("Salário precisa ser maior que R$ 0.00")

while True:
    sexo = str(input("Informe Sexo 'f' ou 'm': "))
    if((sexo == 'f')or(sexo == 'm')):
        print("Sexo ok!")
        break
    else:
        print("Informação de sexo diferente da esperada")

while True:
    estCivil = str(input("Informe Estado Civil 's' - 'c' - 'v' - 'd': "))
    if((estCivil == 's')or(estCivil == 'c')or(estCivil == 'v')or(estCivil == 'd')):
        print("Estado Civil ok!")
        break
    else:
        print("Informação de sexo diferente da esperada")


print("Cadastro Realizado com Sucesso!")
