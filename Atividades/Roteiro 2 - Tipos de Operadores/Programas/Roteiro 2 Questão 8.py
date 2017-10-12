#8. Escreva um programa que leia a idade de uma pessoa e informe
#quantos segundos elas viveu.

SEGUNDOS = 31557600

idade = float ( input ( " Digite sua idade : " ) )

# 1s = 1 segundo 1m = 1 minuto 1h = 1 hora
# 1d = 1 dia 1a = 1ano


# 1minuto = 60s

# 1hora = 60 x 60 = 3.600s

# 24horas ou 1d = 24 x 3.600s = 86.400s

# 1 ano ou 365 dias e 6 horas = 365 x 86.400s + 6h = 6 x 3.600=

# ( 365 x 86.400s ) + ( 6 x 3.600s ) =
# ( 31.536.000s ) + ( 21.600s )

# 31.536.000s + 21.600s = 31.557.600s

# 1 ano ou 365 dias e 6 horas = 31.557.600s

print ( " Você já viveu : ", idade * SEGUNDOS , "Segundos" )


# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada da idade pessoal
# Feito o cálculo de segundos vividos de acordo com a idade em anos
# Considerando um ano como 365 dias e 6 horas deixando esse valor constante
# E impresso o cálculo na tela acrescido da mensagem em aspas
