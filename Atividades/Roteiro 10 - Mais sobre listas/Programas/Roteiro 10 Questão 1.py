'''
1. Escreva um programa que leia e armazene em um vetor de 8 posições um conjunto de
números reais. O programa deve somar os valores de todas as posições e exibir o resultado
na saída padrão.
'''

vetor = []

for i in range(8) :
    valores = float(input("Digite os números para a lista (pertencentes ao conjunto dos reais) : "))
    vetor.append(valores)

vetor = sum(vetor)

print(vetor)


'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,8) que vai de 0 até o 8
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Faz a soma dos números presentes na lista vetor e armazena a soma na própria lista, com o comando : vetor = sum(vetor)
Imprime na tela o valor da soma realizada na lista vetor
'''