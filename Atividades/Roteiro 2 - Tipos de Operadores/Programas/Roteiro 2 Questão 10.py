#10. Escreva um programa que leia um número e informe se ele é PAR ou
#ÍMPAR.

DIV = 2 # Críterio da divisão por 2
SRESTO = 0 # ( Sem resto) Módulo do resto da divisão para que o número seja par

num = int ( input ( " Digite um número inteiro : " ) )

if ( num % DIV ) == SRESTO :
    print ( " O número digitado é par :", num )
else :
    print ( " O número digitado é Ímpar : ", num )


# O programa realizou ou seguinte algoritmo :
# As constantes foram definidas
# Foi realizado a solicitação de entrada do número inteiro
# Em seguida realizado o cálculo para saber se o valor do " resto " da divisão ( com o comando % )
# Fazendo a comparação do valor obtido if ( se ) igual a zero é par else ( se não ) é Ímpar
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas




