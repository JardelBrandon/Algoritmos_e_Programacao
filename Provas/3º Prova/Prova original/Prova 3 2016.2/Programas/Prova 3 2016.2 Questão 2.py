'''
Questão 2: Lanchonete de Ambrosina
Descrição:
Ambrosina é "de Lua". Quase todo dia ela quer mudar o cardápio de sua lanchonete (Ambrosina
disponibilizou um terminal eletrônico para que os usuários fizessem um auto-atendimento).
Ambrósio, o programador do sistema, não agüenta mais alterar o código do programa todas as
vezes que Ambrosina muda o humor. Então Ambrósio resolveu mudar o programa de forma que
Ambrosina possa cadastrar o cardápio todas as manhãs, ao iniciar. O programa, além de
cadastrar o menu, deve ser capaz de registrar os pedidos dos clientes.
Durante o cadastro dos produtos, o programa lê a quantidade de produtos a serem cadastrados
e depois lê o código, a descrição e preço do produto.
No atendimento, os clientes escolhem os produtos pelo código. Se o cliente pede um produto não
cadastrado ou uma quantidade negativa o pedido é considerado inválido. Porém, o programa
deve continuar funcionando.
O sistema calcula quantos itens o cliente escolheu de cada código e imprime o total da conta e os
nomes dos itens que foram pedidos.
Formato da entrada:
● Consiste de um inteiro n, representando o número de produtos a serem cadastrados.
● Depois, segue o cadastro dos n produtos, onde serão lidos para cada produto:
○ Um inteiro representando o código do produto
○ Uma descrição do produto
○ Um número real representando o preço.
● Depois, são lidos os pedidos.
● O pedido consiste do código do produto seguido da quantidade de itens daquele produto
que será pedido. O pedido se encerra quando o código lido é igual a 0.
● O programa encerra quando for digitado um código negativo.
Entrada:
3
501
Guarana Antartica
1.50
101
Coxinha
2
102
Cheese Frango
3.50
501
2
101
3
0
101
1
102
2
501
1
0
-1
Saída:
9.00
10.5
'''

codigos_compra = []
descriçoes = []
preços = []
soma = 0
total = 0
n = int(input("Digite a quantidade de produtos a serem cadastrados : "))

for produtos in range(n):
    codigo_compra = int(input("Digite o código correspondente ao produto : "))
    codigos_compra.append(codigo_compra)
    descriçao = input("Digite uma descrição para o respectivo produto : ")
    descriçoes.append(descriçao)
    preço = float(input("Digite o preço do produto cadastrado : "))
    preços.append(preço)

while True:
    codigo_venda = int(input("Digite o código correspondente ao produto que deseja comprar : "))

    for produto in range(len(codigos_compra)):
        if codigo_venda == codigos_compra[produto]:
            quantidade = int(input("Digite a quantidade que deseja comprar desse produto : "))
            soma += (quantidade * preços[produto])



    while codigo_venda == 0:
        total = soma
        soma = 0
        print("Valor total da compra : ",total)
        break

    if codigo_venda < 0:
        break




