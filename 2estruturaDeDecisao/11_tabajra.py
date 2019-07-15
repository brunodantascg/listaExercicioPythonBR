# Aumento de Salário

salario = float(input("Informe Salário R$ "))

if(salario <= 280):
    aumento = (salario * 0.20)
    salarioTotal = salario + aumento
    print("Salário R${} \nReajuste 20% \nAumento R${} \nSalário novo R${}".format(salario, aumento, salarioTotal))
elif(salario > 280 and salario <= 700):
    aumento = (salario * 0.15)
    salarioTotal = salario + aumento
    print("Salário R${} \nReajuste 15% \nAumento R${} \nSalário novo R${}".format(salario, aumento, salarioTotal))
elif(salario > 700 and salario <= 1500):
    aumento = (salario * 0.10)
    salarioTotal = salario + aumento
    print("Salário R${} \nReajuste 10% \nAumento R${} \nSalário novo R${}".format(salario, aumento, salarioTotal))
elif(salario > 1500):
    aumento = (salario * 0.05)
    salarioTotal = salario + aumento
    print("Salário R${} \nReajuste 5% \nAumento R${} \nSalário novo R${}".format(salario, aumento, salarioTotal))
