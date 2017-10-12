'''
10. Escreva um programa que leia números de duas listas de inteiros com 3 posições cada e
apresente sua intersecção ordenada de forma crescente (use a função sort()). Importante: a
intersecção são os elementos repetidos em ambos os arrays, porém cada número pode
aparecer uma única vez no resultado.
'''

lista_1 =[]
lista_2 = []
intersecçao = []

for i in range(3) :
    numeros_1 = float(input("Digite os números da primeira lista : "))
    lista_1.append(numeros_1)

for i in range(3) :
    numeros_2 = float(input("Digite os números da segunda lista : "))
    lista_2.append(numeros_2)

for n in lista_1 :
    for x in lista_2 :
        if n == x :
            intersecçao.append(n)

intersecçao.sort()

print(intersecçao)




'''
O programa realiza o seguinte algoritmo :
Define três variáveis do tipo lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,3) que vai de 0 até o 3
Espera a entrada dos valores pelo usuário para a 1° Lista
Espera a entrada dos valores pelo usuário para a 2° Lista
Adiciona os valores digitados nas listas
Assume cada valor da 1º lista e cada valor da 2º lista, comparando-os e caso sejam iguais adiciona esse valor na lista intersecção
Ordena os valores da lista intersecção de forma crescente com o comando : intersecçao.sort()
Imprime na tela os números da lista que formam a intersecção de forma ordenada crescente
'''