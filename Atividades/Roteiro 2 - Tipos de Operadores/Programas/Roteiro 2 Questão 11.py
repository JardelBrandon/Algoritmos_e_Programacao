#11. Escreva um programa que leia a quantidade de linhas de um programa, o
#número de funções existente nele, o tamanho da equipe e o número de bugs
#encontrados e calcule a eficiência da equipe de acordo com a seguinte
#formula:
#EFICIENCIA = (QUANTL / QUANTF) / TAMEQ – 4.2*(NUMB)


quantl = float ( input ( " Digite a quantidade de linhas de um programa : " ) )
quantf = float ( input ( " Digite a quantidade de funções do programa : " ) )
tameq = float ( input ( " Digite o tamanho da equipe : " ) )
numb = float ( input ( " Digite a quantidade de bugs encontrados no programa : " ) )

eficiencia = ( quantl / quantf ) / tameq - 4.2 * ( numb )

print ( " A eficiência do programa é de : ", eficiencia )



# O programa realizou ou seguinte algoritmo :
# Foi realizado a solicitação de entrada do número de linhas, funções, equipe e bugs do programa
# Em seguida realizado o cálculo com uma fórmula para definir a Eficiência do programa
# Feito o cálculo e impresso na tela acrescido da mensagem em aspas



