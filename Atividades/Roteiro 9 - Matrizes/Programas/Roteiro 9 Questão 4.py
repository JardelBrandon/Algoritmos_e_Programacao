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
