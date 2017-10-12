#13. Escreva um programa que leia o sexo e o salário de 10 pessoas e calcule:
#- a quantidade de homens;
#- a quantidade de mulheres;
#- a média do salário de homens e de mulheres;
#- o sexo da pessoa com o maior salário;
#- a média de salário dos homens;
MAX = 10

cont = 0
homens = 0
mulheres = 0
maior = 0
sexo_maior = str()
media = 0
media_homens = 0
media_mulheres = 0


sexo = input("Digite seu sexo : \n(M) para Masculino e (F) para Feminino ")
salario = float(input("Digite seu respectivo salário :"))
cont += 1
media += salario
maior = salario

if sexo == "M":
    homens += 1
    media_homens += salario

elif sexo == "F":
    mulheres += 1
    media_mulheres += salario

else:
    print ("Inválido !")

while True :
    sexo = input("Digite seu sexo : (M) para Masculino e (F) para Feminino ")
    salario = float(input("Digite seu respectivo salário :"))
    cont += 1
    media += salario

    if sexo == "M" :
        homens += 1
        media_homens += salario

    elif sexo == "F" :
        mulheres += 1
        media_mulheres += salario

    else :
        print ("Inválido !")

    if salario > maior :
        sexo_maior = sexo
        if sexo_maior == "M" :
            sexo_maior = sexo + " - Masculino"
        elif sexo_maior == "F":
            sexo_maior = sexo + " - Feminino"
        maior = salario

    if cont == MAX :
        break

if media != 0 :
    media /= MAX
if media_homens != 0 :
    media_homens /= homens
if media_mulheres != 0 :
    media_mulheres /= mulheres

print ("Quantidade de homens informado :", homens,"\nQuantidade de mulheres informado :", mulheres,
       "\nMédia salarial dos homens :", media_homens, "\nMédia salarial das mulheres :", media_mulheres,
       "\nSexo da pessoa com o maior salário :", sexo_maior, maior, "\nMédia salarial total :", media)





# O Algoritmo do programa realiza os seguintes comandos :
# Declara o valor da constante e das variáveis
# Realiza a repetição pela primeira vez fora do laço while para se ter um valor de comparação
# Entra em um laço de repetição afirmando que o comando while (Enquanto) é True (Verdadeiro)
# Executa as operações matemáticas, faz as comparações das lógicas
# Realiza as operações em seus respectivos encadeamentos
# Imprime na tela A quantidade de homens e mulheres informados, média salarial dos homens e mulheres,
# Sexo do maior salário apresentado e média salarial total acrescidos das mensagens em aspas
# Atendendo o que se pede na questão



