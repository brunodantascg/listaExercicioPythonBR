# 18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

vezes = 0
soma = 0
maior = 0
menor = 0
res = str('s')

while (res == 's'):
    vezes = vezes + 1
    num = int(input("Informe número: "))

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
