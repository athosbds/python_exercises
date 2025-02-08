#Python Exercise 071: Create a program that simulates the operation of an ATM. At the beginning, ask the user what amount will be withdrawn (whole number) and the program will inform how many bills of each amount will be delivered. 

value = int(input('Que valor gostaria de sacar? '))
total = value
banknote = 50
banknote_total = 0

while total > 0:
    if total >= banknote:
        total -= banknote
        banknote_total += 1
    else:
        if banknote_total > 0:
            print(f'Total de {banknote_total} cédulas de R$ {banknote}')
        elif banknote == 50:
            banknote = 20
        elif banknote == 20:
            banknote = 10
        elif banknote == 10:
            banknote = 1
        if total == 0:
            break
if banknote_total > 0:
    print(f'Total de {banknote_total} cédulas de R$ {banknote}')