'''
11. Um número a é dito permutação de um número b se os dígitos de a formam uma permutação
dos dígitos de b. Exemplo: 5412434 é uma permutação de 4321445, mas não é uma
permutação de 4312455. Obs.: Considere que o dígito 0 (zero) não aparece nos números.
a. Faça uma função contadígitos que dados um inteiro n e um inteiro d, 0 < d < 9,
devolve quantas vezes o dígito d aparece em n.
b. Usando a função do item anterior, faça um programa que lê dois inteiros positivos a e
b e responda se a é permutação de b.
'''

#a.

def contadigitos(n, d):
    vezes = 0
    for verificar in n:
        if verificar == d:
            vezes += 1
    print(vezes)

numero_n = input("Digite uma sequência númerica : ")
procurar = input("Digite um número para verificar quantas vezes aparece na sequência : ")

if int(procurar) <= 0 or int(procurar) > 9:
    print("Inválido ! ")

else:
    contadigitos(numero_n, procurar)

'''
O programa realiza o seguinte algoritmo:
Define a função contadigitos(), que contém
Uma variável vezes que é igual a 0 para armazenar a quantidade de vezes em que o digito procurado aparece na sequência númerica
Um laço de repetição for para assumir a cada iteração um valor do número informado pelo usuário
Verifica se o valor assumido pelo for é igual ao valor procurado inserido pelo usuário
Se sim adiciona 1 na variável vezes
No final da função imprime na tela quantas vezes o número procurado aparece na sequência númerica
Espera a entrada do usuário para informar a sequência númerica
Espera a entrada do usuário para informar o númerico para verificação dentro da sequência
A função contadigitos() é invocada, passando as informações do usuário como parâmetros
'''

#b.

def permutaçao(a, b,):
    lista_a = []
    lista_b = []
    if len(a) == len(b) and a != b:
        for x in a:
            lista_a.append(int(x))

        for x in b:
            lista_b.append(int(x))
        lista_a.sort()
        lista_b.sort()
        if lista_a == lista_b:
            print("Permutação da primeira sequência númerica em relação a segunda é verdadeira !")

        else:
            print("Permutação da primeira sequência númerica em relação a segunda é falsa !")
    else:
        print("Permutação da primeira sequência númerica em relação a segunda é falsa !")

numero_a = input("Digite a primeira sequência númerica : ")
numero_b = input("Digite a segunda sequência númerica : ")

permutaçao(numero_a, numero_b)




'''
O programa realiza o seguinte algoritmo:
Define a função permutaçao(), que contém
Define duas variáveis dos tipos listas, lista_a e lista_b
Verifica se o tamanho da primeira sequência é igual ao tamnanho da segunda e se são diferentes
Se não, imprime na tela que não existe permutação
Se sim, entra em dois laços de repetição for, que assumem cada valor das sequências númericas informadas
Adiciona cada valor da primeira sequência na lista_a e da segunda sequência na lista_b
Ordena as duas listas de forma crescente com o comando .sort()
verifica se após a ordenação das duas listas, elas são iguais
Se sim, Imprime na tela que a existe permutação
Se não, Imprime na tela que não existe permutação
Espera a entrada do usuário para a primeira sequência númerica
Espera a entrada do usuário para a segunda sequência númerica
A função permutação() é invocada, passando as informações do usuário como parâmetros
'''



