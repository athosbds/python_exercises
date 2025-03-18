#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(width, length):
    calculate = width * length
    print(f'A área de um terreno{width}x{length} é de {calculate}m²')

width_value = int(input('Largura: '))
lenght_value = float(input('Comprimento: '))
area(width_value, lenght_value)