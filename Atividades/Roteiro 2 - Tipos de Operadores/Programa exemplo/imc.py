QUADRADO = 2

nome = input("Digite seu nome: ")


massa = float(input("Massa: "))
print(type(massa))
altura = float(input("Altura: "))
print(type(altura))

print(nome + ", o seu IMC eh: ")

print(massa/altura**QUADRADO)

print("Fim.")

