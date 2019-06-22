# calcular desconto de combustivel

valorAlcool = 1.90
valorGasolina = 2.50

print("A - Álcool ou G - Gasolina")

tipo = str(input("Informe tipo de combustível: "))
tipo = tipo.upper()
litros = float(input("Informe quantos litros: "))

if(tipo == 'A'):
    if(litros > 0 and litros <= 20):
        valor = litros * valorAlcool
        desconto = valor * 0.03
        valorTotal = valor - desconto
        print("Valor R${}".format(valorTotal))
    else:
        valor = litros * valorAlcool
        desconto = valor * 0.05
        valorTotal = valor - desconto
        print("Valor R${}".format(valorTotal))
elif(tipo == 'G'):
    if(litros > 0 and litros <= 20):
        valor = litros * valorAlcool
        desconto = valor * 0.04
        valorTotal = valor - desconto
        print("Valor R${}".format(valorTotal))
    else:
        valor = litros * valorAlcool
        desconto = valor * 0.06
        valorTotal = valor - desconto
        print("Valor R${}".format(valorTotal))
else:
    print("Tipo de combustivel errado!")