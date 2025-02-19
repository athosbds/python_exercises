#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
normal_numbers = []
even_numbers = []
odd_numbers = []
while True:
    number = int(input('Digite um número: '))
    normal_numbers.append(number)
    ask = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if ask == 'N':
        break
    elif ask != 'S':
        print('Tente Novamente.')

    if number % 2 == 0:
            even_numbers.append(number)
    elif number % 2 != 0:
        odd_numbers.append(number)
print(f'\n Números Normais: {normal_numbers}')
print(f'Números Pares: {even_numbers}')
print(f'Números Ímpares: {odd_numbers}')