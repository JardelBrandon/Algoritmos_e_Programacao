'''
Engenharia deComputação
Disciplina: AlgoritmoseComputação
SemestreLetivo: 2016
Professor:Marcelo Siqueira/HenriqueCunha
Assunto:  Matrizes
Objetivos: 1. Analisar asintaxedecódigosescritosemPython
2. Observar o comportamento da estrutura de dados
conhecida como lista e sua aplicação na resolução de
problemascommatrizes
3. Resolver problemas usando estruturas de repetição e
listas

ROTEIRO DE AULA 10 – 12/07/2016
'''



'''
1. Escreva um programa que leia os valores referentes a uma matriz 6 X 6 de caracteres
(veja o exemplo da figura abaixo). O programa deve então solicitar ao usuário que informe
um caractere qualquer e identificar quantos iguais a ele estão armazenados na matriz.
3  Z  P  Q  M  O
A  Z  F  S  V  O
B  X  D  H  A  I
3  8  A  8  Q  A
5  6  Z  A  M  S
6  6  0  1  S  S
Exemplo:
>>> Informe o caractere a ser procurado: A
>>> Total de caracteres do tipo A é: 5.
'''

matriz = []
quantidade_iguais = 0

for linha in range(6):
    matriz.append([])
    for coluna in range(6):
        elemento = input("Digite o caractere para a Matriz : ")
        matriz[linha].append(elemento)

caractere_igual = input("Informe o caractere a ser procurado na Matriz informada : ")

for linha in matriz:
    for elemento in linha:
        if elemento == caractere_igual:
            quantidade_iguais += 1

print("Matriz informada : ", matriz, "\nTotal de caracteres do tipo", caractere_igual, "é : ", quantidade_iguais)



'''
O programa realiza o seguinte algoritmo:
Define as variáveis do tipo lista e inteiro para armazenamento posterior
Introduz o comando for para adicionar as linhas da Matriz e outro for para coluna
Espera a entrada do usuário para adição dos caracteres informados na Matriz
Após a Matriz ser montada, espera a entrada do usuário para informar um caractere a ser procurado na Matriz
Entra em um novo encadeamento de for, para analisar cada elemento da Matriz e verificar se é igual ao informado
Se o elemento analisado for igual ao caractere inserido, é adicionado 1 a variável de armazenamento da igualdade
Obtendo-se na saída do interpretador python:
>>> A matriz informada e a quantidade de caracteres iguais ao informado encontrados na Matriz,
Acrescidos das mensagens entre aspas
'''






'''
2. Uma determinada turma tem 10 alunos e cada um faz 4 provas ao longo do ano.
Desenvolva um programa que leia o nome do aluno e armazene em um vetor e em seguida
leia suas 4 notas e armazene-as em uma matriz. O programa deve permitir operações
como: (1) exibir o nome do aluno com maior média, (2) exibir o aluno com menor média, (3)
exibir a média da turma, e (4) exibir os nomes dos alunos lidos.
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






