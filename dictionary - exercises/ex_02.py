#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
board = {}
rank = []
print('Valores Sorteados')
for j in range(1, 4+1):
    board[f"jogador {j}"]=randint( 1,6)
for player, score in board.items():
    print(f"{player} tirou {score}")
rank = sorted(board.items(), key=itemgetter(1), reverse=True)
print('-'* 30)
for i, value in enumerate(rank):
    print(f'{i+1} lugar: {value[0]} com {value[1]}.')
