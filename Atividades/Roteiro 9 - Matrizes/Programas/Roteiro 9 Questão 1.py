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