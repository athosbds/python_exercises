#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fat(number, show=False):
    result = 1
    for x in range(number, 0, -1):
        if show:
            print(x, end='')
            if x>1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        result *= x
    return result
    
print(fat(5, True))
print(fat(5, False))