'''
12. Escreva uma função para verificar se um String é um palíndromo. Escreva um programa para
testar sua função.
'''

def palindromo(palavra):
    palavra_sem_espaço = palavra.replace(' ', '')
    palavra_minuscula = palavra_sem_espaço.lower()
    palavra_invertida = palavra_minuscula[::-1]

    if palavra_invertida == palavra_minuscula:
        print("A string digitada é palíndroma ! ")

    else:
        print("A string digitada não é palíndroma !")


string = input("Digite uma sequência de caracteres para verificar se é palíndromo : ")
palindromo(string)




'''
O programa realiza o seguinte algoritmo:
Define a função palindromo(), que contém
Uma variável palavra_sem_espaço que armazena a palavra informada pelo usuário, retirando os espaços 
Uma variável palavra_minuscula que armazena a palavra informada pelo usuário sem espaços e toda minuscula
Uma variável palavra_invertida que armazena a palavra informada pelo usuário sem espaços e toda minuscula invertida
Verifica se a palavra informada pelo usuário sem espaços, toda minusula e invertida é igual a palavra sem espaços e minuscula informada pelo usuário
Se sim, significa que a string é palíndroma então imprime na tela a string digitada é palíndroma 
Se não, Imprime na tela uma mensagem que a string digitada não é palíndroma 
Espera a entrada do usuário para informar a string que será verificada se é palíndroma 
A função palindromo() é invocada, passando as informações do usuário como parâmetros
'''

