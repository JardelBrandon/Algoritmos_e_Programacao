#1. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando umatabela tal como no exemplo abaixo):

# d)

#cont = 0
#soma = 0
#while (cont <= 6):
#if (cont % 2) == 0:
#soma = soma + 2
#else:
#soma = soma + 3
#cont = cont + 2
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma

# d)


cont = 0
soma = 0

while (cont <= 6):
    if (cont % 2) == 0:
        soma = soma + 2
    else:
        soma = soma + 3
    cont = cont + 2

    print("Valor de soma é:\n ", soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont  2  4  6  8
#soma  2  4  6  8