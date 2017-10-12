#IFPB - Instituto Federal de Educação, Ciência e Tecnologia da Paraíba
#Curso de Engenharia de Computação
#Disciplina: Algoritmos e Programação
#Semestre Letivo: 2016.2
#Professor: Marcelo Siqueira / Henrique Cunha

#Nome: Jardel Brandon de Araujo Regis ________________________________________________________________________

#PROVA 1

#Instruções:

#Não é permitido consultar livros, anotações, Internet etc.
#Não é permitido conversar durante o horário da prova
#Não é permitido usar pendrive
#Todas as questões têm o mesmo valor.
#Salve seus arquivos em alguma pasta que não seja a área de trabalho.
#Para cada problema você tem um conjunto de dados de entrada e de saída que servirão como uma referência na hora de testar seu código.
#A interpretação faz parte da prova.


#DURAÇÃO: 15:00h até 17:30h


#Campina Grande, PB
#30 de Janeiro de 2016


#Questão 1: Plano Cartesiano

#Descrição:
#Faça um programa que leia da entrada padrão duas coordenadas (x e y em sequência) referente a um ponto qualquer e imprime em qual quadrante do plano cartesiano o referido ponto se encontra.
#Os pontos que se encontram sobre um dos eixos (quando x ou y for zero) não se encontram em quadrante algum. Nesse caso, você deve imprimir sobre qual eixo o ponto está, ou se o ponto encontra-se sobre a origem.
#Entrada:                           Saída:
#2
#2                                  #primeiro


#3                                  #quarto
#-2

#-8                                 #terceiro
#-1

#-7                                 #segundo
#1

#0                                  #Sobre o eixo y
#2

#0                                  #Sobre a origem
#0


#x = valor do número em relação ao eixo das abscissas
#y = valor do número em relação ao eixo das ordenadas

ORIGEM = 0


x = float ( input ( " Digite o valor da primeira cordenada referente a x : " ) )

y = float ( input ( " Digite o valor da segunda cordenada referente a y : ") )


# Se x == 0 e y == 0 >>> Origem
# Se x == 0 e y != 0 >>> Sobre o eixo y
# Se x != 0 e y == 0 >>> Sobre o eixo x

# Se x > 0 e y > 0 >>> Primeiro Quadrante
# Se x < 0 e y > 0 >>> Segundo Quadrante
# Se x < 0 e y < 0 >>> Terceiro Quadrante
# Se x > 0 e y < 0 >>> Quarto Quadrante

if x == ORIGEM and y == ORIGEM :
    print ( " O valor das coordenadas digitadas está sobre : \n A origem do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )

elif x == ORIGEM and y != ORIGEM  :
    print ( " O valor das coordenadas digitadas está sobre : \n O eixo Y do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )

elif x != ORIGEM and y == ORIGEM  :
    print ( " O valor das coordenadas digitadas está sobre : \n O eixo X do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )



elif x > ORIGEM and y > ORIGEM  :
    print ( " O valor das coordenadas digitadas está sobre : \n O Primeiro Quadrante do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )

elif x < ORIGEM and y > ORIGEM  :
    print ( " O valor das coordenadas digitadas está sobre : \n O Segundo Quadrante do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )

elif x < ORIGEM and y < ORIGEM  :
    print ( " O valor das coordenadas digitadas está sobre : \n O Terceiro Quadrante do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )

else :
    print ( " O valor das coordenadas digitadas está sobre : \n O Quarto Quadrante do Plano Cartesiano !" "\n Nos pontos x =", x ," e y =", y )







#Questão 2: Formas Geométricas


#Descrição:
#Faça um programa que calcula características de formas geométricas de acordo com a
#necessidade do usuário.
#Em um primeiro momento você deve perguntar ao usuário qual tipo de forma ele gostaria
#de processar: (Q)uadrado, (R)etângulo ou (C)írculo.

#Caso o usuário escolha quadrado, pergunte qual o tamanho do lado e, em seguida
#calcule e imprima a área e o perímetro do quadrado.

#Caso o usuário escolha retângulo, pergunte qual o tamanho da altura e da largura e, em
#seguida calcule e imprima a área e o perímetro do retângulo.


#Caso o usuário escolha círculo, pergunte qual o tamanho do raio e, em seguida calcule e
#imprima a área e o comprimento do círculo (considere pi=3.14).


#Entrada:           Saída:
#C                   #12.56
#2                   #12.56

#Q                    #9
#3                    #12

#R                    #20
#4                    #18
#5



print ( " Digite a letra inicial da forma deseja processar :"
        " \n Considere as iniciais : Q para ( Quadrado ), R Para (Retângulo) ou C para (Círculo) ! " )

forma = input ( )

# Caso for Quadrado
# Área do Quadrado = lado ** 2
# Perímetro do Quadrado = ( 2 * a Base ) + ( 2 * a Altura )

# Caso for Retângulo
# Área do Retângulo = lado * Altura
# Perímetro do Quadrado = ( 2 * a Base ) + ( 2 * a Altura )

# Caso for Círculo
# Área do Círculo = pi * r ** 2
# Comprimento do Círculo = 2 * pi * r

PI = 3.14
QUADRADO = 2

if forma == "Q" :
    ladosQ = float ( input ( " Digite o valor correspondente ao lado do quadrado : " ) )
    áreaQ = ladosQ ** QUADRADO
    perQ = ( ladosQ * QUADRADO ) + ( ladosQ * QUADRADO )

    print ( " A área do Quadrado informado é = ", áreaQ,
            " \n O perímetro do Quadrado informado é = ", perQ )


elif forma == "R" :
    ladoR = float ( input (" Digite o valor correspondente a largura do retângulo : ") )
    alturaR = float ( input ( " Digite o valor correspondente a altura do retângulo : ") )
    áreaR = ladoR * alturaR
    perR = ( ladoR * QUADRADO ) + ( alturaR * QUADRADO )

    print(" A área do Retângulo informado é = ", áreaR,
    " \n O perímetro do Retângulo informado é = ", perR )


elif forma == "C" :
    raioC = float ( input(" Digite o valor correspondente ao raio do círculo : ") )
    áreaC = PI * raioC ** QUADRADO
    compC = QUADRADO * PI * raioC

    print(" A área do Círculo informado é = ", áreaC,
    " \n O comprimento do círculo informado é = ", compC )


else :
    print ( " Inválido ! " )





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
