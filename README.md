# Jogo de Batalha Naval

Este projeto é uma implementação de um jogo de Batalha Naval, onde o jogador deve localizar e afundar todos os navios inimigos em um tabuleiro de 10x10. 
O jogo é jogado diretamente no console e usa apenas estruturas de dados simples como matrizes e vetores.

## Funcionalidades

- **Posicionar Navios:** O jogo posiciona automaticamente os navios no tabuleiro de forma aleatória. Os navios têm comprimentos variados entre 2 e 5 células e podem ser posicionados horizontal ou verticalmente.
- **Ataque:** O jogador insere as coordenadas para realizar ataques no tabuleiro, tentando acertar a posição dos navios.
- **Verificação de Vitória:** O jogo verifica automaticamente se todos os navios foram afundados e declara o jogador como vencedor quando isso acontecer.
- **Exibição do Tabuleiro:** Após cada jogada, o tabuleiro é atualizado e exibido no console, mostrando os acertos (`X`), erros (`O`), e as posições ainda não atacadas (` `).

## Requisitos

Antes de rodar o projeto, certifique-se de que seu ambiente atenda aos seguintes requisitos:

- *Python*: Versão 3.9 ou superior

Este projeto não depende de bibliotecas externas, apenas da instalação padrão do Python.
