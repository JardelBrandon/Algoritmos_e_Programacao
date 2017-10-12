#1. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando umatabela tal como no exemplo abaixo):


# b)

#cont = 0
#soma = 0
#while (cont < 10) and (soma % 2 != 0):
#soma = soma + 3
#cont = cont + 1
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma



# b)

cont = 0
soma = 0

while (cont < 10) and (soma % 2 != 0):
    soma = soma + 3
    cont = cont + 1

    print("Valor de soma é:\n ", soma)

# A saída do interpretador Python apresenta as seguintes saídas:
#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma
# Poís a segunda condição do and não é atendida


