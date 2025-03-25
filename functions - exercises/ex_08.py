#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def binder(player, goals=0):
    if not player:
        player = "<desconhecido>"
    print(f'O Jogador {player} fez {goals} gols(s) no campeonato')

    
name_player = str(input('Nome do Jogador: ')).strip()
goals = int(input('Número de Gols: '))
binder(name_player, goals)