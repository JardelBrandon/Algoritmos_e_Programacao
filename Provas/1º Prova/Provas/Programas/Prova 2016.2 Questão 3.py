#Questão 3: Meu carro multicombustível.


#Descrição:

#Meu carro é multicombustível e funciona com gasolina, etanol, diesel e hidrogênio. Pode
#também funcionar com uma mistura de gasolina e etanol. Para cada um desses
#combustíveis, meu carro faz uma quilometragem diferente:

#● (G)asolina: 13Km/l
#● (E)tanol: 10Km/l
#● (D)iesel: 8Km/l
#● (H)idrogênio: 200Km/l
#● (M)istura: ver abaixo.

#Faça um programa que receba do usuário qual distância que ele vai percorrer, quantos
#litros de combustível ele colocou no carro e qual o tipo de combustível a ser usado.
#Informe ao usuário se ele conseguirá chegar ao seu destino sem reabastecer.
#No caso de haver (M)istura entre gasolina e etanol, você deve perguntar ao usuário em
#qual proporção está a mistura. Por exemplo, se a proporção for 0.7, quer dizer que há
#70% de gasolina e 30% de etanol. Se a proporção for de 0.4, quer dizer que há 40% de
#gasolina e 60% de etanol. Nesse caso, O consumo (em Km/l) deve ser calculado como
#uma média ponderada, de maneira que a proporção determina quais os pesos dessa
#média. Exemplo: Se a proporção for 0.7, a média ponderada do consumo será:
#consumo_gas*0.7 + consumo_etanol*0.3.


#Entrada:                   #Saída:
#100                        #Consumo 13 Km/l
#5                          #Você não conseguirá chegar ao destino sem reabastecer
#G

#200                        #Consumo 200 Km/l
#2                          #Você conseguirá chegar ao destino sem reabastecer
#H

#50                         #Consumo 8 Km/l
#8                          #Você conseguirá chegar ao destino sem reabastecer
#D


#100                        #Consumo 12,1 Km/l
#10                         #Você conseguirá chegar ao destino sem reabastecer
#M
#0.7


# Qual distância ?
# Quantos litros foram colocados e qual o tipo de combustível?
# Informar se ele poderá chegar no destino se reabastecer.

#Caso houver M Mistura entre gasolina e etanol qual a proporção?
#Deve ser calculado como uma média ponderada
#Os pesos são determinados pela proporção

GASOLINA = 13 # 13 Km / l
ETANOL = 10 # 10 Km / l
DIESEL = 8 # 8 Km / l
HIDROGÊNIO = 200 # 200 kM / L

dist = float ( input ( " Por favor, informe qual é a distância que pretendes percorrer em Km ? :") )

litros = float ( input ( " Quantos litros de combustível foram inseridos ? : " ) )

print ( " Digite a letra inicial do combustível que foi inserido :"
        " \n Considere as iniciais : "
        " \n G para ( Gasolina ); E para ( Etanol ); D para ( Diesel ); H para ( Hidrogênio ) e M para ( Mistura ) ! " )

comb = input ( )

if comb == "G" :
    if ( litros * GASOLINA ) >= dist :
        print ( " Você conseguirá chegar ao destino sem reabastecer ! " )
    else :
        print ( " Você não conseguirá chegar ao destino sem reabastecer ! " )

elif comb == "E" :
    if ( litros * ETANOL ) >= dist :
        print ( " Você conseguirá chegar ao destino sem reabastecer ! " )
    else :
        print ( " Você não conseguirá chegar ao destino sem reabastecer ! " )


elif comb == "D" :
    if ( litros * DIESEL ) >= dist :
        print ( " Você conseguirá chegar ao destino sem reabastecer ! " )
    else :
        print ( " Você não conseguirá chegar ao destino sem reabastecer ! " )


elif comb == "H" :
    if ( litros * HIDROGÊNIO ) >= dist :
        print ( " Você conseguirá chegar ao destino sem reabastecer ! " )
    else :
        print ( " Você não conseguirá chegar ao destino sem reabastecer ! " )


elif comb == "M" :
    propG = float ( input ( " Qual a Proporção entre as misturas de Gasolina em relação ao Etanol ? : " ) )
    if ( GASOLINA * propG ) + ( ETANOL * (1 - propG ) )* litros >= dist :
        print ( " Você conseguirá chegar ao destino sem reabastecer ! " )
    else:
        print(" Você não conseguirá chegar ao destino sem reabastecer ! ")


#No caso de haver (M)istura entre gasolina e etanol, você deve perguntar ao usuário em
#qual proporção está a mistura. Por exemplo, se a proporção for 0.7, quer dizer que há
#70% de gasolina e 30% de etanol. Se a proporção for de 0.4, quer dizer que há 40% de
#gasolina e 60% de etanol. Nesse caso, O consumo (em Km/l) deve ser calculado como
#uma média ponderada, de maneira que a proporção determina quais os pesos dessa
#média. Exemplo: Se a proporção for 0.7, a média ponderada do consumo será:
#consumo_gas*0.7 + consumo_etanol*0.3.