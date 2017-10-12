'''
1. Escreva um programa que leia os valores referentes a uma matriz 6 X 6 de caracteres
(veja o exemplo da figura abaixo). O programa deve então solicitar ao usuário que informe
um caractere qualquer e identificar quantos iguais a ele estão armazenados na matriz.
3  Z  P  Q  M  O
A  Z  F  S  V  O
B  X  D  H  A  I
3  8  A  8  Q  A
5  6  Z  A  M  S
6  6  0  1  S  S
Exemplo:
>>> Informe o caractere a ser procurado: A
>>> Total de caracteres do tipo A é: 5.
'''

matriz = []
quantidade_iguais = 0

for linha in range(6):
    matriz.append([])
    for coluna in range(6):
        elemento = input("Digite o caractere para a Matriz : ")
        matriz[linha].append(elemento)

caractere_igual = input("Informe o caractere a ser procurado na Matriz informada : ")

for linha in matriz:
    for elemento in linha:
        if elemento == caractere_igual:
            quantidade_iguais += 1

print("Matriz informada : ", matriz, "\nTotal de caracteres do tipo", caractere_igual, "é : ", quantidade_iguais)



'''
O programa realiza o seguinte algoritmo:
Define as variáveis do tipo lista e inteiro para armazenamento posterior
Introduz o comando for para adicionar as linhas da Matriz e outro for para coluna
Espera a entrada do usuário para adição dos caracteres informados na Matriz
Após a Matriz ser montada, espera a entrada do usuário para informar um caractere a ser procurado na Matriz
Entra em um novo encadeamento de for, para analisar cada elemento da Matriz e verificar se é igual ao informado
Se o elemento analisado for igual ao caractere inserido, é adicionado 1 a variável de armazenamento da igualdade
Obtendo-se na saída do interpretador python:
>>> A matriz informada e a quantidade de caracteres iguais ao informado encontrados na Matriz,
Acrescidos das mensagens entre aspas
'''