#3°.)
#3.  Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é
#o maior.



num1 = input ( " Digite um Número inteiro : " )
num2 = input ( " Digite outro Número inteiro : " )

if num1 > num2:
    print ( " O primeiro número digitado é o maior " )
elif num1 == num2 :
    print ( " Os números digitados são iguais " )
else :
    print ( " O Segundo número digitado é o maior " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de dois números inteiros pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual número digitado foi o maior
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas
