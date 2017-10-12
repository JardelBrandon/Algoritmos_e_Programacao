'''
4. Crie e preencha uma lista com 10 valores fornecidos pelo usuário. Em seguida, imprima
apenas os elementos de índice par. Use fatiamento de listas para resolver esse problema.
'''

lista =[]

for i in range(0,10) :
    valores = float(input("Digite quaisquer valores : "))
    lista.append(valores)

print(lista[::2])


'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 a 9
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Aplica na lista a operação [::2} que significa ir do primeiro índice da lista até o último com step (Passo) de 2 em 2
Imprime na tela os elementos de índice par da lista com os valores lidos
'''