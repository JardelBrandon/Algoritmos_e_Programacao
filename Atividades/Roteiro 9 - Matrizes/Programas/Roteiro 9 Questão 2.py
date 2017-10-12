'''
2. Faça um programa que mostre uma matriz identidade NxN, onde N é um inteiro
informado pelo usuário. Se N, for 3, a saída deve ser a seguinte:
1 0 0
0 1 0
0 0 1
'''

n = int(input("Digite o número N de linhas e colunas da matriz quadrada (NxN) :"))

matriz = []

for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append([])

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if linha == coluna:
            matriz[linha][coluna] = 1
            print(matriz[linha][coluna], end=' ')
        else:
            matriz[linha][coluna] = 0
            print(matriz[linha][coluna], end=' ')
    print()


'''
O programa realiza o seguinte algoritmo :
Espera a entrada do usuário para informar a quantidade de linhas que é igual ao número de colunas, pois a matriz é quadrada
De acordo com o valor informado a matriz é montada adicionando as linhas e elementos vázios para a coluna a cada iteração dos comando for
Após a matriz ser criada, é realizado novas iteração do for para definir os elementos da diagonal principal da matriz
Se o elemento pertencer a diagonal principal o elemento recebe valor 1
Se o elemento não pertencer a diagonal pricipal o elemento recebe o valor 0
Obtendo-se na saída do interpretador python:
A matriz com o tamanho informado de forma tabelar e quadrada, com os elementos da diagonal principal sendo 1 e os demais 0
'''


