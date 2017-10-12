'''
2. Crie um Programa que recebe um String contendo uma palavra ou frase. A String recebida
deve ter pelo menos 1 espaço (“ ”) em branco. Se não tiver, emita uma mensagem de erro até
que o usuário digite uma frase que contenha pelo menos 1 espaço. Em seguida, escreva na
saída padrão a String recebida sem os espaços em branco. Por exemplo, se a String recebida
for “Instituto Federal de Educação, Ciência e Tecnologia da Paraíba”, escreva
“InstitutoFederaldeEducação,CiênciaeTecnologiadaParaíba”.
'''

string = input("Digite uma palavra ou frase : ")

while string.find(" ") < 0:
    print("Inválido, digite uma palavra ou frase com espaços em branco!")
    string = input("Digite uma palavra ou frase : ")

string_sem_espaços = string.replace(" ", "")
print(string_sem_espaços)

"""
O programa realiza o seguinte algoritmo:
Espera a entrada de um usuário para informar uma string 
Análisa se a string digitada contém pelo menos 1 espaço em branco 
Se não houver, entra em um laço de repetição while que,
Imprime uma mensagem de erro, informando que a string precisa conter espaços em branco
Espera a entrada de um usuário para informar uma string novamente
Quando uma string com espaços é digitada 
Uma variável string_sem_espaços, armazena a string informada sem os espaços em branco 
retirando os espaços com o comando .replace(" ", "") que localiza os espaços e substitui tirando eles 
Imrpime a variável sem os espaços em branco
"""