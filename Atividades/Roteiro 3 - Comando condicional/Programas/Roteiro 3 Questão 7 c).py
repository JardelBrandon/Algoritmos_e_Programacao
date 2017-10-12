#7°.) c) 3° maneira de fazer o programa usando o comando if, elif e else
#7.  Escreva um programa que leia as notas de três pessoas pessoas em uma prova e as
#exiba na saída padrão de forma crescente.


aluno1 = float (input ( " Digite a nota do 1° aluno : " ) )

aluno2 = float (input ( " Digite a nota do 2° aluno : " ) )

aluno3 = float (input ( " Digite a nota do 3° aluno : " ) )


# aluno1 < aluno2 < aluno3
# aluno1 < aluno3 < aluno2
# aluno2 < aluno1 < aluno3
# aluno2 < aluno3 < aluno1
# aluno3 < aluno1 < aluno2
# aluno3 < aluno2 < aluno1

# aluno1 = aluno2 < aluno3
# aluno1 = aluno2 > aluno3
# aluno2 = aluno3 < aluno1
# aluno2 = aluno3 > aluno1
# aluno3 = aluno1 < aluno2
# aluno3 = aluno1 > aluno2
# aluno1 = aluno2 = aluno3


if aluno1 == aluno2 and aluno1 < aluno3 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno1 == aluno2 and aluno1 > aluno3 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno2 == aluno3 and aluno2 < aluno1 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno2 == aluno3 and aluno2 > aluno1 :
    print ( " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno3 == aluno1 and aluno3 < aluno2 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 2 foi : " + str ( aluno2 ) )

elif aluno3 == aluno1 and aluno3 > aluno2 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) + "\n" +
            " A nota do aluno 1 foi : " + str ( aluno1 ) + "\n" +
            " A nota do aluno 3 foi : " + str ( aluno3 ) )


elif aluno1 < aluno2 and aluno1 < aluno3 :
    print(" A nota do aluno 1 foi : " + str(aluno1))
    if aluno2 < aluno3 :
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    else :
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )


elif  aluno2 < aluno1 and aluno2 < aluno3 :
    print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
    if aluno1 < aluno3 :
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    else :
        print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )


elif aluno3 < aluno2 and aluno3 < aluno1 :
    print ( " A nota do aluno 3 foi : " + str ( aluno3 ) )
    if aluno1 < aluno2 :
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
    else :
        print ( " A nota do aluno 2 foi : " + str ( aluno2 ) )
        print ( " A nota do aluno 1 foi : " + str ( aluno1 ) )


else :
    print(" A nota do aluno 1 foi : " + str(aluno1) + "\n" +
          " A nota do aluno 2 foi : " + str(aluno2) + "\n" +
          " A nota do aluno 3 foi : " + str(aluno3))



# Os comandos executados no programa realizam o seguinte algoritmo:
# Espera a entrada do valor das notas de três alunos
# Em seguida é feita a comparação por meio da lógica booleana
# E para o resultado final é feito o encadeamento com os comandos if, elif e else ( Se ), ( Senão se ) e ( Se não )
# Tendo o encadeamento e alinhamento de cada condição
# Fazendo as ordenações das notas na forma crescente de acordo com os valores das notas
# Obtendo-se na saída do interpretador do Python as respostas dadas de acordo com a comparação e ordenação feita:
# Acrescidas das mensagens em aspas