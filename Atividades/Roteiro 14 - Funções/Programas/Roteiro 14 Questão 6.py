'''
6. Escreva uma função que verifique se uma letra qualquer está contida em uma string.
'''

def verifique():
    for verificar in palavra:
        if verificar == letra:
            contida = True
            break
        else:
            contida = False

    return contida


contida = bool()
palavra = input("Digite uma palavra para ser armazenada : ")
letra = input("Digite uma letra para verficar se está contida na palavra armazenada : ")

x = verifique()

if x == True:
    print("A letra digitada está contida na palavra armazenada ! ")

else:
    print("A letra digitada não está contida na palavra armazenada ! ")


'''
O programa realiza o seguinte algoritmo:
Define a função verifique() que contém a verificação
Em um laço for que assume cada letra da palavra armazenda a cada iteração e análisa se é igual a letra digitada
Se sim a letra está contida na palavra então a verificação booleana contida recebe True (Verdadeiro)
Se não a verificação booleana contida recebe False (Falso)
Define contida como uma expressão booleana
Espera a entrada da palavra para ser armazenada
Espera a entrada da letra para verificar se ele está contida na palavra
Invoca a função verifique() e armazena o retorno da expressão booleana contida na variável x
Verifica se a variável x é Verdadeira (True)
Se sim, imprime na tela que a letra digitada está contida na palavra armazenada
Se não, imprime na tela que a letra não digitada está contida na palavra armazenada
'''