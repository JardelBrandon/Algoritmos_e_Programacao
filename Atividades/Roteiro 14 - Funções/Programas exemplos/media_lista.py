def calcula_media(l=[], n=1):
    soma = 0
    for i in range(len(l)):
        soma += l[i]
    return soma/n

n = int(input("quantas notas? "))

notas_alunos = []

for i in range(n):
    nota = int(input("Nota " + str(i) + ": "))
    notas_alunos.append(nota)

media = calcula_media(notas_alunos[:], n)
print(notas_alunos)
print(media)