# Informar senha e nome e tem que ser diferente

while(True):
    nome = str(input("Informe nome: "))
    nome = nome.upper()
    senha = str(input("Informe senha: "))
    senha = senha.upper()
    if(nome != senha):
        break
    else:
        print("a senha {} e o nome {} são iguais. Digite diferentes.")

print("Fim!")