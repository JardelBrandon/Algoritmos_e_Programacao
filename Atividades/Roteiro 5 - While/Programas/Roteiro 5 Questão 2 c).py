#2. Dado os programas abaixo, identifique os erros sintáticos e/ou faça comentários sobre a execução
#de cada um (cada programa contém um único erro).


#c)


#j = i + 1  # Erro apresentado nessa linha, pois a variável i ainda não foi identificada de acordo com a leitura de cima para baixo
#i = 0
#while (i < 10):
#i = i + 1
#print(i)


i = 0
j = i + 1

while (i < 10):
    i = i + 1

    print(i)


# A saída do interpretador Python apresenta as seguintes saídas:
#intepretador >>>  0  1  2  3  4  5  6  7  8  9  10


