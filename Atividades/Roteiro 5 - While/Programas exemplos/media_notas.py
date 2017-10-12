MAX_NOTAS = 3
qtde_notas = 1

soma = 0

while qtde_notas <= MAX_NOTAS:
    nota = int(input("Nota " + str(qtde_notas) + ": "))
    soma += nota
    qtde_notas += 1 # Mesma coisa que qtde_notas = qtde_notas + 1

media = soma/MAX_NOTAS

print(media)