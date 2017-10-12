'''
Engenharia de Computação
Disciplina: Algoritmos e Computação
Semestre Letivo: 2016
Professor: Marcelo Siqueira / Henrique Cunha
Assunto:
Listas e Matrizes
Objetivos:

1. Analisar a sintaxe de códigos escritos em Python
2. Observar o comportamento da estrutura de dados conhecida como lista e sua aplicação na resolução de problemas com matrizes
3. Resolver problemas usando estruturas de repetição e listas

ROTEIRO DE AULA 9 – 07/07/2016
'''

'''
1.  SEM USAR O COMPUTADOR, analise e responda qual o valor da variável C após a execução do código abaixo.
Tente fazer sem usar o interpretador Python.
A = [[1,0,2], [0,2,1], [2,0,0]]
	C = [[0,0,0], [0,0,0], [0,0,0]]
	for i in range(0,3):
		for j in range(0,3):
			C[i][j] = A[A[i][j]][A[j][i]]
'''

A = [[1,0,2], [0,2,1], [2,0,0]]
C = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
	for j in range(0,3):
		C[i][j] = A[A[i][j]][A[j][i]]

print(C)


'''
O programa define duas matrizes do tipo três por três
Realiza o comando for para a iteração de i dentro do range de 0 até 2 (intervalo aberto)
Realiza o comando for encadeado dentro do outro for para a iteração de j dentro do range de 0 até 2 (intervalo aberto)
Adiciona os elementos a matriz C de acordo com as iterações recebendo de acordo com as iterações dos elementos da matriz A
Obtendo-se na saída do interpretador do python os seguintes valores para C:
>>>[[2, 1, 0], [1, 0, 0], [0, 0, 1]]
'''




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






'''
3. Escreva um programa que leia da entrada padrão os valores para uma matriz 3 x 3 e
verifique quantos números ímpares foram lidos.
'''
impares = 0
matriz = []

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        elemento = float(input("Digite os elementos da matriz (3x3) : "))
        matriz[linha].append(elemento)

        if elemento % 2 != 0:
            impares += 1



print(matriz, "\nDe acordo com a Matriz informada, foram verificados :", impares,"Números ímpares ! ")



'''
O programa realiza o seguinte algoritmo :
Define as variáveis, impares para armazenar a quantidade de elementos ímpares inseridos e matriz como uma lista vázia
A matriz 3 x 3 é montada adicionando as linhas e elementos vázios para a coluna a cada iteração dos comando for no range 3
Espera a entrada do usuário para informar os elementos da matriz e o adiciona na lista matriz de acordo com sua posição
Quando o elemento for informado é verificado se é ímpar pela operação matemática, caso sim é adiciona 1 na variável impares
Obtendo-se na saída do interpretador python:
A lista da matriz 3 x 3 montada pelo usuário e a quantidade de elementos ímapares da matriz, acrescidos da mensagem entre aspas
'''





#4. Escreva um programa que leia e some todos os valores de uma matriz 3 x 3.
soma = 0
matriz = []

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        elemento = float(input("Digite os elementos da matriz (3x3) : "))
        matriz[linha].append(elemento)
        soma += elemento


print(matriz, "\nDe acordo com a Matriz informada, a soma de todos os elementos foi :", soma)





'''
O programa realiza o seguinte algoritmo :
Define as variáveis, soma para armazenar o valor da soma dos elemento inseridos e matriz como uma lista vázia
A matriz 3 x 3 é montada adicionando as linhas e elementos vázios para a coluna a cada iteração dos comando for no range 3
Espera a entrada do usuário para informar os elementos da matriz e o adiciona na lista matriz de acordo com sua posição
Quando o elemento for informado é feito a soma deles na variável soma
Obtendo-se na saída do interpretador python:
A lista da matriz 3 x 3 montada pelo usuário e o valor da soma dos elementos, acrescidos da mensagem entre aspas
'''




