#5. Escreva um programa que leia dois valores inteiros
#e exiba a soma deles.


valor1 = int ( input ( " Digite o primeiro valor inteiro : " ) )
valor2 = int ( input ( " Digite o segundo valor inteiro : " ) )

print ( " A soma dos dois valores é :", valor1 + valor2 )


# Foi necessário realizar uma conversão explícita
# Utilizando o comando int antes da entrada do input
# Pois se não for realizada a conversão
# O programa apenas concatena as duas entradas pois serão consideradas Strings
# E não faz a operação de soma tendo uma saída " Errada " nesse caso.
# Sendo assim é importante a conversão para o tipo certo do programa
# para descobrir o tipo que será usado, basta encontrar um exemplo
# E aplicar o comando type para descobrir o tipo que é usado
# Nesse caso foi utilizado o comando int para realizar a conversão para inteiros