VAZIO = "_"
JOGADOR_1 = "X"
JOGADOR_2 = "O"

def recebe_tam_tab():
    '''
    IMPLEMENTAR (20 pontos)
    Validação da entrada
    A expressão deve ser to tipo 'aXb', onde:
    a é um número de um único dígito e representa a altura do tabuleiro
    X é um caractere separador
    b é um número de um único dígito e representa a largura do tabuleiro
    Exs.: 7x6,  7x8, 8x9
    a deve ser necessariamente menor que b, mas sempre maior que 7
    O valor máximo de b é 9. Portanto, o valor máximo de a é 8
    '''
    entrada = input()
    return int(entrada[0]), int(entrada[2]) # Esse return pode (e deve) mudar

def cria_tab(l, a):
    m = []
    for i in range(l):
        m.append([])
        for j in range(a):
            m[i].append(VAZIO)
    return m

def colunas(largura):
    '''
    Retorna um string com os números que devem ser impressos nas colunas
    '''
    cols = ""
    for i in range(largura):
        cols += str(i) + " "
    return cols

def imprime_tab(tab):
    '''
    Imprime o tabuleiro de maneira que fique amigável para o usuário
    :param m: o tabuleiro a ser impresso
    '''
    for i in range(len(tab[0])-1, -1, -1):
        for j in range(len(tab)):
            print(tab[j][i], end=" ")
        print()
    print(colunas(len(tab)))

def recebe_jogada():
    '''
    IMPLEMENTAR (15 pontos)
    Validação da jogada. O jogo deve receber da entrada padrão 1 inteiro de um único dígito.
    '''
    jogada = int(input())
    return jogada

def pode_jogar(tab, jogada):
    '''
    IMPLEMENTAR (15 pontos)
    Verifica se pode ser realizada uma jogada naquela posição.
    Para fazer isso, basta verificar se tem um espaço vazio na referida coluna de jogo.
    '''
    return True # Esse return deve mudar

def jogar(jogador_da_vez, jogada, tab=[]):
    '''
    Realiza uma jogada
    '''
    if pode_jogar(tab, jogada):
        coluna = tab[jogada]
        coluna[coluna.index(VAZIO)] = jogador_da_vez
    else:
        print("Coluna está cheia!")

def troca_jogador(jogador_da_vez):
    '''
    Troca o turno dos jogadores
    '''
    turno = ""
    if jogador_da_vez == JOGADOR_1:
        turno = JOGADOR_2
    else:
        turno = JOGADOR_1

    return turno

def terminou(jogador_da_vez, jogada, tab=[]):
    '''
    IMPLEMENTAR (50 pontos)
    15 pontos para verificação horizontal
    15 pontos para verificação vertical
    20 pontos para verificação diagonal
    Deve retornar se a última jogada resulta em uma situação de fim de jogo.
    '''
    return False # Esse return deve mudar


# Setup do jogo
altura, largura = recebe_tam_tab()
tab = cria_tab(largura, altura)
jogador_da_vez = JOGADOR_1

# Loop principal
while True:
    imprime_tab(tab)
    print("Jogador " + jogador_da_vez + " é a sua vez!")
    jogada = recebe_jogada()
    jogar(jogador_da_vez, jogada, tab)
    jogador_da_vez = troca_jogador(jogador_da_vez)
    if terminou(jogador_da_vez, jogada, tab):
        print("Jogador " + jogador_da_vez + ", você venceu!")
        break

