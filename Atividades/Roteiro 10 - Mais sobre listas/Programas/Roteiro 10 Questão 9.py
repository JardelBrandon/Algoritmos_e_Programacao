'''
9. Escreva um programa que leia e armazene um conjunto de 8 valores numéricos inteiros
quaisquer e o exiba na saída padrão de forma ordenada.
Por exemplo:

ENTRADA:
5 2 18 1 3 6 10 21
SAÍDA:
1 2 3 5 6 10 18 21
'''

conjunto_numerico = []
conjunto_numerico_ordenado = []

for numeros in range(8):
    numero = int(input("Digite o número inteiro para ser armazenado :"))
    conjunto_numerico.append(numero)

conjunto_numerico_ordenado = conjunto_numerico
conjunto_numerico_ordenado.sort()

print("Conjunto númerico inserido : \n", conjunto_numerico,
      "\nConjunto númerico ordenado : \n", conjunto_numerico_ordenado)

'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os números do conjunto númerico
Adiciona cada número no final da lista de conjunto númerico
Define que o conjunto númerico ordendado é igual ao conjunto númerico
Ordena de forma crescente lista conujunto númerico ordenado com o comando conjunto_numerico_ordenado.sort() (.sort())
Imprime na tela a lista com o conjunto de números inseridos e o mesmo conjunto de maneira ordenada
Acrescidas das mensagens em aspas
'''