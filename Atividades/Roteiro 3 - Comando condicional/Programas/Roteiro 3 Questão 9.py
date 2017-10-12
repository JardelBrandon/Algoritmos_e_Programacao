#9. Escreva um programa que leia um valor qualquer e informe se ele é divisível por 7,
#positivo e par.

# Divisores de um número natural
# Um número é divisor de outro quando o resto da divisão for igual a 0. Portanto,
# Observações importantes:
# O menor divisor natural de um número é sempre o número 1.
# O maior divisor de um número é o próprio número.
# O zero não é divisor de nenhum número.
# Os divisores de um número formam um conjunto finito.
# Alguns números têm apenas dois divisores: o 1 e ele mesmo.
# Esses números são chamados de primos. Observe os números primos de 1 a 100 destacados no crivo de Eratóstenes:


DIV = 7
RESTO = 0
DIVPAR = 2

# Divisível, Positivo e Par
# Divisível, Positivo e Ímpar
# Divisível, Negativo e Par
# Divisível, Negativo e Ímpar
# Indivisível, Positivo e Par
# Indivisível, Positivo e Ímpar
# Indivisível, Negativo e Par
# Indivisível, Negativo e Ímpar

valor = int ( input ( " Digite um valor : " ) )

if valor == RESTO :
    print(" O valor digitado é : ", valor, "\n Indivisível por quaisquer número \n Neutro\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Positivo\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) != RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Positivo\n e \n Ímpar " )

elif ( DIV % valor == RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) == RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Negativo\n e \n Par " )

elif ( DIV % valor == RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) != RESTO ):
    print ( " O valor digitado é : ", valor, "\n Divisível por 7 \n Negativo\n e \n Ímpar " )

elif ( DIV % valor != RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Positivo\n e \n Par " )

elif ( DIV % valor != RESTO ) and ( valor > RESTO ) and ( ( valor % DIVPAR ) != RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Positivo\n e \n Ímpar " )

elif ( DIV % valor != RESTO ) and ( valor < RESTO ) and ( ( valor % DIVPAR ) == RESTO ) :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Negativo\n e \n Par " )

else :
    print(" O valor digitado é : ", valor, "\n Indivisível por 7 \n Negativo\n e \n Ímpar " )




# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um valor quaisquer pelo usuário
# Em seguida é feita a operação para descobrir o " Resto " da divisão ( Com o comando %)
# A verificação se o valor digitado Positivo ou Negativo
# A verificação se o valor digitado é Par ou Ímpar
# A verificação se é divisível por 0 pois ocorre uma condição especial
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas

