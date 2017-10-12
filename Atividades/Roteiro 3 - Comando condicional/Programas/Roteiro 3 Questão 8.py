#8. Escreva um programa que leia um valor qualquer e informe se ele é múltiplo de 5 (Use
#o operador %).

# Para um número natural ser múltiplo
# É preciso realizar a multiplicação de determinado número
# Por qualquer número do conjunto dos números naturais
# O resultado dos produtos da operação serão considerados múltiplos
# Então o conjunto dos múltiplos são infinitos

# Divisores de um número natural
# Um número é divisor de outro quando o resto da divisão for igual a 0. Portanto,
# Se a divisão for exata ( Não houver "Resto" ) esse número pode ser considerado divisor natural
# Observações importantes:
# ? O menor divisor natural de um número é sempre o número 1.
# ? O maior divisor de um número é o próprio número.
# ? O zero não é divisor de nenhum número.
# ? Os divisores de um número formam um conjunto finito.
# Alguns números têm apenas dois divisores: o 1 e ele mesmo.
# Esses números são chamados de primos.

# Os múltiplos e divisores de um número estão relacionados entre si da seguinte forma:
# Se 15 é divisível por 3, então 3 é divisor de 15, assim, 15 é múltiplo de 3.
# Se 8 é divisível por 2, então 2 é divisor de 8, assim, 8 é múltiplo de 2.
# Se 20 é divisível por 5, então 5 é divisor de 20, assim, 20 é múltiplo de 5.

MUT = 5
RESTO = 0

valor = int ( input ( " Digite um valor natural : " ) )

if valor % MUT == RESTO :
    print ( " O valor digitado é múltiplo de 5 : ", valor )
else :
    print ( " O valor digitado não é múltiplo de 5 : ", valor )


# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada de um valor natural quaisquer
# Em seguida é feita a operação para descobrir o " Resto " da divisão ( Com o comando %)
# Em seguida é feita a comparação por meio da lógica booleana
# Se o valor do " Resto for igual a zero então o valor digitado é múltiplo de 5
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas


