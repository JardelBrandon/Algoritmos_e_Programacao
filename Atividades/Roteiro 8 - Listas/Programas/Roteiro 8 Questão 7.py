'''
7. Escreva um programa que recebe um número arbitrário de valores do usuário. Em seguida, o
usuário deve digitar um valor para que seja procurado dentro da lista passada anteriormente.
O programa retorna True se o valor foi encontrado ou False, caso contrário.
'''

lista = []
maximo = int(input("Digite a quantidade de valores que deseja adicionar a lista : "))

for i in range(0,maximo) :
    valores = float(input("Digite quaisquer valores : "))
    lista.append(valores)

procurado = float(input("Digite um valor para que seja procurado dentro da lista : "))

if procurado in lista :
    print("True !")

else :
    print ("False !")




'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
Espera a entrada da quantidade de valores que se deseja adicionar a lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,maximo) que vai de 0 até o valor informado
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Espera a entrada de um valor que deseja ser procurado dentro da lista
Imprime na tela o resultado da busa, se o número for encontrado é impresso na tela True.
Caso contrário é impresso False
'''
