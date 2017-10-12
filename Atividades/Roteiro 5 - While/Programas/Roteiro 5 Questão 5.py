#5. Escreva um programa que leia números inteiros aleatórios da entrada padrão até que seja
#informado um número negativo.

while True :
    num = int (input ("Digite um número inteiro aleatório :"))
    print (num)

    if num < 0 :
        break

print (num, "Digito negativo, fim !")



# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Quando a condição não é atendida o programa finaliza
# Atendendo o que se pede na questão