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



