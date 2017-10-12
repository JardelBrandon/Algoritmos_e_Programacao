'''
8. Em um ADN em dupla hélice, as bases, se estáveis, emparelham-se com as respectivas
bases complementares: Adenina (A) com Timina (T) e Citosina (C) com Guanina (G).
Escreva um programa que dada uma sequência lida da entrada padrão de tamanho 15,
informe a base complementar:
Entrada: AGGGATTCCCCCAG
Saída: TCCCTAAGGGGGTC
'''

adn = []
base_complementar = []

for entrada in range(15):
    espelhamento = input("Digite a entrada do ADN: "
                         "\nAdenina (A); Timina (T); Citosina (C); Guanina (G)")
    adn.append(espelhamento)

for espelhado in adn:
    if espelhado == "A":
        base_complementar.append("T")

    elif espelhado == "T":
        base_complementar.append("A")

    elif espelhado == "C":
        base_complementar.append("G")

    elif espelhado == "G":
        base_complementar.append("C")

    else:
        base_complementar.append("inválido")

print("Base de ADN inserida: \n", adn,
      "\nBases complementares da ADN : \n", base_complementar)



'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 15
Espera a entrada do usuário para receber os bases de ADN
adiciona as bases de ADN no final da lista adn
Entra em outro laço de repetição for para iteração de cada base de ADN na lista adn
Faz o espelhamento da lista de ADN na lista de bases complementares
Sendo analisado a entrada, é relacionado a saída da seguinte maneira:
Adenina (A) com Timina (T) e Citosina (C) com Guanina (G)
Imprime na tela a Lista da base de ADN inserida e a sua lista espelhada com os elementos respectivos da base complementar,
Acrescidas das mensagens entre aspas
'''

