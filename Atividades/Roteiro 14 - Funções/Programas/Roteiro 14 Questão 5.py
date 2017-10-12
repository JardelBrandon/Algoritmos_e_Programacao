'''
5. Escreva um programa que leia um inteiro não-negativo n e imprima a soma dos n primeiros
números primos. Dica: Use a função da questão anterior.
'''

def primo(numero, divisores):
    for verificar in range(1, numero + 1):
        for dividir in range(1, numero + 1):
            if verificar % dividir == 0:
                divisores += 1

        if divisores == 2:
            primos.append(verificar)

        divisores = 0


    soma_primos = sum(primos)
    return soma_primos

primos = []
numero = int(input("Digite o número para a realização da soma dos primeiros números primos até esse número : "))
divisores = 0
x = primo(numero, divisores)

if numero <= 0:
    print("Inválido!")

elif len(primos) > 1:
    print("Soma dos primeiros números primos até o número inserido :", x,
          "\nNúmero digitado :", numero,
          "\nLista dos primeiros números primos até o número inserido : ", primos)

else:
    print("O número 1 não é um número primo e não antecede nenhum outro (Inválido!) "
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", primos)




'''
O programa realiza o seguinte algoritmo:
Define a função primo(), que possui dois paramêtros numero e divisores
A função contém dois laços for para verificar quais são os números primos que antecedem o número digitado até o número digitado
A verificação consiste em dividir todos on números inteiros antecessores do número digitado pelos números antecessores
Caso a divisão apresente resto zero, então esse número é divisivel do número inserido
Então é adicionado + 1 no contador de divisão
Caso o contador de divisores seja igual a 2 o número é primo, então a função armazena esse número na lista de números primos
Caso contrário, então não acontece nada e o contador de divisores é zerado para realizar nova verificação
No final da função, é realizada uma soma com os primeiros números primos até o número digitado
E a soma da lista dos números primos é armazenada na variável soma_primos que é retornada para o programa
Define a lista de números primos
Espera a entrada do número para verificar a soma dos primeiros números primos até chegar no número digitado
Define o contador de divisores igual a zero
Invoca a função primo() Usando como parâmetros o número inserido e o contador de divisores e armazena o retorno da função na variável x
Caso o número digitado seja negativo, então é impresso na tela que é uma operação inválida, pois não existem primos negativos
Analisa se a variável x e o valor da soma que ela retornou e verfica se é maior que um
Se sim é impresso na tela uma mensagem mostrando a soma dos primeiros números primos até o número digitado, o número digitado e a lista do seus primos antecessores
Se não é impresso na tela uma mensagem afirmando que a operação é inválida, pois o número 1 não é primo e não antecede nenhum outro número primo
'''