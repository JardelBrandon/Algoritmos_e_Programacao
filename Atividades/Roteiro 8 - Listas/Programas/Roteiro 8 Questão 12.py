'''
12. Quem matou quem em Game of Thrones? Às vezes fica difícil de lembrar, portanto faremos
um programa que mantém isso guardado. A entrada do programa deve receber em sequência
o nome do assassino e o nome da pessoa morta por ele. O programa irá rodar até que o
usuário digite “valar morghulis”. Ao final, ele deve imprimir a lista dos assassinos e os nomes
das pessoas que foram mortas por eles, a quantidade de pessoas que cada um matou e
quantidade total de pessoasmortas.
'''

assassino = []
assassinado = []


while True :
    matou = input("Digite o nome do assassino : ")

    if matou == "valar morghulis" :
        break

    morreu = input("Digite o nome da pessoa assassinada : ")

    if morreu == "valar morghulis" :
        break

    assassinado.append(morreu)

    if matou in assassino :
        assassino.pop()

    assassino.append(matou)

    if matou == "valar morghulis" or morreu == "valar morghulis" :
        break

print(assassino , assassinado)

'''
Exemplos de entrada e Saída:
John Snow
João
John Snow
Maria
valar morghulis

John Snow João Maria
'''


'''
O programa realiza o seguinte algoritmo :
Define duas variáveis do tipo lista
Entra em um laço de repetição afirmando que o while True (Enquanto verdadeiro)
Espera a entrada dos nomes pelo usuário para a Lista do assassino e do assassinado respectivamente
Adiciona os nomes digitado na lista respectivamente
Analisa se foi digitado o nome valar morghulis em alguma lista se sim o laço de repetição é encerrado
Analisa se o nome da pessoa que assassinou já contém na lista, caso contenham o nome é apagado para não haver repetição
Imprime na tela os nomes das listas dos assassinos e os assassinados
'''
