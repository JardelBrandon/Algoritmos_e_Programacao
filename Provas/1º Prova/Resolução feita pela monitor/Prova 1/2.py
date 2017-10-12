selec = input("Digite a forma que deseja utilizar (Q)uadrado, (R)etângulo ou (C)írculo: ")
if selec == "q":
    lado = float(input("Digite o tamanho do lado do Quadrado: "))
    print("A área do quadrado é:",lado*lado)
    print("O perímetro do quadrado é:",lado*4)
elif selec == "r":
    altura = float(input("Digite a altura do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    print("A área do retângulo é:",altura*largura)
    print("O perímetro do retângulo é:", (largura*2)+(altura*2))
elif selec == "c":
    raio = float(input("Digite o raio do círculo: "))
    print("O comprimento do círculo é de:",(2*3.14*raio))
    print("A área do círculo é de:",(3.14*(raio**raio)))
else:
    print("Opção inválida!")
    
