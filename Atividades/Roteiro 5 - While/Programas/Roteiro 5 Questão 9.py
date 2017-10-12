#9. Escreva um programa que leia um nome e uma idade até que uma idade negativa seja lida.
#Quando isso ocorrer informe o nome da pessoa mais jovem.

jovem = 0

nome = input("Digite um nome : ")
idade = float(input("Digite uma idade :"))


if idade > 0 :
    ultimo = nome
    jovem += idade
    while True:
        nome = input("Digite um nome : ")
        idade = float(input("Digite uma idade :"))

        if idade > 0 and idade < jovem :
            ultimo = nome
            jovem = idade

        if idade < 0 :
            break

    print("Nome digitado da pessoa mais jovem :", ultimo, "Idade :", jovem )


else :
    print ("Inválido")



# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da variável jovem
# Espera a entrada do nome e sua idade
# Faz uma condição para a idade inserida, caso for verdadeiro, entra no seu encadeamento caso não apresenta a mensagem inválido
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Pede novamente a entrada do nome e sua idade
# Define a condição de quem é o mais jovem por meio de uma comparação matemática
# Se repete infinitamente, até que a idade seja um número negativo
# Imprime na tela o nome digitado da pessoa mais jovem entre todos digitados e sua idade
# Atendendo o que se pede na questão





