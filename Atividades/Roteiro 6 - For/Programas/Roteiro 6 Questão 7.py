#7. Escreva um program que leia três notas de uma turma de 10 alunos, calcule a média individual
#e exiba na saída padrão.
TURMA = 10
NOTAS = 3

numero_do_aluno = 1
media = 0

for turma in range(0,TURMA) :
    for aluno in range(0,NOTAS):
        print("Digite as notas do", numero_do_aluno,"º Aluno :")
        aluno = float(input())
        contador += 1
        media += aluno

    media /= NOTAS
    print("Média das notas do", numero_do_aluno,"º Aluno :", media)
    numero_do_aluno += 1







