gasolina = 13
etanol = 10
diesel = 8
hidrogenio = 200
distancia = float(input("Digite a distância a ser percorrida: "))
tanque = float(input("Ditite a quantidade de combustível no carro: "))
selec_combus = input("Digite o combustível utilizado (G)asolina,(E)tanol,(D)iesel,(H)idrogenio ou (M)istura: ")
if selec_combus == "g":
    total = tanque*gasolina
    print("Consumo 13Km/L")
    if total>=distancia:
        print("Você conseguirá chegar ao destino sem reabastecer")
    else:
        print("Você não conseguirá chegar ao destino sem reabastecer")
elif selec_combus == "e":
    total = tanque*etanol
    print("Consumo 10Km/L")
    if total>=distancia:
        print("Você conseguirá chegar ao destino sem reabastecer")
    else:
        print("Você não conseguirá chegar ao destino sem reabastecer")
elif selec_combus == "d":
    total = tanque*diesel
    print("Consumo 8Km/L")
    if total>=distancia:
        print("Você conseguirá chegar ao destino sem reabastecer")
    else:
        print("Você não conseguirá chegar ao destino sem reabastecer")
elif selec_combus == "h":
    total = tanque*hidrogenio
    print("Consumo 200Km/L")
    if total>=distancia:
        print("Você conseguirá chegar ao destino sem reabastecer")
    else:
        print("Você não conseguirá chegar ao destino sem reabastecer")
elif selec_combus == "m":
    qtd = float(input("Digite a porcentagem de mistura: "))
    psc = 1.0 - qtd
    mistura = qtd*gasolina + psc*etanol
    total = mistura*tanque
    print("Consumo",mistura,"Km/L")
    if total>distancia:
        print("Você conseguirá chegar ao destino sem reabastecer")
    else:
        print("Você não conseguirá chegar ao destino sem reabastecer")
    
    
