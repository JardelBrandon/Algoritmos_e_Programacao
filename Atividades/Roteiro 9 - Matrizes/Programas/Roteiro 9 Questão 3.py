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
