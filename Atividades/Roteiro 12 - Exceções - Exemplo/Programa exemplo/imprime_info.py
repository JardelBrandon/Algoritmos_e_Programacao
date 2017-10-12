idade = 0

while True:
    try:
        idade = int(input("Idade: "))
        if(idade < 0 or idade > 150):
            print("Idade fora da faixa! (Deve ser entre 0 e 150 anos)")
            continue

        break
    except ValueError:
        print("Idade inválida! Digite um número!!")


print(idade)