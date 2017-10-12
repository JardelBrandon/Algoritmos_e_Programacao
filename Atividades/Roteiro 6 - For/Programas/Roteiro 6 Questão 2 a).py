#2. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando uma tabela tal como no exemplo abaixo):

#2°) b)
#soma = 3
#cont = 1
#forx in range(10):
#soma = soma + 2
#cont = cont + 1
#print(x)
#print(soma)
#print(cont)


#iteração   0  1  2  3  4  5  6  7  8  9
#cont       2
#soma       5
#x          0


soma = 3
cont = 1

for x in range(10):
    soma = soma + 2
    cont = cont + 1

    print("Valor de X :", x)
    print("Valor de soma :", soma)
    print("Valor de cont :", cont)




# Foi obtido as seguintes respostas para a tabela na saída do python
#>>>
#iteração   0  1  2  3  4  5  6  7  8  9
#cont       2  3  4  5  6  7  8  9  10 11
#soma       5  7  9  11 13 15 17 19 21 23
#x          0  1  2  3  4  5  6  7  8  9

