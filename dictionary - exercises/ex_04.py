#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
name = {}
name['nome'] = str(input('Nome do Jogador: '))
name['gols'] = []
matches = int(input('Quantas partidas jogou?: '))
for x in range(matches):
    name['gols'].append(int(input(f'Quantos gols na partida {x}')))
name['total'] = sum(name['gols'])
print(name)