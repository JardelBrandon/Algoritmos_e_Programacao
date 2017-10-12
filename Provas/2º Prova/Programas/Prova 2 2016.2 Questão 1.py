'''
Questão: 1 Título: Seguridade Social
Descrição:
A prefeitura de Nova Iorque está tentando implementar um programa de
seguridade social que visa auxiliar famílias que possuem muitos filhos e são de
baixa renda. Uma família é considerada de baixa renda quando recebe até US$
1000 por mês.
De acordo com as regras, quando a família for de baixa renda e a média de idade
dos filhos da família for inferior a 5 anos, a família receberá um auxílio de US$
2000. Quando for superior ou igual a 5 anos e menor do que 10 anos, receberá
um auxílio de US$ 1000. Quando for igual ou superior a 10 e inferior a 18 anos, a
família receberá Us$ 500. Caso seja superior ou igual a 18 anos, não receberá
nada.
O programa desenvolvido lerá dados (renda, quantidade de filhos, idade de cada
filho) de 3 famílias. Para cada família, será informado quanto será o valor do
auxílio por cada filho (Auxílio da família x: VALOR), onde x é o número da família e
VALOR é o valor a ser recebido.
Caso não receba auxílio, será informado o motivo ("Não recebe: média de idade
incompatível" ou "Não recebe: renda incompatível").
'''
FAMILIAS = 3

contador = 0
media_idade_filhos = 0

while contador < FAMILIAS :
    renda = float(input("Digite a renda da família :"))
    contador += 1
    if renda > 1000 :
        quantidade_filhos = int(input("Digite a quantidade de filhos da família : "))
        if renda > 1000:
            print("Não recebe : renda incompatível! ")

    if renda <= 1000 :
        quantidade_filhos = int(input("Digite a quantidade de filhos da família :"))

        for x in range(0, quantidade_filhos) :
            idade = float(input("Digite a idade dos filhos da família :"))
            media_idade_filhos += idade

            media_idade_filhos /= quantidade_filhos

        if media_idade_filhos < 5:
            print("A família receberá um auxílio de : 2000")

        if media_idade_filhos >= 5 and media_idade_filhos < 10:
            print("A família receberá um auxílio de : 1000")

        if media_idade_filhos >= 10 and media_idade_filhos < 18:
            print("A família receberá um auxílio de : 500")

        if media_idade_filhos > 18:
            print("Não recebe : Média de idade incompatível! ")


'''
O código do programa realiza o seguinte algoritmo :
Define o valor da constantes e das variáveis
Entra em um laço de repetição enquanto o contador for menor que o número de famílias
Espera a entrada das informações pelo usuário
Realiza as operações matemáticas e faz suas comparações lógicas seguindo o encadeamento
Apresenta na saída do python o valor do auxílio que será recebido de acordo com a situação
'''

'''
Entradas
Família 1
Renda: 1000
Quantidade de filhos: 3
Idade: 5
Idade: 3
Idade: 2
Família 2
Renda: 500
Quantidade de filhos: 1
Idade: 8
Família 3
Renda: 1200
Quantidade de filhos: 5

Saídas
Auxílio da família 1: 2000
Auxílio da família 2: 1000
Auxílio da família 3: Não recebe: renda
incompatível.
'''