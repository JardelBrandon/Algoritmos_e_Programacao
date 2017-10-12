'''
12. Escreva um programa que leia e armazene números reais em dois vetores distintos com
5 posições. O programa deve inserir os números armazenados em um terceiro vetor com 10
posições de forma ORDENADA.
VETOR A
1 2 5 7 10
VETOR B
3 8 9 11 21
VETOR C
1 2 3 5 7 8 9 10 11 21
'''

vetor_A = []
vetor_B = []
vetor_C = []

for numeros in range(5):
    numero_A = float(input("Digite os números para ser armazenado na primeira lista : "))
    vetor_A.append(numero_A)
    vetor_C.append(numero_A)

for numeros in range(5):
    numero_B = float(input("Digite os números para ser armazenado na segunda lista : "))
    vetor_B.append(numero_B)
    vetor_C.append(numero_B)

vetor_C.sort()

'''
Ou
for numeros in vetor_A:
    vetor_C.append(numeros)
for numeros in vetor_B:
    vetor_C.append(numeros)

vetor_C.sort()
Ou
De forma manual com repetições if, elif e else para verificação de qual é maior o menor para se ordenar
'''


print("Primeira vetor com os números inseridos : \n", vetor_A,
      "\nSegunda vetor com os números inseridos : \n", vetor_B,
      "\nTerceiro vetor com os números inseridos nas duas listas de forma ordenada : \n", vetor_C)


'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 5
Espera a entrada do usuário para receber os números do primeiro vetor
Adiciona cada número no final da lista de vetor A
Adiciona cada número no final da lista de Vetor C
Entra no laço de repetição for para iteração dentro do range até 5
Espera a entrada do usuário para receber os números do segundo vetor
Adiciona cada número no final da lista de vetor B
Adiciona cada número no final da lista de vetor C
Ordena de forma crescente a lista do vetor C com o comando conjunto_numerico_ordenado.sort() (.sort())
Imprime na tela a lista do vetor_A e vetor_B com os números inseridos e
O vetor_C sendo os números das duas listas de maneira ordenada
Acrescidas das mensagens em aspas
'''