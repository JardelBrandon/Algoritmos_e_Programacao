'''
Engenharia deComputação
Disciplina: AlgoritmoseComputação
SemestreLetivo: 2016
Professor:Marcelo Siqueira/HenriqueCunha
Assunto:  Listas
Objetivos: 1. Analisar asintaxedecódigosescritosemPython
2. Observar o comportamento da estrutura de dados
conhecida como lista e sua aplicação na resolução de
problemascommatrizes
3. Resolver problemas usando estruturas de repetição e
listas

ROTEIRO DE AULA 10 – 12/07/2016
'''



'''
1. Escreva um programa que leia e armazene em um vetor de 8 posições um conjunto de
números reais. O programa deve somar os valores de todas as posições e exibir o resultado
na saída padrão.
'''

vetor = []

for i in range(8) :
    valores = float(input("Digite o conjunto de números reais : "))
    vetor.append(valores)

vetor = sum(vetor)

print(vetor)


'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,8) que vai de 0 até o 8
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Faz a soma dos números presentes na lista vetor e armazena a soma na própria lista, com o comando : vetor = sum(vetor)
Imprime na tela o valor da soma realizada na lista vetor
'''




'''
2. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
números inteiros. Em seguida, o programa deve exibir na saída padrão os números ímpares
armazenados.
'''

vetor = []
impares = []

for i in range(10) :
    valores = int(input("Digite os números para a lista (pertencentes ao conjunto dos inteiros) : "))
    vetor.append(valores)

    if valores % 2 != 0 :
        impares.append(valores)

print(impares)




'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define a variável impares como sendo uma lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 até o 10
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Realiza a operação de módulo da divisão e compara se o valor do resto foi diferente de 0
Caso sim o valor digitado é ímpar então é armazenado na lista impares e vetor
Caso não o valor digitado é par e é somento armazenado na lista vetor
Imprime na tela os valores contidos da lista impares
'''




'''
3. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
números inteiros. Em seguida, o programa deve exibir na saída padrão o somatório de
todos os números pares.
'''


vetor = []
pares = []

for i in range(10) :
    valores = int(input("Digite os números para a lista (pertencentes ao conjunto dos inteiros) : "))
    vetor.append(valores)

    if valores % 2 == 0 :
        pares.append(valores)

print(sum(pares))


'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define a variável pares como sendo uma lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 até o 10
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Realiza a operação de módulo da divisão e compara se o valor do resto foi igual a 0
Caso sim o valor digitado é par então é armazenado na lista pares e vetor
Caso não o valor digitado é par e é somento armazenado na lista vetor
Realiza o somatório dos valores contidos na lista pares, com o comando : sum(pares)
Imprime na tela o somatório dos valores contidos da lista pares
'''





'''
4. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
caracteres. O programa deve contar quantas vogais estão armazenadas no vetor e informar
o resultado na saída padrão.
'''

vetor = []
vogais = 0

for i in range(10) :
    caracteres = input("Digite quaisquer caracteres : ")
    vetor.append(caracteres)

    if caracteres in ["a","e","i","o","u","A","E","I","O","U"] :
        vogais += 1

print("Foram digitadas :", vogais, "Vogais")




'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define a variável vogais como sendo 0
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 até o 10
Espera a entrada dos caracteres pelo usuário
Adiciona os caracteres digitados na lista
Faz a comparação se o caractere digitado faz parte das vogais, Caso sim adiciona 1 na variável vogais
Imprime na tela a quantidade das vogais digitadas acrescida das mensagens em aspas
'''




'''
5. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
números reais. O programa deve encontrar: (a) o maior número armazenado, (b) o menor
número armazenado, e (c) a média dos números armazenados.
'''

vetor = []
maior = 0
menor = 0
media = 0

valor = float(input("Digite os números para a lista (pertencentes ao conjunto dos reais) : "))
vetor.append(valor)
menor = valor
maior = valor

for i in range(9) :
    valores = float(input("Digite os números para a lista (pertencentes ao conjunto dos reais) : "))
    vetor.append(valores)

    if valores < menor :
        menor = valores

    if valores > maior :
        maior = valores

media = sum(vetor)
media /= 10

print("(a) Maior número armazenado :", maior,
      "\n(b) Menor número armazenado :", menor,
      "\n(c) Média dos números armazenados :", media)

'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define as variáveis como sendo zero, para após armazenar o valor correspondente a cada variável
Espera a entrada do usuário para o primeiro caso que é especial, pois não existe outro número para comparação
Adiciona esse elemento inserido na lista
Define esse elemento inserido como o maior e o menor número para comparações posteriores
É inserido o comando for (Para) i que assume os valores dentro do range(0,9) que assume os valores de 0 até 8
Espera a entrada dos elementos pelo usuário
Adiciona os elementos digitados na lista
Faz a comparação se o elemento digitado é menor do que o menor valor armazenado, se sim ele passa a ser o menor
Faz a comparação se o elemento digitado é maior do que o maior valor armazenado, se sim ele passa a ser o maior
Faz a soma de todos os números armazenados na lista vetor e depois divide por 10 para obter-se a média
Imprime na tela o maior, menor e média dos númeors armazenados na lista, acrescido das mensagens em aspas
'''




'''
6. Escreva um programa que leia e e armazene em um vetor de 10 posições um conjunto de
caracteres (V_BASE). Em seguida, o programa deve ler um outro conjunto de caracteres e
armazenar em um vetor de 4 posições (V_PROC). O procgrama deve verificar se a
sequência armazenada em V_PROC se encontra dentro de V_BASE.

Exemplo:

V_BASE:
A C B P E B E T O X
V_PROCURA:
B E T O
'''

v_base = []
v_proc = []
v_enc = []
sequencia = bool()

for caractere in range(10):
    vetor_base = input("Digite o caractere da lista base : ")
    v_base.append(vetor_base)

for caractere in range(4):
    vetor_procurar = input("Digite os caracteres desejados para verificação na lista base ")
    v_proc.append(vetor_procurar)

for x in range(len(v_proc)):
    if x > 0:
        break
    for y in range(len(v_base)):
       if v_proc[x] == v_base[y]:
           if x == 0:
               if v_proc[x] in v_enc:
                   v_enc =[]
               v_enc.append(v_proc[x])
               z = x
               z += 1
               w = y
               w += 1
               if z == 4 or w == 10:
                   break

               while v_proc[z] == v_base[w]:
                   v_enc.append(v_proc[z])
                   z += 1
                   w += 1
                   if v_enc == v_proc:
                       sequencia = True
                   if z == 4 or z == 5 or w == 9 or w == 10:
                       break




if sequencia == True:
    print("Lista base: ", v_base,
          "\nLista procurada :", v_proc,
          "\nA sequência para a procura inserida está presente na lista base !")


else:
    print("Lista base: ", v_base,
          "\nLista procurada :", v_proc,
          "\nA sequência para a procura inserida não está presente na lista base !")


'''
O programa realiza o seguinte algoritmo:
Define as variáveis do tipo lista para armazenar os dados nos vetores
Define uma variável do tipo bool (Booleana) para identificar se ocorre uma sequência
Entra em um laço de repetição for para iteração dentro do range até 10
Espera a entrada do usuário e adiciona o elemento inserido no final vetor base
Entra em outro laço de repetição for para iteração dentro do range até 4
Espera a entrada do usuário e adiciona o elemento inserido no final vetor procurar
Entra em outro laço de repetição for para iteração de x dentro do tamanho da lista procurar
Entra em outro laço de repetição for para iteração de y dentro do tamanho da lista base
Se o elemento que estiver no índece x da lista procurar for igual ao elemento que estiver no índece y na lista base
Quando x é maior que zero o laço é quebrado, pois só interessa o primeiro intem da busca para verificação de sequência dos próximos
É feito uma análise para saber se o ídence de x é igual a 0 pois se for é um caso especial por se tratar do primeiro elemento
Se ele foi adicionado mais de uma vez na lista base, é necessário verificar se acontece uma sequência da lista procurado na lista base
Então para cada vez que ele foi adicionado a lista encontrados é apagada para nova verificação de sequência
É definido novas variáveis z e w para verificação de igualdade nos elementos dos índices seguintes
Somando os índeces do primeiro elemento igual com 1, se a soma ultrapassar a quantidade de elementos então o brak para a repetição
Entra em um laço de repetiçao while para fazer uma análise se os elementos seguintes são iguais aos elementos
Somando os índeces do primeiro elemento igual com 1, se a soma ultrapassar a quantidade de elementos então o brak para a repetição
Se todos os elementos seguintes estiverem presentes na lista base de acordo com a sequência da lista procurado
Então significa que a que a sequência é verdadeira, assim sequência recebe True
Repete a verificação de sequência para todos os casos em que o primeiro elemento da lista busca está presente na lista base
Para finalizar, verifica se a variável booleana está verdadeira:
Caso sim, Imprime na tela a lista base, a lista procurada e afirma que a lista procurada está presente em sequência na lista base
Caso não, Imprime na tela a lista base, a lista procurada e afirma que a lista procurada não está presente em sequência na lista base
'''



'''
7. Escreva um programa que leia 5 nomes da entrada padrão e os armazene em um vetor
denominado VETOR A. Em seguida, o programa deve inserir o conteúdo de VETOR A em
ordem inversa em um segundo vetor denominado INVERSO (p. ex., o nome armazenado na
última posição será inserido na primeira, o da penúltima na segunda, e assim por diante).
Exemplo:

VETOR A:
Maria José Pedro Joaquim Teresa
INVERSO:
Teresa Joaquim Pedro José Maria
'''

vetor_A = []
inverso = []

for nomes in range(5):
    nome = input("Digite um nome:")
    vetor_A.append(nome)

for nome_inverte in vetor_A:
    inverso.insert(0,nome_inverte)

print("Lista do vetor com os nomes:\n", vetor_A,
      "\nLita do vetor com as posições dos nomes invertidos:\n",inverso)

'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 5
Espera a entrada do usuário para receber os nomes
adiciona os nomes no final do vetor_A
Entra em outro laço de repetição for para iteração de cada nome no vetor_A
Insere os nomes da iteração no inicio da lista inverso, invertendo assim o vetor_A
Imprime na tela a Lista do vetor_A e a sua lista inversa, acrescida das mensagens entre aspas
'''



'''
8. Em um ADN em dupla hélice, as bases, se estáveis, emparelham-se com as respectivas
bases complementares: Adenina (A) com Timina (T) e Citosina (C) com Guanina (G).
Escreva um programa que dada uma sequência lida da entrada padrão de tamanho 15,
informe a base complementar:
Entrada: AGGGATTCCCCCAG
Saída: TCCCTAAGGGGGTC
'''

adn = []
base_complementar = []

for entrada in range(15):
    espelhamento = input("Digite a entrada do ADN: "
                         "\nAdenina (A); Timina (T); Citosina (C); Guanina (G)")
    adn.append(espelhamento)

for espelhado in adn:
    if espelhado == "A":
        base_complementar.append("T")

    elif espelhado == "T":
        base_complementar.append("A")

    elif espelhado == "C":
        base_complementar.append("G")

    elif espelhado == "G":
        base_complementar.append("C")

    else:
        base_complementar.append("inválido")

print("Base de ADN inserida: \n", adn,
      "\nBases complementares da ADN : \n", base_complementar)



'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 15
Espera a entrada do usuário para receber os bases de ADN
adiciona as bases de ADN no final da lista adn
Entra em outro laço de repetição for para iteração de cada base de ADN na lista adn
Faz o espelhamento da lista de ADN na lista de bases complementares
Sendo analisado a entrada, é relacionado a saída da seguinte maneira:
Adenina (A) com Timina (T) e Citosina (C) com Guanina (G)
Imprime na tela a Lista da base de ADN inserida e a sua lista espelhada com os elementos respectivos da base complementar,
Acrescidas das mensagens entre aspas
'''




'''
9. Escreva um programa que leia e armazene um conjunto de 8 valores numéricos inteiros
quaisquer e o exiba na saída padrão de forma ordenada.
Por exemplo:

ENTRADA:
5 2 18 1 3 6 10 21
SAÍDA:
1 2 3 5 6 10 18 21
'''

conjunto_numerico = []
conjunto_numerico_ordenado = []

for numeros in range(8):
    numero = int(input("Digite o número inteiro para ser armazenado :"))
    conjunto_numerico.append(numero)

conjunto_numerico_ordenado = conjunto_numerico
conjunto_numerico_ordenado.sort()

print("Conjunto númerico inserido : \n", conjunto_numerico,
      "\nConjunto númerico ordenado : \n", conjunto_numerico_ordenado)

'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os números do conjunto númerico
Adiciona cada número no final da lista de conjunto númerico
Define que o conjunto númerico ordendado é igual ao conjunto númerico
Ordena de forma crescente lista conujunto númerico ordenado com o comando conjunto_numerico_ordenado.sort() (.sort())
Imprime na tela a lista com o conjunto de números inseridos e o mesmo conjunto de maneira ordenada
Acrescidas das mensagens em aspas
'''




'''
10. Uma determinada turma tem 10 alunos e cada um faz 4 provas ao longo do ano.
Desenvolva um programa que leia o nome do aluno, suas 4 notas, calcule a média e
armazene o resultado em um vetor. O programa deve permitir operações como: exibir o
nome do aluno com maior média, exibir o aluno com menor média, exibir a média da turma,
e exibir os nomes dos alunos lidos.
Antes de começar a fazer, responda:
· Quantos vetores são necessários?
· Como organizar os índices dos vetores?
'''

'''
Respostas para as perguntas que são feitas antes de se iniciar o programa:
Serão necessários dois vetores um para o nome dos alunos e outro para as notas
Os índices serão organizados de acordo com os valores da iteração de for para cada aluno
'''

quantidade_alunos = 10
quantidade_notas = 4
nomes_alunos =[]
nome_maior_media = ""
nome_menor_media = ""
notas = []
media = 0
maior_media = 0
menor_media = 0
turma_media = 0


for aluno in range(quantidade_alunos):
    nome = input("Digite o nome do aluno : ")
    nomes_alunos.append(nome)
    notas.append([])
    if aluno == 0:
        for primeiro in range(quantidade_notas):
            notas_alunos = float(input("Digite as notas do aluno : "))
            notas[aluno].append(notas_alunos)
            media += notas_alunos
            turma_media += notas_alunos
            if (primeiro + 1) == quantidade_notas:
                media = media / quantidade_notas
                maior_media = media
                nome_maior_media = nome
                menor_media = media
                nome_menor_media = nome
        media = 0
    else:
        for nota in range(quantidade_notas):
            notas_alunos = float(input("Digite as notas do aluno : "))
            notas[aluno].append(notas_alunos)
            media += notas_alunos
            turma_media += notas_alunos

            if (nota + 1) == quantidade_notas:
                media = media / quantidade_notas

                if media > maior_media:
                    maior_media = media
                    nome_maior_media = nome

                if media < menor_media:
                    menor_media = media
                    nome_menor_media = nome
        media = 0



turma_media = turma_media / (quantidade_alunos * quantidade_notas)

operaçao = input('''Digite o número respectivo a operação que deseja realizar :
                 (1) exibir o nome do aluno com maior média, (2) exibir o aluno com menor média,
                 (3) exibir a média da turma, e (4) exibir os nomes dos alunos lidos.''')

if operaçao == "1":
    print("Nome do aluno com a maior média : ", nome_maior_media)

elif operaçao == "2":
    print("Nome do aluno com menor média : ", nome_menor_media)

elif operaçao == "3":
    print("Média de notas da turma : ",turma_media)

elif operaçao == "4":
    print("Nomes dos alunos da lista : ", nomes_alunos)

else:
    print("Inválido ! ")

'''
O programa realiza o seguinte algoritmo:
Define os valores das variáveis, que são dos tipos: Listas, Strings e Inteiros
Entra em laço de repetição for (para) assume cada valor dos alunos até a quantidade informada
Espera a entrada do nome do aluno e o acrescenta na lista dos nomes dos alunos
Adiciona a lista de notas desse aluno
Se for o primeiro aluno, será um caso especial, pois será o primeiro valor de média para comparação das seguintes
Entra em outro laço de repetição para receber os valores das notas desse aluno até a quantidade de provas realizados
Adiciona as notas em uma matriz com o respectivo índece do aluno
Quando o número de notas inseridos é igual a quantidade de provas, é calculado a média
Como o primeiro aluno trata-se de um caso especial,
Os valores da média dele é considerado a maior e menor média usado para comparações posteriores
Após o laço de repetição das notas ser encerrado, a média é zerada para receber a média do novo aluno
Espera a entrada do nome de um novo aluno e o acrescenta na lista dos nomes dos alunos
Adiciona a lista de notas desse aluno
Como esse aluno não é o primeiro, o laço de repetição é diferente, pois já temos um valor de média para comparação
Entra em outro laço de repetição para receber os valores das notas desse aluno até a quantidade de provas realizados
Adiciona as notas em uma matriz com o respectivo índece do aluno
Quando o número de notas inseridos é igual a quantidade de provas, é calculado a média
Como esse aluno não é o primeiro, os valores da média dele é comparado com a maior e menor média anterior
Caso a média desse aluno seja maior que a média maior armazenada, a maior média receberá o valor da média desse aluno e o nome dele
Caso a média desse aluno seja menor que a média menor armazenada, a menor média receberá o valor da média desse aluno e o nome dele
Após o laço de repetição das notas ser encerrado, a média é zerada para receber a média do novo aluno
Esse ciclo se repete até ser inseridas todas informações de alunos e notas de toda a quantidade da turma
No final, é calculado a média total da turma, dividindo todas as notas pela quantidade de alunos por prova
Espera a entrada do usuário para qual operação ele deseja realizar em relação as matrizes inseridas
O programa permiti operações como:
(1) exibir o nome do aluno com maior média, (2) exibir o aluno com menor média,
(3) exibir a média da turma, e (4) exibir os nomes dos alunos lidos.
De acordo com o valor da operação inserido, é análisado para saber qual operação se deseja realizar
Obtendo-se na saída do interpretador do python:
A informação desejada da operação desejada, acrescidas das mensagens entre aspas
'''





'''
11. Escreva um programa que leia e armazene nomes de pessoas em dois vetores distintos
com 8 posições. O programa deve identificar os nomes que constam nos dois vetores.
'''

vetor_nomes_A = []
vetor_nomes_B = []
vetor_nomes_A_e_B = []

for nomes in range(8):
    nome_A = input("Digite o nome para ser armazenado na primeira lista : ")
    vetor_nomes_A.append(nome_A)

for nomes in range(8):
    nome_B = input("Digite o nome para ser armazenado na segunda lista : ")
    vetor_nomes_B.append(nome_B)

for procurado in vetor_nomes_A:
    for procurar in vetor_nomes_B:
        if procurado == procurar:
            if procurado in vetor_nomes_A_e_B:
                break
            vetor_nomes_A_e_B.append(procurado)


if len(vetor_nomes_A_e_B) > 0:
    print("Primeira lista com os nomes armazenados : \n", vetor_nomes_A,
          "\nSegunda lista com os nomes armazenados : \n", vetor_nomes_B,
          "\nNomes que estão presentes em ambas as listas : \n", vetor_nomes_A_e_B)

else:
    print("Primeira lista com os nomes armazenados : \n", vetor_nomes_A,
          "\nSegunda lista com os nomes armazenados : \n", vetor_nomes_B,
          "\nNão existe nomes que estão presentes em ambas as listas !")


'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os nomes da primeira lista do vetor
Adiciona cada nome no final da lista vetor_A
Entra em outro laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os nomes da segunda lista do vetor
Adiciona cada nome no final da lista vetor_B
Entra em outro laço de repetição for para iteração de cada elemento do vetor_A para procurar no vetor_B
Entra em outro laço de repetição for para iteração de cada elemento do vetor_B que será procurado pelo elemento do vetor_A
Caso o elemento que está sendo procurando seja igual ao elemento procurado, significa que o elemento está presente nas duas listas
Se o elemnto que está presente nas duas lista já foi adicionado na lista do vetor_A_e_B, então o laço é quebrado (break) para o elemento não se repetir
Se ainda não está presente na lista do vetor_A_e_B então o elemento é adicionado a lista de nomes que estão presentes em ambas as listas
Imprime na tela a primeira lista de nomes inseridos, a segunda lista de nomes inseridos e
Caso haja nomes presentes em ambas as listas imprime os nomes em comum
Caso não haja nomes presentes em ambas as listas imprime o aviso que não existe
Acrescidas das mensagens em aspas
'''



'''
12. Escreva um programa que leia e armazene números reais em dois vetores distintos com
5 posições. O programa deve inserir os números armazenados em um terceiro vetor com 10
posições de forma ORDENADA.
VETOR A
1 2 5 7 10
VETOR B
3 8 9 11 21
VETOR C
1 2 3 5 7 8 9 10 11 21
'''

vetor_A = []
vetor_B = []
vetor_C = []

for numeros in range(5):
    numero_A = float(input("Digite os números para ser armazenado na primeira lista : "))
    vetor_A.append(numero_A)
    vetor_C.append(numero_A)

for numeros in range(5):
    numero_B = float(input("Digite os números para ser armazenado na segunda lista : "))
    vetor_B.append(numero_B)
    vetor_C.append(numero_B)

vetor_C.sort()

'''
Ou
for numeros in vetor_A:
    vetor_C.append(numeros)
for numeros in vetor_B:
    vetor_C.append(numeros)

vetor_C.sort()
Ou
De forma manual com repetições if, elif e else para verificação de qual é maior o menor para se ordenar
'''


print("Primeira vetor com os números inseridos : \n", vetor_A,
      "\nSegunda vetor com os números inseridos : \n", vetor_B,
      "\nTerceiro vetor com os números inseridos nas duas listas de forma ordenada : \n", vetor_C)


'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 5
Espera a entrada do usuário para receber os números do primeiro vetor
Adiciona cada número no final da lista de vetor A
Adiciona cada número no final da lista de Vetor C
Entra no laço de repetição for para iteração dentro do range até 5
Espera a entrada do usuário para receber os números do segundo vetor
Adiciona cada número no final da lista de vetor B
Adiciona cada número no final da lista de vetor C
Ordena de forma crescente a lista do vetor C com o comando conjunto_numerico_ordenado.sort() (.sort())
Imprime na tela a lista do vetor_A e vetor_B com os números inseridos e
O vetor_C sendo os números das duas listas de maneira ordenada
Acrescidas das mensagens em aspas
'''





