PI = 3.14159265359


raio1 = input ( " Digite o raio do primeiro circulo : " )
raio2 = input ( " Digite o raio do segundo circulo : " )

A1 = PI * float ( raio1 ) ** 2

A2 = PI * float ( raio2 ) ** 2

if A1 > A2:
    print ( " O primeiro círculo possui a área maior " )
elif raio1 == raio2 :
    print ( " Os círculos possuem áreas iguais " )
else :
    print ( " O Segundo círculo possui a área maior " )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de dois valores de áreas do círculo pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual área foi a maior
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas
