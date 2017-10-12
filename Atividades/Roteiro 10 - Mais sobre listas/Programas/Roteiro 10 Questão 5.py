'''
5. Escreva um programa que leia e armazene em um vetor de 10 posições um conjunto de
números reais. O programa deve encontrar: (a) o maior número armazenado, (b) o menor
número armazenado, e (c) a média dos números armazenados.
'''

vetor = []
maior = 0
menor = 0
media = 0

valor = float(input("Digite os números para a lista (pertencentes ao conjunto dos reais) : "))
vetor.append(valor)
menor = valor
maior = valor

for i in range(9) :
    valores = float(input("Digite os números para a lista (pertencentes ao conjunto dos reais) : "))
    vetor.append(valores)

    if valores < menor :
        menor = valores

    if valores > maior :
        maior = valores

media = sum(vetor)
media /= 10

print("(a) Maior número armazenado :", maior,
      "\n(b) Menor número armazenado :", menor,
      "\n(c) Média dos números armazenados :", media)

'''
O programa realiza o seguinte algoritmo :
Define a variável vetor como sendo uma lista
Define as variáveis como sendo zero, para após armazenar o valor correspondente a cada variável
Espera a entrada do usuário para o primeiro caso que é especial, pois não existe outro número para comparação
Adiciona esse elemento inserido na lista
Define esse elemento inserido como o maior e o menor número para comparações posteriores
É inserido o comando for (Para) i que assume os valores dentro do range(0,9) que assume os valores de 0 até 8
Espera a entrada dos elementos pelo usuário
Adiciona os elementos digitados na lista
Faz a comparação se o elemento digitado é menor do que o menor valor armazenado, se sim ele passa a ser o menor
Faz a comparação se o elemento digitado é maior do que o maior valor armazenado, se sim ele passa a ser o maior
Faz a soma de todos os números armazenados na lista vetor e depois divide por 10 para obter-se a média
Imprime na tela o maior, menor e média dos númeors armazenados na lista, acrescido das mensagens em aspas
'''
