sal = float(input("Digite o seu salário bruto: "))
vale = input("Descontar o vale transporte? ")


if sal <1320.00:
    inss = (sal*0.075)
    total = (sal-inss)
    print (f"Calculo do INSS R${inss}")
    print (f"Seu salário liquído é de:R$ {total}")
elif sal <2571.29:
    inss = ((sal-1320)*0.09 + 99)
    total = (sal-inss)
    print (f"Calculo do INSS R${inss}")
    print (f"Seu salário liquído é de:R$ {total}")
elif sal <3856.94:
    inss = ((sal-2571.29)*0.12 + 112.62 + 99)
    total = (sal-inss)
    print (f"Calculo do INSS R${inss}")
    print (f"Seu salário liquído é de:R$ {total}")
elif sal <7507.49:
    inss = ((sal-3856.94)*0.14 + 154.28 + 112.62 + 99)
    total = (sal-inss)
    print (f"Calculo do INSS R${inss}")
    print (f"Seu salário liquído é de:R$ {total}")
elif sal >=7507.50:
    inss = 876.95
    total = (sal-inss)
    print (f"Calculo do INSS R${inss}")
    print (f"Seu salário liquído é de:R$ {total}")

if vale == "S" or vale == "s":
    valvale =sal*0.06
    print ("O valor do Vale transporte é de: R$", valvale)
    total = sal-valvale
    print ("Seu salário liquído com desconto do Vale Transporte é de: R$", total)
