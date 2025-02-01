#Python Exercise 62: Better CHALLENGE 61, asking the user if he wants to show some more terms. The program will exit when it says it wants to show 0 terms.

first_term = int(input('Primeiro Termo: '))
reason = int(input('Razão: '))


actually_term = first_term
count = 1
tot = 0
more = 10
while more != 0:
    tot += more
    while count <= tot:
        print('{}'.format(actually_term), end=' -> ')
        actually_term += reason
        count += 1
    more = int(input('\n Quantos termos você quer agora? '))
print('Fim.')