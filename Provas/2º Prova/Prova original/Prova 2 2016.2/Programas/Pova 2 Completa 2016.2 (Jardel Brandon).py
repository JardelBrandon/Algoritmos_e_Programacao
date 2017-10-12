'''
IFPB - Instituto Federal de Educação, Ciência e Tecnologia da Paraíba
Curso de Engenharia de Computação
Disciplina: Algoritmos e Programação
Semestre Letivo: 2016.2
Professor: Marcelo Siqueira / Henrique Cunha
PROVA 2
Instruções:
1. Não é permitido consultar livros, anotações, Internet etc.
2. Não é permitido conversar durante o horário da prova
3. Todas as questões têm o mesmo valor.
4. Utilize essas folhas como rascunho quando necessário.
5. Salve seus arquivos em alguma pasta que não seja a área de trabalho.
6. Para cada problema você tem um conjunto de dados de entrada e de saída que
servirão como uma referência na hora de testar seu código.
7. A interpretação faz parte da prova.
Campina Grande, PB
15 de Fevereiro de 2017
'''


'''
Questão: 1  Título: Seguridade Social
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
auxílio por cada filho. Caso não receba auxílio, será informado o motivo ("Não
recebe: média de idade incompatível" ou "Não recebe: renda incompatível").
'''
MAX = 3

media = 0
contador = 0

while True :
    renda = float(input("Digite a renda da família : "))
    quantidade_de_filhos = int(input("Digite a quantidade de filhos da família : "))
    for x in range(0, quantidade_de_filhos) :
        idade = float(input("Digite a idade dos filhos da família : "))
        media += idade
    contador += 1

    media = media / quantidade_de_filhos

    if renda > 1000:
        print("Não recebe : renda incompatível! ")

    if renda <= 1000:
        if media < 5:
            print("O valor do auxílio será : 2000 ")
            media = 0

        if media >= 5 and media < 10:
            print("O valor do auxílio será : 1000 ")
            media = 0

        if media >= 10 and media < 18:
            print("O valor do auxílio será : 500 ")
            media = 0

        if media >= 18:
            print("Não recebe : média de idade incompatível! ")
            media = 0

    if contador == MAX :
        break





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


'''
Questão: 2  Título: Serra Talhada
Descrição:
A polícia rodoviária de Serra Talhada deseja monitorar os carros que passam pela
fronteira da cidade. Para isso vai adotar um sistema de software que recebe como
entrada a cor, velocidade que passou pelo posto, ano e marca de cada automóvel
e exibe as seguintes informações na saída:
A cor do carro mais antigo
O marca do carro mais veloz
A quantidade de carros amarelos do ano 1980
A média de velocidade dos carros das marcas BMW e VOLVO
A quantidade de carros cuja velocidade esteja entre 80.0 e 120.00 e sejam azuis
O sistema deve finalizar a execução quando uma velocidade negativa ou nula for
informada.
'''
cor_antigo = str()
antigo = 0
cor_amarelo_1989 = 0
veloz = 0
marca_veloz = str()
quantidade_amarelos_1980 = 0
media_velocidade_bmw_volvo = 0
quantidade_bmw_volvo = 0
quantidade_velocidade_entre_80_e_120_azuis = 0


velocidade = float(input("Digite a velocidade que o automóvel passou pelo posto : "))
veloz = velocidade
cor = input("Digite a cor do automóvel : ")
cor_antigo = cor
ano = float(input("Digite o ano do automóvel : "))
antigo = ano
marca = input("Digite a marca do automóvel : ")
marca_veloz = marca

if velocidade >= 80 and velocidade <= 120 and cor == "azul":
    quantidade_velocidade_entre_80_e_120_azuis += 1

if marca == "BMW" or marca == "VOLVO":
    media_velocidade_bmw_volvo += velocidade
    quantidade_bmw_volvo += 1

if velocidade <= 0 :
    print("Cor do automóvel mais antigo : ", cor_antigo)
    print("Marca do automóvel mais veloz : ", marca_veloz)

    if cor == "amarelo" and ano == 1980 :
        cor_amarelo_1989 += 1


    media_velocidade_bmw_volvo = media_velocidade_bmw_volvo / quantidade_bmw_volvo

    print("Quantidade de automóveis amarelos do ano 1980 : ", cor_amarelo_1989)
    print("Média de velocidade dos automóveis da marca BMW e VOLVO :", media_velocidade_bmw_volvo)
    print("Quantidade de automóveis cuja velocidade esteja entre 80.0 e 120.00 e sejam azuis ", quantidade_velocidade_entre_80_e_120_azuis)

if velocidade > 0 :
    while True :
        velocidade = float(input("Digite a velocidade que o automóvel passou pelo posto : "))
        if velocidade <= 0:
            break
        cor = input("Digite a cor do automóvel : ")
        ano = float(input("Digite o ano do automóvel : "))
        marca = input("Digite a marca do automóvel : ")

        if ano < antigo :
            antigo = ano
            cor_antigo = cor

        if velocidade > veloz :
            veloz = velocidade
            marca_veloz = marca

        if cor == "amarelo" and ano == 1980:
            cor_amarelo_1989 += 1

        if marca == "BMW" or marca == "VOLVO":
            media_velocidade_bmw_volvo += velocidade
            quantidade_bmw_volvo += 1

        if velocidade >= 80 and velocidade <= 120 and cor == "azul":
            quantidade_velocidade_entre_80_e_120_azuis += 1

        if velocidade <= 0:
            break

media_velocidade_bmw_volvo = media_velocidade_bmw_volvo / quantidade_bmw_volvo

print("Cor do automóvel mais antigo : ", cor_antigo)
print("Marca do automóvel mais veloz : ", marca_veloz)
print("Quantidade de automóveis amarelos do ano 1980 : ", cor_amarelo_1989)
print("Média de velocidade dos automóveis da marca BMW e VOLVO :", media_velocidade_bmw_volvo)
print("Quantidade de automóveis cuja velocidade esteja entre 80.0 e 120.00 e sejam azuis ", quantidade_velocidade_entre_80_e_120_azuis)

'''
Velocidade: 100
Cor: azul
Ano: 1980
Marca: VOLVO
Velocidade: 110
Cor: amarelo
Ano: 1990
Marca: BMW
Velocidade: 110
Cor: azul
Ano: 1980
Marca: fiat
Velocidade: 90
Cor: azul
Ano: 1970
Marca: ford
Velocidade: 150
Cor: amarelo
Ano: 1980
Marca: BMW
Velocidade: 0
A cor do carro mais antigo é: amarelo
A marca do carro mais veloz é: BMW
A quantidade de carros amarelos do ano de 1980 é: 1
A média de velocidade dos carros das marcas BMW e VOLVO
é: 120.0
A quantidade de carros cuja velocidade esteja entre 80.0 e
120.00 e são azuis é: 3
'''

