'''
5. Python tem uma função chamada sum() para retornar a soma dos elementos de uma lista.
Implemente um programa que forneça a soma dos elementos de uma lista sem usar essa
função. Considere que a lista tem elementos de apenas um único tipo.
'''

lista = []
soma = 0
maximo = int(input("Digite a quantidade de valores que deseja somar : "))

for i in range (0,maximo) :
    valores = float(input("Digite quaisquer valores : "))
    soma += valores

lista.append(soma)

print(lista)


'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista e uma variável para armazenar o valor da soma
Espera a entrada da quantidade de valores que se deseja somar
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na variável soma, acrescido dos números anteriores
Insere na lista o valor da soma dos valores digitados
Imprime na tela o resultado da lista que é composta da soma dos valores digitados
'''


