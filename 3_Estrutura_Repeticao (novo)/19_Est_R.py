# 19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

vezes = 0
soma = 0
maior = 0
menor = 0
res = str('s')

while (res == 's'):
    vezes = vezes + 1

    while True:
        num = int(input("Informe número: "))
        if(num >= 0 and num <= 1000):
            break
        else:
            print("Número tem que ser entre 0 e 1000, Informe novamente!")

    while(res == 's' or res == 'n'):
        res = str(input("Deseja informar outro número: s - SIM n - NÃO "))
        if(res == 's' or res == 'n'):
            break
        else:
            print("Resposta tem que tá no padrão s - SIM ou n - NÃO")
    
    if((num > maior)or(vezes == 1)):
        maior = num

    if((num < menor)or(vezes == 1)):
        menor = num

    soma = soma + num


print("Maior valor: ", maior)
print("Menor valor: ", menor)
print("Soma dos valores: ", soma)
