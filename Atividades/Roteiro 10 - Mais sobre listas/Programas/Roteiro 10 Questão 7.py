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

