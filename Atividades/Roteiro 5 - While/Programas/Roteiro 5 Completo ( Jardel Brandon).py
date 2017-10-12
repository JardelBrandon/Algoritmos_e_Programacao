#Engenharia deComputação
#Disciplina: AlgoritmoseComputação
#SemestreLetivo: 2016
#Professor:Marcelo Siqueira/HenriqueCunha
#Assunto:  WHILE
#Objetivos: 1. Analisar a sintaxe de códigos escritos em Python
#2. Observar o comportamento da estrutura de repetição
#WHILE
#3. Resolver problemasusando estrutura de repetição
# O comando while pode ser considerado como enquanto a condição for verdadeira
# o programa deve executar seu lação de repetição até a condição ser falsa.


#ROTEIRO DE AULA5 – 07/06/2016


#1. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando umatabela tal como no exemplo abaixo):

# a)

#cont = 0
#soma = 0
#while (cont < 10):
#soma = soma + 2
#cont = cont + 1
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont  1  2  3  4
#soma  2  4  6  8



cont = 0
soma = 0

while (cont < 10):
    soma = soma + 2
    cont = cont + 1

    print("Valor de some é :\n ", soma)


# A saída do interpretador Python apresenta as seguintes saídas:
#iteração  0  1  2  3  4  5  6  7  8  9
#cont  1  2  3  4  5  6  7  8  9
#soma  2  4  6  8  10  12  14  16  18


# b)

#cont = 0
#soma = 0
#while (cont < 10) and (soma % 2 != 0):
#soma = soma + 3
#cont = cont + 1
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma



cont = 0
soma = 0

while (cont < 10) and (soma % 2 != 0):
    soma = soma + 3
    cont = cont + 1

    print("Valor de soma é:\n ", soma)

# A saída do interpretador Python apresenta as seguintes saídas:
#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma
# Poís a segunda condição do and não é atendida



# c)

#cont = 0
#soma = 0
#while (cont <= 6) or (soma < 12):
#soma = soma + 2
#cont = cont + 2
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma

cont = 0
soma = 0

while (cont <= 6) or (soma < 12):
    soma = soma + 2
    cont = cont + 2

    print("Valor de soma é:\n ", soma)


# A saída do interpretador Python apresenta as seguintes saídas:
#iteração  0  1  2  3  4  5  6  7  8  9
#cont  2  4  6  8  10  12
#soma  2  4  6  8  10  12
# Poís enquanto um ou outro for verdadeiro fica encadeiado no laço de repetição

# d)

#cont = 0
#soma = 0
#while (cont <= 6):
#if (cont % 2) == 0:
#soma = soma + 2
#else:
#soma = soma + 3
#cont = cont + 2
#print(“Valor de soma é:\n ”, soma)


#iteração  0  1  2  3  4  5  6  7  8  9
#cont
#soma



cont = 0
soma = 0

while (cont <= 6):
    if (cont % 2) == 0:
        soma = soma + 2
    else:
        soma = soma + 3
    cont = cont + 2

    print("Valor de soma é:\n ", soma)


# A saída do interpretador Python apresenta as seguintes saídas:
#iteração  0  1  2  3  4  5  6  7  8  9
#cont  2  4  6  8
#soma  2  4  6  8






#2. Dado os programas abaixo, identifique os erros sintáticos e/ou faça comentários sobre a execução
#de cada um (cada programa contém um único erro).

# a)

#i = 0
#j = i + 2
#while (i < 10) # Erro na falta do encadeamento ultilizando o comando : no final
#i = i + 1
#print(i)


i = 0
j = i + 2

while (i < 10) :
    i = i + 1

    print(i)

# A saída do interpretador Python apresenta as seguintes saídas:
#intepretador >>>  0  1  2  3  4  5  6  7  8  9  10


# b)


#i = 0
#j = i + 2
#while (i <> 10): # Erro na comparação do comando <> que não existe
#i = i + 1
#print(i)


i = 0
j = i + 2

while (i < 10) :
    i = i + 1

    print(i)

# A saída do interpretador Python apresenta as seguintes saídas:
#intepretador >>>  0  1  2  3  4  5  6  7  8  9  10


#c)


#j = i + 1  # Erro apresentado nessa linha, pois a variável i ainda não foi identificada de acordo com a leitura de cima para baixo
#i = 0
#while (i < 10):
#i = i + 1
#print(i)


i = 0
j = i + 1

while (i < 10):
    i = i + 1

    print(i)


# A saída do interpretador Python apresenta as seguintes saídas:
#intepretador >>>  0  1  2  3  4  5  6  7  8  9  10





#3. Escreva um programa que exiba na saída padrão os 100 primeiros números inteiros positivos
#(incluindo o zero).

NUM_MAX = 100
num = 0


while num < NUM_MAX :
    print (num)
    num += 1


# O Algoritmo do programa realiza os seguintes comandos :
# Define o valor dos contadores
# Introduz o comando while (Enquanto)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Atendendo o que se pede na questão


#4. Escreva um programa que exiba na saída padrão os 100 primeiros números ímpares inteiros
#positivos.

num = 1

while num % 2 != 0 and num <= 200 :
    print (num)
    num += 1
    while num % 2 == 0 :
        num += 1



# O Algoritmo do programa realiza os seguintes comandos :
# Define o valor dos contadores
# Introduz o comando while (Enquanto)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Atendendo o que se pede na questão






#5. Escreva um programa que leia números inteiros aleatórios da entrada padrão até que seja
#informado um número negativo.

while True :
    num = int (input ("Digite um número inteiro aleatório :"))
    print (num)

    if num < 0 :
        break

print (num, "Digito negativo, fim !")



# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Quando a condição não é atendida o programa finaliza
# Atendendo o que se pede na questão





#6. Escreva um programa que leia números da entrada padrão enquanto o(a)usuário(a)s desejar (ou
#seja, enquanto resposta for igual a “SIM”). Quando ele(a) não desejar mais informar números
#(resposta for igual a “NÃO”), será exibido a quantidade e o somatório dos números lidos.

soma = 0
cont = 0

while True :
    num = int (input ("Digite um número : "))
    pergunta = input ("Deseja informar outro número : (SIM) ou NÂO)")
    soma = soma + num
    cont += 1

    if pergunta == "NÃO" :
        break

print ("A somatória dos números digitados foi :", soma , " A quantidade de números digitados foi : ", cont)



# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Espera a entrada de um número e pergunta se o usuário deseja continuar
# Define a condição por meio de uma comparação da resposta caso sim pede outro número caso não
# Imprime na tela a somatória dos números informados e a quantidade de números que foram digitados
# Atendendo o que se pede na questão





#7. Escreva um programa que leia números inteiros da entrada padrão até que seja informado um
#número negativo ou par.

while True :
    num = int (input ("Digite um número inteiro aleatório :"))
    print (num)

    if num < 0  :
        print(num, "Digito negativo, fim !")
        break



    if num % 2 == 0 :
        print(num, "Digito par, fim !")
        break


# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Imprime na tela os números de acordo com a condição imposta
# Quando uma das condições não são atendidas
# O programa imprime o número digitado acrescido da mensagem entre aspas e finaliza
# Atendendo o que se pede na questão






#8. Escreva um programa que leia um nome e uma idade até que uma idade negativa seja lida.
#Quando isso ocorrer informe qual o ultimo nome lido.

while True :
    nome = input ("Digite um nome : ")
    idade = int (input ("Digite uma idade :"))


    if idade < 0 :
        break

print ("Nome :" , nome , "Ultimo nome digitado sendo que a idade digitada foi negativa ! ")


# O Algoritmo do programa realiza os seguintes comandos :
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição por meio de uma comparação matemática
# Quando a condição não é atendida, sendo a idade digitada negativa
# O programa imprime o ultimo nome digitado acrescido da mensagem entre aspas e finaliza
# Atendendo o que se pede na questão







# 9. Escreva um programa que leia um nome e uma idade até que uma idade negativa seja lida.
# Quando isso ocorrer informe o nome da pessoa mais jovem.

jovem = 0

nome = input("Digite um nome : ")
idade = float(input("Digite uma idade :"))

if idade > 0:
    ultimo = nome
    jovem += idade
    while True:
        nome = input("Digite um nome : ")
        idade = float(input("Digite uma idade :"))

        if idade > 0 and idade < jovem:
            ultimo = nome
            jovem = idade

        if idade < 0:
            break

    print("Nome digitado da pessoa mais jovem :", ultimo, "Idade :", jovem)


else:
    print("Inválido")



# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da variável jovem
# Espera a entrada do nome e sua idade
# Faz uma condição para a idade inserida, caso for verdadeiro, entra no seu encadeamento caso não apresenta a mensagem inválido
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Pede novamente a entrada do nome e sua idade
# Define a condição de quem é o mais jovem por meio de uma comparação matemática
# Se repete infinitamente, até que a idade seja um número negativo
# Imprime na tela o nome digitado da pessoa mais jovem entre todos digitados e sua idade
# Atendendo o que se pede na questão






#10. Escreva um programa que leia 10 números quaisquer e informe : o maior valor, o menor valor, a
#média e o desvio padrão.
MAX = 10

cont = 0
menor = 0
maior = 0
média = 0

num = float(input("Digite números quaisquer : "))
menor = num
maior = num
cont += 1
média += num

while True :
    num = float(input("Digite números quaisquer : "))
    cont += 1
    média += num

    if num < menor :
        num = menor

    elif num > maior :
        maior = num

    if cont == MAX :
        break


média = média / MAX

print("\nO menor valor inserido foi :", menor, "O maior valor inserido foi :", maior, "A média dos números inseridos foi :", média)







# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da constante e das variáveis
# Espera a entrada de dez números quaisquer
# Faz comparações entre os números introduzidos
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Define a condição de qual número é o menor, o maior e a média por meio de uma comparação matemática
# Imprime na tela os números satisfeitos das condições
# Atendendo o que se pede na questão









#11. Escreva um programa que calcule os N termos da série S abaixo:
#S = (1/3) + (2/6) + (3/9) + (4/12) + …

dividendo = 1
divisor = 3
quociente = 0
resto = 0

while True :
    quociente = dividendo / divisor
    resto = dividendo % divisor
    print ("O valor da divisão :", dividendo, "/", divisor, "\nTeve como resultado :", quociente, "\nE o resto da módulo da divisão foi :", resto)
    dividendo += 1
    divisor += 3






# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor das variáveis
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas e adiciona 1 ao numerador e 2 ao denominador
# Após executa as operações com os valores adicionados infinitamente
# Imprime na tela os números dos resultados das respectivas divisões
# Atendendo o que se pede na questão




# 12. Escreva um programa que calcule os N termos da série S :
# S = (1/4) + 1 + (3/8) + 1 + (5/12) + …


dividendo = 1
divisor = 4
quociente = 0
resto = 0

while True:
    quociente = (dividendo / divisor) + 1
    resto = dividendo % divisor
    print ("O valor da divisão :", dividendo, "/", divisor, "\nTeve como resultado :", quociente,
           "\nE o módulo da divisão foi :", resto)
    dividendo += 2
    divisor += 4





# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor das variáveis
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas e adiciona 2 ao numerador e 4 ao denominador somando tudo com 1
# Após executa as operações com os valores adicionados infinitamente
# Imprime na tela os números dos resultados das respectivas divisões
# Atendendo o que se pede na questão




#13. Escreva um programa que leia o sexo e o salário de 10 pessoas e calcule:
#- a quantidade de homens;
#- a quantidade de mulheres;
#- a média do salário de homens e de mulheres;
#- o sexo da pessoa com o maior salário;
#- a média de salário dos homens;
MAX = 10

cont = 0
homens = 0
mulheres = 0
maior = 0
sexo_maior = str()
media = 0
media_homens = 0
media_mulheres = 0


sexo = input("Digite seu sexo : \n(M) para Masculino e (F) para Feminino ")
salario = float(input("Digite seu respectivo salário :"))
cont += 1
media += salario
maior = salario

if sexo == "M":
    homens += 1
    media_homens += salario

elif sexo == "F":
    mulheres += 1
    media_mulheres += salario

else:
    print ("Inválido !")

while True :
    sexo = input("Digite seu sexo : (M) para Masculino e (F) para Feminino ")
    salario = float(input("Digite seu respectivo salário :"))
    cont += 1
    media += salario

    if sexo == "M" :
        homens += 1
        media_homens += salario

    elif sexo == "F" :
        mulheres += 1
        media_mulheres += salario

    else :
        print ("Inválido !")

    if salario > maior :
        sexo_maior = sexo
        if sexo_maior == "M" :
            sexo_maior = sexo + " - Masculino"
        elif sexo_maior == "F":
            sexo_maior = sexo + " - Feminino"
        maior = salario

    if cont == MAX :
        break

if media != 0 :
    media /= MAX
if media_homens != 0 :
    media_homens /= homens
if media_mulheres != 0 :
    media_mulheres /= mulheres

print ("Quantidade de homens informado :", homens,"\nQuantidade de mulheres informado :", mulheres,
       "\nMédia salarial dos homens :", media_homens, "\nMédia salarial das mulheres :", media_mulheres,
       "\nSexo da pessoa com o maior salário :", sexo_maior, maior, "\nMédia salarial total :", media)





# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da constante e das variáveis
# Realiza a repetição pela primeira vez fora do laço while para se ter um valor de comparação
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas, faz as comparações das lógicas
# Realiza as operações em seus respectivos encadeamentos
# Imprime na tela A quantidade de homens e mulheres informados, média salarial dos homens e mulheres,
# Sexo do maior salário apresentado e média salarial total acrescidos das mensagens em aspas
# Atendendo o que se pede na questão





'''
14. Uma loja deseja conhecer o perfil de seus (suas) clientes e para isso vai fazer uma pesquisa
usando um programa que ficará no caixa. Ele vai perguntar a cada cliente no momento da compra
as seguintes informações: idade, valor da compra e tipo de pagamento (C: cartão; V: à vista).
Essas perguntas serão feitas enquanto a resposta for SIM. Quando a resposta for NÃO, a pesquisa
deve ser encerrada e o programa deve exibir as seguintes informações:
- a quantidade de vendas realizadas;
- o total de vendas à vista e no cartão;
- a idade do cliente mais jovem;
- o valor da maior compra;
- a média de compras feitas à vista;
'''

vendas = 0
vendas_a_vista = 0
vendas_no_cartao = 0
maior_compra = 0
media_a_vista = 0

idade = float(input("Digite a idade do cliente : "))
valor_da_compra = float(input("Digite o valor da compra : "))
pagamento = input("Digite a forma de pagamento: \nConsidere (C para Cartão ou V para à vista)")
resposta = input("Digite se deseja continuar a pesquisa: \nConsidere (SIM para continuar ou NÃO para encerrar)")
vendas += 1
maior_compra = valor_da_compra
jovem = idade

while True :
    idade = float(input("Digite sua idade : "))
    valor_da_compra = float(input("Digite o valor da compra : "))
    pagamento = input("Digite a forma de pagamento: \nConsidere (C para Cartão ou V para à vista)")
    resposta = input("Digite se deseja continuar a pesquisa: \nConsidere (SIM para continuar ou NÃO para encerrar)")
    vendas += 1

    if pagamento == "V" :
        vendas_a_vista += 1

    if pagamento == "C" :
        vendas_no_cartao += 1

    if idade < jovem :
        jovem = idade

    if valor_da_compra > maior_compra :
        maior_compra = valor_da_compra

    if resposta == "NÃO" :
        break




media_a_vista = vendas / vendas_a_vista

print("Total de vendas à vista e no cartão: ", vendas)
print("Idade do cliente mais jovem :", jovem)
print("Valor da maior compra :", maior_compra)
if media_a_vista == 0 :
    print("Média de compras feitas à vista : 0")
else :
    print("Média de compras feitas à vista :", media_a_vista)






# O Algoritmo do programa realiza os seguintes comandos :
# Declara os valores das variáveis
# Realiza a repetição pela primeira vez fora do laço while para se ter um valor de comparação
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas, faz as comparações das lógicas
# Realiza as operações em seus respectivos encadeamentos
# Imprime na tela o total de vendas, cliente mais jovem, valor da maior compra e média das compras feitas à vista
# Acrescidos das mensagens em aspas
# Atendendo o que se pede na questão





