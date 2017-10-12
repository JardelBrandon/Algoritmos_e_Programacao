'''
4. Escreva um programa que contenha uma função que verifique se um número lido da entrada
padrão é PRIMO ou não. Retorne True em caso positivo e False em caso negativo.
'''

def primo(numero, divisores):
    for verificar in range(1, numero):
        if numero % verificar == 0:
            divisivel.append(verificar)
            divisores += 1

        if verificar >= numero / 2:
            divisivel.append(numero)
            divisores += 1
            break

    if divisores == 2:
        primos = True

    else:
        primos = False

    return primos

divisivel = []
numero = int(input("Digite o número para verificar se ele é primo : "))
divisores = 0
x = primo(numero, divisores)

if numero <= 0:
    print("Inválido!")

elif x == True:
    print("O número digitado é primo, pois só possui dois divisores!"
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", divisivel)

else:
    print("O número digitado não é primo, pois não possui dois divisores!"
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", divisivel)


'''
O programa realiza o seguinte algoritmo:
Define a função primo(), que possui dois paramêtros numero e divisores
A função contém um laço for para realizar uma verificação se o número digitado é primo
A verificação consiste em dividir todos on números inteiros antecessores do número digitado pelo o número digitado
Caso a divisão apresente resto zero, então esse número é divisivel do número inserido
Então é adicionado + 1 no contador de divisão e esse número é adicionado na lista de divisores
Até chegar na metade do número digitado, onde nenhum número a mais será divisível pelo número digitado
A não ser ele mesmo, então o contador de divisão recebe + 1 e o número digitado é adicionado na lista de divisores
No final da função, Caso o contador de divisores seja igual a 2, a função retorna que primos é verdadeiro (True)
Caso contrário, então o número digitado não é primo e a função retora que primos é falso (False)
Define a lista de números divisíveis
Espera a entrada do número para verificação se ele é primo
Define o contador de divisores igual a zero
Invoca a função primo() Usando como parâmetros o número inserido e o contador de divisores e armazena o retorno da função na variável x
Caso o número digitado seja negativo, então é impresso na tela que é uma operação inválida, pois não existem primos negativos
Analisa se a variável x que armazena o resultado da função retornou True
Se sim é impresso na tela uma mensagem afirmando que o número digitado é primo, mostra o número digitado e seus dois divisores
Se não é impresso na tela uma mensagem afirmando que o número digitado não é primo, mostra o número digitado e a lista de seus divisores
'''