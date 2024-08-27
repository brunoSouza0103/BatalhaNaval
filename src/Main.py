import random

def configurar_e_posicionar_navios():
    """Solicita ao usuário a quantidade de navios e os posiciona na matriz."""
    linhas = 10
    colunas = 10
    
    # Inicializa a matriz
    matriz = [['x' for _ in range(colunas)] for _ in range(linhas)]
    
    def pode_posicionar_navio(x, y, comprimento, horizontal):
        """Verifica se é possível posicionar um navio de determinado comprimento na matriz."""
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
        """Posiciona um navio na matriz, se possível."""
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

if __name__ == "__main__":
    configurar_e_posicionar_navios()
