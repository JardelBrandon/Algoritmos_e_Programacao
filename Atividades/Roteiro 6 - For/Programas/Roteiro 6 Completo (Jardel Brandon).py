#Engenharia de Computação
#Disciplina: Algoritmos e Computação
#Semestre Letivo: 2016
#Professor: Marcelo Siqueira/Henrique Cunha
#Assunto:  FOR

#Objetivos:
#1. Analisar a sintaxe de códigos escritos em Python
#2. Observar o comportamento da estrutura de repetição
#FOR
#3. Resolver problemas usando estrutura de repetição
#4. Traduzindo (FOR) para português, significa (para)

#ROTEIRO DE AULA 6 –09/06/2016





#1. Observe qual valor gerado em cada um dos comandos abaixo e depois teste no interpreador
#Python.

#1. list(range(10))
#2. list(range(-5,5))
#3. list(range(-5,5,2))
#4. list(range(2,10))
#5. list(range(2,10,3))
#6. list(range(20,100))
#7. list(range(20,100,2))
#8. list(range(30,0,-1))
#9. list(range(30,15,-1))
#10.list(range(30,15,-2))


list(range(10))
#Saída do interpretador:
#>>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(-5,5))
#Saída do interpretador:
#>>>[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list(range(-5,5,2))
#Saída do interpretador:
#>>>[-5, -3, -1, 1, 3]

list(range(2,10))
#Saída do interpretador:
#>>>[2, 3, 4, 5, 6, 7, 8, 9]

list(range(2,10,3))
#Saída do interpretador:
#>>>[2, 5, 8]

list(range(20,100))
#Saída do interpretador:
#>>>[20, 21, 22, 23, 24, 25, 26,
# 27, 28, 29, 30, 31, 32, 33, 34,
# 35, 36, 37, 38, 39, 40, 41, 42,
# 43, 44, 45, 46, 47, 48, 49, 50,
# 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66,
# 67, 68, 69, 70, 71, 72, 73, 74,
# 75, 76, 77, 78, 79, 80, 81, 82,
# 83, 84, 85, 86, 87, 88, 89, 90,
# 91, 92, 93, 94, 95, 96, 97, 98, 99]

list(range(20,100,2))
#Saída do interpretador:
#>>>[20, 22, 24, 26, 28, 30, 32,
# 34, 36, 38, 40, 42, 44, 46, 48,
# 50, 52, 54, 56, 58, 60, 62, 64,
# 66, 68, 70, 72, 74, 76, 78, 80,
# 82, 84, 86, 88, 90, 92, 94, 96, 98]

list(range(30,0,-1))
#Saída do interpretador:
#>>>[30, 29, 28, 27, 26, 25, 24,
# 23, 22, 21, 20, 19, 18, 17, 16,
# 15, 14, 13, 12, 11, 10, 9, 8,
# 7, 6, 5, 4, 3, 2, 1]

list(range(30,15,-1))
#Saída do interpretador:
#>>>[30, 29, 28, 27, 26, 25, 24,
#23, 22, 21, 20, 19, 18, 17, 16]

list(range(30,15,-2))
#Saída do interpretador:
#>>>[30, 28, 26, 24, 22, 20, 18, 16]







#2. Analise o algoritmo abaixo e informe quais resultados serão exibidos na saída padrão (para cada
#algoritmo acompanhe os valores das variáveis usando uma tabela tal como no exemplo abaixo):

#soma = 3
#cont = 1
#forx in range(10):
#soma = soma + 2
#cont = cont + 1
#print(x)
#print(soma)
#print(cont)


#iteração   0  1  2  3  4  5  6  7  8  9
#cont       2
#soma       5
#x          0


soma = 3
cont = 1

for x in range(10):
    soma = soma + 2
    cont = cont + 1

    print("Valor de X :", x)
    print("Valor de soma :", soma)
    print("Valor de cont :", cont)




# Foi obtido as seguintes respostas para a tabela na saída do python
#>>>
#iteração   0  1  2  3  4  5  6  7  8  9
#cont       2  3  4  5  6  7  8  9  10 11
#soma       5  7  9  11 13 15 17 19 21 23
#x          0  1  2  3  4  5  6  7  8  9



#2°) b)
#soma = 3
#cont = 1
#forx in range(0,10,2):
#soma = soma + 2
#cont = cont + 1
#print(x)
#print(soma)
#print(cont)


#iteração   0  1  2  3  4  5  6  7  8  9
#cont
#soma
#x


soma = 3
cont = 1

for x in range(0,10,2):
    soma = soma + 2
    cont = cont + 1

    #print("Valor de X :", x)
    #print("Valor de soma :", soma)
    print("Valor de cont :", cont)


# Foi obtido as seguintes respostas para a tabela na saída do python
#>>>
#iteração   0  1  2  3  4  5  6  7  8  9
#cont       2  3  4  5  6
#soma       5  7  9  11  13
#x          0  2  4  6  8




#3°) c)
#for i in range(-5,5):
#j = i + 2
#print(i)
#print(j)

#iteração  0  1  2  3  4  5  6  7  8  9
#i
#j

for i in range(-5,5) :
    j = i + 2

    #print ("Valor de i :", i)
    print ("Valor de j :", j)






# Foi obtido as seguintes respostas para a tabela na saída do python
#>>>
#iteração  0  1  2  3  4  5  6  7  8  9
#i        -5 -4 -3 -2 -1  0  1  2  3  4
#j        -3 -2 -1  0  1  2  3  4  5  6





#3. Escreva um programa que exiba na saída padrão os 100 primeiros números.

for i in range(0,100) :
    print (i, end=" " )

#O comando end=" " define a forma de saída no interpretador
#Por exemplo, end="\n" Linha abaixo de linha
#end=" " na mesma linha com 1 espaço
#end="" na mesma linha sem espaço, etc...
#O programa apresenta na saída do pyhton :
#>>> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58
# 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77
# 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96
# 97 98 99





# 4. Escreva um programa que exiba na saída padrão os 100 primeiros números ímpares.

for i in range(1, 200, 2):
    print(i, end=" ")



# O comando end=" " define a forma de saída no interpretador
# Por exemplo, end="\n" Linha abaixo de linha
# end=" " na mesma linha com 1 espaço
# end="" na mesma linha sem espaço, etc...
# O programa apresenta na saída do pyhton :
# >>> 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
# 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59
# 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89
# 91 93 95 97 99 101 103 105 107 109 111 113 115
# 117 119 121 123 125 127 129 131 133 135 137 139
# 141 143 145 147 149 151 153 155 157 159 161 163
# 165 167 169 171 173 175 177 179 181 183 185 187
# 189 191 193 195 197 199





# 5. Escreva um programa que exiba na saída padrão os 100 primeiros números em ordem
# descrescente.

for i in range(99, -1, -1):
    print(i, end=" ")

# O comando end=" " define a forma de saída no interpretador
# Por exemplo, end="\n" Linha abaixo de linha
# end=" " na mesma linha com 1 espaço
# end="" na mesma linha sem espaço, etc...
# O programa apresenta na saída do pyhton :
# >>> 99 98 97 96 95 94 93 92 91 90
# 89 88 87 86 85 84 83 82 81 80 79
# 78 77 76 75 74 73 72 71 70 69 68
# 67 66 65 64 63 62 61 60 59 58 57
# 56 55 54 53 52 51 50 49 48 47 46
# 45 44 43 42 41 40 39 38 37 36 35
# 34 33 32 31 30 29 28 27 26 25 24
# 23 22 21 20 19 18 17 16 15 14 13
# 12 11 10 9 8 7 6 5 4 3 2 1 0





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




