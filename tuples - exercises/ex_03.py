#Python Exercise 074: Create a program that will generate five random numbers and place them in a tuple. After that, show the list of generated numbers and also indicate the smallest and largest values ​​that are in the tuple.
from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for number in numbers:
    print(f'{number} ', end =' ')

print(f' \n O menor foi {min(numbers)}')
print(f' O maior foi {max(numbers)}')