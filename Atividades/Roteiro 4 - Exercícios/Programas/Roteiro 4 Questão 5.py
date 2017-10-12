'''
5. Crie um programa que calcula as raízes de uma equação do 2o grau:
ax² + bx + c=0
Para ela existir, o coeficiente 'a' deve ser diferente de zero. No caso de a ser
igual a zero, envie uma mensagem de erro ao usuário.
O delta é dado por b² - 4ac. Caso o delta seja maior ou igual a zero, calcule
as raízes (que serão reais). Caso o delta seja negativo, exiba a mensagem:
"As raízes são números complexos"
'''

a = float(input("Digite o valor do primeiro coeficiente da equação do segundo grau (a) : "))

if a == 0 :
    print("Inválido ! ")

b = float(input("Digite o valor do segundo coeficiente da equação do segundo grau (b) : "))
c = float(input("Digite o valor do terceiro coeficiente da equação do segundo grau (c) : "))

delta = b ** 2 - 4 * a * c

if delta < 0 :
    print("As raízes são números complexos ! ")

else :
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

print ("Primeira raíz da equação : ", x1, "\nSegunda raíz da equação : ", x2)



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para os coeficientes da equação do segundo grau (a,b e c)
É feita a comparação se a é igual a zero, pois se for a operação é inválida por que se tornaria uma equação de primeiro grau
É calculado o delta da equação e verificado se é maior que zero, pois se não for as raízes serão complexas
De acordo com os valores introduzidos calcula-se os valores das raízes para a equação
Obtendo-se na saída do interpretador do Python as raízes dadas de acordo com os calculos feito:
Acrescidas das mensagens em aspas
'''