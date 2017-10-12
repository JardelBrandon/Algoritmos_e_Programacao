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

