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
