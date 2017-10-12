'''
8. Escreva uma função desenhaQuadrado() que exibe um quadrado sólido (o mesmo número de
linhas e colunas). O caracter utilizando para preencher o quadrado e o valor do lado são
passados como argumentos para a função. Por exemplo, se o caractere for x e o valor do lado
for 5, a função deverá exibir:
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
'''

def desenha_quadrado(caractere, lado):
    for linha in range(lado):
        for coluna in range(lado):
            print(caractere, end=" ")
        print()

caractere = input("Digite o caracere que será utilizado para preencher o quadrado : ")
lado = int(input("Digite o tamanho do quadado : "))

desenha_quadrado(caractere,lado)




'''
O programa realiza o seguinte algoritmo:
Define a função desenha_quadrado(), que contém
Um laço de repetição for para assumir cada valor das linhas do quadrado informado pelo usuário
Outro laço de repetição for para assumir cada valor das colunas do quadrado informado pelo usuário
Imprime cada caratere informado pelo usuário, intercalados com espaço, até o valor da coluna
Imprime uma linha abaixo, quando termina a coluna para outra linha
Formando um quadrado, Sendo o número de linhas igual ao número de colunas
Espera a entrada do usuário para informar o caractere que deseja utilizar para preencher o quadrado
Espera a entrada do usuário para informar o tamanho do quadrado que deseja imprimir
A função desenha_quadrado() é invocada, passando as informações do usuário como parâmetros
'''