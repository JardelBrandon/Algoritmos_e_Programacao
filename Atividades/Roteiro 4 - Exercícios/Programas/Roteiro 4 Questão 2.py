#2. Escreva um programa que calcule a quantidade máxima de dados a ser transmitida
#por um usuário levando em consideração a taxa de transmissão maxima de video,
#áudio e dados e a capacidade do canal contratado: QDmax = (TVideo*5.2 +
#TAudio*3.4 + TDados*1.5) / Capacidade
#O programa deve exibir uma mensagem informando qual o nível de aceitabilidade de
#transferência obtido:

#- Alto: >=100
#- Medio: >=10 a 99
#- Baixo: >=0 a 10

ALTO = 100
MÉDIO = 10
BAIXO = 0

vídeo = float(input("Digite o valor da taxa máxima de transmissão de vídeo : "))
áudio = float(input("Digite o valor da taxa de transmissão de áudio : "))
dados = float(input("Digite o valor da taxa de transmissão de dados : "))
capacidade = float(input("Digite o valor da capacidade do canal contratado : "))

qdmax = (vídeo * 5.2 + áudio * 3.4 + dados * 1.5) / capacidade

if qdmax >= ALTO :
    print ("O nível de aceitabilidade de transferência foi Alto : ", qdmax)

elif qdmax < ALTO and qdmax >= MÉDIO :
    print ("O nível de aceitabilidade de transferência foi Médio : ", qdmax)

elif qdmax < MÉDIO and qdmax >= BAIXO :
    print ("O nível de aceitabilidade de transferência foi Baixo : ", qdmax)

else :
    print ("Inválido !")

# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos valores das taxas de tramissões e da capacidade do canal contratado
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual é o nível de aceitabilidade de transferência
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas