'''
9. Escreva um programa que contenha uma função que receba uma palavra e um número inteiro
e imprima esse na saída padrão a palavra a quantidade de vezes igual ao numero recebido.
'''

def imprimir_palavra(palvra, vezes):
    for vez in range(vezes):
        print(palvra)

nome = input("Digite a palavra que deseja imprimir : ")
quantidade = int(input("Dogite a quantidade de vezes que deseja imprimir : "))

imprimir_palavra(nome, quantidade)




'''
O programa realiza o seguinte algoritmo:
Define a função imprimir_palavra(), que contém
Um laço de repetição for para assumir cada iteração de 0 até o valor informado
Imprime a cada iteração formada a palvra informada pelo usuário o número de vezes informado
Espera a entrada do usuário para informar a palavra que deseja imprimir
Espera a entrada do usuário para informar a quantidade de vezes que desja imprimir a palavra informada
A função imprimir_palavra() é invocada, passando as informações do usuário como parâmetros
'''