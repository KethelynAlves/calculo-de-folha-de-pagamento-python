sal = float(input("Digite o seu salário bruto: "))


if sal <1302.00:
    inss = sal*0.075
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído sem INSS é de:R$", (sal-inss))
elif sal <2571.29:
    inss = sal*0.09
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de:R$", (sal-inss))
elif sal <3856.94:
    inss = sal*0.12
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de:R$", (sal-inss))
elif sal <7507.49:
    inss = sal*0.14
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de:R$", (sal-inss))
elif sal >7507.50:
    inss = 876.95
    print (f"Calculo do INSS R${inss}")
    print ("Seu salálario liquído é de:R$", (sal-inss))
