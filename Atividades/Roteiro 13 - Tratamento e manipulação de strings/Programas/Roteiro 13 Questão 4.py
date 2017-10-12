'''
4. Modique a questão anterior para que a palavra também seja lida da entrada padrão.
'''

'''
3. Escreva um programa que leia um caractere da entrada padrão e verifique se o mesmo está
contido na palavra "engenharia"
'''
palavra = input("Digite uma palavra :")
verificar = input("Digite um caractere para verificar se está contida na palavra : ")

if palavra.find(verificar) >= 0:
    print("O caractere digitado :", verificar,
          "\nEstá contido na palavra :", palavra)
else:
    print("O caractere digitado : ", verificar,
          "\nNão está contido na palavra :", palavra)

'''
O programa realiza o seguinte algoritmo:
Espera a entrada do usuário para digitar uma palavra
Espera a entrada do usuário para digitar um caractere para verificar se pertence a palavra
Verifica se o comando .find(verificar) retorna um valor maior ou igual a zero 
Se sim, significa que o caractere informado está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual está contida 
Se não, significa que o caractere informado não está contido na palavra definida 
Então é impresso uma mensagem informando o caractere buscado e a palavra na qual não está contida 
'''