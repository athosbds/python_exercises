#Python Exercise 65: Create a program that reads several integers from the keyboard. At the end of the execution, show the average of all values ​​and which were the highest and lowest values ​​read. The program must ask the user whether or not he wants to continue typing values.

flag = True
count = solve = middle = upper = lower = 0
while flag:
    number = int(input('Digite um número: '))
    count += 1
    solve += number
    if count == 1:
        upper = lower = number
    else:
        if number > upper:
            upper = number
        if number < lower:
            lower = number
    answer = str(input('Quer continuar? [S/N]'))
    if answer.lower() == 'n':
        flag = False
middle = solve / count
print('Digitou {} números e sua média é {}'.format(count, middle))
print('O maior valor foi {} e o menor foi {}'.format(upper, lower))


