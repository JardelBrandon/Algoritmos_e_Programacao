'''
13. Escreva uma função que receba um número inteiro e retorne seu fatorial.
'''

def fatorial(numero):
    if numero == 0:
        print("Número informado : 0"
              "\nFatorial do número informado : 1")

    else:
        resposta = numero
        while numero > 1:
            numero -= 1
            resposta *= numero

        print("Número informado : ", valor,
              "\nFatorial do número informado : ",resposta)

valor = int(input("Digite um número para receber o valor de seu fatorial : "))

if valor < 0:
    print("Inválido ! ")
else:
    fatorial(valor)




'''
O programa realiza o seguinte algoritmo:
Define a função fatorial(), que contém
Uma verificação se o número informado pelo usuário é 0
Se sim, então é um caso especial, pois o fatorial de 0 é igual a 1 diferente do padrão 
Então, é impresso na tela o número informado que foi zero e o seu fatorial que é 1 
Se não, é definido uma variável resposta que recebe o valor informado pelo usuário 
Entra em um laço de repetição enquanto o número informado é maior que 1 
Subtrai 1 do valor do número informado pelo usuário 
A variável resposta armazena o valor da multiplicação dela pelo número informado pelo usuário que foi subtraído de 1 
Quando o número informado é subtraído de 1 até chegar em 1 quebra o laço de repetição
Então, é impresso na tela o número informado pelo usuário e o valor de seu fatorial
Espera a entrada do usuário para informar o número que deseja para retornar o seu valor fatorial
Se o número informado for menor que 0 é impresso um mensagem de inválido
Se não a função fatorial() é invocada, passando as informações do usuário como parâmetros
'''