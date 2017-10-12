'''
8. Faça uma prova de matemática para crianças que estão aprendendo a somar
números inteiros menores do que 100. Escolha números aleatórios entre 1 e
100, e mostre na tela a pergunta: “ qual é a soma de a + b? ”, onde a e b são
os números aleatórios. Peça a resposta. Faça cinco perguntas como essa ao
aluno e mostre para ele as perguntas e as respostas corretas, além de
quantas vezes o aluno acertou.
Para gerar um número aleatório em python, faça o seguinte:
● No início do código importe a biblioteca de geração de números
aleatórios:
○ from random import randint
● Para gerar um número aleatório entre 0 e 100
○ randint(0,100)
'''
from random import randint

corretas = 0
a = randint(0,100)
b = randint(0,100)

pergunta_1 = a + b
print("Qual é a soma de ", a, "+", b, ":")
resposta_1 = float(input())

if resposta_1 == pergunta_1 :
    corretas += 1

c = randint(0,100)
d = randint(0,100)

pergunta_2 = c + d
print("Qual é a soma de ", c, "+", d, ":")
resposta_2 = float(input())

if resposta_2 == pergunta_2 :
    corretas += 1

e = randint(0,100)
f = randint(0,100)

pergunta_3 = e + f
print("Qual é a soma de ", e, "+", f, ":")
resposta_3 = float(input())

if resposta_3 == pergunta_3 :
    corretas += 1

g = randint(0,100)
h = randint(0,100)

pergunta_4 = g + h
print("Qual é a soma de ", g, "+", h, ":")
resposta_4 = float(input())

if resposta_4 == pergunta_4 :
    corretas += 1

i = randint(0,100)
j = randint(0,100)

pergunta_5 = i + j
print("Qual é a soma de ", i, "+", j, ":")
resposta_5 = float(input())

if resposta_5 == pergunta_5 :
    corretas += 1

print("1º Pergunta :", a, "+", b, "\nResposta correta : ", pergunta_1, "\nResposta informada : ", resposta_1,
"\n2º Pergunta :", c, "+", d, "\nResposta correta : ", pergunta_2, "\nResposta informada : ", resposta_2,
"\n3º Pergunta :", e, "+", f, "\nResposta correta : ", pergunta_3, "\nResposta informada : ", resposta_3,
"\n4º Pergunta :", g, "+", h, "\nResposta correta : ", pergunta_4, "\nResposta informada : ", resposta_4,
"\n5º Pergunta :", i, "+", j, "\nResposta correta : ", pergunta_5, "\nResposta informada : ", resposta_5,
"\nTotal de respostas corretas : ", corretas)



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Define as varíaveis de resposta correta e os valores aleatórios de a e b para realização da soma
Realiza a soma para armazenar o valor correto e pergunta ao usuário a resposta para essa soma
Espera a entrada do valor resposta do usuário para aquela pergunta e a armazena
Compara se o valor informado é o valor correto para a resposta, caso sim adiciona 1 a variável correta
E repete esse algoritmo até a ultima pergunta
Obtendo-se na saída do interpretador do Python qual era a pergunta, a resposta correta e a resposta informada para todas as perguntas:
Acrescidas das mensagens em aspas e do número total de respostas corretas
'''