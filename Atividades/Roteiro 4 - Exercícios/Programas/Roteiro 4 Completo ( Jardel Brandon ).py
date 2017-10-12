#IFPB - Engenharia de Computação
#Disciplina: Algoritmos e Programação
#Semestre Letivo: 2016
#Professor : Marcelo Siqueira / Henrique Cunha

#ROTEIRO DE AULA 4 – 31/05/2016

# 1. Escreva um programa que receba do usuário a quantidade de linhas (QUANTL) de
# um programa e o tamanho da equipe (TAMEQ) encontrados e calcule a
# produtividade da equipe de acordo com a seguinte formula: produt = quantl / tameq.
# O programa deve exibir uma mensagem informando qual o nível de produtividade
# obtido:

# - Master: >=90
# - Medio: >=60 a 89
# - Razoável: >=50 a 59
# - Básico: >=0 a 49

MASTER = 90
MÉDIO = 60
RAZOÁVEL = 50
BÁSICO = 0

quantl = int(input("Digite a quantidade de linhas do programa : "))
tameq = int(input("Digite o tamanho da equipe : "))

produt = quantl / tameq

if produt >= MASTER:
    print("O nível de produtividade do programa é considerado Master : ", produt)

elif produt < MASTER and produt >= MÉDIO:
    print("O nível de produtividade do programa é considerado Médio : ", produt)

elif produt < MÉDIO and produt >= RAZOÁVEL:
    print("O nível de produtividade do programa é considerado Razoável : ", produt)

elif produt < RAZOÁVEL and produt >= BÁSICO:
    print("O nível de produtividade do programa é considerado Básico : ", produt)

else:
    print("Inválido !")


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos valores de linhas e quantidade da equipe
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual é o nível do programa
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas


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




# 3. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
# possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%;
# MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino
# do produto e o programa retorne o preço final do produto acrescido do imposto do
# estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma
# mensagem de erro.

MG = 7 / 100
SP = 12 / 100
RJ = 15 / 100
MS = 8 / 100

valor = float(input("Digite o valor dos produtos : "))
estado = input("""Digite a sigla do estado destino do produto
Considere :
MG para (Minas Gerais), SP para (São Paulo) RJ para (Rio de Janeiro) e MS para (Mato Grosso do Sul) :""")

if estado == "MG":
    impostoMG = valor + (MG * valor)
    print ("O preço final do produto acrescido do imposto para MG foi :", impostoMG)

elif estado == "SP":
    impostoSP = valor + (SP * valor)
    print ("O preço final do produto acrescido do imposto para SP foi :", impostoSP)

elif estado == "RJ":
    impostoRJ = valor + (RJ * valor)
    print ("O preço final do produto acrescido do imposto para RJ foi :", impostoRJ)

elif estado == "MS":
    impostoMS = valor + (MS * valor)
    print ("O preço final do produto acrescido do imposto para MS foi :", impostoMS)

else:
    print ("Inválido")



    # Os comandos executados no programa realizam o seguinte algoritmo:
    # Espera a entrada do valor do produto comprado e o estado destino
    # Em seguida é feita a comparação por meio da lógica booleana
    # E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
    # Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
    # Fazendo as comparações pedidas na questão sobre qual é o valor final do produto acrescido do imposto de cada estado
    # Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
    # Acrescidas das mensagens em aspas




#3. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
#possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%;
#MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino
#do produto e o programa retorne o preço final do produto acrescido do imposto do
#estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma
#mensagem de erro.

MG = 7 / 100
SP = 12 / 100
RJ = 15 / 100
MS = 8 / 100

valor = float(input ("Digite o valor dos produtos : "))
estado = input ("""Digite a sigla do estado destino do produto
Considere :
MG para (Minas Gerais), SP para (São Paulo) RJ para (Rio de Janeiro) e MS para (Mato Grosso do Sul) :""")

if estado == "MG" :
    impostoMG = valor + (MG * valor)
    print ("O preço final do produto acrescido do imposto para MG foi :", impostoMG)

elif estado == "SP" :
    impostoSP = valor + (SP * valor)
    print ("O preço final do produto acrescido do imposto para SP foi :", impostoSP)

elif estado == "RJ" :
    impostoRJ = valor + (RJ * valor)
    print ("O preço final do produto acrescido do imposto para RJ foi :", impostoRJ)

elif estado == "MS" :
    impostoMS = valor + (MS * valor)
    print ("O preço final do produto acrescido do imposto para MS foi :", impostoMS)

else :
    print ("Inválido")



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada do valor do produto comprado e o estado destino
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual é o valor final do produto acrescido do imposto de cada estado
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas







'''
5. Crie um programa que calcula as raízes de uma equação do 2o grau:
ax² + bx + c=0
Para ela existir, o coeficiente 'a' deve ser diferente de zero. No caso de a ser
igual a zero, envie uma mensagem de erro ao usuário.
O delta é dado por b² - 4ac. Caso o delta seja maior ou igual a zero, calcule
as raízes (que serão reais). Caso o delta seja negativo, exiba a mensagem:
"As raízes são números complexos"
'''

a = float(input("Digite o valor do primeiro coeficiente da equação do segundo grau (a) : "))

if a == 0 :
    print("Inválido ! ")

b = float(input("Digite o valor do segundo coeficiente da equação do segundo grau (b) : "))
c = float(input("Digite o valor do terceiro coeficiente da equação do segundo grau (c) : "))

delta = b ** 2 - 4 * a * c

if delta < 0 :
    print("As raízes são números complexos ! ")

else :
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

print ("Primeira raíz da equação : ", x1, "\nSegunda raíz da equação : ", x2)



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para os coeficientes da equação do segundo grau (a,b e c)
É feita a comparação se a é igual a zero, pois se for a operação é inválida por que se tornaria uma equação de primeiro grau
É calculado o delta da equação e verificado se é maior que zero, pois se não for as raízes serão complexas
De acordo com os valores introduzidos calcula-se os valores das raízes para a equação
Obtendo-se na saída do interpretador do Python as raízes dadas de acordo com os calculos feito:
Acrescidas das mensagens em aspas
'''





'''
6. Fazer um programa que solicita o total gasto pelo cliente de uma loja,
imprime as opções de pagamento, solicita a opção desejada e imprime o
valor total das prestações (se houverem).
1) Opção: a vista com 10% de desconto
2) Opção: em duas vezes (preço da etiqueta)
3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para
compras acima de R$ 100,00).
'''

total_gasto = float(input("Digite o valor total gasto pelo cliente : "))

pagamento = input('''Selecione a forma de pagamento :
A vista com 10% de desconto (V) :
Em duas vezes com o preço normal (D) :
Parcelado de 3 até 10 vezes com 3% de juros ao mês disponível para compras acima de R$ 100.00 (P) : ''')

if pagamento == "V" :
    orçamento = total_gasto * 0.9

elif pagamento == "D" :
    orçamento = total_gasto / 2

elif pagamento == "P" and total_gasto >= 100 :
    parcelas = int(input("Digite a quantidade de parcelas desejadas :"))
    orçamento = (parcelas * 0.03 * total_gasto + total_gasto) / parcelas

else :
    print("Inválido")

print("Valor do orçamento para a opção de pagamento desejada : ", orçamento)




'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para o valor do gasto do cliente e a forma de pagamento
De acordo com a forma de pagamento selecionado, calcula o valor do orçamento
Se o pagamento for a vista é apresentado o valor com o desconto, se a prazo é o valor das parcelas de acordo com as condições
Obtendo-se na saída do interpretador do Python o valor de pagamento:
Acrescidas das mensagens em aspas
'''



'''
7. Dados três valores, A, B, C, verificar se esses valores formam um triângulo.
Em caso positivo informe se o triângulo é equilátero, isósceles ou escaleno.
Use os seguintes critérios:
a. O comprimento de cada lado de um triangulo é menor do que a soma
dos outros ´dois lados.
b. Chama-se equilátero o triângulo que tem três lados iguais.
c. Denominam-se isósceles o triângulo que tem o comprimento de dois
lados iguais.
d. Recebe o nome de escaleno o triangulo que tem os três lados
diferentes.
'''
'''
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

lado_A = float(input("Digite o valor A : "))
lado_B = float(input("Digite o valor B : "))
lado_C = float(input("Digite o valor C : "))

if abs(lado_B - lado_C) < lado_A < lado_B + lado_C or abs(lado_A -  lado_C) < lado_B < lado_A + lado_C or abs(lado_A - lado_B) < lado_C < lado_A + lado_B :
    if lado_A == lado_B == lado_C :
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo equilátero ")

    elif lado_A == lado_B or lado_B == lado_C or lado_A == lado_C :
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo isósceles ")

    else:
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo escaleno ")

else:
    print("Os valores informado não formam um triângulo")



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para os valores de verificação dos lados do triângulo (a,b e c)
É feita a comparação se os valores informados podem construir um triângulo atendendo as seguintes condições :
A medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
E maior que o valor absoluto da diferença entre essas medidas.
O comando abs() foi introduzido para descorbrir o valor absoluto da operação matemática
Se não for possível a construção do triângulo é informado ao usuário
Se for possível a construção do triângulo, é feito o encadeamento de comparações para descobrir o tipo do triângulo
O triângulo pode ser classificado segundo a medida do seu lado.
Triângulo escaleno: Todos os lados e ângulos são diferentes.
Triângulos isósceles: dois lados iguais e os ângulos opostos a esses lados iguais.
Triângulo equilátero: Todos os lados e ângulos iguais. Concluímos que seus ângulos serão de 60°.
Obtendo-se na saída do interpretador do Python as informações sobre os triângulos de acordo com os valores :
'''




'''
8. Faça uma prova de matemática para crianças que estão aprendendo a somar
números inteiros menores do que 100. Escolha números aleatórios entre 1 e
100, e mostre na tela a pergunta: “ qual é a soma de a + b? ”, onde a e b são
os números aleatórios. Peça a resposta. Faça cinco perguntas como essa ao
aluno e mostre para ele as perguntas e as respostas corretas, além de
quantas vezes o aluno acertou.
Para gerar um número aleatório em python, faça o seguinte:
● No início do código importe a biblioteca de geração de números
aleatórios:
○ from random import randint
● Para gerar um número aleatório entre 0 e 100
○ randint(0,100)
'''
from random import randint

corretas = 0
a = randint(0,100)
b = randint(0,100)

pergunta_1 = a + b
print("Qual é a soma de ", a, "+", b, ":")
resposta_1 = float(input())

if resposta_1 == pergunta_1 :
    corretas += 1

c = randint(0,100)
d = randint(0,100)

pergunta_2 = c + d
print("Qual é a soma de ", c, "+", d, ":")
resposta_2 = float(input())

if resposta_2 == pergunta_2 :
    corretas += 1

e = randint(0,100)
f = randint(0,100)

pergunta_3 = e + f
print("Qual é a soma de ", e, "+", f, ":")
resposta_3 = float(input())

if resposta_3 == pergunta_3 :
    corretas += 1

g = randint(0,100)
h = randint(0,100)

pergunta_4 = g + h
print("Qual é a soma de ", g, "+", h, ":")
resposta_4 = float(input())

if resposta_4 == pergunta_4 :
    corretas += 1

i = randint(0,100)
j = randint(0,100)

pergunta_5 = i + j
print("Qual é a soma de ", i, "+", j, ":")
resposta_5 = float(input())

if resposta_5 == pergunta_5 :
    corretas += 1

print("1º Pergunta :", a, "+", b, "\nResposta correta : ", pergunta_1, "\nResposta informada : ", resposta_1,
"\n2º Pergunta :", c, "+", d, "\nResposta correta : ", pergunta_2, "\nResposta informada : ", resposta_2,
"\n3º Pergunta :", e, "+", f, "\nResposta correta : ", pergunta_3, "\nResposta informada : ", resposta_3,
"\n4º Pergunta :", g, "+", h, "\nResposta correta : ", pergunta_4, "\nResposta informada : ", resposta_4,
"\n5º Pergunta :", i, "+", j, "\nResposta correta : ", pergunta_5, "\nResposta informada : ", resposta_5,
"\nTotal de respostas corretas : ", corretas)



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Define as variáveis de resposta correta e os valores aleatórios de a e b para realização da soma
Realiza a soma para armazenar o valor correto e pergunta ao usuário a resposta para essa soma
Espera a entrada do valor resposta do usuário para aquela pergunta e a armazena
Compara se o valor informado é o valor correto para a resposta, caso sim adiciona 1 a variável correta
E repete esse algoritmo até a ultima pergunta
Obtendo-se na saída do interpretador do Python qual era a pergunta, a resposta correta e a resposta informada para todas as perguntas:
Acrescidas das mensagens em aspas e do número total de respostas corretas
'''






'''
9. Leia uma data e determine se ela e válida. Ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias
em anos bissextos, e 28 dias em anos não bissextos. Procure uma forma de
identificar se um número é bissexto sem perguntar ao usuário.
'''

dia = int(input("Digite o dia : "))
mes = int(input("Digite o mês : "))
ano = int(input("Digite o ano : "))
bissexto = bool()
meses = bool()
dias = bool
anos = bool()

if ano % 400 == 0:
    bissexto = True

elif ano % 4 == 0:
    if ano % 100 != 0 :
        bissexto = True

    else:
        bissexto = False

else:
    bissexto = False


if mes > 0 and mes <= 12:
    meses = True

else:
    meses = False

if ano > 0:
    anos = True

else:
    anos = False

if bissexto == True and meses == True:
    if mes == 1:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 2:
        if dia > 0 and dia <= 29:
            dias = True

        else:
            dias = False

    if mes == 3:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 4:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 5:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 6:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 7:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 8:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 9:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 10:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 11:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 12:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False


if bissexto == False and meses == True:
    if mes == 1:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 2:
        if dia > 0 and dia <= 28:
            dias = True

        else:
            dias = False

    if mes == 3:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 4:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 5:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 6:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 7:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 8:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 9:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 10:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 11:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 12:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False


if dias == True and meses == True and anos == True :
    print("A data informada é valida !")

else:
    print("A data informada não é valida !  ")




'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada do dia, mês e ano pelo usuário
Define as variáveis booleanas para comparação se é verdadeira o falsa
Realiza operações matemática com o ano informado para calcular se o ano é bissexto ou não
Faz os encadeamentos para definir as condições verdadeiras das datas informadas
Compara se o dia, mês e ano é verdadeiro, caso sim armazena True (Verdadeiro) para sua variável, se não False (Falso)
Ao final analisa se as variáveis da data são verdadeiras, se sim:
Obtendo-se na saída do interpretador do Python : >>> A data informada é valida !
Se não :
Obtendo-se na saída do interpretador do Python : >>> A data informada não é valida !
'''






'''
10.As tarifas de certo parque de estacionamento são as seguintes:
a. 1 a e 2 a hora : R$ 1,00 cada
b. 3 a e 4 a hora : R$ 1,40 cada
c. 5 a hora e seguintes : R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso.
Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os
momentos de chegada ao parque e partida deste são apresentados na forma
de pares de inteiros, representando horas e minutos. Por exemplo, o par (12,
50) representará “12 horas e cinquenta minutos”. Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida,
escreva na tela o preço cobrado pelo estacionamento. Admite-se que a
chegada e a partida se dão com intervalo não superior a 24 horas. Portanto,
se uma dada hora de chegada for superior a da partida, isso não é uma
situação de erro, antes significa que a partida ocorreu no dia seguinte ao da
chegada.
'''
taxa = 0
total_a_pagar = 0

hora_de_chegada = int(input("Digite o par de horas do momento da chegada (hh) :"))
hora_de_chegada *= 60
minutos_de_chegada = int(input("Digite o par de minutos do momento da chegada (mm) :"))

hora_de_partida = int(input("Digite o par de horas do momento da partida (hh) :"))
hora_de_partida *= 60
minutos_de_partida = int(input("Digite o par de minutos do momento da partida (mm) :"))

permanencia = (hora_de_partida - hora_de_chegada) + (minutos_de_partida - minutos_de_chegada)

while permanencia % 60 != 0:
    permanencia += 1

if permanencia > 0 and permanencia <= 120 :
    taxa = 1

elif permanencia > 120 and permanencia <= 240:
    taxa = 1.40

else:
    taxa = 2

total_a_pagar = (permanencia / 60) * taxa

print("Valor total a ser pago pelo tempo de estacionamento : ", total_a_pagar)





'''
Os comandos executados no programa realizam o seguinte algoritmo:
Define as variáveis taxa e total a pagar
Espera a entrada dos pares dos horários de chegada e saída
Converte o horário das horas informadas pelo usuário em minutos
Faz a subtração subtração da partida pela chegada para se ter o tempo de permanência no estacionamento
Após é realizado o arredondamento do horário para se ter o valor de horas permanecido no estacionamento
É considerado o arredondamento para o valor acima de horas para o tempo permanecido
Para isso é acrescido um minuto ao tempo de permanência até que o valor seja divísivel por 60
Formando assim uma hora completa, esse procedimento é realizado caso seja informado um tempo não completo de hora
Faz comparações do tempo permanecido para definir o valor da taxa a ser cobrada
Calcula o valor total a ser pago, mutiplicando a permanência em horas pela taxa a ser cobrada
Obtendo-se na saída do interpretador do Python :
>>> O valor total a ser pago acrescido da mensagem entre aspas !
'''








