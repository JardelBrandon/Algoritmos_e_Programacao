#1. Escreva um programa que receba do usuário a quantidade de linhas (QUANTL) de
#um programa e o tamanho da equipe (TAMEQ) encontrados e calcule a
#produtividade da equipe de acordo com a seguinte formula: produt = quantl / tameq.
#O programa deve exibir uma mensagem informando qual o nível de produtividade
#obtido:

#- Master: >=90
#- Medio: >=60 a 89
#- Razoável: >=50 a 59
#- Básico: >=0 a 49

MASTER = 90
MÉDIO = 60
RAZOÁVEL = 50
BÁSICO = 0

quantl = int (input ("Digite a quantidade de linhas do programa : "))
tameq = int (input ("Digite o tamanho da equipe : "))

produt = quantl / tameq

if produt >= MASTER :
    print ("O nível de produtividade do programa é considerado Master : ", produt)

elif produt < MASTER and produt >= MÉDIO :
    print ("O nível de produtividade do programa é considerado Médio : ", produt)

elif produt < MÉDIO and produt >= RAZOÁVEL :
    print ("O nível de produtividade do programa é considerado Razoável : ", produt)

elif produt < RAZOÁVEL and produt >= BÁSICO :
    print ("O nível de produtividade do programa é considerado Básico : ", produt)

else :
    print ("Inválido !")


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos valores de linhas e quantidade da equipe
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual é o nível do programa
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas
