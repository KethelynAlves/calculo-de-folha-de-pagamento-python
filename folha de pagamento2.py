sal = float(input("Digite o seu salário bruto: "))
vale = input("Descontar o vale transporte? ")


if sal <1302.00:
    inss = sal*0.075
    print (f"Calculo do INSS R${inss}")
    total = (sal-inss)
    print ("Seu salário liquído é de:R$", total)
elif sal <2571.29:
    inss = sal*0.09
    print (f"Calculo do INSS R${inss}")
    total = (sal-inss)
    print ("Seu salário liquído é de:R$", total)
elif sal <3856.94:
    inss = sal*0.12
    print (f"Calculo do INSS R${inss}")
    total = (sal-inss)
    print ("Seu salário liquído é de:R$", total)
elif sal <7507.49:
    inss = sal*0.14
    print (f"Calculo do INSS R${inss}")
    total = (sal-inss)
    print ("Seu salário liquído é de:R$", total)
elif sal >7507.50:
    inss = 876.95
    print (f"Calculo do INSS R${inss}")
    total = (sal-inss)
    print ("Seu salário liquído é de:R$", total)
if vale == "S" or vale == "s":
    valvale =total*0.06
    print ("O valor do Vale transporte é de: R$", valvale)
    total = sal-valvale
    print ("Seu salário liquído com desconto do Vale Transporte é de: R$", total)