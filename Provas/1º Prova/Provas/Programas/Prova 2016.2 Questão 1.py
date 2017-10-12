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



