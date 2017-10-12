'''
4. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
caracteres. O programa deve contar quantas vogais estão armazenadas no vetor e informar
o resultado na saída padrão.
'''

vetor = []
vogais = 0

for i in range(10) :
    caracteres = input("Digite quaisquer caracteres : ")
    vetor.append(caracteres)

    if caracteres in ["a","e","i","o","u","A","E","I","O","U"] :
        vogais += 1

print("Foram digitadas :", vogais, "Vogais")




'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define a variável vogais como sendo 0
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 até o 10
Espera a entrada dos caracteres pelo usuário
Adiciona os caracteres digitados na lista
Faz a comparação se o caractere digitado faz parte das vogais, Caso sim adiciona 1 na variável vogais
Imprime na tela a quantidade das vogais digitadas acrescida das mensagens em aspas
'''
