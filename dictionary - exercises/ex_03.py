#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
date = {}
date['nome'] = str(input('Nome: '))
birthday = int(input('Ano de Nascimento: '))
date['idade'] = datetime.now().year - birthday
date['ctps'] = int(input('Carteira De Trabalho[0 se não houver.]: '))
if date['ctps'] != 0:
    date['contrato'] = int(input('Ano de Contratação: '))
    date['salário'] = float(input('Salário: '))
    date['aposentadoria'] = date['idade'] + (date['contrato'] + 35) - datetime.now().year
print('-'*30)
for keys, value in date.items():
    print(f'- {keys} tem valor {value}')
    print('-'*30)