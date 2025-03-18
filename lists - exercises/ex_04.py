#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
numbers = list()
while True:
    number = int(input('Digite um número: '))
    numbers.append(number)

    answer = str(input('Quer Continuar [S/N]: ')).strip().upper()
    if answer == 'N':
        break
    elif answer != 'S':
        print('Opção Errada. Tente Novamente.')
amount = len(numbers)
numbers.sort(reverse=True)
print(f'A lista possui {amount} elementos.')
print(f'Ordem Decrescente: {numbers}')
if 5 in numbers:
    print('\033[33m O número 5 está na lista!\033[m')
else:
    print('O número não tá na lista burrão.')