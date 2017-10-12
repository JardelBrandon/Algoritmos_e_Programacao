'''
10. Escreva um programa que contenha uma função que receba dois números inteiros quaisquer e
retorne a quantidade de ímpares entre os dois.
'''

def impares(inicio, fim, quantidade_impares):
    for comparar in range(inicio, (fim + 1)):
        if comparar % 2 != 0:
            quantidade_impares += 1

    return quantidade_impares

iniciar = int(input("Digite um número inteiro quaisquer : "))
finalizar = int(input("Digite um número inteiro quaisquer : "))
quantidade_impares = 0

resposta = impares(iniciar, finalizar, quantidade_impares)
print(resposta)






'''
O programa realiza o seguinte algoritmo:
Define a função impares(), que contém
Um laço de repetição for para assumir e comparar cada iteração que inicia no valor informado pelo usuário até o valor informado pelo usuário
Dividi cada valor assumido pelo laço for por 2 e compara se o resto é diferente de 0
Se sim, quer dizer que esse número é impar, então a quantidade_impares é adicionada mais 1
No final a função retorna a quantidade de números ímpares entre os números informados
Espera a entrada do usuário para informar o número do ínicio da verificação
Espera a entrada do usuário para informar o número para finalização da verificação
A função impares() é invocada, passando as informações do usuário como parâmetros e aramazenada na variável resposta
Imprimi na tela o valor da variável resposta com a quantidade de números impares
'''