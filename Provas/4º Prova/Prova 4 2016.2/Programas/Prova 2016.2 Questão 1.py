'''
Questão 1:
Leet é uma maneira de escrever palavras na qual algumas letras, sílabas ou palavras são
substituídas por números ou símbolos. Isso é muito usado no contexto da informática para
confundir leitores "não iniciados” ou escrever de forma resumida (por exemplo, na escrita
de tweets).
Dentro desse contexto, você vai escrever um programa que que transforma palavras na
grafia comum em palavras na escrita Leet de forma invertida.
Ao final, o programa deve informar a quantidade de substituições realizadas.
Use a seguinte codificação:
a, A: @
e, E: 3
i, I: 1
o, O: 0
t, T: 7
s, S: 5
Não haverão palavras acentuadas.
Se o usuário informar uma string vazia, o programa emitirá uma mensagem de erro e a
quantidade 0 (zero).
Se o usuário informar uma string que contém pelo menos um número, o programa
escreverá uma mensagem de erro e a quantidade 0 (zero).
O código deve fazer uso de funções sempre que necessário, observando os princípios da
modularização e separação de objetivos.
Entrada
>> marcelo
>> 1999
>> Turing
Saída
0l3cr@m
3
erro
0
gn1ru7
2
'''

def verificar_erro(texto):
    quantidade_de_substituiçoes = 0
    valido = True
    if texto == "":
        valido = False
        print("Erro, String vazia ! "
              "\nQuantidade de substituições realizadas : ", quantidade_de_substituiçoes)
    '''
    Trecho de código que seria usado se caso a string contesse apenas espaços em brancos fosse um erro:
    elif texto.isspace() == True:
        valido == False
        print("Erro, String contém somente espaços em branco:", texto,
              "\nQuantidade de substituições realizadas : ", quantidade_de_substituiçoes)
    '''

    for caractere in range(len(texto)):
        if texto[caractere].isnumeric() == True:
            valido = False
            print("A string informada é inválida, pois contém número(s) :",texto,
                  "\nQuantidade de substituições realizadas : ", quantidade_de_substituiçoes)
            break

    return valido





def substituir(texto):
    quantidade_de_substituiçoes = 0
    for caractere in range(len(texto)):
        if texto[caractere] ==  "a":
            texto = texto.replace("a", "@", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "A":
            texto = texto.replace("A", "@", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "e":
            texto = texto.replace("e", "3", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "E":
            texto = texto.replace("E", "3", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "i":
            texto = texto.replace("i", "1", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "I":
            texto = texto.replace("I", "1", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "o":
            texto = texto.replace("o", "0", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "O":
            texto = texto.replace("O", "0", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "t":
            texto = texto.replace("t", "7", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "T":
            texto = texto.replace("T", "7", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "s":
            texto = texto.replace("s", "5", 1)
            quantidade_de_substituiçoes += 1

        elif texto[caractere] == "S":
            texto = texto.replace("S", "5", 1)
            quantidade_de_substituiçoes += 1


    texto_invertido = texto[::-1]
    print("Novo texto com caracteres substituidos e invertido :",texto_invertido,
          "\nQuantidade de substituições realizadas :",quantidade_de_substituiçoes)

string = input("Digite letras, sílabas ou palavras : ")

if verificar_erro(string) == True:
    substituir(string)
