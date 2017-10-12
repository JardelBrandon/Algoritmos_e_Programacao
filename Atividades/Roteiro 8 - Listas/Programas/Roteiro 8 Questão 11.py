'''
11. Escreva um programa que ordena uma lista de inteiros de acordo com o seguinte critério:
Primeiro os pares em ordem crescente e, em seguida, os ímpares em ordem decrescente.
'''

lista = []
pares = []
impares = []
maximo = int(input("Digite a quantidade de valores para a lista que deseja informar : "))

for i in range(maximo) :
    valores = float(input("Digite os valores da lista : "))
    lista.append(valores)

for n in lista :
    if n % 2 == 0 :
        pares.append(n)
    else :
        impares.append(n)

pares.sort()
impares.sort(reverse = True)

print ("Pares em ordem crescente : ", pares, "\nÍmpares em ordem decrescente : ", impares)





'''
O programa realiza o seguinte algoritmo :
Define três variáveis do tipo lista
Espera a entrada do usuário informando a quantos valores deseja inserir na lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores pelo usuário para a Lista
Adiciona os valores digitado na lista
Assume cada valor da lista, faz uma operação matemática e após faz a seguinte comparação
Se o resto da divisão for igual a zero o número é par então o número é adicionado a lista de pares
Caso contrário, quando o resto da divisão for diferente de zero então o número é adicionado na lista de ímpares
Ordena os valores da lista pares de forma crescente com o comando : pares.sort()
Ordena os valores da lista ímpares de forma decrescente com o comando : impares.sort(reverse = False) revertendo-os
Imprime na tela os números das listas que formam a lista pares de forma ordenada crescente
e na linha seguinte
Imprime na tela os números das listas que formam a lista ímpares de forma ordenada decrescente
'''