#12. Escreva um programa que calcule os N termos da série S :
#S = (1/4) + 1 + (3/8) + 1 + (5/12) + …


dividendo = 1
divisor = 4
quociente = 0
resto = 0

while True :
    quociente = (dividendo / divisor) + 1
    resto = dividendo % divisor
    print ("O valor da divisão :", dividendo, "/", divisor, "\nTeve como resultado :", quociente, "\nE o módulo da divisão foi :", resto)
    dividendo += 2
    divisor += 4





# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor das variáveis
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas e adiciona 2 ao numerador e 4 ao denominador somando tudo com 1
# Após executa as operações com os valores adicionados infinitamente
# Imprime na tela os números dos resultados das respectivas divisões
# Atendendo o que se pede na questão