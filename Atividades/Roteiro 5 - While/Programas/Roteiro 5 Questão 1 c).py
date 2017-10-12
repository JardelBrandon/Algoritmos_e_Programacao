#1. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando umatabela tal como no exemplo abaixo):

# c)

#cont = 0
#soma = 0
#while (cont <= 6) or (soma < 12):
#soma = soma + 2
#cont = cont + 2
#print(“Valor de soma é:\n ”, soma)


# c)

#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma

cont = 0
soma = 0

while (cont <= 6) or (soma < 12):
    soma = soma + 2
    cont = cont + 2

    print("Valor de soma é:\n ", soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont  2  4  6  8  10  12
#soma  2  4  6  8  10  12
# Poís enquanto um ou outro for verdadeiro fica encadeiado no laço de repetição