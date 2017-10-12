'''
14. Uma loja deseja conhecer o perfil de seus (suas) clientes e para isso vai fazer uma pesquisa
usando um programa que ficará no caixa. Ele vai perguntar a cada cliente no momento da compra
as seguintes informações: idade, valor da compra e tipo de pagamento (C: cartão; V: à vista).
Essas perguntas serão feitas enquanto a resposta for SIM. Quando a resposta for NÃO, a pesquisa
deve ser encerrada e o programa deve exibir as seguintes informações:
- a quantidade de vendas realizadas;
- o total de vendas à vista e no cartão;
- a idade do cliente mais jovem;
- o valor da maior compra;
- a média de compras feitas à vista;
'''

vendas = 0
vendas_a_vista = 0
vendas_no_cartao = 0
maior_compra = 0
media_a_vista = 0

idade = float(input("Digite a idade do cliente : "))
valor_da_compra = float(input("Digite o valor da compra : "))
pagamento = input("Digite a forma de pagamento: \nConsidere (C para Cartão ou V para à vista)")
resposta = input("Digite se deseja continuar a pesquisa: \nConsidere (SIM para continuar ou NÃO para encerrar)")
vendas += 1
maior_compra = valor_da_compra
jovem = idade

while True :
    idade = float(input("Digite sua idade : "))
    valor_da_compra = float(input("Digite o valor da compra : "))
    pagamento = input("Digite a forma de pagamento: \nConsidere (C para Cartão ou V para à vista)")
    resposta = input("Digite se deseja continuar a pesquisa: \nConsidere (SIM para continuar ou NÃO para encerrar)")
    vendas += 1

    if pagamento == "V" :
        vendas_a_vista += 1

    if pagamento == "C" :
        vendas_no_cartao += 1

    if idade < jovem :
        jovem = idade

    if valor_da_compra > maior_compra :
        maior_compra = valor_da_compra

    if resposta == "NÃO" :
        break




media_a_vista = vendas / vendas_a_vista

print("Total de vendas à vista e no cartão: ", vendas)
print("Idade do cliente mais jovem :", jovem)
print("Valor da maior compra :", maior_compra)
if media_a_vista == 0 :
    print("Média de compras feitas à vista : 0")
else :
    print("Média de compras feitas à vista :", media_a_vista)






# O Algoritmo do programa realiza os seguintes comandos :
# Declara os valores das variáveis
# Realiza a repetição pela primeira vez fora do laço while para se ter um valor de comparação
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas, faz as comparações das lógicas
# Realiza as operações em seus respectivos encadeamentos
# Imprime na tela o total de vendas, cliente mais jovem, valor da maior compra e média das compras feitas à vista
# Acrescidos das mensagens em aspas
# Atendendo o que se pede na questão

