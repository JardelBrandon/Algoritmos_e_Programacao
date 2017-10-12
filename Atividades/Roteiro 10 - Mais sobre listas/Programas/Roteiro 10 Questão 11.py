'''
11. Escreva um programa que leia e armazene nomes de pessoas em dois vetores distintos
com 8 posições. O programa deve identificar os nomes que constam nos dois vetores.
'''

vetor_nomes_A = []
vetor_nomes_B = []
vetor_nomes_A_e_B = []

for nomes in range(8):
    nome_A = input("Digite o nome para ser armazenado na primeira lista : ")
    vetor_nomes_A.append(nome_A)

for nomes in range(8):
    nome_B = input("Digite o nome para ser armazenado na segunda lista : ")
    vetor_nomes_B.append(nome_B)

for procurado in vetor_nomes_A:
    for procurar in vetor_nomes_B:
        if procurado == procurar:
            if procurado in vetor_nomes_A_e_B:
                break
            vetor_nomes_A_e_B.append(procurado)


if len(vetor_nomes_A_e_B) > 0:
    print("Primeira lista com os nomes armazenados : \n", vetor_nomes_A,
          "\nSegunda lista com os nomes armazenados : \n", vetor_nomes_B,
          "\nNomes que estão presentes em ambas as listas : \n", vetor_nomes_A_e_B)

else:
    print("Primeira lista com os nomes armazenados : \n", vetor_nomes_A,
          "\nSegunda lista com os nomes armazenados : \n", vetor_nomes_B,
          "\nNão existe nomes que estão presentes em ambas as listas !")


'''
O programa realiza o seguinte algoritmo:
Define as variáveis lista como sendo vetor de armazenamento
Entra no laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os nomes da primeira lista do vetor
Adiciona cada nome no final da lista vetor_A
Entra em outro laço de repetição for para iteração dentro do range até 8
Espera a entrada do usuário para receber os nomes da segunda lista do vetor
Adiciona cada nome no final da lista vetor_B
Entra em outro laço de repetição for para iteração de cada elemento do vetor_A para procurar no vetor_B
Entra em outro laço de repetição for para iteração de cada elemento do vetor_B que será procurado pelo elemento do vetor_A
Caso o elemento que está sendo procurando seja igual ao elemento procurado, significa que o elemento está presente nas duas listas
Se o elemnto que está presente nas duas lista já foi adicionado na lista do vetor_A_e_B, então o laço é quebrado (break) para o elemento não se repetir
Se ainda não está presente na lista do vetor_A_e_B então o elemento é adicionado a lista de nomes que estão presentes em ambas as listas
Imprime na tela a primeira lista de nomes inseridos, a segunda lista de nomes inseridos e
Caso haja nomes presentes em ambas as listas imprime os nomes em comum
Caso não haja nomes presentes em ambas as listas imprime o aviso que não existe
Acrescidas das mensagens em aspas
'''