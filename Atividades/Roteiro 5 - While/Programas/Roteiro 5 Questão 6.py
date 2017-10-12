#6. Escreva um programa que leia números da entrada padrão enquanto o(a)usuário(a)s desejar (ou
#seja, enquanto resposta for igual a “SIM”). Quando ele(a) não desejar mais informar números
#(resposta for igual a “NÃO”), será exibido a quantidade e o somatório dos números lidos.

soma = 0
cont = 0

while True :
    num = int (input ("Digite um número : "))
    pergunta = input ("Deseja informar outro número : (SIM) ou NÂO)")
    soma = soma + num
    cont += 1

    if pergunta == "NÃO" :
        break

print ("A somatória dos números digitados foi :", soma , " A quantidade de números digitados foi : ", cont)



# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Espera a entrada de um número e pergunta se o usuário deseja continuar
# Define a condição por meio de uma comparação da resposta caso sim pede outro número caso não
# Imprime na tela a somatória dos números informados e a quantidade de números que foram digitados
# Atendendo o que se pede na questão