#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def counter(begin, last_item, by):
   
    if by < 0:
        by *= -1
    if by == 0:
        by = 1
    elif by < 0:            #Esse if aqui é pra conferir que o by conte até a repetição desejada
        last_item -= 1
    print(f'Contagem de {begin} até {last_item}, de {by} em {by}')
    if begin < last_item:
        total = begin
        while total <= last_item:
            print(f'{total} ', end =' ')
            total += by
        print('\n Acabou essa merda')
    else:
        total = begin
        while total >= last_item:
            print(f'{total}', end =' ')
            total -= 1
        print(' \n Acabou essa merda')
        
counter(1, 10, 1)
counter(10, 0, -2)
print('Agora é Sua vez!')
init = int(input('Início: '))
number_end = int(input('Fim: '))
pass_number = int(input('Passo: '))
print('\n')
counter(init, number_end, pass_number)