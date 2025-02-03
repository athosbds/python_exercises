# Python Exercise 63: Write a program that reads any N integer and displays the first N elements of a Fibonacci Sequence on the screen.

print('Sequeência de Fibonacci')

number = int(input('Quantos termos quer mostrar? '))

first_term = 0
second_term = 1
print('{} -> {}'.format(first_term, second_term), end ='')

count = 3

while count < number:
     third_term = first_term + second_term
     print('-> {}'.format(third_term), end='')
     first_term = second_term
     second_term = third_term
     count += 1
print('Fim')
