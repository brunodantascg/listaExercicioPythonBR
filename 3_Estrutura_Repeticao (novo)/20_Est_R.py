# 20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while(True):

    while(True):
        num = int(input("Informe número: "))
        fatorial = 1
        if((num >= 0) and (num <= 16)):
            break
        print("Só podemos calcular o fatorial entre 0 - 16.\nInforme fatorial correto.")

    while(num > 0):
        fatorial = fatorial * num
        num = num - 1

    print(fatorial)

    resposta = int(input("Você quer relizar outro fatorial: 1 - Sim | 2 - Não\n"))
    if(resposta == 2):
        break
    print("Ok, vamos calcular outra fatorial!")
        
print("Obrigado! Até mais.")
