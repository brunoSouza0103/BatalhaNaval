def criar_tabuleiro(tamanho):
    return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(linha))
    print()

def adicionar_navio(tabuleiro, navio):
    for (linha, coluna) in navio['posicoes']:
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = 'N'  
        else:
            raise ValueError("Posição já ocupada") #O programa sobe o ValueError para levantar a exceção e mostrar que a posição já foi ocupada.

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

def verificar_vitoria(tabuleiros, navios):
    for i, tabuleiro in enumerate(tabuleiros): #enumerate é utilizado parar iterar sobre uma sequência e ao mesmo tempo, obter o índice de cada elemento.
        afundado = True
        for navio in navios[i]:
            if any(tabuleiro[linha][coluna] == 'N' for linha, coluna in navio['posicoes']):
                afundado = False
                break
        if afundado:
            return f"Jogador {i + 1} venceu!"
    return None #caso nenhum jogador tenha vencido, retorna None

