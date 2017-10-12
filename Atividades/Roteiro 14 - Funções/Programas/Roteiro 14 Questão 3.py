'''
3. Escreva um programa que contenha uma função que verifique se um número lido da entrada
padrão é PAR ou não.
'''

def par():
    if numero % 2 == 0:
        x = "O número inserido é par : "
    else:
        x = "O número inserido não é par : "

    return x

numero = float(input("Digite um número para verificar se ele é par ou não :"))

print(par(), numero)




'''
O programa realiza o seguinte algoritmo:
Define a função nomeada como par()
A função contém uma verificação se o número inserido é par ou não
Se o número divído por dois possuir o resto igual a zero, ele é par
Se não, ele não é par
x recebe a mensagem de acordo se ele é par ou não e retorna esse valor para o programa
Espera a entrada do número pelo usuário para a verificação
Invoca a função par() e espera o retorno de x para imprimir a mensagem se é par ou não, acrescido do número digitado
Obtendo-se na saída padrão do python: A informação se ele é par ou não
'''
