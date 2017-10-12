MAX_NOTAS = 3
qtde_notas = 1

soma = 0

while True:
    nota = int(input("Nota " + str(qtde_notas) + ": "))
    soma += nota
    qtde_notas += 1 # Mesma coisa que qtde_notas = qtde_notas + 1
    if qtde_notas > MAX_NOTAS:
        break

media = soma/MAX_NOTAS

print(media)