'''
8. Dadas duas listas encadeadas A e B, escreva um programa para verificar se B é um
subconjunto de A. A primeira linha de entrada será o tamanho (n) da primeira lista (número
inteiro). Em seguida, uma lista com n números inteiros. A terceira linha de entrada é o
tamanho da segunda lista (número inteiro). Por fim, uma lista com m números inteiros. Nesse
caso, m e n podem assumir valores iguais ou diferentes. O programa imprime True se B é
subconjunto de A e False caso contrário.
'''

lista_A = []
lista_B = []

maximo_A = int(input("Digite a quantidade do tamanho da lista A : "))
for a in range(maximo_A) :
    valores_A = input("Digite os valores para a lista A : ")
    lista_A.append(valores_A)

maximo_B = int(input("Digite a quantidade do tamanho da lista B : "))
for b in range (maximo_B) :
    valores_B = input("Digite os valores para a lista B : ")
    lista_B.append(valores_B)

eh_subconjunto = True
for n in lista_B:
    if not(n in lista_A):
        eh_subconjunto = False

if eh_subconjunto:
    print("True")

else :
    print("False")







'''
Exemplos de entradaeSaída:
7 # tamanho de A                True
1
2
3
4
5
6
7

5 # tamanho de B
5
4
3
1
7



3 # tamanho de A                False
2
4
5

1 # tamanho de B
0
'''



'''
O programa realiza o seguinte algoritmo :
Define duas variáveis do tipo lista
Espera a entrada da quantidade de valores que se deseja adicionar a lista A
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Espera a entrada da quantidade de valores que se deseja adicionar a lista B
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Faz a iteração de cada elemento da lista B em relação a lista B se todos os elementos de B estiverem contidos em A a condição é verdadeira
Caso contrário, quando houver algum elemento em B ques não esteja presente em A a condição é falsa
Imprime na tela o resultado da operação de iteração para descobrir se B é subconjunto de A
Se o conjunto B for subconjunto do conjunto A é impresso na tela True.
Caso contrário é impresso False
'''
