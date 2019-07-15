# Ler cinco números informar soam e média dos números
soma = float(0)

for i in range(1, 6, 1):
    num = float(input("Informe número {}:".format(i)))
    soma = soma + num

print("Soma: ",soma)
print("Média: ", (soma)/i)