#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
player = {}
players = []
while True:
        player.clear()
        player['nome'] = str(input('Nome do Jogador: '))
        player['gols'] = []
        matches = int(input('Quantas partidas jogadas: '))
        for x in range(1, matches+1):
            goal = int(input(f'Quantos gols na partida {x}: '))
            player['gols'].append(goal)
        player['total'] = sum(player['gols'])
        players.append(player.copy())
        while True:
            continuos = str(input('Continuar? [S/N]: ')).strip().upper()
            if continuos in 'SN':
                 break
            print('Erro! Tente S ou N!')
        if continuos == 'N':
            break
print(players)