#5. Escreva um programa que leia e some os valores de duas matrizes 3 x 3.

soma = 0
matriz_a = []
matriz_b = []
matriz_resultante = []


for linha in range(3):
    matriz_a.append([])
    matriz_resultante.append([])
    for coluna in range(3):
        elemento_a = float(input("Digite os elementos da primeira matriz (3x3) : "))
        matriz_a[linha].append(elemento_a)
        matriz_resultante[linha].append(elemento_a)
        soma += elemento_a

for linha in range(3):
    matriz_b.append([])
    for coluna in range(3):
        elemento_b = float(input("Digite os elementos da segunda matriz (3x3) : "))
        matriz_b[linha].append(elemento_b)
        matriz_resultante[linha] += matriz_b[linha]
        soma += elemento_b




print("Primeira Matriz informada : ", matriz_a,
      "\nSegunda Matriz informada : ", matriz_b,
      "\nMatriz resultante da soma dos elementos das suas Matrizes : ", matriz_resultante,
      "\nDe acordo com a Matriz informada, a soma de todos os elementos foi :", soma)