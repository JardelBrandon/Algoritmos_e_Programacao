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











