#(IFPB - Engenharia de Computação
#Disciplina: Algoritmos e Programação
#Semestre Letivo: 2016
#Professor: Marcelo Siqueira / Henrique Cunha
#Aluno: Jardel Brandon
#ROTEIRO DE AULA 3 – 24/05/2016
#Objetivos:
#a. Analisar a sintaxe de códigos escritos em Python
#b. Observar o comportamento da estrutura de decisão if-elif-else
#c. Entender o funcionamento do comando input e suas variações.



#1°.Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão:
# a)


# a = 10
# b = 4
# c = 32
# d = 2


# if (a/4) > (b*4):
# print(“Alternativa 1”)
# else:
# print(“Alternativa 2”)
# if c > d:
# print(“Alternativa 3”)
# else:
# print(“Alternativa 4”)



a = 10
b = 4
c = 32
d = 2

if ( a / 4 ) > ( b * 4 ) :
    print ( " Alternativa 1 " )
else :
    print ( " Alternativa 2 " )

if c > d :
    print ( " Alternativa 3 " )
else :
    print ( " Alternativa 4 " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Definem valores constantes para determinadas letras
# Após é realizado a manipulação das constantes por meio de cálculos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não )
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com algoritmo feito:
# >>> Alternativa 2
#     Alternativa 3
# 1 a) Logo: Respostas = Alternativa 2 e Alternativa 3






#1°.Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão:
# b)



# x = 8
# y = 2
# z = 25
# m = x**2 + 2*x + z
# n = x + y
# p = z**(1/2)


# if (m > 100) and (n == 10) and (z <= 5):
# print(“Resposta 1”)
# else:
# print(“Resposta 2”)
# if (x > z + y) or (x != z**y):
# print(“Resposta 3”)
# else:
# print(“Resposta 4”)



x = 8
y = 2
z = 25
m = x ** 2 + 2 * x + z
n = x + y
p = z ** ( 1 / 2 )

if ( m > 100 ) and ( n == 10 ) and ( z <= 5 ):
    print ( " Resposta 1 " )
else :
    print ( " Resposta 2 " )

if ( x > z + y ) or ( x != z ** y ):
    print ( " Resposta 3" )
else :
    print ( " Resposta 4 " )

x = 8
y = 2
z = 25
m = x ** 2 + 2 * x + z
n = x + y
p = z ** ( 1 / 2 )

if ( m > 100 ) and ( n == 10 ) and ( z <= 5 ):
    print ( " Resposta 1 " )
else :
    print ( " Resposta 2 " )

if ( x > z + y ) or ( x != z ** y ):
    print ( " Resposta 3" )
else :
    print ( " Resposta 4 " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Definem valores constantes para determinadas letras
# Após é realizado a manipulação das constantes por meio de cálculos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não )
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com algoritmo feito:
# >>> Resposta 2
#     Resposta 3
# 1 b) Logo: Respostas = Resposta 2 e Resposta 3





#1°.Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão:
# c)


# m = 8
# n = 2
# z = 25


# if (m > 100) and (n == 10) and (z <= 5):
# print(“Resposta 1”)
# elif (m == 10):
# print(“Resposta 2”)
# elif (z > m + n):
# print(“Resposta 3”)
# else:
# print(“Resposta 4”)
# Respostas: Resposta 3



m = 8
n = 2
z = 25


if ( m > 100 ) and ( n == 10 ) and ( z <= 5 ):
    print ( " Resposta 1 " )
elif ( m == 10 ):
    print ( " Resposta 2 " )
elif ( z > m + n ):
    print ( " Resposta 3 " )
else :
    print ( " Resposta 4 " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Definem valores constantes para determinadas letras
# Após é realizado a manipulação das constantes por meio de cálculos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com algoritmo feito:
# >>> Resposta 3
# 1 c) Logo: solução = Resposta 3





#2°.)
#2. Dado o algoritmo abaixo, informe quais serão os valores de result para cada linha da
#tabela:


#if (valor3 % 2 == 0):
#valor1 = valor2
#valor2 = valor3*2
#result = valor2*(-1)
#else:
#result = valor3 - 2
#valor1  valor2  valor3  result
#1        5       4
#2        -1      9
#0        7       30
#3        8       8



valor1 = 3
valor2 = 8
valor3 = 8


if ( valor3 % 2 == 0 ):
    valor1 = valor2
    valor2 = valor3 * 2
    result = valor2 * (-1)
    print( " result if = " + str(result))
else :
    result = valor3 - 2
    print ( " result else = " + str(result))



# Os comandos executados no programa realizam o seguinte algoritmo:
# Define três valores por linha da tabela apresentada
# De acordo com os valores definidos, é realizado as operações matemáticas
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com algoritmo feito:
# >>> -8
#      7
#     -60
#     -16
# 2º.) Logo: solução = A tabela apresentada abaixo com os respectivos valores de result:

#Resposta = #valor1  valor2  valor3  result
#               1        5       4        -8
#               2        -1      9        7
#               0        7       30       -60
#               3        8       8        -16






#3°.)
#3.  Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é
#o maior.



num1 = input ( " Digite um Número inteiro : " )
num2 = input ( " Digite outro Número inteiro : " )

if num1 > num2:
    print ( " O primeiro número digitado é o maior " )
elif num1 == num2 :
    print ( " Os números digitados são iguais " )
else :
    print ( " O Segundo número digitado é o maior " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de dois números inteiros pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual número digitado foi o maior
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas




#4°.)
# 4.  Escreva um programa que leia os valores dos raios de dois círculos diferentes e informe
#qual dos dois possui área maior ou se possuem a mesma área.



PI = 3.14159265359


raio1 = input ( " Digite o raio do primeiro circulo : " )
raio2 = input ( " Digite o raio do segundo circulo : " )

A1 = PI * float ( raio1 ) ** 2

A2 = PI * float ( raio2 ) ** 2

if A1 > A2:
    print ( " O primeiro círculo possui a área maior " )
elif raio1 == raio2 :
    print ( " Os círculos possuem áreas iguais " )
else :
    print ( " O Segundo círculo possui a área maior " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de dois valores de áreas do círculo pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual área foi a maior
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas


#5.  Escreva um programa que leia os valores dos lados de um triângulo e informe se ele é
#equilátero, isósceles ou escaleno.

lado1 = input ( " Digite o valor do primeiro lado do triângulo : " )
lado2 = input ( " Digite o valor do segundo lado do triângulo : " )
lado3 = input ( " Digite o valor do terceiro lado do triângulo : " )


if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print ( " O triângulo informado é do tipo escaleno " )
elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print ( " O triângulo informado é do tipo equilátero " )
else :
    print ( " O triângulo informado é do tipo isósceles " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos valores dos lados do triângulo pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual  foi o tipo do triâgulo
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas





#6°.)
# 6.  Escreva um programa que leia o valor do índice de acidez (pH) de uma solução e
#informe se ela é ácida ou não.

NEUTRALIDADE = 7

input ( " Programa que lê o pH da água pH significa potencial hidrogeniônico (quantidade de prótons H+). aperte a tecla enter para continuar... " )

pH = float (input ( " Digite o valor do pH encontrado na água " ))



if pH < NEUTRALIDADE :
    print ( " O valor de pH encontrado na água é considerado ácido pois foi um valor abaixo que um pH de nível 7 (Neutro) " )
elif pH == NEUTRALIDADE :
    print ( " O valor de pH encontrado na água é considerado neutro " )
else :
    print ( " O valor de pH encontrado na água é considerado alcalino pois foi um valor maior que um pH de nível 7 (Neutro) " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Explica o programa e espera o pressionamento da tecla enter
# Espera a entrada do valor do pH encontrado na água pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual foi o pH da água e o estado em que ela se encontra
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas






#7°.) a) 1° maneira de fazer o programa usando o comando if
#7.  Escreva um programa que leia as notas de três pessoas pessoas em uma prova e as
#exiba na saída padrão de forma crescente.





aluno1 = float (input ( " Digite a nota do 1° aluno : " ) )

aluno2 = float (input ( " Digite a nota do 2° aluno : " ) )

aluno3 = float (input ( " Digite a nota do 3° aluno : " ) )


# aluno1 < aluno2 < aluno3
# aluno1 < aluno3 < aluno2
# aluno2 < aluno1 < aluno3
# aluno2 < aluno3 < aluno1
# aluno3 < aluno1 < aluno2
# aluno3 < aluno2 < aluno1

# aluno1 = aluno2 < aluno3
# aluno1 = aluno2 > aluno3
# aluno2 = aluno3 < aluno1
# aluno2 = aluno3 > aluno1
# aluno3 = aluno1 < aluno2
# aluno3 = aluno1 > aluno2
# aluno1 = aluno2 = aluno3


if aluno1 < aluno2 < aluno3 :
    print ( ' A nota do aluno 1 foi : ' + str ( aluno1 ) + "\n" +
            ' A nota do aluno 2 foi : ' + str ( aluno2 ) + "\n" +
            ' A nota do aluno 3 foi : ' + str ( aluno3 ) )


if aluno1 < aluno3 < aluno2:
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) )


if aluno2 < aluno1 < aluno3 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


if aluno2 < aluno3 < aluno1 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


if aluno3 < aluno1 < aluno2 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) )


if aluno3 < aluno2 < aluno1 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


if aluno1 == aluno2 and aluno1 < aluno3 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


if aluno1 == aluno2 and aluno1 > aluno3 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


if aluno2 == aluno3 and aluno2 < aluno1 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


if aluno2 == aluno3 and aluno2 > aluno1 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


if aluno3 == aluno1 and aluno3 < aluno2 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) )

if aluno3 == aluno1 and aluno3 > aluno2 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


if aluno1 == aluno2 == aluno3 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada do valor das notas de três alunos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if ( Se )
# Fazendo as ordenações das notas na forma crescente de acordo com os valores das notas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação e ordenação feita:
# Acrescidas das mensagens em aspas









#7°.) b) 2° maneira de fazer o programa usando o comando if e else
#7.  Escreva um programa que leia as notas de três pessoas pessoas em uma prova e as
#exiba na saída padrão de forma crescente.



aluno1 = float (input ( " Digite a nota do 1° aluno : " ) )

aluno2 = float (input ( " Digite a nota do 2° aluno : " ) )

aluno3 = float (input ( " Digite a nota do 3° aluno : " ) )


# aluno1 < aluno2 < aluno3
# aluno1 < aluno3 < aluno2
# aluno2 < aluno1 < aluno3
# aluno2 < aluno3 < aluno1
# aluno3 < aluno1 < aluno2
# aluno3 < aluno2 < aluno1

# aluno1 = aluno2 < aluno3
# aluno1 = aluno2 > aluno3
# aluno2 = aluno3 < aluno1
# aluno2 = aluno3 > aluno1
# aluno3 = aluno1 < aluno2
# aluno3 = aluno1 > aluno2
# aluno1 = aluno2 = aluno3


if aluno1 == aluno2 and aluno1 < aluno3:
    print(" A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))

if aluno1 == aluno2 and aluno1 > aluno3:
    print(" A nota do aluno 3 foi : " + str(aluno3) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 1 foi : " + str(aluno1))

if aluno2 == aluno3 and aluno2 < aluno1:
    print(" A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3) + "\n" +
          " A nota do aluno 1 foi : " + str(aluno1))

if aluno2 == aluno3 and aluno2 > aluno1:
    print(" A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))

if aluno3 == aluno1 and aluno3 < aluno2:
    print(" A nota do aluno 3 foi : " + str(aluno3) + "\n" +
          " A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2))

if aluno3 == aluno1 and aluno3 > aluno2:
    print(" A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))

if aluno1 == aluno2 == aluno3:
    print(" A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))



else:
    if aluno1 < aluno2 and aluno1 < aluno3:
        print(" A nota do aluno 1 foi : " + str(aluno1))
        if aluno2 < aluno3:
            print(" A nota do aluno 2 foi : " + str(aluno2))
            print(" A nota do aluno 3 foi : " + str(aluno3))
        else:
            print(" A nota do aluno 3 foi : " + str(aluno3))
            print(" A nota do aluno 2 foi : " + str(aluno2))

    if aluno2 < aluno1 and aluno2 < aluno3:
        print(" A nota do aluno 2 foi : " + str(aluno2))
        if aluno1 < aluno3:
            print(" A nota do aluno 1 foi : " + str(aluno1))
            print(" A nota do aluno 3 foi : " + str(aluno3))
        else:
            print(" A nota do aluno 3 foi : " + str(aluno3))
            print(" A nota do aluno 1 foi : " + str(aluno1))


    else:
        if aluno3 < aluno1 and aluno3 < aluno2:
            print(" A nota do aluno 3 foi : " + str(aluno3))
            if aluno1 < aluno2:
                print(" A nota do aluno 1 foi : " + str(aluno1))
                print(" A nota do aluno 2 foi : " + str(aluno2))
            else:
                print(" A nota do aluno 2 foi : " + str(aluno2))
                print(" A nota do aluno 1 foi : " + str(aluno1))



# Os comandos executados no programa realizam o seguinte algoritmo:
#  Espera a entrada do valor das notas de três alunos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não )
# Tendo o encadeamento e alinhamento de cada condição
# Fazendo as ordenações das notas na forma crescente de acordo com os valores das notas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação e ordenação feita:
# Acrescidas das mensagens em aspas



#7°.) c) 3° maneira de fazer o programa usando o comando if, elif e else
#7.  Escreva um programa que leia as notas de três pessoas pessoas em uma prova e as
#exiba na saída padrão de forma crescente.


aluno1 = float (input ( " Digite a nota do 1° aluno : " ) )

aluno2 = float (input ( " Digite a nota do 2° aluno : " ) )

aluno3 = float (input ( " Digite a nota do 3° aluno : " ) )


# aluno1 < aluno2 < aluno3
# aluno1 < aluno3 < aluno2
# aluno2 < aluno1 < aluno3
# aluno2 < aluno3 < aluno1
# aluno3 < aluno1 < aluno2
# aluno3 < aluno2 < aluno1

# aluno1 = aluno2 < aluno3
# aluno1 = aluno2 > aluno3
# aluno2 = aluno3 < aluno1
# aluno2 = aluno3 > aluno1
# aluno3 = aluno1 < aluno2
# aluno3 = aluno1 > aluno2
# aluno1 = aluno2 = aluno3


if aluno1 == aluno2 and aluno1 < aluno3 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno1 == aluno2 and aluno1 > aluno3 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno2 == aluno3 and aluno2 < aluno1 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno2 == aluno3 and aluno2 > aluno1 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno3 == aluno1 and aluno3 < aluno2 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) )

elif aluno3 == aluno1 and aluno3 > aluno2 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno1 < aluno2 and aluno1 < aluno3 :
    print(" A nota do aluno 1 foi : " + str(aluno1))
    if aluno2 < aluno3 :
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    else :
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )


elif  aluno2 < aluno1 and aluno2 < aluno3 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
    if aluno1 < aluno3 :
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    else :
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno3 < aluno2 and aluno3 < aluno1 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    if aluno1 < aluno2 :
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
    else :
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )


else :
    print(" A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada do valor das notas de três alunos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ), ( Senão se ) e ( Se não )
# Tendo o encadeamento e alinhamento de cada condição
# Fazendo as ordenações das notas na forma crescente de acordo com os valores das notas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação e ordenação feita:
# Acrescidas das mensagens em aspas




# 8. Escreva um programa que leia um valor qualquer e informe se ele é múltiplo de 5 (Use
# o operador %).

# Para um número natural ser múltiplo
# É preciso realizar a multiplicação de determinado número
# Por qualquer número do conjunto dos números naturais
# O resultado dos produtos da operação serão considerados múltiplos
# Então o conjunto dos múltiplos são infinitos

# Divisores de um número natural
# Um número é divisor de outro quando o resto da divisão for igual a 0. Portanto,
# Se a divisão for exata ( Não houver "Resto" ) esse número pode ser considerado divisor natural
# Observações importantes:
# ? O menor divisor natural de um número é sempre o número 1.
# ? O maior divisor de um número é o próprio número.
# ? O zero não é divisor de nenhum número.
# ? Os divisores de um número formam um conjunto finito.
# Alguns números têm apenas dois divisores: o 1 e ele mesmo.
# Esses números são chamados de primos.

# Os múltiplos e divisores de um número estão relacionados entre si da seguinte forma:
# Se 15 é divisível por 3, então 3 é divisor de 15, assim, 15 é múltiplo de 3.
# Se 8 é divisível por 2, então 2 é divisor de 8, assim, 8 é múltiplo de 2.
# Se 20 é divisível por 5, então 5 é divisor de 20, assim, 20 é múltiplo de 5.

MUT = 5
RESTO = 0

valor = int(input(" Digite um valor natural : "))

if valor % MUT == RESTO:
    print(" O valor digitado é múltiplo de 5 : ", valor)
else:
    print(" O valor digitado não é múltiplo de 5 : ", valor)


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um valor natural quaisquer
# Em seguida é feita a operação para descobrir o " Resto " da divisão ( Com o comando %)
# Em seguida é feita a comparação por meio da lógica booleana
# Se o valor do " Resto for igual a zero então o valor digitado é múltiplo de 5
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas




#9. Escreva um programa que leia um valor qualquer e informe se ele é divisível por 7,
#positivo e par.

# Divisores de um número natural
# Um número é divisor de outro quando o resto da divisão for igual a 0. Portanto,
# Observações importantes:
# O menor divisor natural de um número é sempre o número 1.
# O maior divisor de um número é o próprio número.
# O zero não é divisor de nenhum número.
# Os divisores de um número formam um conjunto finito.
# Alguns números têm apenas dois divisores: o 1 e ele mesmo.
# Esses números são chamados de primos. Observe os números primos de 1 a 100 destacados no crivo de Eratóstenes:


DIV = 7
RESTO = 0
DIVPAR = 2

# Divisível, Positivo e Par
# Divisível, Positivo e Ímpar
# Divisível, Negativo e Par
# Divisível, Negativo e Ímpar
# Indivisível, Positivo e Par
# Indivisível, Positivo e Ímpar
# Indivisível, Negativo e Par
# Indivisível, Negativo e Ímpar

valor = int ( input ( " Digite um valor : " ) )

if valor == RESTO :
    print(" O valor digitado é : ", valor, "\n Indivisível por quaisquer número \n Neutro\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Positivo\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) != RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Positivo\n e \n Ímpar " )

elif ( DIV % valor == RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) == RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Negativo\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) != RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Negativo\n e \n Ímpar " )

elif ( DIV % valor != RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Positivo\n e \n Par " )

elif ( DIV % valor != RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) != RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Positivo\n e \n Ímpar " )

elif ( DIV % valor != RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Negativo\n e \n Par " )

else :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Negativo\n e \n Ímpar " )




# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um valor quaisquer pelo usuário
# Em seguida é feita a operação para descobrir o " Resto " da divisão ( Com o comando %)
# A verificação se o valor digitado Positivo ou Negativo
# A verificação se o valor digitado é Par ou Ímpar
# A verificação se é divisível por 0 pois ocorre uma condição especial
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas





#10. Escreva um programa que solicite ao usuário sua temperatura, se está tendo secreção,
#tosse e dor no corpo (“S” ou “N”). Caso a temperatura seja maior do que 37 graus e as
#demais respostas sejam iguais a “S”, uma mensagem “Exames Especiais” deve ser
#exibida. Caso a temperatura seja menor do que 37 graus e não houver secreção, tosse
#e dor no corpo, a mensagem será “Liberado”. Caso a temperatura seja inferior a 37
#graus, mas houver dor no corpo, tosse e secreção, a mensagem deve ser igual a
#“Exames Básicos”.

GRAUS = 37


temperatura = float ( input ( " Digite sua temperatura : " ) )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
secreção = input ( )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
tosse = input ( )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
dor = input ( )



if temperatura >= GRAUS and  secreção == "S" and  tosse == "S" and  dor == "S" :
    print ( " Exames Especiais ! " )

elif temperatura < GRAUS and secreção == "N" and tosse == "N" and dor == "N" :
    print ( " Liberado ! " )

else :
    print ( " Exames Básicos ! " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos dados perguntados a respeito dos sintomas sentidos
# Em seguida é feita a operação para o estado do paciente
# A verificação da temperatura
# A verificação se existe dor no corpo, tosse e secreção
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas




# 11. Escreva um programa que leia um caractere da entrada padrão e informe se ele é uma
# vogal.


print(" Digite um caractere quaisquer : ")
letra = input()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(" O caractere digitado é uma vogal minúscula : ", letra)

elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(" O caractere digitado é uma vogal maiúscula : ", letra)

else:
    print(" O caractere digitado não é uma vogal ", letra)


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um caractere quaiquer pelo usuário
# Após é ralizado as comparações pelos comandos condicionais
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas





