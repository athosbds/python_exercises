#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
everyone = []
date = {}
total_ages = middle_ages = 0
while True:
    date.clear()
    date['nome'] = str(input('Nome: '))
    
    while True:
        date['sexo'] = str(input('Sexo: [M/F]: ')).upper()
        if date['sexo'] in 'MF':
            break
        print('Tente por M ou F!')
    date['idade'] = int(input('Idade: '))
    total_ages += date['idade']
    everyone.append(date.copy())
    while True:
        continuos = str(input('Quer Continuar?: [S/N]: ')).upper()
        if continuos in 'SN':
            break
        print('Tente S ou N!')
    if continuos == 'N':
        break
middle_ages = total_ages / len(everyone)
print(f'Ao total temos {len(everyone)} pessoas cadastradas')
print(f'A média das idades é de {middle_ages:.2f}')
print('\n Mulheres: ')
for person in everyone:
    if person['sexo'] == 'F':
        print(f'{person['nome']} ', end ='')
print()
print('Pessoas acima da média de idades: ')
for person in everyone:
    if person['idade'] >= middle_ages:
        print(f'    ')
        for keys, value in person.items():
            print(f'{keys} = {value}; ', end ='')
        print()