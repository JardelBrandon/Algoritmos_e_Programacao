#7. Escreva um programa que leia números inteiros da entrada padrão até que seja informado um
#número negativo ou par.

while True :
    num = int (input ("Digite um número inteiro aleatório :"))
    print (num)

    if num < 0  :
        print(num, "Digito negativo, fim !")
        break



    if num % 2 == 0 :
        print(num, "Digito par, fim !")
        break


# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Quando uma das condições não são atendidas
# O programa imprime o número digitado acrescido da mensagem entre aspas e finaliza
# Atendendo o que se pede na questão