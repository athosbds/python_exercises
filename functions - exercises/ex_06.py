#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime
def voted(year):
    actually_year = datetime.now().year
    age = actually_year - year
    if age < 16:
        print(f'Com {age} anos anos: NÃO VOTA.')
    elif 16 <= age <= 17:
        print(f'Com {age} anos É FACULTATIVO O VOTO.')
    elif 18 <= age <= 69:
        print(f'Com {age} anos: É OBRIGATÓRIO VOTAR.')
    elif age >= 70:
        print(f'Com {age} anos: É FACULTATIVO O VOTO.')
birthday = int(input('Ano de Nascimento: '))
voted(birthday)