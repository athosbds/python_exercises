#Python Exercise 060: Write a program that reads any number and displays its factorial. Example:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

any_number = int(input('Digite um número: '))
fac = factorial(any_number)
predecessor = any_number
fac = 1
while predecessor > 0:
    print('{}'.format(predecessor), end='')
    print(' X ' if predecessor > 1 else ' = ', end =' ')
    fac*=predecessor
    predecessor -= 1
print('{}'.format(fac))
