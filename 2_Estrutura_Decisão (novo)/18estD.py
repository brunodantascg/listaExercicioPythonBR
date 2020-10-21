# 18 -  Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Informe da data no formato DD/MM/AAAA")

dd = int(input("Informe DD: "))
mm = int(input("Informe MM: "))
aaaa = int(input("Informe AAAA: "))

if(((dd > 0)and(dd<=31))and(mm > 0)and(mm <= 12)and(aaaa > 0)and(aaaa <= 9999)):
    print("A data é válida!")
