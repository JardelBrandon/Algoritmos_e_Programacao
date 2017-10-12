'''
14. Faça um programa com uma função chamada calculaImposto. A função tem dois parâmetros:
imposto, que é a quantidade de imposto sobre vendas expressa em porcentagem e custo, que é
o valor do produto antes do imposto.
'''

def calcula_imposto(imposto, custo):
    total = imposto / 100 * custo + custo
    print("Custo inicial do produto : ", custo,
          "\nValor do imposto expressa em porcentagem : ",imposto,"%",
          "\nCusto final do produto (Acrescido da porcentagem) : ",total)

impostos = float(input("Digite o valor do imposto em porcentagem : "))
valor = float(input("Digite o preço do produto : "))

calcula_imposto(impostos, valor)




'''
O programa realiza o seguinte algoritmo:
Define a função calcula_imposto(), que contém
Uma variável total que armazena o cálculo do produto acrescido do imposto incidente nele
Imprime o custo inicial do produto, o valor da porcentagem e o custo final acrescido da porcentagem incidente
Espera a entrada do usuário para informar o valor do imposto a ser acrescido
Espera a entrada do usuário para informar o valor inicial do produto
A função calcula_imposto() é invocada, passando as informações do usuário como parâmetros
'''

