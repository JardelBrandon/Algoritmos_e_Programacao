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



