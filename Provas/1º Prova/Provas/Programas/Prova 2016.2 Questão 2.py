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









