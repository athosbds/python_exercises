#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
def grades(first_grade, second_grade, third_grade, situation=False):
    informations = {}
    informations['total'] = len([first_grade, second_grade, third_grade])
    informations['maior'] = max([first_grade, second_grade, third_grade])
    informations['menor'] = min([first_grade, second_grade, third_grade])
    average = sum([first_grade, second_grade, third_grade]) / len([first_grade, second_grade, third_grade])
    informations['média'] = average
    if situation:
        if average < 6:
            informations['situaçã0'] = 'Ruim'
        else:
            informations['situaçã0'] = 'Boa'
    print(informations)
grades(8, 8, 8, situation=True)