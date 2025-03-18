#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

values = list()
for x in range(5+1):
    value = int(input(f'Digite o valor para posição {x}: '))
    values.append(value)

upper = max(values)
lower = min(values)

print(f'Os números digitados foram: {values}')
print(f'O maior número {upper} na posições ', end ='')
for position, value in enumerate(values):
    if values[position] == upper:
        print(f'{position}..', end ='')
print()
print(f'O menor número é {lower} nas posições ', end ='')
for position, value in enumerate(values):
    if values[position] == lower:
        print(f'{position}..', end='')
print()