#3. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
#possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%;
#MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino
#do produto e o programa retorne o preço final do produto acrescido do imposto do
#estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma
#mensagem de erro.

MG = 7 / 100
SP = 12 / 100
RJ = 15 / 100
MS = 8 / 100

valor = float(input ("Digite o valor dos produtos : "))
estado = input ("""Digite a sigla do estado destino do produto
Considere :
MG para (Minas Gerais), SP para (São Paulo) RJ para (Rio de Janeiro) e MS para (Mato Grosso do Sul) :""")

if estado == "MG" :
    impostoMG = valor + (MG * valor)
    print ("O preço final do produto acrescido do imposto para MG foi :", impostoMG)

elif estado == "SP" :
    impostoSP = valor + (SP * valor)
    print ("O preço final do produto acrescido do imposto para SP foi :", impostoSP)

elif estado == "RJ" :
    impostoRJ = valor + (RJ * valor)
    print ("O preço final do produto acrescido do imposto para RJ foi :", impostoRJ)

elif estado == "MS" :
    impostoMS = valor + (MS * valor)
    print ("O preço final do produto acrescido do imposto para MS foi :", impostoMS)

else :
    print ("Inválido")



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada do valor do produto comprado e o estado destino
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ) e ( Se não ),
# Também foi introduzido o comando elif ( Senão se ) apresentando outras condições mutuamentes excludentes
# Fazendo as comparações pedidas na questão sobre qual é o valor final do produto acrescido do imposto de cada estado
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação feita:
# Acrescidas das mensagens em aspas