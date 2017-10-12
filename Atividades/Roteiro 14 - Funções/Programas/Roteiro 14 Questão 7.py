'''
7. Faça uma função que receba uma sequência de vários nomes e os imprima um por um de
acordo com o seguinte padrão:
********************
COISINHA DE JESUS
********************
BELTRANO DE TAL
********************
a. A linha de asteriscos deve ser escrita na saída padrão por uma função chamada linha()
b. Faça uma alteração na função linha do item anterior para receber um caractere e
imprimir uma linha desses caracteres em vez de uma linha de asteriscos.
'''

def linha():
    for asteriscos in range(len(nomes)) :
        print("********************")
        for caractere in nomes[asteriscos]:
            print(caractere, end='')
        print("\n********************")

nomes = []

while True:
    palavra = input("Digite uma sequência de nome : ")
    nomes.append(palavra.upper())
    sequencia = input("Digite se deseja inserir mais nomes : "
                  "\nSe sim tecle enter, se não digite (sair)  ")

    if sequencia == "sair":
        break

linha()


'''
O programa realiza o seguinte algoritmo:
Define a função linha() que contém
Um laço for para imprimir uma linha de asteriscos a cada palavra armazenada
Outro laço for que a cada iteração recebe um carctere da palavra armazenada e imprime
Imprime outra linha de asteriscos a baixo da palavra armazenada
Repete-se os passos acima de acordo com a quantidade de palavras inseridas
Define a lista nomes
Entra em um laço de repetição while True
Espera a entrada da sequência de nomes do usuário
Adiciona os nomes inseridos na lista nomes em maísculo com o comando .upper()
Espera o usuário inserir se deseja continuar a digitar mais nomes ou não
Se sim o lação continua
Caso contrário, se ele digitou sair, o laço é quebrado e o programa continua
É invocado a função linha()
Obtendo-se na saída do interpretador python as palavras digitadas,
Com linhas de asteriscos acima e abaixo da palavra digitada
'''