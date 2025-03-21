#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def largest(*numbers):
    date = []
    print('\n  Analisando os valores:')
    date.append(numbers)
    for number in date:
        print(number, end=' ')
        print(f'\nSendo o maior número: {max(number)}')
largest(4, 6, 5, 4, 2, 3, 0)
largest(20, 9, 4, 5, 3, 2, 1)