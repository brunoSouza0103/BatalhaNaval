import os
import random

# Definições globais
max_col = 10
max_lin = 10

# Funções para manipulação do tabuleiro
def inicializatabuleiro():
    return [[' ' for _ in range(max_col)] for _ in range(max_lin)]

def imprimirBorda(ultimo):
    print('+---' * max_col + '+')
    if not ultimo:
        print('|   ' * max_col + '|')

def imprimirtabuleiro(tabuleiro):
    os.system('clear')  # Para Windows use 'cls'
    for l in range(max_lin):
        imprimirBorda(False)
        for c in range(max_col):
            print(f' {tabuleiro[l][c]} |', end='')
        print(f' {l + 1}')
    imprimirBorda(True)

def validaResultado(tabuleiro, navios):
    for l in range(max_lin):
        for c in range(max_col):
            if tabuleiro[l][c] == ' ' and navios[l][c] == 'N':
                return "Jogando"
    return "Ganhou"

def criar_tabuleiro(tamanho):
    return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

def adicionar_navio(tabuleiro, navio):
    for (linha, coluna) in navio['posicoes']:
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = 'N'
        else:
            raise ValueError("Posição já ocupada")

def atacar(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'X'
        return "Acertou!"
    elif tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = 'O'
        return "Água"
    elif tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'O':
        return "Já atacado"
    else:
        return "Erro no ataque"

def verificar_vitoria(tabuleiro, navios):
    for l in range(max_lin):
        for c in range(max_col):
            if navios[l][c] == 'N' and tabuleiro[l][c] != 'X':
                return False
    return True

def configurar_e_posicionar_navios():
    """Configura e posiciona navios na matriz."""
    linhas = colunas = 10
    matriz = [['x' for _ in range(colunas)] for _ in range(linhas)]

    def pode_posicionar_navio(x, y, comprimento, horizontal):
        if horizontal:
            if y + comprimento > colunas:
                return False
            for i in range(y, y + comprimento):
                if matriz[x][i] != 'x':
                    return False
        else:
            if x + comprimento > linhas:
                return False
            for i in range(x, x + comprimento):
                if matriz[i][y] != 'x':
                    return False
        return True

    def posicionar_navio(comprimento, horizontal):
        while True:
            if horizontal:
                x = random.randint(0, linhas - 1)
                y = random.randint(0, colunas - comprimento)
            else:
                x = random.randint(0, linhas - comprimento)
                y = random.randint(0, colunas - 1)
            
            if pode_posicionar_navio(x, y, comprimento, horizontal):
                if horizontal:
                    for i in range(y, y + comprimento):
                        matriz[x][i] = 'N'
                else:
                    for i in range(x, x + comprimento):
                        matriz[i][y] = 'N'
                return True

    try:
        num_navios = int(input("Quantos navios você deseja posicionar? "))
        if num_navios <= 0:
            print("Número de navios deve ser maior que zero. Usando 1 navio como padrão.")
            num_navios = 1
    except ValueError:
        print("Entrada inválida. Usando 1 navio como padrão.")
        num_navios = 1

    for _ in range(num_navios):
        comprimento = random.randint(2, 5)
        horizontal = random.choice([True, False])
        while not posicionar_navio(comprimento, horizontal):
            comprimento = random.randint(2, 5)
            horizontal = random.choice([True, False])

    for linha in matriz:
        print(' '.join(celula for celula in linha))

    return matriz

def capturar_entrada(jogador, coordenadas_jogadas):
    while True:
        entrada = input(f"{jogador}, insira suas coordenadas de ataque (formato: linha,coluna): ")
        try:
            linha, coluna = map(int, entrada.split(','))
            if 1 <= linha <= 10 and 1 <= coluna <= 10:
                coordenada = (linha - 1, coluna - 1)  # Ajuste para zero-indexado
                if coordenada in coordenadas_jogadas:
                    print("Você já jogou nessa coordenada. Tente outra.")
                else:
                    coordenadas_jogadas.add(coordenada)
                    return coordenada
            else:
                print("Coordenadas fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Formato inválido. Certifique-se de usar o formato linha,coluna.")

def exibir_resultado(mensagem):
    print(mensagem)

def main():
    # Inicializa tabuleiros e configurações
    tabuleiro_jogador1 = inicializatabuleiro()
    navios_jogador1 = configurar_e_posicionar_navios()
    
    tabuleiro_jogador2 = inicializatabuleiro()
    navios_jogador2 = configurar_e_posicionar_navios()

    coordenadas_jogadas_jogador1 = set()
    coordenadas_jogadas_jogador2 = set()

    jogador_atual = 1
    resultado = "Jogando"

    while resultado == 'Jogando':
        if jogador_atual == 1:
            imprimirtabuleiro(tabuleiro_jogador1)
            print('Onde vai jogar?')

            linha, coluna = capturar_entrada("Jogador 1", coordenadas_jogadas_jogador1)
            mensagem = atacar(tabuleiro_jogador2, linha, coluna)
            print(mensagem)
            resultado = "Jogando" if not verificar_vitoria(tabuleiro_jogador2, navios_jogador2) else "Jogador 1 venceu!"

            jogador_atual = 2
        else:
            imprimirtabuleiro(tabuleiro_jogador2)
            print('Onde vai jogar?')

            linha, coluna = capturar_entrada("Jogador 2", coordenadas_jogadas_jogador2)
            mensagem = atacar(tabuleiro_jogador1, linha, coluna)
            print(mensagem)
            resultado = "Jogando" if not verificar_vitoria(tabuleiro_jogador1, navios_jogador1) else "Jogador 2 venceu!"

            jogador_atual = 1

    imprimirtabuleiro(tabuleiro_jogador1)
    imprimirtabuleiro(tabuleiro_jogador2)
    print(resultado)

if __name__ == "__main__":
    main()
