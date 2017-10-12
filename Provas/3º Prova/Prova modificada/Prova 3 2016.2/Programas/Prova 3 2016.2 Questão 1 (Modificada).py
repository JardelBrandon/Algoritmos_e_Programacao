'''
Questão 1: Sequência bitônica
Descrição:
Uma sequência é dita bitônica quando ela é crescente até atingir um ápice (chamado o
ponto bitônico), e a partir do ponto bitônico ela é decrescente.
Escreva um algoritmo que recebe x números informados pelo usuário, sendo que x deve
ser pedido no início do algoritmo. O algoritmo deve imprimir ao final do recebimento dos
valores:
● Se a sequência é biônica / não bitônica
● A posição do ponto bitônico
● Sequência bitônica
Entrada:
7
2
3
4
5
1
0
-2
4
2
10
9
11
3
1
3
2
Saída:
Sequência bitônica
3
2, 3, 4, 5, 1, 0, -2
Sequência não-bitônica
Sequência bitônica
1
1, 3, 2
'''

bitonica = bool()
vetor = []
crescente = 0
decrescente = 0
apice_bitonico = 0


x = int(input("Digite a quantidade de números que serão informados :"))

for numeros in range(x):
    numero = int(input("Digite os números para verificação de sequência : "))
    vetor.append(numero)

for indice in range(len(vetor)):
        if indice == 0:
            crescente = vetor[indice]

        if indice == 1:
            if vetor[indice] < crescente:
                bitonica = False

            else:
                bitonica = False
                crescente = vetor[indice]
                comparaçao_proximo = indice

                while vetor[comparaçao_proximo] >= crescente:
                    crescente = vetor[comparaçao_proximo]
                    comparaçao_proximo +=1
                    if comparaçao_proximo == x:
                        comparaçao_proximo -= 1
                        break

                apice_bitonico = (comparaçao_proximo - 1)

                while vetor[comparaçao_proximo] < crescente:
                    decrescente = vetor[comparaçao_proximo]
                    comparaçao_proximo += 1

                    if comparaçao_proximo == x:
                        bitonica = True
                        break



if bitonica == True:
    print("Sequência bitônica !"
          "\nPosição do índece em que ocorre o ápice bitônico :", apice_bitonico,
          "\nLista da sequência de números inseridos :", vetor)
        
if bitonica == False:
    print("Sequência não bitônica !")






'''
O programa realiza o seguinte algoritmo:
Define as variáveis dos tipos: booleana, lista e float para armazenamento posteriores
Espera a entrada do usuário para inserir a quantidade de números que deseja informar
Entra em um laço de repetição for dentro do range x que vai até o valor informado pelo usuário
Espera a entrada dos números que serão colocados na lista de verificação
Armazena os números informados na lista vetor
Após a lista ser formada, o programa entra em outro laço de repetição dentro do range que vai até o tamanho da lista
Para o primeiro elemento, o caso é especial porque ele será o valor de comparação para os próximos casos
Como para a lista ser bitônica é necessário que os valores a partir do primeiro sejam crescentes
Até um ponto, chamado de ápice em que os valores seguintes serão decrescentes
Dessa forma o segundo elemento é análisado, caso seja menor que o primeiro elemento da lista, a bitõnica é considerada falsa
Se for maior, Ele passa a ser um valor de comparação para o proximo caso, e assim sucessivamente (Laço realizado com o comando while)
Até que o valor de comparação seja menor que o valor do próximo índece, então o laço é encerrado e o valor desse índece é o ápice bitônico
Se a comparação próximo for igual ao número de quantidade de números, o laço é quebrado e o índece subtrai 1 para não ultrapassar o limite da lista
Então o programa entra em outro laço de repetição, para saber se todos os próximos elementos da lista, são menores que o valor comparado
Se caso afirmativo, a Bitônica é verdadeira (True), caso contrário, a Bitônica continua sendo falsa (False).
Finalmente é analisado se a bitônica é falsa, é impresso na tela uma mensagem que informa ao usuário que a sequência não é bitônica
Caso a bitônica seja verdadeira, é impresso na tela uma mensagem que informa ao usuário que a sequência é bitônica,
O índece em que ocorre o ápice bitônico e lista de sequência bitônica inserida pelo usuário, acrescidas das mensagens entre aspas
'''

