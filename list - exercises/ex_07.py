#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

people = []
data = []
upper = lower = 0
while True:
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    print('-'*20)
    if len(people) == 0:
        upper = lower = data[1]
    else:
        if data[1] > upper:
            upper = data[1]
        if data[1] < lower:
            lower = data[1]
    people.append(data[:])
    data.clear()
    continuos = str(input('Quer Continuar? [S/N]: ')).upper().strip()
    print('-'*20)
    if continuos == 'N':
        break
print(f'Os dados foram: {people}')
print(f'\n As pessoas cadastradas foram: {len(people)}')

print(f'O maior peso foi de {upper}kg ', end ='->')
for person in people:
    if person[1] == upper:
        print(f'{person[0]}', end ='')

print(f'\n O menor peso foi de {lower}kg ', end='->')
for person in people:
    if person[1] == lower:
        print(f'{person[0]}', end ='')
print()

