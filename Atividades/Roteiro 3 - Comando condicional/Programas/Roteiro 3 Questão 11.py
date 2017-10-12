#11. Escreva um programa que leia um caractere da entrada padrão e informe se ele é uma
#vogal.


print ( " Digite um caractere quaisquer : ")
letra = input ( )

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" :
    print ( " O caractere digitado é uma vogal minúscula : ", letra )

elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" :
    print ( " O caractere digitado é uma vogal maiúscula : ", letra )

else :
    print ( " O caractere digitado não é uma vogal ", letra )



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um caractere quaiquer pelo usuário
# Após é ralizado as comparações pelos comandos condicionais
# Em seguida são ralizadas as comparaçãos por meio da lógicas booleanas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas
