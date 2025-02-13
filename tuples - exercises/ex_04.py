#Python Exercise 075: Develop a program that reads four values ​​from the keyboard and stores them in a tuple. No ending, more: A) How many times did the value 9 appear. 
# B) In which position was the first value 3 entered. C) What were the even numbers.
number = ()
count = 0
for x in range(0, 4):
    numbers = int(input('Digite um número: '))
    number += (numbers,)
    
print(f'O número 9 aparecer {number.count(9)} vezes')
if 3 in number:
    print(f'O 3 se encontra na posição {number.index(3)+1}')
else:
    print('O número 3 não foi digitado.')

for numbers in number:
    if numbers % 2 == 0:
        count += 1
print(f'Foram digitados {count} números pares.')