'''
3. Escreva um programa que simule a reserva de poltronas em um avião (assuma uma
matriz 3 X 8 conforme esquema abaixo). O programa deve exibir para o usuário  as
seguintes opções: 1 – reservar poltrona,  2 – liberar poltronas, 3 – informar poltronas
ocupadas, e 4 – sair.
Exemplo do esquema de um avião:
X  0  0  0  0  0  0  0
0  0  X  0  0  0  X  0
0  X  0  0  0  0  0  0
OBSERVAÇÕES:
- Na primeira opção o usuário deve escolher uma poltrona. Caso esteja livre e o
usuário confirme, ela será selecionada (marcar com ‘X’). Do contrário, o programa
deverá solicitar outra cadeira.
- Na segunda opção, o usuário deverá informar a cadeira que ele havia selecionado
e o programa deve liberá-la para outro usuário (marcar com ‘0’). Caso a cadeira
selecionada não tenha sido selecionada, o programa deve informar o erro.
- Na terceira opção, o programa deve informar todas as cadeiras ocupadas.
'''

matriz = []

for linha in range(3):
    matriz.append([])

    for coluna in range(8):
        matriz[linha].append(0)
        print(matriz[linha][coluna], end = ' ')
    print(matriz[linha][coluna], end = '\n')

opçao = input('''Digite o número respectivo a operação que deseja realizar :
                 1 – reservar poltrona,  2 – liberar poltronas, 3 – informar poltronas''')

if opçao == "1":

elif opçao == "2":

elif opçao == "3":

else:
    print("Inválido ! ")


