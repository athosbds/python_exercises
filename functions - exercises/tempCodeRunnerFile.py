def counter(begin, last_item, by):
    original_end = last_item
    if by > 0:
        last_item += 1
    else:            #Esse if aqui é pra conferir que o by conte até a repetição desejada
        last_item -= 1
    if by < 0:
        by_display = -by
    else:             #Esse if é pra deixar no print positivo o by por by
        by_display = by
    print(f'Contagem de {begin} até {original_end}, de {by_display} em {by_display}')
    for i in range(begin, last_item, by):
        print(f'{i}', end =' ')
    print('Fim')

counter(1, 10, 1)
counter(10, 0, -2)
print('Agora é Sua vez!')
init = int(input('Início: '))
number_end = int(input('Fim: '))
pass_number = int(input('Passo: '))
print('\n')
counter(init, number_end, pass_number)