'''
Engenharia de Computação
Disciplina: Algoritmos e Computação
Semestre Letivo: 2016
Professor : Marcelo Siqueira / Henrique Cunha
Assunto: STRINGS
Objetivos:
1. Analisar a sintaxe de códigos escritos em Python
2. Observar o comportamento da estrutura STRING
3. Resolver problemas usando estrutura de repetição
y

ROTEIRO DE AULA 13 – 21/07/2016
'''

'''
1. Observe qual valor gerado em cada um dos comandos abaixo e depois teste no interpretador
Python.
s = “computador”
print(s[0])
for i in s:
print(i)
print(s[0] + s[3] + s[5])
print(s[0] + s[len(s)-1])
print(s[:5])
for k in range(0,len(s)):
print(s[k])
print(s[0:])
t = “celular”
for i in s:
print(i + t)
print(s[:])
for i in range(len(s)-1,-1,-1):
print(s[i])
'''

s = "computador"

print(s[0])

for i in s:
    print(i)

print(s[0] + s[3] + s[5])
print(s[0] + s[len(s) - 1])
print(s[:5])

for k in range(0, len(s)):
    print(s[k])

print(s[0:])

t = "celular"

for i in s:
    print(i + t)

print(s[:])

for i in range(len(s) - 1, -1, -1):
    print(s[i])

"""
Foi obtido na saída do interpretador python:
para : print(s[0])
>>> c

para : for i in s:
    print(i)

>>>c
o
m
p
u
t
a
d
o
r

para : print(s[0] + s[3] + s[5])
>>>cpt

para : print(s[0] + s[len(s)-1])
>>>cr

para : print(s[:5])
>>>compu

para : for k in range(0,len(s)):
    print(s[k])
>>>c
o
m
p
u
t
a
d
o
r

para : print(s[0:])
>>>computador

para : for i in s:
    print(i + t)
>>>ccelular
ocelular
mcelular
pcelular
ucelular
tcelular
acelular
dcelular
ocelular
rcelular

para : print(s[:])
>>>computador

para : for i in range(len(s)-1,-1,-1):
    print(s[i])
>>>r
o
d
a
t
u
p
m
o
c
"""



'''
2. Crie um Programa que recebe um String contendo uma palavra ou frase. A String recebida
deve ter pelo menos 1 espaço (“ ”) em branco. Se não tiver, emita uma mensagem de erro até
que o usuário digite uma frase que contenha pelo menos 1 espaço. Em seguida, escreva na
saída padrão a String recebida sem os espaços em branco. Por exemplo, se a String recebida
for “Instituto Federal de Educação, Ciência e Tecnologia da Paraíba”, escreva
“InstitutoFederaldeEducação,CiênciaeTecnologiadaParaíba”.
'''

string = input("Digite uma palavra ou frase : ")

while string.find(" ") < 0:
    print("Inválido, digite uma palavra ou frase com espaços em branco!")
    string = input("Digite uma palavra ou frase : ")

string_sem_espaços = string.replace(" ", "")
print(string_sem_espaços)

"""
O programa realiza o seguinte algoritmo:
Espera a entrada de um usuário para informar uma string 
Análisa se a string digitada contém pelo menos 1 espaço em branco 
Se não houver, entra em um laço de repetição while que,
Imprime uma mensagem de erro, informando que a string precisa conter espaços em branco
Espera a entrada de um usuário para informar uma string novamente
Quando uma string com espaços é digitada 
Uma variável string_sem_espaços, armazena a string informada sem os espaços em branco 
retirando os espaços com o comando .replace(" ", "") que localiza os espaços e substitui tirando eles 
Imrpime a variável sem os espaços em branco
"""


'''
3. Escreva um programa que leia um caractere da entrada padrão e verifique se o mesmo está
contido na palavra "engenharia"
'''
palavra = "engenharia"
verificar = input("Digite um caractere para verificação : ")

if palavra.find(verificar) >= 0:
    print("O caractere digitado :", verificar,
          "\nEstá contido na palavra :", palavra)
else:
    print("O caractere digitado : ", verificar,
          "\nNão está contido na palavra :", palavra)

'''
O programa realiza o seguinte algoritmo:
Define a variável palavra, que contém a string "engenharia"
Espera a entrada do usuário para digitar um caractere para verificar se pertence a palavra
Verifica se o comando .find(verificar) retorna um valor maior ou igual a zero 
Se sim, significa que o caractere informado está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual está contida 
Se não, significa que o caractere informado não está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual não está contida 
'''


'''
4. Modique a questão anterior para que a palavra também seja lida da entrada padrão.
'''

'''
3. Escreva um programa que leia um caractere da entrada padrão e verifique se o mesmo está
contido na palavra "engenharia"
'''
palavra = input("Digite uma palavra :")
verificar = input("Digite um caractere para verificar se está contida na palavra : ")

if palavra.find(verificar) >= 0:
    print("O caractere digitado :", verificar,
          "\nEstá contido na palavra :", palavra)
else:
    print("O caractere digitado : ", verificar,
          "\nNão está contido na palavra :", palavra)

'''
O programa realiza o seguinte algoritmo:
Espera a entrada do usuário para digitar uma palavra
Espera a entrada do usuário para digitar um caractere para verificar se pertence a palavra
Verifica se o comando .find(verificar) retorna um valor maior ou igual a zero 
Se sim, significa que o caractere informado está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual está contida 
Se não, significa que o caractere informado não está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual não está contida 
'''


'''
5. Faça um programa que recebe uma frase e substitui todas as ocorrências de espaço por “#”,
sem usar a função replace() .
'''

# Uma maneira de realizar este programa:

string = input("Digite uma frase : ")
string_sem_espaços = ""

for verificar in range(len(string)):
    if string[verificar] != " ":
        string_sem_espaços += string[verificar]

print(string_sem_espaços)

'''
O programa realiza o seguinte algoritmo:
Espera a entrada do usuário para informar uma frase 
Define uma variável string_sem_espaços do tipo string
Entra em um laço de repetição for que vai até o tamanho da frase informada 
Verifica cada índece da frase informada 
Se o contéudo do índece da frase for diferente de um espaço em branco,
Então o contéudo desse índece na frase é armazenado na variável string_sem_espaços 
Então essa variável não terá nenhum espaço em branco, pois não são adicionados 
Imprime a frase informada sem os espaços em branco 
'''

#Outra maneira de realizar este programa:

string = input("Digite uma frase : ")
string_sem_espaços = ""

string = string.split(" ")
string_sem_espaços = string_sem_espaços.join(string)

print(string_sem_espaços)

'''
O programa realiza o seguinte algoritmo:
Espera a entrada do usuário para informar uma frase 
Define uma variável string_sem_espaços do tipo string
Separa a frase nos espaços em branco com o comando .split(" ")
Junta a frase separada na variável string_sem_espaços com o comando .join(string)
Então essa variável não terá nenhum espaço em branco,
Pois onde continha espaços em branco, foram separados os elementos, 
Criando uma lista separadas por "," após é feita a junção da lista,
Logo os espaços e as separações dos elementos da lista indicada por "," são disfeitas
Imprime a frase informada sem os espaços em branco 
'''
