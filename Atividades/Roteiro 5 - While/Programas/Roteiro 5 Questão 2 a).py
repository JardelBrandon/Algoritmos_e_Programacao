#2. Dado os programas abaixo, identifique os erros sintáticos e/ou faça comentários sobre a execução
#de cada um (cada programa contém um único erro).

# a)

#i = 0
#j = i + 2
#while (i < 10) # Erro na falta do encadeamento ultilizando o comando : no final
#i = i + 1
#print(i)


i = 0
j = i + 2

while (i < 10) :
    i = i + 1

    print(i)

# A saída do interpretador Python apresenta as seguintes saídas:
#intepretador >>>  0  1  2  3  4  5  6  7  8  9  10
