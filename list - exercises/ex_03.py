#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

values = list()
for i in range(0, 5):
    value = int(input('Digite um valor: '))
    if i  == 0:
        values.append(value)
    elif value > values[-1]:
        values.append(value)
    else:
        position = 0
        while position < len(values):
            if value <= values[position]:
                values.insert(position, value)
                break
            position += 1
print(f'Os números adicionados na lista foram: {values}')
    
