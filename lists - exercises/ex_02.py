#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numbers = list()
while True:
    number = int(input('Digite um valor: '))
    print('Valor Adicionado.')
    if number not in numbers:
        numbers.append(number)
    else:
        print('Número existente, não vai ser adicionado.')
    
    answer = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if answer == 'N':
        break
    elif answer != 'S':
        print('Opção Inválida.')
        break
numbers.sort()
print(f'\n {numbers}')