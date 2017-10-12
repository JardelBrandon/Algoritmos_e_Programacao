'''
2. Crie e preencha uma lista com 10 valores lidos da entrada padrão. No final, imprima a lista na
tela.
'''

lista = []

for i in range(0,10) :
    valores = float(input("Digite quaisquer valor : "))
    lista.append(valores)

print(lista)

'''
O programa realiza o seguinte algoritmo :
Define uma variável do tipo lista
É inserido o comando for (Para) i que assume os valores dentro do range(0,10) que vai de 0 a 9
Espera a entrada dos valores pelo usuário
Adiciona os valores digitados na lista
Imprime na tela a lista com os 10 valores lidos
'''