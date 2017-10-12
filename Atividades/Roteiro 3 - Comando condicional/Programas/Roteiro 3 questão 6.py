#6°.)
# 6.  Escreva um programa que leia o valor do índice de acidez (pH) de uma solução e
#informe se ela é ácida ou não.

NEUTRALIDADE = 7

input ( " Programa que lê o pH da água pH significa potencial hidrogeniônico (quantidade de prótons H+). aperte a tecla enter para continuar... " )

pH = float (input ( " Digite o valor do pH encontrado na água " ))



if pH < NEUTRALIDADE :
    print ( " O valor de pH encontrado na água é considerado ácido pois foi um valor abaixo que um pH de nível 7 (Neutro) " )
elif pH == NEUTRALIDADE :
    print ( " O valor de pH encontrado na água é considerado neutro " )
else :
    print ( " O valor de pH encontrado na água é considerado alcalino pois foi um valor maior que um pH de nível 7 (Neutro) " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Explica o programa e espera o pressionamento da tecla enter
# Espera a entrada do valor do pH encontrado na água pelo usuário
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual foi o pH da água e o estado em que ela se encontra
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas