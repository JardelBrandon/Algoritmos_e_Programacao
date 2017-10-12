#5.  Escreva um programa que leia os valores dos lados de um triângulo e informe se ele é
#equilátero, isósceles ou escaleno.

lado1 = input ( " Digite o valor do primeiro lado do triângulo : " )
lado2 = input ( " Digite o valor do segundo lado do triângulo : " )
lado3 = input ( " Digite o valor do terceiro lado do triângulo : " )


if lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print ( " O triângulo informado é do tipo escaleno " )
elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print ( " O triângulo informado é do tipo equilátero " )
else :
    print ( " O triângulo informado é do tipo isósceles " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos valores dos lados do triângulo pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual foi o tipo do triâgulo
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas