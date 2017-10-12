#Engenharia de Computação
#Disciplina: Algoritmos e Computação
#Semestre Letivo: 2016
#Professor: Marcelo Siqueira / Henrique Cunha
#Aluno: Jardel Brandon
#ROTEIRO DE AULA 1 – 17/05/2016
#Objetivos:
#a. Apresentar ao aluno o interpretador da linguagem Python
#b. Observar o comportamento do interpretador a partir de comandos aritméticos
#c. Entender o funcionamento do comando print




#1. Utilizando o prompt do interpretador do Python (>>>), digite as seguintes operações abaixo e observe o valor produzido.
#a) 1 + 2

1 + 2


# Foi apresentado o valor 3 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas


#b) 5 – 3

5 - 3


# Foi apresentado o valor 2 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas


#c) 3 * (4 – 1)

3 * ( 4 - 1 )

# Foi apresentado o valor 9 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências


#d) 71 / 4

71 / 4

# Foi apresentado o valor 17.75 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# O valor produzido foi em forma de decimais logo o Python trabalho com números racionais


#e) (32 / 4) *(8 + (29 – (8 – 1)))

( 32 / 4 ) * ( 8 + ( 29 - ( 8 - 1 ) ) )


# Foi apresentado o valor 240.0 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências


#f) (2**4)

2 ** 4

# Foi apresentado o valor 16 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# O comando ** é utilizado para realizar operações de potênciação


#g) (20 + 5*2 + 3**2)

( 20 + 5 * 2 + 3 ** 2 )

# Foi apresentado o valor 39 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências



#h) 4 % 2

4 % 2

# Foi apresentado o valor 0 na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# O Comando % Significa o módulo da divisão (O Resto)

#i) ((2*3-1)) / ((4+14/2))

( ( 2 * 3 - 1 ) ) / ( ( 4 + 14 / 2 ) )

# Foi apresentado o valor 0.454545... na saída do interpretador do Python
# Inferindo-se que o interpretador realiza as operações matemáticas
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências
# O valor produzido demonstra que o Python suporta saídas do tipo dízimas
# No último bit do interpretador é feito um arredondamento




#2. Descreva o que ocorre se retirarmos os espaços em branco da operação 1 + 2.

1+2


# Foi apresentado o valor 3 na saída do interpretador do Python
# Inferindo-se que o interpretador do Python não registra os espaçoes em branco
# Então é possível se fazer o comando com ou sem espaços em branco
# A saída do interpretador não altera o resultado dos comando espaçados ou não.
# Sendo possível duas maneiras a mais de escrever os códigos em Python




#3. Descreva o que ocorre se retiramos os parêntesis das letras (c),(e) e (i) da questão 1.

#c) 3 * (4 – 1)

3 * 4 - 1

# Foi apresentado o valor 11 na saída do interpretador do Python
# Diferente do valor apresentado com parêntesis que foi 9
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências


#e) (32 / 4) *(8 + (29 – (8 – 1)))

32 / 4 * 8 + 29 - 8 - 1

# Foi apresentado o valor 84.0 na saída do interpretador do Python
# Diferente do valor apresentado com parêntesis que foi 240.0
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências



#i) ((2*3-1)) / ((4+14/2)))

2 * 3 - 1 / 4 + 14 / 2

# Foi apresentado o valor 12.75 na saída do interpretador do Python
# Diferente do valor apresentado com parêntesis que foi 0.454545...
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências

#Resumo:
# Todas as opreções obtiveram divergências na saída
# A precedência do parêntesi foi respeitada assim como as ordens das operações
# Os comandos foram interpretados de Acordo com a regra matemática
# É importante ter atenção aos comandos para evitar erros




#4. Utilizando o comando print, escreva a mensagem “Olá, Mundo” na saída padrão.

print ( " Olá, Mundo " )

# O comando print é utilizado para imprimir algo na saída do interpretador (tela)
# O comando deve ser utilizado seguido de parêntesis que indica o ínicio e o fim do comando
# O comando deve ser utilizado com aspas caso se faça necessário o uso de uma string entre os parêntesis
# No caso dessa questão foi " Impresso na tela" a mensagem >>>Olá, Mundo




5. Modifique o comando para “Olá, \n Mundo” na saída padrão.

#5. Modifique o comando para “Olá, \n Mundo” na saída padrão.

print ( " Olá, \n Mundo")


# O \n realiza a quebra de linha na saída do programa
# A modificação no programa com o comando \n fez a descida de uma linha após ele
# O comando print é utilizado para imprimir algo na saída do interpretador (tela)
# O comando deve ser utilizado seguido de parêntesis que indica o ínicio e o fim do comando
# O comando deve ser utilizado com aspas caso se faça necessário o uso de uma string entre os parêntesis
# No caso dessa questão foi " Impresso na tela" o mensagem:
# >>>Olá,
#    Mundo



#6. Observe qual a saída de cada um dos comandos abaixo:
#a) print(1 + 1)

print ( 1 + 1 )


# Foi apresentado o valor 2 na saída do interpretador do Python
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências
# Independente de estar sob o comando print ou diretamente sem o comando
# O resultado da saída será igual ao comando 1 + 1 sem o print


#b) print("O resultado da soma de 1 + 1 é", 1 + 1)

print ( " O resultado da soma de 1 + 1 é ", 1 + 1 )


# O comando print foi concatenado com a mensagem string entre aspas
# Foi apresentado >>> O resultado da soma de 1 + 1 é 2 na saída do interpretador do Python
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências
# E que faz a concatenação de operações para apresentar na saída do interpretador



#c) print("O resultado da soma de 1 + 1 é\n", 1 + 1)


print ( " O resultado da soma de 1 + 1 é \n", 1 + 1 )


# O \n realiza a quebra de linha na saída do programa
# A modificação no programa com o comando \n fez a descida de uma linha após ele
# O comando print foi concatenado com a mensagem string entre aspas
# Foi apresentado >>> O resultado da soma de 1 + 1 é 2 na saída do interpretador do Python
# Provando que o interpretador do Python realiza as operações de acordo com:
# A ordem das operações e seguindo suas Precedências
# E que faz a concatenação de operações para apresentar na saída do interpretador
# No caso dessa questão foi " Impresso na tela" o mensagem:
# >>>  O resultado da soma de 1 + 1 é
#      2




#d) print("----")

print ( "---" )


# O comando print é utilizado para imprimir algo na saída do interpretador (tela)
# O comando deve ser utilizado seguido de parêntesis que indica o ínicio e o fim do comando
# O comando deve ser utilizado com aspas caso se faça necessário o uso de uma string entre os parêntesis
# No caso dessa questão foi " Impresso na tela" a mensagem >>> ---


#e) print("--\n--\n--")

print ( "--\n--\n--" )


# O comando print é utilizado para imprimir algo na saída do interpretador (tela)
# O comando deve ser utilizado seguido de parêntesis que indica o ínicio e o fim do comando
# O comando deve ser utilizado com aspas caso se faça necessário o uso de uma string entre os parêntesis
# O \n realiza a quebra de linha na saída do programa
# A modificação no programa com o comando \n fez a descida de uma linha após ele
# No caso dessa questão foi " Impresso na tela" a mensagem:
# >>> --
#     --
#     --


#f) print("-\n-\n-\n-\n-\n-")

print ( "-\n-\n-\n-\n-\n-\n")

# O comando print é utilizado para imprimir algo na saída do interpretador (tela)
# O comando deve ser utilizado seguido de parêntesis que indica o ínicio e o fim do comando
# O comando deve ser utilizado com aspas caso se faça necessário o uso de uma string entre os parêntesis
# O \n realiza a quebra de linha na saída do programa
# A modificação no programa com o comando \n fez a descida de uma linha após ele
# No caso dessa questão foi " Impresso na tela" a mensagem:
# >>> -
#     -
#     -
#     -
#     -
#     -


#7. Apresente os comandos que produzem as saídas abaixo:
#a)
#++++++
#+++++
#++++
#+++
#++
#+


print ( "++++++\n+++++\n++++\n+++\n++\n+" )


#ou

print ( " ++++++ " )
print ( " +++++ " )
print ( " ++++ " )
print ( " +++ " )
print ( " ++ " )
print ( " + " )


# Usando um dos dois comandos assima teremos a saída desejada para a questão





#b)
#*****
#-----
#-----
#*****


print ( "*****\n-----\n-----\n*****" )

#ou

print ( "*****" )
print ( "-----" )
print ( "-----" )
print ( "*****" )

# Usando um dos dois comandos assima teremos a saída desejada para a questão




#c)
#a a a
# b b b
#  c c c

print ( "a a a\n b b b\n  c c c" )


#ou


print ( "a a a" )
print ( " b b b" )
print ( "  c c c" )

# Usando um dos dois comandos assima teremos a saída desejada para a questão




#d)
#* * * * * * * * * * *
# * * * * * * * * * * * * *

print ( "* * * * * * * * * * *\n * * * * * * * * * * *" )


#ou


print ( "* * * * * * * * * * *" )
print ( " * * * * * * * * * * *" )


# Usando um dos dois comandos assima teremos a saída desejada para a questão





#e)
#* * * * * * * * * * *
# * * * * * * * * * * * * *
#* * * * * * * * * * *
# * * * * * * * * * * * * *


print ( "* * * * * * * * * * *\n * * * * * * * * * * *\n* * * * * * * * * * *\n * * * * * * * * * * *" )


#ou


print ( "* * * * * * * * * * *" )
print ( " * * * * * * * * * * *" )
print ( "* * * * * * * * * * *" )
print ( " * * * * * * * * * * *" )


# Usando um dos dois comandos assima teremos a saída desejada para a questão







#Fim













