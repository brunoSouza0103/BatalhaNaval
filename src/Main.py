def capturar_entrada(jogador, coordenadas_jogadas):
    while True:
        entrada = input(f"{jogador}, insira suas coordenadas de ataque (formato: linha,coluna): ")
        try:
            linha, coluna = map(int, entrada.split(','))
            if 0 <= linha < 10 and 0 <= coluna < 10:
                coordenada = (linha, coluna)
                if coordenada in coordenadas_jogadas:
                    print("Você já jogou nessa coordenada. Tente outra.")
                else:
                    coordenadas_jogadas.add(coordenada)
                    return linha, coluna
            else:
                print("Coordenadas fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Formato inválido. Certifique-se de usar o formato linha,coluna.")

def exibir_resultado(mensagem):
    print(mensagem)

def main():
    jogador = "Jogador 1"
    coordenadas_jogadas = set()
    while True:
        linha, coluna = capturar_entrada(jogador, coordenadas_jogadas)
        mensagem = f"Coordenadas capturadas: Linha {linha}, Coluna {coluna}"
        exibir_resultado(mensagem)

if __name__ == "__main__":
    main()
