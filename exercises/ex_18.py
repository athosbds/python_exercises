#Python Exercise 64: Create a program that reads multiple integers from the keyboard. The program will only stop when the user enters the value 999, which is a stop condition. At the end, show how many numbers were entered and what the sum was between them (ignoring the flag)


flag = True
count = 1
while flag:
    number = int(input('Digite um número inteiro: '))
    if number == 999:
        flag = False
        
    else:
        print('Fim')
        count += number
print(count)
    
        
  