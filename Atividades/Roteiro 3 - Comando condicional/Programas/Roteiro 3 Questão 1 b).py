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



# Os comandos executados no programa realizam o seguinte algoritmo:
# Definem valores constantes para determinadas letras
# Após é realizado a manipulação das constantes por meio de cálculos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não )
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com algoritmo feito:
# >>> Resposta 2
#     Resposta 3
# 1 a) Logo: Respostas = Resposta 2 e Resposta 3