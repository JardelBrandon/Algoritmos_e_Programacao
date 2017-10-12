'''
7. Dados três valores, A, B, C, verificar se esses valores formam um triângulo.
Em caso positivo informe se o triângulo é equilátero, isósceles ou escaleno.
Use os seguintes critérios:
a. O comprimento de cada lado de um triangulo é menor do que a soma
dos outros ´dois lados.
b. Chama-se equilátero o triângulo que tem três lados iguais.
c. Denominam-se isósceles o triângulo que tem o comprimento de dois
lados iguais.
d. Recebe o nome de escaleno o triangulo que tem os três lados
diferentes.
'''
'''
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''

lado_A = float(input("Digite o valor A : "))
lado_B = float(input("Digite o valor B : "))
lado_C = float(input("Digite o valor C : "))

if abs(lado_B - lado_C) < lado_A < lado_B + lado_C or abs(lado_A -  lado_C) < lado_B < lado_A + lado_C or abs(lado_A - lado_B) < lado_C < lado_A + lado_B :
    if lado_A == lado_B == lado_C :
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo equilátero ")

    elif lado_A == lado_B or lado_B == lado_C or lado_A == lado_C :
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo isósceles ")

    else:
        print("Os valores informados formam um triângulo \nO triângulo informado é do tipo escaleno ")

else:
    print("Os valores informado não formam um triângulo")



'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para os valores de verificação dos lados do triângulo (a,b e c)
É feita a comparação se os valores informados podem construir um triângulo atendendo as seguintes condições :
A medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
E maior que o valor absoluto da diferença entre essas medidas.
O comando abs() foi introduzido para descorbrir o valor absoluto da operação matemática
Se não for possível a construção do triângulo é informado ao usuário
Se for possível a construção do triângulo, é feito o encadeamento de comparações para descobrir o tipo do triângulo
O triângulo pode ser classificado segundo a medida do seu lado.
Triângulo escaleno: Todos os lados e ângulos são diferentes.
Triângulos isósceles: dois lados iguais e os ângulos opostos a esses lados iguais.
Triângulo equilátero: Todos os lados e ângulos iguais. Concluímos que seus ângulos serão de 60°.
Obtendo-se na saída do interpretador do Python as informações sobre os triângulos de acordo com os valores :
'''
