#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
people = []
upper = lower = 0
while True:
    data = []
    data.append(str(input('Nome: ')))
    data.append(float(input('Peso: ')))
    people.append(data)
    continuos = str(input('Quer Continuar? [S/N]: ')).upper().strip()
    if continuos == 'N':
        break
print(f'As pessoas cadastradas foram: {len(people)}')


