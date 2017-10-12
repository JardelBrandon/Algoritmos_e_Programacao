#10. Escreva um programa que solicite ao usuário sua temperatura, se está tendo secreção,
#tosse e dor no corpo (“S” ou “N”). Caso a temperatura seja maior do que 37 graus e as
#demais respostas sejam iguais a “S”, uma mensagem “Exames Especiais” deve ser
#exibida. Caso a temperatura seja menor do que 37 graus e não houver secreção, tosse
#e dor no corpo, a mensagem será “Liberado”. Caso a temperatura seja inferior a 37
#graus, mas houver dor no corpo, tosse e secreção, a mensagem deve ser igual a
#“Exames Básicos”.

GRAUS = 37


temperatura = float ( input ( " Digite sua temperatura : " ) )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
secreção = input ( )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
tosse = input ( )

print ( " Caso apresente dor no corpo digite S Caso contrário N : " )
dor = input ( )



if temperatura >= GRAUS and  secreção == "S" and  tosse == "S" and  dor == "S" :
    print ( " Exames Especiais ! " )

elif temperatura < GRAUS and secreção == "N" and tosse == "N" and dor == "N" :
    print ( " Liberado ! " )

else :
    print ( " Exames Básicos ! " )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada dos dados perguntados a respeito dos sintomas sentidos
# Em seguida é feita a operação para o estado do paciente
# A verificação da temperatura
# A verificação se existe dor no corpo, tosse e secreção
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas


