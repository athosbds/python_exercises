#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
drawn = []
generation_draw = int(input('Quantos jogos quer que eu sorteie?: '))
for x in range(1, generation_draw + 1): #Aqui gera números apartir do 1 até o que o usuário deseja.
    drawn.append(sample(list(range(1, 61)), 6)) #Aqui criando listas dentro de uma única lista com números não repetidos com a função sample
for x in range(len(drawn)):
    print(f'Jogo {x + 1}: {drawn[x]}') # O for percorre cada lista até o número que o usuário desejou gerar, sendo assim o drawn[x] acompanha com cada uma das listas com números não repetidos