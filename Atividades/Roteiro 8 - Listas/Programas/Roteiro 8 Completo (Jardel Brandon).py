'''
Engenharia deComputação
Disciplina: AlgoritmoseComputação
SemestreLetivo: 2016
Professor:Marcelo Siqueira/HenriqueCunha
Assunto:  Listas
Objetivos: 1. Analisar asintaxedecódigosescritosemPython
2. Observar o comportamento da estrutura de dados
conhecidacomo lista
3. Resolver problemas usando estruturas de repetição e
listas

ROTEIRO DE AULA 8 –04/07/2016
'''

'''
1. Qual a saída de cada um dos seguintes programas abaixos: (Tente fazer no papel antes de usar
o interpretador python)

1°
l = []
print(l)

2°
x = [10,20,30]
print(x[1])

x = [10,20,30]
print(x[-1])

3°
l = [10,20,30]
print(l[3])

4°
l.append(50)
print(l)

5°
l.insert(40)
print(l)

6°
x.insert(40,3)
print(x)

7°
l.append(1)
print(l)

8°
x =[0, 1, [2]]
x[2][0] = 3
print(x)

9°
x[2].append(4)
print(x)

10°
x[2] = 2
print x
print(x+l)
'''

l = []
print(l)

x = [10,20,30]
print(x[1])

l = [10,20,30]
print(l[3])

l.append(50)
print(l)

l.insert(40)
print(l)

x.insert(40,3)
print(x)

l.append(1)
print(l)

x =[0, 1, [2]]
x[2][0] = 3
print(x)

x[2].append(4)
print(x)

x[2] = 2
print(x)
print(x+l)

'''
Foi apresentado as seguintes saídas no interpretador do python:
1°
>>> []

2°
>>> 20

3°
>>> Traceback (most recent call last):
  File "D:/Users/IFPB/Documents/Roteiro 8 - Listas (Jardel Brandon)/Programas/Roteiro 8 Questão 1.py", line 58, in <module>
    print(l[3])
IndexError: list index out of range

4°
>>> [10, 20, 30, 50]

5°
>>> Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l.insert(40)
TypeError: insert() takes exactly 2 arguments (1 given)

6°
>>> [10, 20, 30, 3]

7°
>>> [10, 20, 30, 50, 1]

8°
>>> [0, 1, [3]]

9°
>>> [0, 1, [3, 4]]

10°
>>> [0, 1, 2]
    [0, 1, 2, 10, 20, 30, 50, 1]

'''





'''
2. Crie e preencha uma lista com 10 valores lidos da entrada padrão. No final, imprima a lista na
tela.
'''

lista = []

for i in range(0,10) :
    valores = float(input("Digite quaisquer valor : "))
    lista.append(valores)

print(lista)

'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 a 9
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Imprime na tela a lista com os 10 valores lidos
'''





'''
3. Crie e preencha uma lista com 10 valores lidos da entrada padrão. Importante: a inserção de
cada um dos elementos deve ser feita no início da lista.
'''

lista = []

for i in range(0,10) :
    valores = float(input("Digite quaisquer valores : "))
    lista.insert(0, valores)

print(lista)

'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 a 9
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados no início da lista
Imprime na tela a lista com os 10 valores lidos
'''





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




'''
6. Na questão anterior, caso a lista tenha elementos de tipos diferentes, o interpretador retornará
um erro. Dessa forma, faça um programa que resolva essa problema realizando a soma apenas
entre tipos compatíveis. Assim, se a lista tiver 3 strings e 4 inteiros, as 3 strings serão
concatenadas entre elas e o 4 inteiros serão somados entre eles. Como inteiros e floats podem
ser naturalmente somados, seu programa não deve fazer diferença entre eles.
'''

#Questão anulada, pois falta conhecimentos ainda não repassados para resolve-lá






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
Exemplos de entrada e Saída:
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





'''
12. Quem matou quem em Game of Thrones? Às vezes fica difícil de lembrar, portanto faremos
um programa que mantém isso guardado. A entrada do programa deve receber em sequência
o nome do assassino e o nome da pessoa morta por ele. O programa irá rodar até que o
usuário digite “valar morghulis”. Ao final, ele deve imprimir a lista dos assassinos e os nomes
das pessoas que foram mortas por eles, a quantidade de pessoas que cada um matou e
quantidade total de pessoasmortas.
'''

assassino = []
assassinado = []


while True :
    matou = input("Digite o nome do assassino : ")

    if matou == "valar morghulis" :
        break

    morreu = input("Digite o nome da pessoa assassinada : ")

    if morreu == "valar morghulis" :
        break

    assassinado.append(morreu)

    if matou in assassino :
        assassino.pop()

    assassino.append(matou)

    if matou == "valar morghulis" or morreu == "valar morghulis" :
        break

print(assassino , assassinado)

'''
Exemplos de entrada e Saída:
John Snow
João
John Snow
Maria
valar morghulis

John Snow João Maria
'''




'''
O programa realiza o seguinte algoritmo :
Define duas variáveis do tipo lista
Entra em um laço de repetição afirmando que o while True (Enquanto verdadeiro)
Espera a entrada dos nomes pelo usuário para a Lista do assassino e do assassinado respectivamente
Adiciona os nomes digitado na lista respectivamente
Analisa se foi digitado o nome valar morghulis em alguma lista se sim o laço de repetição é encerrado
Analisa se o nome da pessoa que assassinou já contém na lista, caso contenham o nome é apagado para não haver repetição
Imprime na tela os nomes das listas dos assassinos e os assassinados
'''




