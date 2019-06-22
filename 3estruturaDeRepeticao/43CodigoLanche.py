# Lanche

# Valores dos lanches
c100 = float(1.20)
c101 = float(1.30)
c102 = float(1.50)
c103 = float(1.20)
c104 = float(1.30)
c105 = float(1.00)

# Função para da print em cardápio
def card():
    print('----------------- CARDÁPIO -----------------')
    print('-- Especificação ---- Código ---- Preço ----')
    print('-- Cachorro Quente -- 100    ---- R$ {} ---'.format(c100))
    print('-- Bauru Simples   -- 101    ---- R$ {} ---'.format(c101))
    print('-- Bauru com ovo   -- 102    ---- R$ {} ---'.format(c102))
    print('-- Hambúrguer      -- 103    ---- R$ {} ---'.format(c103))
    print('-- Cheeseburguer   -- 104    ---- R$ {} ---'.format(c104))
    print('-- Refrigerante    -- 105    ---- R$ {} ---'.format(c105))

print(card())
while(True):
    while(True):
        cod = int(input("Informe código do pedido: "))
        if(cod >= 100 and cod <= 105):
            break
        else:
            print("Código informado errado!")

    quant = int(input("Informe quantidade: "))
    if(cod == 100): cod = c100
    elif(cod == 101): cod = c101
    elif(cod == c102): cod = c102
    elif(cod == c103): cod = c103
    elif(cod == c104): cod = c104
    elif(cod == c105): cod = c105
    valor = quant * cod
    while(True):
        outroPedido = int(input("Outro pedido: 1 - Sim ___ 2 - Não"))
        if(outroPedido >= 1 and outroPedido <= 2):
            break
        else:
            print("Informação errada. 1 - Sim ___ 2 - Não")

    if(outroPedido == 1):
        print("Ok")
    else:
        break