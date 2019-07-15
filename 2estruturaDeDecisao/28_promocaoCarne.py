# Promoção de carne

fD = float(4.90)
fDA = float(5.80)
al = float(5.90)
alA = float(6.80)
pi = float(6.90)
piA = float(7.80)
desconto = float(0.05)
desc = float(0)

def l():
    print('---------------------------------')
def tipo(fD, fDA, al, alA, pi, piA):
    print("1 - File Duplo - R${0} até 5 Kg - R${1} acima de 5".format(fD, fDA))
    print("2 - Alcatra - R${0} até 5 Kg - R${1} acima de 5".format(al, alA))
    print("3 - Picanha - R${0} até 5 Kg - R${1} acima de 5".format(pi, piA))
def paga():
    print("FORMA DE PAGAMENTO")
    print("1 - à vista")
    print("2 - Cartão de Crédito TABAJARA")
    print("3 - Cartão de Crédito")
    print("4 - Cartão de Débito")
def desconto(desconto, valorTotal):
    desconto = desconto * valorTotal
    return valorTotal - desconto

def cupom(tipoCarne, quant, pagamento, valorTotal,desc):
    if(tipoCarne == 1):
        tipoCarne = str('1 - File Duplo')
    elif(tipoCarne == 2):
        tipoCarne = str('2 - Alcatra')
    else:
        tipoCarne = str('3 - Picanha')
    print("Tipo de Carne: {}".format(tipoCarne))
    print("Kg: {}".format(quant))
    print("Preço Total: R${}".format(valorTotal))
    if(pagamento == 1):
        pagamento = str('1 - À Vista')
    elif(pagamento == 2):
        pagamento = str('2 - Cartão de Crédito TABAJARA')
    elif(pagamento == 3):
        pagamento = str('3 - Cartão de Crédito')
    else:
        pagamento = str('4 - Cartão de Débito')
    print("Pagamento: {}".format(pagamento))
    print("Desconto: R${}".format(desc))
    print("Valor a Pagar: R${}".format(valorTotal - desc))

l()
tipo(fD, fDA, al, alA, pi, piA)
l()

while(True):
    tipoCarne = int(input("Informe tipo de carne: "))
    if(tipoCarne > 0 and tipoCarne <= 3):
        break
    else:
        print("Tipo de carne inválida. Informe novamente!")

quant = float(input("Informe quantidade "))
l()
paga()
l()
while(True):
    pagamento = int(input("Informe forma de pagamento: "))
    if(pagamento > 0 and pagamento <=4):
        break
    else:
        print("Tipo de pagamento inválido. Informe novamente")

if(tipo == 1):
    if(quant > 0 and quant < 5):
        valorTotal = quant * fD
        if(pagamento == 2):
            desc = desconto(desconto, valorTotal)
    else:
        valorTotal = quant * fDA
        if(pagamento == 2):
            desc = desconto(desconto, valorTotal)
elif(tipo == 2):
    if(quant > 0 and quant < 5):
        valorTotal = quant * al
        if (pagamento == 2):
            desc = desconto(desconto, valorTotal)
    else:
        valorTotal = quant * alA
        if (pagamento == 2):
            desc = desconto(desconto, valorTotal)
else:
    if(quant > 0 and quant < 5):
        valorTotal = quant * pi
        if (pagamento == 2):
            desc = desconto(desconto, valorTotal)
    else:
        valorTotal = quant * piA
        if (pagamento == 2):
            desc = desconto(desconto, valorTotal)

l()
cupom(tipoCarne, quant, pagamento, valorTotal, desc)
l()