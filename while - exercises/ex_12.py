#Python Exercise 68: Write a program that plays odd or even with the computer. The game will only stop when the player loses, showing the total number of consecutive wins he has achieved at the end of the game.

import random
list = list(range(0, 10))
count = 0
player = ever_odd = 0

while True:
    random_number = random.choice(list)
    player = int(input('Digite um valor: '))
    odd = str(input('Par ou Ímpar? [I/P]: '))
    
    total = player + random_number
    result = 'P' if total % 2 == 0 else 'I'

    if odd == result:
        print('Você ganhou')
        count += 1
    else:
        print('GAME OVER! Você perdeu.')
        break
print('Venceu {} vezes'.format(count))

#não comitto a!!!!

