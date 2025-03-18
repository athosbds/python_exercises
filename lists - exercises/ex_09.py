#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta

matrices = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Trabalhando com 9 números já que é 3x3
for line in range(0, 3):
    for column in range(0, 3):
        matrices[line][column] = int(input(f'Ditite um valor:({line}, {column}) '))
print('-'*25)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrices[line][column]:^5}]', end ='') #Quebrando a linha pra ficar melhor visualmente.
    print()