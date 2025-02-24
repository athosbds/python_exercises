#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Digite uma expressão: '))
pile = []
for simbol in pile:
    if expression == '(':
        expression.append('(')
    elif expression == ')':
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(')')
            break
if len(pile) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida.')

