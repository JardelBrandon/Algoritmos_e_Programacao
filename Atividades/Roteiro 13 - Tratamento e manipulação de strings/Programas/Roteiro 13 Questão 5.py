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
