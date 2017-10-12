# 9. Escreva um programa que ordena uma lista de inteiros de forma crescente.

lista = []
maximo = int(input("Digite a quantidade dos números inteiros que deseja ordenar : "))

for i in range(maximo) :
    inteiros = int(input("Digite os números inteiros : "))
    lista.append(inteiros)

lista.sort()
print(lista)



'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
Espera a entrada da quantidade de inteiros que se deseja ordenar
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores inteiros pelo usuário
Adiciona os valores digitados na lista
Ordena a lista de valores inteiros digitados de forma crescente com o comando : lista.sort()
Imprime na tela os números digitados para a lista de forma ordenada crescente
'''
