'''
Questão: 2 Título: Serra Talhada
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



velocidade = float(input("Digite a velocidade do automóvel : "))
cor = input("Digite a cor do automóvel : ")
ano = int(input("Digite o ano do automóvel : "))
marca = input("Digite a marca do automóvel : ")



while True :
