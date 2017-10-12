#6. Escreva um programa que leia 10 caracteres da entrada padrão e informe quantas vogais foram
#lidas.
MAX = 10

contador = 0
vogais = 0

while contador < MAX :
    letra = str(input("Digite qualquer caractere :"))
    contador += 1

    if letra in ["a","e","i","o","u","A","E","I","O","U"] :
        vogais += 1


print("Número de vogais digitadas :", vogais)


#Os comandos desse programa realizam o seguinte algoritimo:
#Define o valor da constante e variáveis
#Entra em um laço de repetição enquanto o contador for menor que MAX (Máximo)
#Espera a entrada de um caractere quaisquer
#Se a letra digitada for uma vogal, entra para a contagem das vogais
#No final imprime na tela o número de vogais digitadas
