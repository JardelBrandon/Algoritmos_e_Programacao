#12. Escreva um programa que calcule a quantidade máxima de dados a ser
#transmitida por um usuário levando em consideração a taxa de transmissão
#maxima de video, áudio e dados e a capacidade do canal contratado:
#QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade


tvideo = float ( input ( " Digite a taxa de tramissão máxima de vídeo : " ) )
taudio = float ( input ( " Digite a taxa de tramissão máxima de áudio : " ) )
tdados = float ( input ( " Digite a taxa de tramissão máxima de dados : " ) )
ccanal = float ( input ( " Digite a capacidade do canal contratado : " ) )

qdmax = ( tvideo * 5.2 + taudio * 3.4 + tdados * 1.5 ) / ccanal

print ( " A quantidade máxima de dados a ser trasmitido no canal é : ", qdmax )



# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada do valor para as seguintes taxas de transmissões:
# Vídeo, Áudio, Dados e Capacidade do canal contratado
# Em seguida realizado o cálculo com uma fórmula para definir a Quantidade máxima de dados do canal
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas
