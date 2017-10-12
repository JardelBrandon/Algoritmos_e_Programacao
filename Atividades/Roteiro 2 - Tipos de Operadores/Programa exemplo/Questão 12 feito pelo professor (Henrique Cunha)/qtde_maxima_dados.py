tVideo = float(input("Entre com a taxa maxima de transmissao de video: "))
tAudio = float(input("Entre com a taxa maxima de transmissao de audio: "))
tDados = float(input("Entre com a taxa maxima de transmissao de dados: "))
capacidade = float(input("Capacidade: "))

qdMax = (tVideo*5.2+tAudio*3.4+tDados*1.5)/capacidade

print(qdMax)