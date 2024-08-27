#batalha naval

import os

max_col = 10
max_lin = 10

tabuleiro = [[" " for _ in range(max_col)] for _ in range(max_lin)]

#navios = [[" " for _ in range(max_col)] for _ in range(max_lin)]
#Declaração necessaria da matriz dos navios

resultado = "Jogando"




def inicializatabuleiro():
    for l in range(max_lin):
        for c in range(max_col):
            tabuleiro[l][c] = ' '    #Define os valores da matriz como vazio

def imprimirBorda(ultimo):
    print('+---' * max_col + '+')
    if not ultimo:
        print('|   ' * max_col + '|')       #Se for o ultimo imprime para gerar a borda

def imprimirtabuleiro():
    os.system('clear')
    for l in range(max_lin):
        imprimirBorda(False)
        for c in range(max_col):
            print(f' {tabuleiro[l][c]} |', end='')      #o end=' ' faz não adicionar uma nova linha para ter o espaço
        print(f' {l + 1}')
    imprimirBorda(True)                 #Define borda como ultimo para imprimi-la

def validaResultado():
    for l in range(max_lin):
        for c in range(max_col):
            if tabuleiro[l][c] == ' ' and navios[l][c] == 'N':      #Verifica as posições do tabuleiro para retornar se tem navio ou nao
                return "Jogando"
    return "Ganhou"

inicializatabuleiro()
resultado = 'Jogando'

while resultado == 'Jogando':
    imprimirtabuleiro()
    print('Onde vai jogar?')


    linha=0
    while((linha<1) or (linha>max_lin)):
        print("Informe a linha: ")
        linha = int(input())
        if ((linha<1) or (linha>max_lin)):
            print('Linha inválida')
          
    coluna=0
    while((coluna<1) or (coluna>max_col)):
        print('Informe a coluna')
        coluna=int(input())
        if ((coluna<1) or (coluna>max_col)):
            print('Coluna inválida')


    linha -= 1  # Ajusta pq a matriz é baseada no zero então se colocar a linha 1 sera como a segunda, mas isso faz se tornar a primeira
    coluna -= 1
    
    if navios[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'N'
    else:
        tabuleiro[linha][coluna] = 'X'
        resultado = validaResultado()


imprimirtabuleiro()
print(resultado)
