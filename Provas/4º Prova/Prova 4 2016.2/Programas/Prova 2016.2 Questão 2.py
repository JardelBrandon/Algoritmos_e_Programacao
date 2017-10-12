'''
Questão 2: Conversão para binário
Faça um programa para converter de decimal, octal ou hexadecimal para binário. O seu
programa deve primeiro perguntar qual é a base da qual se deseja converter (8, 10 ou 16),
em seguida, o número que se quer converter.
Seu programa deve verificar se o usuário digitou um número possível de representar
naquela base. Por exemplo, o número 739 não pode estar na base 8, por conter um dígito
que não pode ser representado na base 8, nesse caso o dígito 9.
Uma vez, digitado um número corretamente, o programa deve imprimir na tela o número
convertido para a base 2.
Atente para o valor de cada feature​ que você implementar:
● Valida a entrada de dados corretamente. Ou seja, faz o programa aceitar apenas as
bases 8, 10 e 16 (10 pontos)
● Valida um número octal corretamente (15 pontos)
● Valida um número hexa corretamente (15 pontos)
● Valida um número decimal corretamente (15 pontos)
● Converte um número octal corretamente (15 pontos)
● Converte um número hexa corretamente (15 pontos)
● Converte um número decimal corretamente (15 pontos)
Cada feature​ só terá pontuação máxima se você usar funções sempre que necessário,
observando os princípios da modularização e separação de objetivos.
Dica:Para realizar a conversão de decimal para binário, basta usar a técnica de divisões
sucessivas e guardar o resto da divisão.
Entrada
Base: 8
Num: 839
Base: 8
Num: 777
Base: 5
Base: 10
Num: 1AB3
Base: 16
Num: 1AB3
Base: 10
Num: 31442
Saída
O número 839 não pode ser representado na
base 8. Digite outro número.
111111111(2)
Base inválida. Apenas as bases 8, 10 e 16
são válidas. Entre novamente com a base.
O número 1AB3 não pode ser representado
na base 10. Digite outro número.
1101010110011(2)
111101011010010(2)
'''

def validar_base(base):
    valido = bool()
    if base == 8 or base == 10 or base == 16:
        valido = True

    else:
        print("Base inválida, Apenas as bases 8, 10 e 16"
              "\nSão válidas. Entre novamente com a base !")
        valido = False
    return valido

def validar_octal(valor):
    for numero in valor:
        if numero.isnumeric() == True:
            if int(numero) >= 0 and int(numero) < 9:
                valido = True

            else:
                valido = False
                print("O número :", valor, "não pode ser representado na"
                      "\nbase 8. Digite outro número.")
                break

        else:
            valido = False
            print("O número :", valor, "não pode ser representado na"
                  "\nbase 8. Digite outro número.")
            break

    return valido

def validar_decimal(valor):
    for numero in valor:
        if numero.isnumeric() == True:
            if int(numero) >= 0 and int(numero) < 10:
                valido = True

            else:
                valido = False
                print("O número :", valor, "não pode ser representado na"
                      "\nbase 10. Digite outro número.")
                break

        else:
            valido = False
            print("O número :", valor, "não pode ser representado na"
                  "\nbase 10. Digite outro número.")
            break

    return valido

def validar_hexadecimal(valor):
    for numero in valor:
        if numero.isnumeric() == True:
            if int(numero) >= 0 and int(numero) < 10:
                valido = True

            else:
                valido = False
                print("O número :", valor, "não pode ser representado na"
                      "\nbase 16. Digite outro número.")
                break

        else:
            if numero == "a" or numero == "A":
                valido = True

            elif numero == "b" or numero == "B":
                valido = True

            elif numero == "c" or numero == "C":
                valido = True

            elif numero == "d" or numero == "D":
                valido = True

            elif numero == "e" or numero == "E":
                valido = True

            elif numero == "f" or numero == "F":
                valido = True

            else:
                valido = False
                print("O número :", valor, "não pode ser representado na"
                  "\nbase 16. Digite outro número.")
                break

    return valido

def converter_decimal(valor):
    binario = []
    valor = int(valor)
    while valor > 0:
        if valor % 2 != 0:
            binario.append(1)
            valor = valor // 2

        else:
            binario.append(0)
            valor = valor // 2

    binario = binario[::-1]
    print(binario)

def converter_octal(valor):
    binario = []
    for numero in valor:
        if numero == "0":
            binario.append(0)

        elif numero == "1":
            binario.append(1)

        elif numero == "2":
            binario.append(10)

        elif numero == "3":
            binario.append(11)

        elif numero == "4":
            binario.append(100)

        elif numero == "5":
            binario.append(101)

        elif numero == "6":
            binario.append(110)

        elif numero == "7":
            binario.append(111)

        else:
            binario.append(1000)
    print(binario)


def converter_hexadecimal(valor):
    binario = []
    for numero in valor:
        if numero == "0":
            binario.append(0)

        elif numero == "1":
            binario.append(1)

        elif numero == "2":
            binario.append(10)

        elif numero == "3":
            binario.append(11)

        elif numero == "4":
            binario.append(100)

        elif numero == "5":
            binario.append(101)

        elif numero == "6":
            binario.append(110)

        elif numero == "7":
            binario.append(111)

        elif numero == "8":
            binario.append(1000)

        elif numero == "9":
            binario.append(1001)

        elif numero == "10":
            binario.append(1010)

        elif numero == "a" or numero == "A":
            binario.append(1011)

        elif numero == "b" or numero == "B":
            binario.append(1100)

        elif numero == "c" or numero == "C":
            binario.append(1101)

        elif numero == "d" or numero == "D":
            binario.append(1110)

        elif numero == "e" or numero == "E":
            binario.append(1111)

        else:
            binario.append(10000)

    print(binario)



converter_base = int(input("Digite o valor da base que deseja converter para binário : "))

while validar_base(converter_base) == False:
    converter_base = int(input("Digite o valor da base que deseja converter para binário : "))


if converter_base == 8:
    numero = input("Digite o número octal que deseja converter para binário : ")
    while validar_octal(numero) == False:
        numero = input("Digite o número octal que deseja converter para binário : ")

    converter_octal(numero)

elif converter_base == 10:
    numero = input("Digite o número decimal que deseja converter para binário : ")
    while validar_decimal(numero) == False:
        numero = input("Digite o número decimal que deseja converter para binário : ")

    converter_decimal(numero)

else:
    numero = input("Digite o número hexadecimal que deseja converter para binário : ")
    while validar_hexadecimal(numero) == False:
        numero = input("Digite o número hexadecimal que deseja converter para binário : ")

    converter_hexadecimal(numero)



