#Python Exercise 58: Improve the CHALLENGE 28 game where the computer will “think” of a number between 0 and 10. But now the player will try to guess until he gets it right, showing at the end how many guesses were needed to win.
print('Estou pensando em número de 0 a 10! Tente Adivinhar!')
import random
order_list = list(range(0, 3))
choose_computer = random.choice(order_list)
hit = False
tryagain = 0
while not hit:
    player = int(input('Seu Palpite: '))
    tryagain += 1
    if player == choose_computer:
        hit = True
print('Você acertou! Com {} tentativas'.format(tryagain))