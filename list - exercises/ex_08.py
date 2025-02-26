#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

unique_list = [[], []]
for i in range(0, 7):
    number = int(input('Digite um número: '))
    
    if number % 2 == 0:
        unique_list[0].append(number)
    elif number % 2 != 0:
        unique_list[1].append(number)
unique_list[0].sort() and unique_list[1].sort()
print(f'\nOs números pares: {unique_list[0]}')
print(f'Os números ímpares: {unique_list[1]}')