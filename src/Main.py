def capturar_entrada(jogador):
    while True:
        entrada = input(f"{jogador}, insira suas coordenadas de ataque (formato: linha,coluna): ")
        try:
            linha, coluna = map(int, entrada.split(','))
            if 0 <= linha < 10 and 0 <= coluna < 10:
                return linha, coluna
            else:
                print("Coordenadas fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Formato inválido. Certifique-se de usar o formato linha,coluna.")

def exibir_resultado(mensagem):
    print(mensagem)

def main():
    jogador = "Jogador 1"
    while True:
        linha, coluna = capturar_entrada(jogador)
        mensagem = f"Coordenadas capturadas: Linha {linha}, Coluna {coluna}"
        exibir_resultado(mensagem)

if __name__ == "__main__":
    main()
