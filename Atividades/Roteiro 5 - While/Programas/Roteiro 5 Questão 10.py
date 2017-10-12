#10. Escreva um programa que leia 10 números quaisquer e informe : o maior valor, o menor valor, a
#média e o desvio padrão.
MAX = 10

cont = 0
menor = 0
maior = 0
média = 0

num = float(input("Digite números quaisquer : "))
menor = num
maior = num
cont += 1
média += num

while True :
    num = float(input("Digite números quaisquer : "))
    cont += 1
    média += num

    if num < menor :
        num = menor

    elif num > maior :
        maior = num

    if cont == MAX :
        break


média = média / MAX

print("\nO menor valor inserido foi :", menor, "O maior valor inserido foi :", maior, "A média dos números inseridos foi :", média)







# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da constante e das variáveis
# Espera a entrada de dez números quaisquer
# Faz comparações entre os números introduzidos
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição de qual número é o menor, o maior e a média por meio de uma comparação matemática
# Imprime na tela os números satisfeitos das condições 
# Atendendo o que se pede na questão