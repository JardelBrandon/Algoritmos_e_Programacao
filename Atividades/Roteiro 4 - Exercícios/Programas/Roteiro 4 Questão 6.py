'''
6. Fazer um programa que solicita o total gasto pelo cliente de uma loja,
imprime as opções de pagamento, solicita a opção desejada e imprime o
valor total das prestações (se houverem).
1) Opção: a vista com 10% de desconto
2) Opção: em duas vezes (preço da etiqueta)
3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para
compras acima de R$ 100,00).
'''

total_gasto = float(input("Digite o valor total gasto pelo cliente : "))

pagamento = input('''Selecione a forma de pagamento :
A vista com 10% de desconto (V) :
Em duas vezes com o preço normal (D) :
Parcelado de 3 até 10 vezes com 3% de juros ao mês disponível para compras acima de R$ 100.00 (P) : ''')

if pagamento == "V" :
    orçamento = total_gasto * 0.9

elif pagamento == "D" :
    orçamento = total_gasto / 2

elif pagamento == "P" and total_gasto >= 100 :
    parcelas = int(input("Digite a quantidade de parcelas desejadas :"))
    orçamento = (parcelas * 0.03 * total_gasto + total_gasto) / parcelas

else :
    print("Inválido")

print("Valor do orçamento para a opção de pagamento desejada : ", orçamento)




'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada dos valores para o valor do gasto do cliente e a forma de pagamento
De acordo com a forma de pagamento selecionado, calcula o valor do orçamento
Se o pagamento for a vista é apresentado o valor com o desconto, se a prazo é o valor das parcelas de acordo com as condições
Obtendo-se na saída do interpretador do Python o valor de pagamento:
Acrescidas das mensagens em aspas
'''