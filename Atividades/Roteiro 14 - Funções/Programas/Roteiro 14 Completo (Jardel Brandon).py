'''
Engenharia de Computação
Disciplina: Algoritmos e Computação
Semestre Letivo: 2016
Professor: Marcelo Siqueira / Henrique Cunha
Assunto:  Exceções
Objetivos: 1. Analisar a sintaxe de códigos escritos em Python

ROTEIRO DE AULA 14 – 26/07/2016
'''

'''
1. Escreva um programa que contenha uma função que imprima na saída padrão a palavra
"Engenharia" 10 vezes.
'''

def imprimir():
    print("Engenharia")

for i in range(10):
    imprimir()



'''
O programa realiza o seguinte algoritmo:
Define a função nomeada como imprimir()
A função contém imprimir (print) a palavra engenharia
Entra em um for que vai de 0 até 9
Onde a função imprimir() é invocada a cada iteração do for
Obtendo-se na saída padrão do python: A palavra engenharia 10 vezes
'''



'''
2. Escreva um programa que contenha uma função que some dois números e retorne o resultado.
'''

def soma():
    x = a + b
    return x


a = float(input("Digite o primeiro número para a soma :"))
b = float(input("Digite o segundo número para ser somado :"))

print(soma())





'''
O programa realiza o seguinte algoritmo:
Define a função nomeada como soma()
A função contém uma variável que soma os valores informados de a e b
Espera a entrada pelo usuário para inserir os valores a e b para serem somados
Invoca a função, que realiza a soma das variáveis a e b e armazena na variável x, e retorna o valor de x para o programa
Obtendo-se na saída padrão do python: O valor da soma
'''




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





'''
4. Escreva um programa que contenha uma função que verifique se um número lido da entrada
padrão é PRIMO ou não. Retorne True em caso positivo e False em caso negativo.
'''

def primo(numero, divisores):
    for verificar in range(1, numero):
        if numero % verificar == 0:
            divisivel.append(verificar)
            divisores += 1

        if verificar >= numero / 2:
            divisivel.append(numero)
            divisores += 1
            break

    if divisores == 2:
        primos = True

    else:
        primos = False

    return primos

divisivel = []
numero = int(input("Digite o número para verificar se ele é primo : "))
divisores = 0
x = primo(numero, divisores)

if numero <= 0:
    print("Inválido!")

elif x == True:
    print("O número digitado é primo, pois só possui dois divisores!"
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", divisivel)

else:
    print("O número digitado não é primo, pois não possui dois divisores!"
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", divisivel)


'''
O programa realiza o seguinte algoritmo:
Define a função primo(), que possui dois paramêtros numero e divisores
A função contém um laço for para realizar uma verificação se o número digitado é primo
A verificação consiste em dividir todos on números inteiros antecessores do número digitado pelo o número digitado
Caso a divisão apresente resto zero, então esse número é divisivel do número inserido
Então é adicionado + 1 no contador de divisão e esse número é adicionado na lista de divisores
Até chegar na metade do número digitado, onde nenhum número a mais será divisível pelo número digitado
A não ser ele mesmo, então o contador de divisão recebe + 1 e o número digitado é adicionado na lista de divisores
No final da função, Caso o contador de divisores seja igual a 2, a função retorna que primos é verdadeiro (True)
Caso contrário, então o número digitado não é primo e a função retora que primos é falso (False)
Define a lista de números divisíveis
Espera a entrada do número para verificação se ele é primo
Define o contador de divisores igual a zero
Invoca a função primo() Usando como parâmetros o número inserido e o contador de divisores e armazena o retorno da função na variável x
Caso o número digitado seja negativo, então é impresso na tela que é uma operação inválida, pois não existem primos negativos
Analisa se a variável x que armazena o resultado da função retornou True
Se sim é impresso na tela uma mensagem afirmando que o número digitado é primo, mostra o número digitado e seus dois divisores
Se não é impresso na tela uma mensagem afirmando que o número digitado não é primo, mostra o número digitado e a lista de seus divisores
'''






'''
5. Escreva um programa que leia um inteiro não-negativo n e imprima a soma dos n primeiros
números primos. Dica: Use a função da questão anterior.
'''

def primo(numero, divisores):
    for verificar in range(1, numero + 1):
        for dividir in range(1, numero + 1):
            if verificar % dividir == 0:
                divisores += 1

        if divisores == 2:
            primos.append(verificar)

        divisores = 0


    soma_primos = sum(primos)
    return soma_primos

primos = []
numero = int(input("Digite o número para a realização da soma dos primeiros números primos até esse número : "))
divisores = 0
x = primo(numero, divisores)

if numero <= 0:
    print("Inválido!")

elif len(primos) > 1:
    print("Soma dos primeiros números primos até o número inserido :", x,
          "\nNúmero digitado :", numero,
          "\nLista dos primeiros números primos até o número inserido : ", primos)

else:
    print("O número 1 não é um número primo e não antecede nenhum outro (Inválido!) "
          "\nNúmero digitado :", numero,
          "\nLista de seus divisores : ", primos)




'''
O programa realiza o seguinte algoritmo:
Define a função primo(), que possui dois paramêtros numero e divisores
A função contém dois laços for para verificar quais são os números primos que antecedem o número digitado até o número digitado
A verificação consiste em dividir todos on números inteiros antecessores do número digitado pelos números antecessores
Caso a divisão apresente resto zero, então esse número é divisivel do número inserido
Então é adicionado + 1 no contador de divisão
Caso o contador de divisores seja igual a 2 o número é primo, então a função armazena esse número na lista de números primos
Caso contrário, então não acontece nada e o contador de divisores é zerado para realizar nova verificação
No final da função, é realizada uma soma com os primeiros números primos até o número digitado
E a soma da lista dos números primos é armazenada na variável soma_primos que é retornada para o programa
Define a lista de números primos
Espera a entrada do número para verificar a soma dos primeiros números primos até chegar no número digitado
Define o contador de divisores igual a zero
Invoca a função primo() Usando como parâmetros o número inserido e o contador de divisores e armazena o retorno da função na variável x
Caso o número digitado seja negativo, então é impresso na tela que é uma operação inválida, pois não existem primos negativos
Analisa se a variável x e o valor da soma que ela retornou e verfica se é maior que um
Se sim é impresso na tela uma mensagem mostrando a soma dos primeiros números primos até o número digitado, o número digitado e a lista do seus primos antecessores
Se não é impresso na tela uma mensagem afirmando que a operação é inválida, pois o número 1 não é primo e não antecede nenhum outro número primo
'''



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




'''
7. Faça uma função que receba uma sequência de vários nomes e os imprima um por um de
acordo com o seguinte padrão:
********************
COISINHA DE JESUS
********************
BELTRANO DE TAL
********************er444444444444444444444
a. A linha de asteriscos deve ser escrita na saída padrão por uma função chamada linha()
b. Faça uma alteração na função linha do item anterior para receber um caractere e
imprimir uma linha desses caracteres em vez de uma linha de asteriscos.
'''

def linha():
    for asteriscos in range(len(nomes)) :
        print("********************")
        for caractere in nomes[asteriscos]:
            print(caractere, end='')
        print("\n********************")

nomes = []

while True:
    palavra = input("Digite uma sequência de nome : ")
    nomes.append(palavra.upper())
    sequencia = input("Digite se deseja inserir mais nomes : "
                  "\nSe sim tecle enter, se não digite (sair)  ")

    if sequencia == "sair":
        break

linha()


'''
O programa realiza o seguinte algoritmo:
Define a função linha() que contém
Um laço for para imprimir uma linha de asteriscos a cada palavra armazenada
Outro laço for que a cada iteração recebe um carctere da palavra armazenada e imprime
Imprime outra linha de asteriscos a baixo da palavra armazenada
Repete-se os passos acima de acordo com a quantidade de palavras inseridas
Define a lista nomes
Entra em um laço de repetição while True
Espera a entrada da sequência de nomes do usuário
Adiciona os nomes inseridos na lista nomes em maísculo com o comando .upper()
Espera o usuário inserir se deseja continuar a digitar mais nomes ou não
Se sim o lação continua
Caso contrário, se ele digitou sair, o laço é quebrado e o programa continua
É invocado a função linha()
Obtendo-se na saída do interpretador python as palavras digitadas,
Com linhas de asteriscos acima e abaixo da palavra digitada
'''






'''
8. Escreva uma função desenhaQuadrado() que exibe um quadrado sólido (o mesmo número de
linhas e colunas). O caracter utilizando para preencher o quadrado e o valor do lado são
passados como argumentos para a função. Por exemplo, se o caractere for x e o valor do lado
for 5, a função deverá exibir:
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
'''

def desenha_quadrado(caractere, lado):
    for linha in range(lado):
        for coluna in range(lado):
            print(caractere, end=" ")
        print()

caractere = input("Digite o caracere que será utilizado para preencher o quadrado : ")
lado = int(input("Digite o tamanho do quadado : "))

desenha_quadrado(caractere,lado)




'''
O programa realiza o seguinte algoritmo:
Define a função desenha_quadrado(), que contém
Um laço de repetição for para assumir cada valor das linhas do quadrado informado pelo usuário
Outro laço de repetição for para assumir cada valor das colunas do quadrado informado pelo usuário
Imprime cada caratere informado pelo usuário, intercalados com espaço, até o valor da coluna
Imprime uma linha abaixo, quando termina a coluna para outra linha
Formando um quadrado, Sendo o número de linhas igual ao número de colunas
Espera a entrada do usuário para informar o caractere que deseja utilizar para preencher o quadrado
Espera a entrada do usuário para informar o tamanho do quadrado que deseja imprimir
A função desenha_quadrado() é invocada, passando as informações do usuário como parâmetros
'''




'''
9. Escreva um programa que contenha uma função que receba uma palavra e um número inteiro
e imprima esse na saída padrão a palavra a quantidade de vezes igual ao numero recebido.
'''

def imprimir_palavra(palvra, vezes):
    for vez in range(vezes):
        print(palvra)

nome = input("Digite a palavra que deseja imprimir : ")
quantidade = int(input("Dogite a quantidade de vezes que deseja imprimir : "))

imprimir_palavra(nome, quantidade)




'''
O programa realiza o seguinte algoritmo:
Define a função imprimir_palavra(), que contém
Um laço de repetição for para assumir cada iteração de 0 até o valor informado
Imprime a cada iteração formada a palvra informada pelo usuário o número de vezes informado
Espera a entrada do usuário para informar a palavra que deseja imprimir
Espera a entrada do usuário para informar a quantidade de vezes que desja imprimir a palavra informada
A função imprimir_palavra() é invocada, passando as informações do usuário como parâmetros
'''




'''
10. Escreva um programa que contenha uma função que receba dois números inteiros quaisquer e
retorne a quantidade de ímpares entre os dois.
'''

def impares(inicio, fim, quantidade_impares):
    for comparar in range(inicio, (fim + 1)):
        if comparar % 2 != 0:
            quantidade_impares += 1

    return quantidade_impares

iniciar = int(input("Digite um número inteiro quaisquer : "))
finalizar = int(input("Digite um número inteiro quaisquer : "))
quantidade_impares = 0

resposta = impares(iniciar, finalizar, quantidade_impares)
print(resposta)






'''
O programa realiza o seguinte algoritmo:
Define a função impares(), que contém
Um laço de repetição for para assumir e comparar cada iteração que inicia no valor informado pelo usuário até o valor informado pelo usuário
Dividi cada valor assumido pelo laço for por 2 e compara se o resto é diferente de 0
Se sim, quer dizer que esse número é impar, então a quantidade_impares é adicionada mais 1
No final a função retorna a quantidade de números ímpares entre os números informados
Espera a entrada do usuário para informar o número do ínicio da verificação
Espera a entrada do usuário para informar o número para finalização da verificação
A função impares() é invocada, passando as informações do usuário como parâmetros e aramazenada na variável resposta
Imprimi na tela o valor da variável resposta com a quantidade de números impares
'''






'''
11. Um número a é dito permutação de um número b se os dígitos de a formam uma permutação
dos dígitos de b. Exemplo: 5412434 é uma permutação de 4321445, mas não é uma
permutação de 4312455. Obs.: Considere que o dígito 0 (zero) não aparece nos números.
a. Faça uma função contadígitos que dados um inteiro n e um inteiro d, 0 < d < 9,
devolve quantas vezes o dígito d aparece em n.
b. Usando a função do item anterior, faça um programa que lê dois inteiros positivos a e
b e responda se a é permutação de b.
'''


# a.

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


# b.

def permutaçao(a, b, ):
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




'''
13. Escreva uma função que receba um número inteiro e retorne seu fatorial.
'''

def fatorial(numero):
    if numero == 0:
        print("Número informado : 0"
              "\nFatorial do número informado : 1")

    else:
        resposta = numero
        while numero > 1:
            numero -= 1
            resposta *= numero

        print("Número informado : ", valor,
              "\nFatorial do número informado : ",resposta)

valor = int(input("Digite um número para receber o valor de seu fatorial : "))

if valor < 0:
    print("Inválido ! ")
else:
    fatorial(valor)




'''
O programa realiza o seguinte algoritmo:
Define a função fatorial(), que contém
Uma verificação se o número informado pelo usuário é 0
Se sim, então é um caso especial, pois o fatorial de 0 é igual a 1 diferente do padrão 
Então, é impresso na tela o número informado que foi zero e o seu fatorial que é 1 
Se não, é definido uma variável resposta que recebe o valor informado pelo usuário 
Entra em um laço de repetição enquanto o número informado é maior que 1 
Subtrai 1 do valor do número informado pelo usuário 
A variável resposta armazena o valor da multiplicação dela pelo número informado pelo usuário que foi subtraído de 1 
Quando o número informado é subtraído de 1 até chegar em 1 quebra o laço de repetição
Então, é impresso na tela o número informado pelo usuário e o valor de seu fatorial
Espera a entrada do usuário para informar o número que deseja para retornar o seu valor fatorial
Se o número informado for menor que 0 é impresso um mensagem de inválido
Se não a função fatorial() é invocada, passando as informações do usuário como parâmetros
'''




'''
14. Faça um programa com uma função chamada calculaImposto. A função tem dois parâmetros:
imposto, que é a quantidade de imposto sobre vendas expressa em porcentagem e custo, que é
o valor do produto antes do imposto.
'''

def calcula_imposto(imposto, custo):
    total = imposto / 100 * custo + custo
    print("Custo inicial do produto : ", custo,
          "\nValor do imposto expressa em porcentagem : ",imposto,"%",
          "\nCusto final do produto (Acrescido da porcentagem) : ",total)

impostos = float(input("Digite o valor do imposto em porcentagem : "))
valor = float(input("Digite o preço do produto : "))

calcula_imposto(impostos, valor)




'''
O programa realiza o seguinte algoritmo:
Define a função calcula_imposto(), que contém
Uma variável total que armazena o cálculo do produto acrescido do imposto incidente nele
Imprime o custo inicial do produto, o valor da porcentagem e o custo final acrescido da porcentagem incidente
Espera a entrada do usuário para informar o valor do imposto a ser acrescido
Espera a entrada do usuário para informar o valor inicial do produto
A função calcula_imposto() é invocada, passando as informações do usuário como parâmetros
'''

