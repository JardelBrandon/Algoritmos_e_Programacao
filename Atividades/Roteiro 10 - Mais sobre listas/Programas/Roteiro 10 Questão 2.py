'''
2. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
números inteiros. Em seguida, o programa deve exibir na saída padrão os números ímpares
armazenados.
'''

vetor = []
impares = []

for i in range(10) :
    valores = int(input("Digite os números para a lista (pertencentes ao conjunto dos inteiros) : "))
    vetor.append(valores)

    if valores % 2 != 0 :
        impares.append(valores)

print(impares)




'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define a variável impares como sendo uma lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 até o 10
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Realiza a operação de módulo da divisão e compara se o valor do resto foi diferente de 0
Caso sim o valor digitado é ímpar então é armazenado na lista impares e vetor
Caso não o valor digitado é par e é somento armazenado na lista vetor
Imprime na tela os valores contidos da lista impares
'''