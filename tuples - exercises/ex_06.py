##Python Exercise 077: Create a program that has a tuple with several words (do not use accents). After that, you must show, for each word, what its vowels are.

words = ('Programar', 'Viver', 'Sonhar', 'Morrer', 'Ajudar')
for word in words:
    print(f'\n Na palavra {word} temos ', end='')
    for letter in word:
        if letter.lower() in 'aeio':
            print(letter, end='')
            