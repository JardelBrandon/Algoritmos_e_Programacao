#8. Escreva um programa que leia um nome e uma idade até que uma idade negativa seja lida.
#Quando isso ocorrer informe qual o ultimo nome lido.

while True :
    nome = input ("Digite um nome : ")
    idade = float (input ("Digite uma idade :"))


    if idade < 0 :
        break

print ("Nome :" , nome , "Ultimo nome digitado sendo que a idade digitada foi negativa ! ")


# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Quando a condição não é atendida, sendo a idade digitada negativa
# O programa imprime o ultimo nome digitado acrescido da mensagem entre aspas e finaliza
# Atendendo o que se pede na questão