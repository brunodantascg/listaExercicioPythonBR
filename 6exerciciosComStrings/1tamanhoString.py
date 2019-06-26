# Questão 1
# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

print("Compara duas strings")
st1 = input("String 1: ")
st2 = input("String 2: ")

print('Tamanho de "%s": %d caracteres' % (st1, len(st1)))
print('Tamanho de "%s": %d caracteres' % (st2, len(st2)))

if (len(st1) != len(st2)):
    print("As duas strings sao de tamanhos diferentes")
    print("As duas strings possuem conteudo diferente")
else:
    print("As duas strings tem tamanho igual")
    if (st1 == st2):
        print("As duas strings possuem o mesmo conteudo")
    else:
        print("As duas strings possuem conteudo diferente")
