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

