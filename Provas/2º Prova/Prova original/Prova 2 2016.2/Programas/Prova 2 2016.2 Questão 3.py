'''
Questão: 3  Série Periódica
Descrição:
José observou que sua orquídea cresce de acordo com um comportamento
específico. Ele observou que a cada dia a planta crescia um certo valor e modelou
uma função matemática. Vamos ajudar João a saber qual será o tamanho de sua
orquídea em N dias?
Escreva um programa que calcule os N primeiros termos da série S abaixo:
S = 10π + 1/2 + 100π + 3/4 + 1000π + 5/6 + ...
Observação:
= 3.14 π
'''
PI = 3.14
vezes_PI = 1
numerador = 1
denominador = 2

dias = int(input("Digite a quantidade de dias : "))

if dias < 0 :
    print ("Inválido! ")

elif dias == 1 :
    vezes_PI *= 10
    N = vezes_PI * PI

    print("Valor de crescimento da planta de acordo com a quantidade de dias : ", N)

else:
    for N in range(0, dias):
        vezes_PI *= 10

        N = (vezes_PI * PI)

        for S in range(1, dias):
            numerador += 2
            denominador += 2


            S = N + numerador / denominador

    print("Valor de crescimento da planta de acordo com a quantidade de dias : ", S)








'''
Entrada
N = 4
N = 1
N = 0
N = 10

Saída
S = 3173.4
S = 31.400000000000002
S = 0.0
S = 3171717183.9
'''

'''
Saída corrigida
S = 346.65
S = 31.400000000000002
S = 0
S = 348889.25
'''
