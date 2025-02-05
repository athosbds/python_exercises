#Python Exercise 67: Write a program that shows the multiplication table of several numbers, one at a time, for each value entered by the user. The program will stop when the requested number is negative.

x = number = count = 0
while number >= 0:
    number = int(input('Tabuada do Número: '))
    if number < 0:
        break
    for x in range(0,10+1):
        print('{} X {} = {}'.format(number, x, number*x))
print('Números Negativos não são permitidos.')