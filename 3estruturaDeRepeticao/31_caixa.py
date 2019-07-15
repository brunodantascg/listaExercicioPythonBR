# Questão 31
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...


soma = 0
quant = 1
precoProduto = 1
while(precoProduto != 0):
    precoProduto = float(input("Produto {0}: R$ {1}".format(precoProduto - 1, quant)))
    soma += precoProduto

print("Total: R$ {0}".format(soma))
pagamento = float(input('Dinheiro: R$ '))

print("Troco: R$ {0}".format(pagamento - soma))
