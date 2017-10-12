'''
11.Faça um programa que calcula o imposto de renda devido de uma pessoa
sabendo que:
a. O imposto que uma pessoa paga é proporcional ao que ela ganha de
acordo com a seguinte tabela :
(Tabela presente no Roteiro de Aulas 4 na questão 11)
b. A contribuição previdenciária de 11% sobre o valor bruto é deduzida
da base de cálculo
c. Para cada dependente, é descontado R$ 189,59 da base de cálculo
d. Caso o indivíduo pague pensão alimentícia, esse valor também é
deduzido da base de cálculo
e. Para calcular o imposto final devido o programa deve aplicar a alíquota
referente a cada faixa sobre a qual a base de cálculo (após as
deduções) cai. Por exemplo, se a base de cálculo for de R$ 3000,00, a
pessoa está isenta de pagar imposto referente a R$ 1903,89 dessa
base de cálculo e, portanto, pagará imposto apenas sobre o que
excede a base, que nesse caso é R$ 1096,11. Na segunda faixa, a
pessoa deve pagar 7,5% sobre um máximo de R$ 922,67, o que dá R$
69,20. Em nosso exemplo ainda restam R$ 173,44 (1096,11 - 922,67)
sobre o qual será aplicado uma alíquota de 15%, o que dá R$26,00.
Dessa forma, o imposto total devido é de 26 + 69,20 = R$ 95,20
f. Ao final você deve também calcular a alíquota efetiva que é calculada
a partir do percentual do imposto sobre o rendimento tributável. No
nosso exemplo ficaria (95,20/3000)*100 = 3,17%
g. Para conferir os resultados do seu programa, use o simulador da
receita federal.
'''

PRIMEIRA_FAIXA = 1903.98
SEGUNDA_FAIXA = 922.67
TERCEIRA_FAIXA = 924.40
QUARTA_FAIXA = 913.63
#QUINTA_FAIXA = valor restante

deduçoes = 0.00
base_calculo = 0.00
total_dependentes = 0.00
valor_impostos = 0.00
deduçao_dependente = 189.59


print('''Simulação de Alíquota Efetiva
       \nIMPOSTO SOBRE A RENDA MENSAL - Valores em Reais
       \n1. Rendimentos tributáveis:''')

renda = float(input("Digite o valor da renda : "))

print("2. Deduções:")

previdencia = float(input("2.1 Digite o valor pago para a Previdência Oficial : "))
dependentes = int(input("2.2 Digite a quantidade de dependentes : "))
total_dependentes = (dependentes * deduçao_dependente)
print("O valor da dedução é R$ 189,59 mensais, por dependente.",
      dependentes,"*", deduçao_dependente, "=", total_dependentes)
pensao_alimenticia = float(input("2.3 Digite o valor da Pensão alimentícia"))
outras_deduçoes = float(input("2.4 Digite o valor de outras deduções :"))

deduçoes = (previdencia - total_dependentes - pensao_alimenticia - outras_deduçoes)
base_calculo = (renda - deduçoes)

print("Total de deduções : ", deduçoes,
      "3. Base de cálculo (1 - 2.5)"
      "Total para a base de cálculo : ", base_calculo,
      "4. Imposto")

if base_calculo < PRIMEIRA_FAIXA:




print('''Demonstrativo da Apuração do Imposto
        Faixa da Base de Cálculo	Alíquota	Valor do Imposto
        1ª Faixa	1.903,98	        Isento	0,00
        2ª Faixa	922,67	             7,5%	69,20
        3ª Faixa	924,40	             15,0%	138,66
        4ª Faixa	913,63	             22,5%	205,57
        5ª Faixa	295.335,32	         27,5%	81.217,21
        
        Total	    300.000,00	    ---    	81.630,64

''')

print("5. Alíquota efetiva - % ", x,"Percentual do imposto sobre os rendimentos tributáveis."
      "Senhor contribuinte, apesar do seu rendimento estar na faixa de " , x," sua alíquota efetiva é de", x)


