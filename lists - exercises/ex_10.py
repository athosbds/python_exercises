#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.
matrices = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
even_total = third_line = upper = 0
for line in range(0, 3):
    for column in range(0, 3):
        matrices[line][column] = int(input(f'Digite o valor para: ({line}, {column}): '))
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrices[line][column]}]', end ='')
    print()
for line in range(len(matrices)):
    for column in range(len(matrices[line])):
        if matrices[line][column] % 2 == 0:
            even_total += matrices[line][column]
third_line = sum(matrices[2])
upper = max(matrices[1])
print('-'*30)
print(f'\nSoma de todos números pares: {even_total}')
print(f'Soma dos números da terceira linha: {third_line}')
print(f'Maior número da segunda linha: {upper}')