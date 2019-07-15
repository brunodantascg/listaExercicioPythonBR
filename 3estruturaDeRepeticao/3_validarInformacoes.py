# Validar Informações

while(True):
    nome = str(input("Informe nome: "))
    if(len(nome) > 3):
        break
    else:
        print("O nome deve ser maior que 3 carecteres.")

while(True):
    idade = int(input("Informe idade: "))
    if(idade > 0 and idade <= 150):
        break
    else:
        print("Idade errada. Informe novamente")

while(True):
    salario = float(input("Informe salário: "))
    if(salario > 0):
        break
    else:
        print("Valor do salário errado.")

while(True):
    sexo = str(input("Informe sexo: "))
    sexo = sexo.upper()
    if(sexo == 'F' or sexo == 'M'):
        break
    else:
        print("Informe sexo válido.")

while(True):
    estado = str(input("Informe estado civil: "))
    estado = estado.upper()
    if(estado == 'S' or estado == 'C' or estado == 'V' or estado == 'D'):
        break
    else:
        print("Estado civil errado. Informe, S - C - V - D")
