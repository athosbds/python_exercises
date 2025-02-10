#Exercise 72 in Python: Create a program that has a pair completely filled with a word count, from zero to twenty. Your program should read a number from the keyboard (between 0 and 20) and display it in full.

extension = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input('Digite um número de 0 a 20: '))
    if 0 <= number <= 20:
        break
    print('Tente Novamente!')
print(f'Você digitou o número {extension[number]}')
 