#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

grades = []
while True:
    student = str(input('Nome: '))
    grade_one = float(input('Nota 1: '))
    grade_two = float(input('Nota 2: '))
    middle = (grade_one + grade_two) / 2
    grades.append([student, [grade_one, grade_two], middle])
    continuos = str(input('Quer Continuar? [S/N]: ')).strip().upper()
    if continuos == 'N':
        break
    elif continuos != 'S':
        print('Tente Novamente!')
        break
print('-'*35)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for x, student in enumerate(grades):
    print(f'{x:<4}{student[0]:<10}{student[2]:>8.1f}')
while True:
    print('>'*35)
    choose = int(input('Mostrar nota do aluno: [999 para finalizar]: '))
    if choose == 999:
        print('Finalizado.')
        break
    if choose <= len(grades) - 1:
        print(f'Notas de {grades[choose][0]} são {grades[choose][1]}')

