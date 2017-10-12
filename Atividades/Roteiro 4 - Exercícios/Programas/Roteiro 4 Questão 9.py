'''
9. Leia uma data e determine se ela e válida. Ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias
em anos bissextos, e 28 dias em anos não bissextos. Procure uma forma de
identificar se um número é bissexto sem perguntar ao usuário.
'''

dia = int(input("Digite o dia : "))
mes = int(input("Digite o mês : "))
ano = int(input("Digite o ano : "))
bissexto = bool()
meses = bool()
dias = bool
anos = bool()

if ano % 400 == 0:
    bissexto = True

elif ano % 4 == 0:
    if ano % 100 != 0 :
        bissexto = True

    else:
        bissexto = False

else:
    bissexto = False


if mes > 0 and mes <= 12:
    meses = True

else:
    meses = False

if ano > 0:
    anos = True

else:
    anos = False

if bissexto == True and meses == True:
    if mes == 1:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 2:
        if dia > 0 and dia <= 29:
            dias = True

        else:
            dias = False

    if mes == 3:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 4:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 5:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 6:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 7:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 8:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 9:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 10:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 11:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 12:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False


if bissexto == False and meses == True:
    if mes == 1:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 2:
        if dia > 0 and dia <= 28:
            dias = True

        else:
            dias = False

    if mes == 3:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 4:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 5:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 6:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 7:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 8:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 9:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 10:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False

    if mes == 11:
        if dia > 0 and dia <= 30:
            dias = True

        else:
            dias = False

    if mes == 12:
        if dia > 0 and dia <= 31:
            dias = True

        else:
            dias = False


if dias == True and meses == True and anos == True :
    print("A data informada é valida !")

else:
    print("A data informada não é valida !  ")




'''
Os comandos executados no programa realizam o seguinte algoritmo:
Espera a entrada do dia, mês e ano pelo usuário
Define as variáveis booleanas para comparação se é verdadeira o falsa
Realiza operações matemática com o ano informado para calcular se o ano é bissexto ou não
Faz os encadeamentos para definir as condições verdadeiras das datas informadas
Compara se o dia, mês e ano é verdadeiro, caso sim armazena True (Verdadeiro) para sua variável, se não False (Falso)
Ao final analisa se as variáveis da data são verdadeiras, se sim:
Obtendo-se na saída do interpretador do Python : >>> A data informada é valida !
Se não :
Obtendo-se na saída do interpretador do Python : >>> A data informada não é valida !
'''


