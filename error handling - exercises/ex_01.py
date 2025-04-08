def readInt(message, second_message):
    while True:
        try:
            int_number = int(input(message))
            break
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
    while True:
        try:
            real_number = float(input(second_message))
            break
        except ValueError:
            print('ERRO! DIGITE UM NÚMERO REAL VÁLIDO')
    return int_number, real_number

int_number, real_number = readInt('Digite um numero Inteiro: ', 'Digite um número Real: ')
print(f'Você digitou o número inteiro {int_number} e o real {real_number}')
