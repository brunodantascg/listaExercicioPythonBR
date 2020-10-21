# 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nomeUsuario = str(input("Informe Usuário: "))
    senhaUsuario = str(input("Informe senha: "))

    if(nomeUsuario == senhaUsuario):
        print("Usuário e Senha Iguais! Modifique Senha")
    else:
        print("Ok")
        break
