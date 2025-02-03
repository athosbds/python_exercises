# Python Exercise 61: Redo CHALLENGE 51, reading the first term and the reason of a PA, showing the first 10 terms of the progression using the while structure.

first_term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))

term = 10
actually_term = first_term
count = 1
while count <= term:
    print('{}'.format(actually_term), end=' -> ')
    actually_term += reason
    count += 1
print('Fim.')