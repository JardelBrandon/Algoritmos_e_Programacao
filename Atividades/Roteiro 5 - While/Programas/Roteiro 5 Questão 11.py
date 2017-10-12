#11. Escreva um programa que calcule os N termos da série S abaixo:
#S = (1/3) + (2/6) + (3/9) + (4/12) + …

dividendo = 1
divisor = 3
quociente = 0
resto = 0

while True :
    quociente = dividendo / divisor
    resto = dividendo % divisor
    print ("O valor da divisão :", dividendo, "/", divisor, "\nTeve como resultado :", quociente, "\nE o módulo da divisão foi :", resto)
    dividendo += 1
    divisor += 3






# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor das variáveis
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas e adiciona 1 ao numerador e 2 ao denominador
# Após executa as operações com os valores adicionados infinitamente
# Imprime na tela os números dos resultados das respectivas divisões
# Atendendo o que se pede na questão