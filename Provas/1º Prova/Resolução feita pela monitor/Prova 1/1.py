x = int(input("Digite a posição no ponto X: "))
y = int(input("Digite a posição no ponto Y: "))
if x>0 and y>0:
    print("Primeiro")
elif x>0 and y<0:
    print("Quarto")
elif x<0 and y>0:
    print("Segundo")
elif x<0 and y<0:
    print("Terceiro") 
elif x==0 and (y>0 or y>0):
    print("Sobre o eixo y") 
elif y==0 and (x>0 or x<0):
    print("Sobre o eixo x") 
elif x==0 and y==0:
    print("Sobre a origem") 
else:
    print("Coordenada inválida!")
    

