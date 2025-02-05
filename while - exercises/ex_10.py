#Python Exercise 66: Create a program that reads integers from the keyboard. The program will only stop when the user enters the value 999, which is a stop condition. At the end, show how many numbers were entered and what the sum was between them (ignoring the flag).

count = number = solve = 0
while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    count +=1  
    solve += number
print('A soma dos {} valores é igual a {}'.format(count, solve))  
