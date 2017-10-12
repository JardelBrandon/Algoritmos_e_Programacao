#Engenharia de Computação
#Disciplina: Algoritmos e Computação
#Semestre Letivo: 2016
#Professor: Marcelo Siqueira / Henrique Cunha
#ROTEIRO DE AULA 1 – 19/05/2016
#Objetivos:
#a. Apresentar ao aluno alguns exemplos de Ambientes de Desenvolvimento
#Integrado.
#b. Observar o comportamento do interpretador a partir de comandos
#aritméticos
#c. Entender o funcionamento do comando input e suas variações.


#1. Em um papel à papel, resolva as expressões a seguir. Em seguida,
#utilizando o prompt do interpretador do Python (>>>), digite cada uma
#delas e observe se o valor produzido condiz com o resolvido.
#a) (723/87) > 52

( 723 / 87 ) > 52

# O valor da operação feita no papel foi de ( 723 / 87 ) = 8,310344...
# Que é um valor menor que o 52 usado na comparação
# No Interpretador do Python foi obtido uma saída Falsa pois a comparação está errada
# >>> False




#b) (216-36)*4 == 2**4


( 216 - 36 ) * 4 == 2 ** 4


# O valor da operação feita no papel foi de ( 216 - 36 ) = 180 * 4 = 720
# Que é um valor maior que o 2 ** 4 = 16 usado na comparação
# No Interpretador do Python foi obtido uma saída Falsa pois a comparação está errada por não serem números iguais
# >>> False




#c) (10 > 5*2) and (2**3 == (3**2)*2)


( 10 > 5 * 2 ) and ( 2 ** 3 == ( 3 ** 2 ) * 2 )



# O valor da operação feita no papel foi de ( 10 > 5 * 2 ) = ( 10 > 10 )
# E ( 2 ** 3 == ( 3 ** 2 ) * 2 ) = ( 8 == 9 * 2 ) = ( 8 == 18 )
# Logo a primeira condição não é atendida pois, 10 é == a 10 ( == Comparação de igualdade )
# E a segunda condição também não é atendida pois, 8 é != 18 ( != Comparação de diferença )
# O Comando and só é verdadeiro se todas as condições forem Verdadeiras.
# Sendo assim no Interpretador do Python foi obtido uma saída Falsa pois as condições estão erradas
# >>> False




#d) not(16>32) or (False or True)


not ( 16 > 32 ) or ( False or True )



# A primeira condição foi atendida pois, 16 é > que 32 porém o comando not inverte a operação ( > Comparação de maior que )
# E a segunda condição também é atendida pois, False or True é verdadeiro por que é um ou o outro
# Se fosse o comando False and True seria Falso pois um e o outro não são iguais
# O Comando or só é verdadeiro se uma das condições forem Verdadeiras.
# Sendo assim no Interpretador do Python foi obtido uma saída Verdadeira pois as condições estão corretas
# >>> True




#e) (((15/5)%3)>=1)


( ( ( 15 / 5 ) % 3 ) >= 1 )


# O valor da operação feita no papel foi de ( 15 / 5 ) = ( 3 % 3 ) = 0 ( % Módulo da divisão " Resto ") que no caso é igual a zero
# E ( 0 >= 1 ) é falso, pois 0 não é igual ou maior que 1 ( >= Comparação Maior ou igual )
# Logo a condição não é atendida e a comparação está errada
# Sendo assim no Interpretador do Python foi obtido uma saída Falsa pois a condição está errada
# >>> False




#f) (2**1/2) != (2**(1/2))


( 2 ** 1 / 2 ) != ( 2 ** ( 1 / 2 ) )


# O valor da operação feita no papel foi de ( 2 ** 1 / 2) = ( 2 / 2 ) = 1
# E ( 2 ** ( 1 / 2 ) ) = ( 2 ** 0.5 ) = 1.4142135623730951...
# Logo a condição é atendida, pois 1 é != de 1.4142135623730951... ( != Comparação de desigualdade )
# Sendo assim no Interpretador do Python foi obtido uma saída Verdadeira pois a condição está correta
# >>> True




#g) False == (False or True)


False == ( False or True )


# O valor da operação feita no papel foi de ( False or True ) = True , pois a lógica é verdadeira sendo um ou outro
# E False == True = False pois, False não é igual a True ( == Comparação de igualdade)
# Logo a condição não é atendida e a comparação está errada
# Sendo assim no Interpretador do Python foi obtido uma saída Falsa pois a condição está errada
# >>> False





#h) ((not(False) and False) == (False or True))


( ( not ( False ) and False ) == ( False or True ) )


# O valor da operação feita no papel foi de ( ( not ( False ) = True = ( True and False ) = False, pois um e o outro não são iguais
# E ( False or True ) = True, pois é um ou o outro ( == Comparação de igualdade)
# Logo a condição False == True não é atendida e a comparação está errada ( == Comparação de igualdade )
# Sendo assim no Interpretador do Python foi obtido uma saída Falsa pois a condição está errada
# >>> False




#i) ((7 > 2*4) and (43.5/1.2)) or (False == not(True))


( ( 7 > 2 * 4 ) and ( 43.5 / 1.2 ) ) or ( not ( True ) == False )


# O valor da operação feita no papel foi de ( ( 7 > 2 2 * 4 ) = 7 > 8 Verdadeiro
# E ( 43.5 / 1.2 ) = 36.25 False 7 não é maior que 36.25
# E ( ( not ( True ) ) = False ( False == False ) Verdadeiro
# Logo a primeira condição não é atendida, pois o and só tem uma expressão verdadeira e a outra falsa
# Porém a segunda condição é atendida, pois o or é verdadeiro atendendo a sua condição
# Sendo assim no Interpretador do Python foi obtido uma saída Verdadeira pois a condição está correta
# >>> True





#j) (False or True or True and (14/2 > 2*3 + 1))


( False or True or True and ( 14 / 2 > 2 * 3 + 1 ) )


# O valor da operação feita no papel foi de ( False or True or true ) = True
# E ( 14 / 2 > 2 * 3 + 1 ) = ( 7 > 6 + 1) = ( 7 > 7 ) = False
# Logo a primeira condição é atendida e a segunda condição não
# Porém como as duas expressões são comparados com o comando:
# or onde se uma das condições for verdadeira a saída também é verdadeira.
# Sendo assim no Interpretador do Python foi obtido uma saída Verdadeira pois a condição está correta
# >>> True




#k) ((91 >= 3*4) and (True or (1 != 1000/10**3))


( ( 91 >= 3 * 4 ) and ( True or ( 1 != 1000 / 10 ** 3 ) ) )


# O valor da operação feita no papel foi de ( 91 >= 3 * 4 ) = ( 91 >= 12 ) = Verdadeiro
# E ( True or ( 1 != 1000 / 10 ** 3 ) = ( True or ( 1 != 1000 / 1000) ) = ( True or ( 1 != 1) ) = True
# Logo as duas condições são atendidas e as condições são verdadeiras
# Como as duas expressões são comparados com o comando:
# and onde se todas as condições forem verdadeiras a saída também é verdadeira.
# Sendo assim no Interpretador do Python foi obtido uma saída Verdadeira pois a condição está correta
# >>> True



#2. Utilizando o comando type, verifique os valores abaixo:
#a) “Teste”


type ( " Teste " )

# A saída do interpretador do Python foi:
# >>> <class 'str'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe str ( String )





#b) 10.2


type ( 10.2 )


# A saída do interpretador do Python foi:
# >>> <class 'float'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe float ( Fração )




#c) 4


type ( 4 )


# A saída do interpretador do Python foi:
# >>> <class 'int'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe int ( Inteiros )




#d) True


type ( True )


# A saída do interpretador do Python foi:
# >>> <class 'bool'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe bool ( Booleano " Lógica booleana" )




#e) 18 + 2


type ( 18 + 2 )


# A saída do interpretador do Python foi:
# >>> <class 'int'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe int ( Inteiros )




#f) 4 > 5


type ( 4 > 5 )


# A saída do interpretador do Python foi:
# >>> <class 'bool'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe bool ( Booleano " Lógica booleana" )




#g) 10 == (2**3 + 2)


type ( 10 == ( 2 ** 3 + 2 ) )


# A saída do interpretador do Python foi:
# >>> <class 'bool'>
# O que significa que o tipo testado ( Entre parêntesis ) é da classe bool ( Booleano " Lógica booleana" )



#3. Escreva um programa que dado os valores de a, b, c, d, e, f e g abaixo,
#realize as operações abaixo:
#a = 1
#b = 2
#c = 6
#d = 0
#e = 8
#f = -1
#g = b


#h = f + g
#i = 4**b
#j = i + (42 – 8 / b)
#k = j
#l = k + h
#m = l + 10
#n = (j + k + 2*l) / 2*h
#o = 4*f + c**b + d*e


#print(h)
#print(“o valor de I é”, i)
#print(“os valores de j, k, l e m são”, j, k, l, m)
#print(“Resultado: \n\n”, n + o)


a = 1
b = 2
c = 6
d = 0
e = 8
f = -1
g = b


h = f + g
i = 4 ** b
j = i + ( 42 - 8 / b )
k = j
l = k + h
m = l + 10
n = ( j + k + 2 * l ) / 2 * h
o = 4 * f + c ** b + d * e


print ( h )
print ( "O valor de I é", i )
print ( "Os valores de j, k, l e m são", j, k, l, m )
print ( "Resultado:\n\n" , n + o)



#4. Escreva um programa que leia o nome de uma pessoa e exiba a
#mensagem “Olá, FULANO” (onde FULANO é igual ao nome da pessoa).


nome = input ( " Escreva seu nome : " )
print ( " Olá,", nome )

# O comando input espera a entrada do usuário
# Com o comando input o usuário tem interação com o programa
# Podendo digitar a entrada de informações para o programa




#5. Escreva um programa que leia dois valores inteiros
#e exiba a soma deles.


valor1 = int ( input ( " Digite o primeiro valor inteiro : " ) )
valor2 = int ( input ( " Digite o segundo valor inteiro : " ) )

print ( " A soma dos dois valores é :", valor1 + valor2 )


# Foi necessário realizar uma conversão explícita
# Utilizando o comando int antes da entrada do input
# Pois se não for realizada a conversão
# O programa apenas concatena as duas entradas pois serão consideradas Strings
# E não faz a operação de soma tendo uma saída " Errada " nesse caso.
# Sendo assim é importante a conversão para o tipo certo do programa
# para descobrir o tipo que será usado, basta encontrar um exemplo
# E aplicar o comando type para descobrir o tipo que é usado
# Nesse caso foi utilizado o comando int para realizar a conversão para inteiros



#6. Escreva um programa que leia dois valores inteiros
#e exiba o maior deles.


valor1 = int ( input ( " Digite um valor inteiro : " ) )
valor2 = int ( input ( " Digite outro valor inteiro : " ) )

if valor1 > valor2 :
    print ( " O maior valor digitado foi o primeiro : ", valor1 )
else :
    print ( " O maior valor digitado foi o segundo : ", valor2 )


# O comando if faz a comparação (se):
# Se as condições apresentadas forem verdadeiras
# O programa realiza o prosseguimento dos comandos em seu encadeamento
# O comando else faz a comparação ( se não ou caso contrário)
# Então se a condição apresentada na comparação if for falsa,
# Os comandos sejam mutuamente excludentes e ao contrário do if
# O programa realiza o prosseguimento dos comandos em seu encadeamento




#7. Escreva um programa que leia os lados de um retângulo e informe o
#valor de sua área.
#A saída deve ter o seguinte formato (por exemplo):
#“O valor da área do retângulo é 40 m2.”


lado1 = float ( input ( " Digite o valor de um lado do retângulo : " ) )
lado2 = float ( input ( " Digite o valor do outro lado do retângulo : " ) )
unimed = input ( " Escreva a unidade de medida utilizada para efetuar o cálculo : " )

print ( " O valor da área do retângulo é : ", lado1 * lado2 , unimed+"²" )


# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada dos valores dos lados do retângulo
# Solicitado a unidade de medida para maior precisão na resposta
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas




#8. Escreva um programa que leia a idade de uma pessoa e informe
#quantos segundos elas viveu.


SEGUNDOS = 31557600

idade = float ( input ( " Digite sua idade : " ) )

# 1s = 1 segundo 1m = 1 minuto 1h = 1 hora
# 1d = 1 dia 1a = 1ano


# 1minuto = 60s

# 1hora = 60 x 60 = 3.600s

# 24horas ou 1d = 24 x 3.600s = 86.400s

# 1 ano ou 365 dias e 6 horas = 365 x 86.400s + 6h = 6 x 3.600=

# ( 365 x 86.400s ) + ( 6 x 3.600s ) =
# ( 31.536.000s ) + ( 21.600s )

# 31.536.000s + 21.600s = 31.557.600s

# 1 ano ou 365 dias e 6 horas = 31.557.600s

print ( " Você já viveu : ", idade * SEGUNDOS , "Segundos" )


# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada da idade pessoal
# Feito o cálculo de segundos vividos de acordo com a idade em anos
# Considerando um ano como 365 dias e 6 horas deixando esse valor constante
# E impresso o cálculo na tela acrescido da mensagem em aspas




#9. Escreva um programa que realize a conversão de dólar para real: para
#cada valor lido em dólar da entrada padrão, será exibido o correspondente
#em reais (1 dólar = 3.55 reais).


REAIS = 3.55 #Dólares

dólar = float ( input ( " Digite o valor da quantia em dólares : " ) )

print ( " O valor convertido para reais é correspondente a : R$"+ str ( dólar * REAIS) )


# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada do valor em dólares
# E convertido para reais realizando o cálculo
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas



#10. Escreva um programa que leia um número e informe se ele é PAR ou
#ÍMPAR.


DIV = 2  # Críterio da divisão por 2
SRESTO = 0  # ( Sem resto) Módulo do resto da divisão para que o número seja par

num = int(input(" Digite um número inteiro : "))

if (num % DIV) == SRESTO:
    print(" O número digitado é par :", num)
else:
    print(" O número digitado é Ímpar : ", num)


# O programa realizou ou seguinte algoritmo :
# As constantes foram definidas
# Foi realizado a solicitação de entrada do número inteiro
# Em seguida realizado o cálculo para saber se o valor do " resto " da divisão ( com o comando % )
# Fazendo a comparação do valor obtido if ( se ) igual a zero é par else ( se não ) é Ímpar
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas




#11. Escreva um programa que leia a quantidade de linhas de um programa, o
#número de funções existente nele, o tamanho da equipe e o número de bugs
#encontrados e calcule a eficiência da equipe de acordo com a seguinte
#formula:
#EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2*(NUMB)


quantl = float ( input ( " Digite a quantidade de linhas de um programa : " ) )
quantf = float ( input ( " Digite a quantidade de funções do programa : " ) )
tameq = float ( input ( " Digite o tamanho da equipe : " ) )
numb = float ( input ( " Digite a quantidade de bugs encontrados no programa : " ) )

eficiencia = ( quantl / quantf ) / tameq - 4.2 * ( numb )

print ( " A eficiência do programa é de : ", eficiencia )



# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada do número de linhas, funções, equipe e bugs do programa
# Em seguida realizado o cálculo com uma fórmula constate para definir a Eficiência do programa
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas



#12. Escreva um programa que calcule a quantidade máxima de dados a ser
#transmitida por um usuário levando em consideração a taxa de transmissão
#maxima de video, áudio e dados e a capacidade do canal contratado:
#QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade



#12. Escreva um programa que calcule a quantidade máxima de dados a ser
#transmitida por um usuário levando em consideração a taxa de transmissão
#maxima de video, áudio e dados e a capacidade do canal contratado:
#QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade


tvideo = float ( input ( " Digite a taxa de tramissão máxima de vídeo : " ) )
taudio = float ( input ( " Digite a taxa de tramissão máxima de áudio : " ) )
tdados = float ( input ( " Digite a taxa de tramissão máxima de dados : " ) )
ccanal = float ( input ( " Digite a capacidade do canal contratado : " ) )

qdmax = ( tvideo * 5.2 + taudio * 3.4 + tdados * 1.5 ) / ccanal

print ( " A quantidade máxima de dados a ser trasmitido no canal é : ", qdmax )



# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada do valor para as seguintes taxas de transmissões:
# Vídeo, Áudio, Dados e Capacidade do canal contratado
# Em seguida realizado o cálculo com uma fórmula para definir a Quantidade máxima de dados do canal
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas













