import os
import random

# Definições iniciais
max_col = 10  # Número máximo de colunas no tabuleiro
max_lin = 10  # Número máximo de linhas no tabuleiro

# Funções para manipular o tabuleiro
def inicializatabuleiro():
    """
    Inicializa um tabuleiro vazio.
    Retorna uma matriz 10x10 de espaços em branco.
    """
    return [[" " for _ in range(max_col)] for _ in range(max_lin)]

def imprimirBorda(ultimo):
    """
    Imprime as bordas do tabuleiro. A borda final é diferente.
    :param ultimo: Booleano indicando se é a última borda a ser impressa.
    """
    k=1
    print(end="+")
    for k in range(max_col):
        print(end="---+")
    print('')
    if not ultimo:
        print(end="|")

def imprimirtabuleiro(tabuleiro):
    """
    Imprime o tabuleiro no console, limpando a tela antes para uma visualização limpa.
    :param tabuleiro: Matriz representando o estado atual do tabuleiro.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para Windows ou sistemas Unix-like
    for l in range(max_lin):
        imprimirBorda(False)  # Imprime a borda superior
        for c in range(max_col):
            print(f' {tabuleiro[l][c]} |', end='')  # Imprime cada célula do tabuleiro
        print(f' {l + 1}')  # Imprime o número da linha
    imprimirBorda(True)  # Imprime a borda inferior

def validaResultado(tabuleiro, navios):
    """
    Verifica se o jogo terminou. Se ainda houver navios não afundados, o jogo continua.
    tabuleiro: Matriz atual do tabuleiro.
    navios: Matriz que contém a posição dos navios.
    :return: String indicando o status do jogo ("Jogando" ou "Ganhou").
    """
    for l in range(max_lin):
        for c in range(max_col):
            if tabuleiro[l][c] == ' ' and navios[l][c] == 'N':
                return "Jogando"
    return "Ganhou"

# Funções para configurar e posicionar navios
def configurar_e_posicionar_navios():
    """
    Solicita ao usuário a quantidade de navios a ser posicionada e configura aleatoriamente.
    Retorna a matriz de navios configurada.
    """
    linhas = 10
    colunas = 10
    
    matriz = [['x' for _ in range(colunas)] for _ in range(linhas)]  # Inicializa a matriz do campo de navios
    
    def pode_posicionar_navio(x, y, comprimento, horizontal):
        """
        Verifica se é possível posicionar um navio na posição especificada.
         x: Linha inicial.
         y: Coluna inicial.
         comprimento: Comprimento do navio.
         horizontal: Booleano indicando se o navio será posicionado horizontalmente.
        return: Booleano indicando se o posicionamento é possível.
        """
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
        """
        Tenta posicionar um navio na matriz de forma aleatória.
         comprimento: Comprimento do navio.
         horizontal: Booleano indicando se o navio será posicionado horizontalmente.
         return: Booleano indicando se o posicionamento foi bem-sucedido.
        """
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
    
    return matriz

# Funções para lógica do jogo
def atacar(tabuleiro, navios, linha, coluna):
    """
    Realiza um ataque na coordenada especificada e atualiza o tabuleiro.
     tabuleiro: Matriz atual do tabuleiro.
     navios: Matriz com a posição dos navios.
     linha: Linha da coordenada de ataque.
     coluna: Coluna da coordenada de ataque.
    return: Mensagem sobre o resultado do ataque.
    """
    if not (0 <= linha < len(tabuleiro)) or not (0 <= coluna < len(tabuleiro[0])):
        return "Posição fora dos limites do tabuleiro"
    
    if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'O':
        return "Já atacado"
    
    if navios[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'X'
        return "Acertou!"
    else:
        tabuleiro[linha][coluna] = 'O'
        return "Água"

def capturar_entrada(coordenadas_jogadas):
    """
    Captura e valida a entrada do jogador para coordenadas de ataque, garantindo que não sejam repetidas.
    coordenadas_jogadas: Conjunto contendo coordenadas já informadas.
    return: Tupla(sequencia de valores) com a linha e coluna da coordenada de ataque.
    """
    while True:
        entrada = input("Insira suas coordenadas de ataque (formato: linha,coluna): ")
        try:
            linha, coluna = map(int, entrada.split(','))
            # Ajusta para zero-baseado e verifica limites
            if 1 <= linha <= max_lin and 1 <= coluna <= max_col:
                coordenada = (linha - 1, coluna - 1)
                if coordenada in coordenadas_jogadas:
                    print("Você já informou esta coordenada. Tente outra.")
                else:
                    coordenadas_jogadas.add(coordenada)
                    return coordenada
            else:
                print("Coordenadas fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Formato inválido. Certifique-se de usar o formato linha,coluna.")

def main():
    """
    Função principal do jogo. Inicializa o tabuleiro, posiciona os navios, e gerencia o loop do jogo.
    """
    # Inicializa tabuleiros
    tabuleiro = inicializatabuleiro()
    navios = configurar_e_posicionar_navios()
    
    print("Configuração do tabuleiro inicial:")
    imprimirtabuleiro(tabuleiro)
    
    coordenadas_jogadas = set()  # Conjunto para armazenar coordenadas já jogadas
    resultado = "Jogando"
    
    while resultado == "Jogando":
        linha, coluna = capturar_entrada(coordenadas_jogadas)  # Captura a entrada do jogador
        mensagem = atacar(tabuleiro, navios, linha, coluna)  # Realiza o ataque
        print(mensagem)
        resultado = validaResultado(tabuleiro, navios)  # Verifica se o jogo terminou
        imprimirtabuleiro(tabuleiro)  # Atualiza a visualização do tabuleiro
        if resultado == "Ganhou":
            print("Você ganhou o jogo!")  # Mensagem de vitória
            break

if __name__ == "__main__":
    main()  # Executa a função principal se o script for executado diretamente
